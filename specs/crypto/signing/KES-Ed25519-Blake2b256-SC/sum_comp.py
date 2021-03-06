from nacl.encoding import RawEncoder
from nacl.encoding import HexEncoder
from nacl.signing import SigningKey
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from hashlib import blake2b
import colorama
import random

colorama.init()
heads_up_display = True


def hash(msg: bytes) -> bytes:
    digest = blake2b(digest_size=32)
    digest.update(msg)
    output = digest.digest()
    return output


def chex(s: bytes):
    random.seed(s)
    style = random.randrange(8)
    fg = random.randrange(30, 38)
    s1 = ''
    bg = random.randrange(40, 48)
    fmt = ';'.join([str(style), str(fg), str(bg)])
    data = HexEncoder.encode(s)[0:8]
    s1 += '\x1b[%sm %s \x1b[0m' % (fmt, data)
    return s1


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def get(self):
        return self.value, self.left, self.right

    def encode(self):
        left = self.left
        right = self.right
        if isinstance(left, Node):
            (sr, wl, wr) = self.value
            zero = 0
            return sr + wl + wr + zero.to_bytes(1, byteorder='big') + left.encode()
        elif isinstance(right, Node):
            (sr, wl, wr) = self.value
            one = 1
            return sr + wl + wr + one.to_bytes(1, byteorder='big') + right.encode()
        else:
            (sk, vk) = self.value
            if isinstance(sk, SigningKey):
                return sk.encode(encoder=RawEncoder) + vk.encode(encoder=RawEncoder)
            else:
                return vk.encode(encoder=RawEncoder)

    @classmethod
    def decode(cls, data: bytes):
        if len(data) > 64:
            ptr = 0
            sr = data[ptr:ptr+32]
            ptr = ptr + 32
            wl = data[ptr:ptr+32]
            ptr = ptr + 32
            wr = data[ptr:ptr+32]
            ptr = ptr + 32
            b = int.from_bytes(data[ptr:ptr+1], byteorder='big')
            ptr = ptr + 1
            if b == 0:
                return cls((sr, wl, wr), cls.decode(data[ptr:]), None)
            else:
                return cls((sr, wl, wr), None, cls.decode(data[ptr:]))
        else:
            if len(data) == 32:
                vk = VerifyKey(data)
                return cls((None, vk), None, None)
            else:
                sk = SigningKey(data[0:32])
                vk = VerifyKey(data[32:64])
                return cls((sk, vk), None, None)


class SumSignature:
    def __init__(self, vk: bytes, sigma: bytes, w: list[bytes]):
        self.vk = vk
        self.sigma = sigma
        self.w = w

    @classmethod
    def decode(cls, data: bytes):
        vk = data[0:32]
        sigma = data[32:96]
        wd = data[96:]
        w = []
        for i in range(0, len(wd) // 32):
            wi = wd[32 * i:32 * (i + 1)]
            w = w + [wi]
        return cls(vk, sigma, w)

    def get(self) -> (bytes, bytes, list[bytes]):
        return self.vk, self.sigma, self.w

    def encode(self) -> bytes:
        out = self.vk + self.sigma
        for wi in self.w:
            out = out + wi
        return out

    def print(self):
        print("Verification Key: ["+self.vk.hex()+"]")
        print("Sigma: ["+self.sigma.hex()+"]")
        i = 0
        for wi in self.w:
            print("W["+str(i)+"]: ["+wi.hex()+"]")
            i = i + 1


def print_split(string: str) -> str:
    n = 64
    chunks = [string[j:j + n] for j in range(0, len(string), n)]
    out = ""
    j = 0
    for chunk in chunks:
        if j < len(chunks)-1:
            out = out + chunk + "\n"
        else:
            out = out + chunk
        j = j + 1
    return out


def print_key(n: Node):
    (v, l, r) = n.get()
    if l is None and isinstance(r, Node):
        (sr, wl, wr) = v
        if heads_up_display:
            print("1 ", chex(wl), chex(wr), chex(hash(wl + wr)))
        print_key(r)
    elif r is None and isinstance(l, Node):
        (sr, wl, wr) = v
        if heads_up_display:
            print("0 ", chex(wl), chex(wr), chex(hash(wl + wr)))
        print_key(l)


def print_vector(n: Node):
    (v, l, r) = n.get()
    print("Height:", height(n))
    if l is None and isinstance(r, Node):
        (sr, wl, wr) = v
        print("Binary configuration: 1")
        print("Right Seed:    ["+sr.hex()+"]")
        print("Left Witness:  ["+wl.hex()+"]")
        print("Right Witness: ["+wr.hex()+"]")
        print_vector(r)
    elif r is None and isinstance(l, Node):
        (sr, wl, wr) = v
        print("Binary configuration: 0")
        print("Right Seed:    ["+sr.hex()+"]")
        print("Left Witness:  ["+wl.hex()+"]")
        print("Right Witness: ["+wr.hex()+"]")
        print_vector(l)
    else:
        (sk, vk) = v
        print("Ed25519 Secret Key:       ["+sk.encode().hex()+"]")
        print("Ed25519 Verification Key: ["+vk.encode().hex()+"]")


def height(n) -> int:
    if isinstance(n, Node):
        if n.is_leaf():
            return 0
        else:
            return max(height(n.left), height(n.right)) + 1
    else:
        return 0


def keygen(s: bytes) -> (SigningKey, VerifyKey):
    sk = SigningKey(seed=s)
    vk = sk.verify_key
    return sk, vk


def generate_signature(sk: SigningKey, m: bytes) -> bytes:
    sig = sk.sign(m, encoder=RawEncoder)
    sigma = RawEncoder.decode(sig.signature)
    return sigma


def test_signature(vk: VerifyKey, sigma: bytes, m: bytes) -> bool:
    try:
        vk.verify(m, sigma, encoder=RawEncoder)
        return True
    except BadSignatureError:
        return False


def doubling_prng(s: bytes) -> (bytes, bytes):
    sl = hash(bytes([0x00]) + s)
    sr = hash(bytes([0x01]) + s)
    return sl, sr


def seed_tree(s: bytes, h: int) -> Node:
    if h > 0:
        (sl, sr) = doubling_prng(s)
        nl = seed_tree(sl, h - 1)
        nr = seed_tree(sr, h - 1)
        return Node(sr, nl, nr)
    else:
        (sk, vk) = keygen(s)
        return Node((sk, vk), None, None)


def merkle_vk(n: Node) -> Node:
    if n.is_leaf():
        return n
    else:
        (v, l, r) = n.get()
        (vl, ll, lr) = l.get()
        (vr, rl, rr) = r.get()
        nl = merkle_vk(l)
        nr = merkle_vk(r)
        if l.is_leaf() and r.is_leaf():
            (skl, vkl) = vl
            (skr, vkr) = vr
            vkl_bytes = vkl.encode(encoder=RawEncoder)
            vkr_bytes = vkr.encode(encoder=RawEncoder)
            return Node((v, hash(vkl_bytes), hash(vkr_bytes)), nl, nr)
        else:
            (x, l_nl, r_nl) = nl.get()
            (y, l_nr, r_nr) = nr.get()
            (sx, xl, xr) = x
            (sy, yl, yr) = y
            return Node((v, hash(xl + xr), hash(yl + yr)), nl, nr)


def reduce_tree(n: Node) -> Node:
    if n.is_leaf():
        return n
    else:
        (v, l, r) = n.get()
        return Node(v, reduce_tree(l), None)


def key_gen_sum(s: bytes, h: int) -> Node:
    t1 = seed_tree(s, h)
    t2 = merkle_vk(t1)
    t3 = reduce_tree(t2)
    return t3


def verification_key_sum(n: Node) -> bytes:
    (v, l, r) = n.get()
    (sr, wl, wr) = v
    return hash(wl + wr)


def key_time_sum(n: Node) -> int:
    if n.is_leaf():
        return 0
    else:
        (v, l, r) = n.get()
        if l is None and isinstance(r, Node):
            if r.is_leaf():
                return 1
            else:
                h = height(r)
                return key_time_sum(r) + pow(2, h)
        else:
            return key_time_sum(l)


def key_update_sum(n: Node, t: int) -> Node:
    tk = key_time_sum(n)
    h = height(n)
    if tk < t < pow(2, h):
        return evolve_key(n, t)
    else:
        return n


def evolve_key(n: Node, t: int) -> Node:
    if n.is_leaf():
        return n
    else:
        (v, l, r) = n.get()
        h = height(n)
        tp = t % pow(2, h - 1)
        if t >= pow(2, h - 1):
            if isinstance(l, Node) and r is None:
                if l.is_leaf():
                    (sr, ul, ur) = v
                    (sk, vk) = keygen(sr)
                    nr = Node((sk, vk), None, None)
                    return Node((bytes(32), ul, ur), None, nr)
                else:
                    (sr, wl, wr) = v
                    nr = key_gen_sum(sr, h - 1)
                    nrp = evolve_key(nr, tp)
                    return Node((bytes(32), wl, wr), None, nrp)
            else:
                nr = evolve_key(r, tp)
                return Node(v, None, nr)
        else:
            if l is None and isinstance(r, Node):
                nr = evolve_key(r, tp)
                return Node(v, None, nr)
            else:
                nl = evolve_key(l, tp)
                return Node(v, nl, None)


def sign_sum(n: Node, m: bytes) -> SumSignature:
    w = []
    (v, l, r) = n.get()
    while isinstance(l, Node) or isinstance(r, Node):
        (sr, wl, wr) = v
        if l is None and isinstance(r, Node):
            w = [wl] + w
            (v, l, r) = r.get()
        else:
            w = [wr] + w
            (v, l, r) = l.get()
    (sk, vk) = v
    sigma = generate_signature(sk, m)
    vk_bytes = vk.encode(encoder=RawEncoder)
    return SumSignature(vk_bytes, sigma, w)


def verify_sum_signature(r: bytes, sigma_t: SumSignature, t: int, m: bytes) -> bool:
    (vk, sigma, w) = sigma_t.get()
    bw = True
    if len(w) > 0:
        wl = None
        wr = None
        h = len(w)
        head, *tail = w
        if t % 2 == 0:
            wl = hash(vk)
            wr = head
            if heads_up_display:
                print("0 ", chex(wl), chex(wr), chex(hash(wl + wr)))
        else:
            wl = head
            wr = hash(vk)
            if heads_up_display:
                print("1 ", chex(wl), chex(wr), chex(hash(wl + wr)))
        w = tail
        while len(w) > 0:
            head, *tail = w
            hp = h - len(w)
            if (t // pow(2, hp)) % 2 == 0:
                wl = hash(wl + wr)
                wr = head
                if heads_up_display:
                    print("0 ", chex(wl), chex(wr), chex(hash(wl + wr)))
            else:
                wr = hash(wl + wr)
                wl = head
                if heads_up_display:
                    print("1 ", chex(wl), chex(wr), chex(hash(wl + wr)))
            w = tail
        bw = bw and r == hash(wl + wr)
        if heads_up_display:
            print("vk match?  ", r == hash(wl + wr), chex(r), chex(hash(wl + wr)))
    else:
        bw = bw and r == hash(vk)
    verify_key = VerifyKey(vk, encoder=RawEncoder)
    bs = test_signature(verify_key, sigma, m)
    if heads_up_display:
        print("Sigma verified?", bs)
    return bw and bs
