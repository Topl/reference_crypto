
_____________________________________________________________

Define mnemonic -> entropy -> seed pathway with
				mnemonic -> BIP-0039 -> entropy and
				entropy -> SLIP-0023 -> seed pathways defined at a high level

_____________________________________________________________




## Description
The test vectors for generating WhisperSystem Curve25519-Axolotl key pairs [[1](https://en.wikipedia.org/wiki/Double_Ratchet_Algorithm)][[2](https://github.com/tgalal/python-axolotl-curve25519)][[3](https://github.com/signalapp/libsignal-protocol-java)] is a modified set from [SLIP-0023]().

## Key Concepts
- Entropy - An initial input of randomness to be used in deriving a unique output or seed
- Seed - The input to a key generation function for deterministically deriving a public private key pair
- Mnemonic Password - Also called a salt or generation password, used to provide an extra layer of randomness to the key derivation function in order to securely derive a unique entropy

Table
