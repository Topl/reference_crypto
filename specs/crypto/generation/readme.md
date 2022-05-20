## Description

## Key Concepts
- Entropy - An initial input of randomness to be used in deriving a unique output or seed
- Seed - The input to a key generation function for deterministically deriving a public private key pair
- Mnemonic Password - Also called a salt or generation password, used to provide an extra layer of randomness to the key derivation function in order to securely derive a unique entropy



## Mnemonics
Acceptable mnemonics for key generation in Topl's Bifrost client are derived from the [BIP-0039](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) standard.

To create a binary seed from the mnemonic, we use the PBKDF2 function with a mnemonic sentence (in UTF-8 NFKD) used as the password and the passphrase (again in UTF-8 NFKD) used as the salt. The iteration count is set to 4096 and HMAC-SHA512 is used as the pseudo-random function. The length of the derived key is 512 bits (= 64 bytes).



Let M be a BIP-0039 mnemonic and P the passphrase entered by the user.

Determine the initial entropy E that was used to generate M.

Compute S := PBKDF2-HMAC-SHA512(password = P, salt = E, iterations = 4096, dkLen = 96).

Modify S by assigning S[0] := S[0] & 0xf8 and S[31] := (S[31] & 0x1f) | 0x40.

Interpret S[0:32] as a 256-bit integer kL in little-endian byte order. Let kR := S[32:64] and use (kL, kR) as the root extended private key and c := S[64:96] as the root chain code.