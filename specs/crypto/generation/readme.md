## Key Generation Specification
Secret keys are used to provide bearer level authentication to network participants via elliptic curve based signing routines. 

This section describes Topl's process for secret key generation over all supported signature routines. For information on signing routines and test vectors please refer to `/signing`[link](/specs/crypto/signing/)

Generation of these 

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