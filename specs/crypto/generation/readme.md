## Description

## Key Concepts
- Entropy - An initial input of randomness to be used in deriving a unique output or seed
- Seed - The input to a key generation function for deterministically deriving a public private key pair
- Mnemonic Password - Also called a salt or generation password, used to provide an extra layer of randomness to the key derivation function in order to securely derive a unique entropy



## Mnemonics
Acceptable mnemonics for key generation in Topl's Bifrost client are derived from the [BIP-0039](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) standard.

To create a binary seed from the mnemonic, we use the PBKDF2 function with a mnemonic sentence (in UTF-8 NFKD) used as the password and the string "mnemonic" + passphrase (again in UTF-8 NFKD) used as the salt. The iteration count is set to 2048 and HMAC-SHA512 is used as the pseudo-random function. The length of the derived key is 512 bits (= 64 bytes).