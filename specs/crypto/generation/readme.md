## Key Generation Specification
Secret keys are used to provide bearer level authentication to network participants via elliptic curve based signing routines. 

This section describes Topl's process for secret key generation over all supported signature routines. 
For information on signing routines and test vectors please refer to `/signing`.

While Topl supports several different secret key types and signing constructions, we have standardized the creation of each type of key to improve developer usability and provide for forward compatibility.


Generation of secret keys is a multi-step process that supports creation of random and hierarchical determinstic key pairs. 
Below is a summary of the relationship between the components involved in secret key generation.




 the Tetra era of the Topl protocol will delegate end-user bearer level authentication to use hierarchical deterministic wallets based on the Edwards 25519 (Ed25519) signing routine. 


Therefore Topl IS NOT BIP-32 or BIP-44 compatible as this standard is specified for the elliptic curve `secp256k1`[1](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki#conventions). 
Topl follows an algorithm known as [Bip32-Ed25519](/specs/crypto/generation/Ed25519_BIP Final.pdf) for child key derivation.
The Cardano network similarly provide HD key support using this scheme and as such have defined [CIP-1852](https://cips.cardano.org/cips/cip1852/) which specifies that `purpose = 1852'`
Furthermore, Topl has chosen `coin type = 7091'`

using a derivation path 


This implementation conforms to [SLIP-0023 Icarus](https://github.com/satoshilabs/slips/blob/master/slip-0023.md#cardano-icarus-master-node-derivation) for root key generation and . See [here](/specs/crypto/generation/readme.md) for more information.

 of secret keys by adhering to

## Mnemonic --[BIP-39]--> Entropy
BIP-39 mnemonic process



## Routine specific
Something about 

### Curve25519-Axolotl
- [Reference](https://github.com/signalapp/libaxolotl-j2me/blob/master/src/main/java/org/whispersystems/libaxolotl)
- [Link](/specs/crypto/signing/Curve25519-Axolotl)
- [Test vectors](/specs/crypto/signing/Curve25519-Axolotl/Curve25519Axolotl.json)
### Ed25519
- [Reference](https://datatracker.ietf.org/doc/html/rfc8032)
- [Link](/specs/crypto/signing/Ed25519)
- [Test vectors](/specs/crypto/signing/Ed25519/Ed25519.json)
### ExtendedEd25519
- [Reference](https://ieeexplore.ieee.org/document/7966967)
- [Link](/specs/crypto/signing/ExtendedEd25519)
- [Test vectors](/specs/crypto/signing/ExtendedEd25519/ExtendedEd25519.json)
### KES-Ed25519-Blake2b256-SC (-PC2)
- [Reference](papers/kes_formal_spec/KES_Formal_Spec.pdf)
- [Link](/specs/crypto/signing/KES-Ed25519-Blake2b256-SC)
### VRF-Ed25519-Sha512-TAI
- [Reference](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-09)
- [Link](/specs/crypto/signing/VRF-Ed25519-Sha512-TAI)
- [Test vectors](/specs/crypto/signing/VRF-Ed25519-Sha512-TAI/VrfEd25519.json)