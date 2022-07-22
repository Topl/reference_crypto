## Digital signature specification
Secret keys provide bearer level authentication to network participants via elliptic curve based signing routines. 

This section describes Topl's supported signing routines and provides test vectors to ensure cryptographic integrity and facilitate integrations with the Topl protocol. 
For information on the key generation process, including hierarchical deterministic (HD) key derivation, please refer to `/generation`

Below are listed the supported signature constructions
### Curve25519-Axolotl
- [Specification](/specs/crypto/signing/Curve25519-Axolotl)
- [Test vectors](/specs/crypto/signing/Curve25519-Axolotl/Curve25519Axolotl.json)
- [Reference](https://github.com/signalapp/libaxolotl-j2me/blob/master/src/main/java/org/whispersystems/libaxolotl)
### Ed25519
- [Specification](/specs/crypto/signing/Ed25519)
- [Test vectors](/specs/crypto/signing/Ed25519/Ed25519.json)
- [Reference](https://datatracker.ietf.org/doc/html/rfc8032)
### ExtendedEd25519
- [Specification](/specs/crypto/signing/ExtendedEd25519)
- [Test vectors](/specs/crypto/signing/ExtendedEd25519/ExtendedEd25519.json)
- [Reference](https://ieeexplore.ieee.org/document/7966967)
### KES-Ed25519-Blake2b256-SC (-PC2)
- [Specification](/specs/crypto/signing/KES-Ed25519-Blake2b256-SC)
- [Reference](papers/kes_formal_spec/KES_Formal_Spec.pdf)
### VRF-Ed25519-Sha512-TAI
- [Specification](/specs/crypto/signing/VRF-Ed25519-Sha512-TAI)
- [Test vectors](/specs/crypto/signing/VRF-Ed25519-Sha512-TAI/VrfEd25519.json)
- [Reference](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-09)