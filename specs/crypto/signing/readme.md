## Supported Digital Signature Specification
Secret keys are used to provide bearer level authentication to network participants via elliptic curve based signing routines. 

This section describes Topl's supported signing routines and provides test vectors to ensure cryptographic integrity and facilitate integrations with the Topl protocol.

Additional information on supported generation schemes, including hierarchical deterministic (HD) key derivation, may be found in `/generation`

Below are listed the supported signature constructions
- [Curve25519-Axolotl]
  - [Reference](https://github.com/signalapp/libaxolotl-j2me/blob/master/src/main/java/org/whispersystems/libaxolotl/ecc/Curve.java)
  - [Link](specs/crypto/signing/Curve25519-Axolotl)
  - [Test Vectors](specs/crypto/signing/Curve25519-Axolotl/Curve25519Axolotl.json)
- [Ed25519](https://datatracker.ietf.org/doc/html/rfc8032)
- [ExtenedEd25519](https://ieeexplore.ieee.org/document/7966967)
- [KES-Ed25519-Blake2b256-SC (-PC2)](papers/kes_formal_spec/KES_Formal_Spec.pdf)
- [VRF-Ed25519-Sha512-TAI](https://datatracker.ietf.org/doc/html/draft-irtf-cfrg-vrf-09)