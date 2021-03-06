## Description
Test vectors for Topl implementation of a single tree key evolving signature scheme in the construction of [Malkin-Micciancio-Miner](https://cseweb.ucsd.edu/~daniele/papers/MMM.pdf). A full specification including protocol box descriptions is available in this repo.
All values below are Hex encoded byte representations unless otherwise specified.

Table of Contents
- [Test vector - 1](#test-vector---1)
- [Test vector - 2](#test-vector---2)
- [Test vector - 3](#test-vector---3)
- [Test vector - 4](#test-vector---4)
- [Test vector - 5](#test-vector---5)
- [Test vector - 6](#test-vector---6)
- [Test vector - 7](#test-vector---7)
- [Test vector - 8](#test-vector---8)
- [Test vector - 9](#test-vector---9)
- [Test vector - 10](#test-vector---10)
## Test Vector - 1
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 1]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
5b74fae39b7a367da736490fa4a2bac992d011bcfb1d39b4dfdb4cf3a6dd1def
```
- h (int):

```1```

- Message (string):
```
"language shares a common tongue"
```
- Message (bytes) with `utf-8` encoding:
```
6c616e677561676520736861726573206120636f6d6d6f6e20746f6e677565
```
### Outputs
- Sum Composition Verification Key:
```
4162a383fd371823120a8bb8573dcb91d4b7e95e946598d202330f7cb0571a49
```
- Sum Composition Secret Key, t = 0:
```
Height: 1
Binary configuration: 0
Right Seed:    [485921a472aa49fb10ff914e4f57ce331c6e42f36fc58e0676f1c5c8c7281908]
Left Witness:  [6d35211032dfede271b1c311f84b3dabfaf0a664c2c6a16eb7b6a3b3130ebf35]
Right Witness: [6d44789d918310507d283b48c57b96a94f68b2fd13969df8d1ce1356a0726574]
Height: 0
Ed25519 Secret Key:       [2dbdcce64a39c09f8b9c827d5965fbbc9fe56adf9cb87e253eb2e52a707b77a8]
Ed25519 Verification Key: [210368f7c37b1e3c04b08dce0f28264af902388cfbc17b98e739adcf28b4edc5]
```
- Sigma t = 0:
```
Verification Key: [210368f7c37b1e3c04b08dce0f28264af902388cfbc17b98e739adcf28b4edc5]
Sigma: [3e2f86db64a383c144063c8a17a376e248e03a3e36e46607a03412f2f4d1b702f679e17368a58bb9d2f95a6eed27d6143663b116e4039fb05cb75f4bf9b1e10a]
W[0]: [6d44789d918310507d283b48c57b96a94f68b2fd13969df8d1ce1356a0726574]
```
- Sum Composition Secret Key, t = 0:
```
Height: 1
Binary configuration: 0
Right Seed:    [485921a472aa49fb10ff914e4f57ce331c6e42f36fc58e0676f1c5c8c7281908]
Left Witness:  [6d35211032dfede271b1c311f84b3dabfaf0a664c2c6a16eb7b6a3b3130ebf35]
Right Witness: [6d44789d918310507d283b48c57b96a94f68b2fd13969df8d1ce1356a0726574]
Height: 0
Ed25519 Secret Key:       [2dbdcce64a39c09f8b9c827d5965fbbc9fe56adf9cb87e253eb2e52a707b77a8]
Ed25519 Verification Key: [210368f7c37b1e3c04b08dce0f28264af902388cfbc17b98e739adcf28b4edc5]
```
- Sigma t = 1:
```
Verification Key: [46d553fcac44083dd37ce353ad683b9cc3c4867e49cc5ebc778a2b64f80f0510]
Sigma: [32d9610a6a6486a45b1f0328997dc20447f245378641799ddbe35a4fec20296e53b31fc63624a55bc80ae8892ff7b05c4089dc0253c98915db1c60c2e5e1d701]
W[0]: [6d35211032dfede271b1c311f84b3dabfaf0a664c2c6a16eb7b6a3b3130ebf35]
```
- Sum Composition Secret Key, t = 1:
```
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [6d35211032dfede271b1c311f84b3dabfaf0a664c2c6a16eb7b6a3b3130ebf35]
Right Witness: [6d44789d918310507d283b48c57b96a94f68b2fd13969df8d1ce1356a0726574]
Height: 0
Ed25519 Secret Key:       [485921a472aa49fb10ff914e4f57ce331c6e42f36fc58e0676f1c5c8c7281908]
Ed25519 Verification Key: [46d553fcac44083dd37ce353ad683b9cc3c4867e49cc5ebc778a2b64f80f0510]
```
## Test Vector - 2
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 1, 2, 3]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
cd6fbfd1305556ca26b98077c7b1b0df79559c09f693fe0fc920f9f53fb0959f
```
- h (int):

```2```

- Message (string):
```
"huddled masses with socks"
```
- Message (bytes) with `utf-8` encoding:
```
687564646c6564206d6173736573207769746820736f636b73
```
### Outputs
- Sum Composition Verification Key:
```
15482211cce0a8c90a564ec64632b1eeea40c75b4575851303690afcece729e2
```
- Sum Composition Secret Key, t = 0:
```
Height: 2
Binary configuration: 0
Right Seed:    [46508e16037e4a4ae3e1b60d5ccf327b808561e7d374a45a6f3bc5b44588158d]
Left Witness:  [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
Right Witness: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
Height: 1
Binary configuration: 0
Right Seed:    [2beb10fbe777095fc2532e61aee21bf33d74917e48ceeb11167fb9e2b9727a44]
Left Witness:  [a5bef7f1979ed0d776fed04c50c27c221b2f834b369744b4b84bc10e742fd396]
Right Witness: [5a856ffe0c9c680312a0847a56efa48f230da440d435ef8a6b2f5a5c5e140476]
Height: 0
Ed25519 Secret Key:       [aa7a50d1a4b2c2a0664e0467062889fa1690fe349347d7c88fb6f877c8d88351]
Ed25519 Verification Key: [7b3060f42759972ae50b70521f9f920587ba1aaa9434fa4e059da40f4aa53f94]
```
- Sigma t = 0:
```
Verification Key: [7b3060f42759972ae50b70521f9f920587ba1aaa9434fa4e059da40f4aa53f94]
Sigma: [5ba965947324fea9e78df19f7a2859f58aa2440ee2afad4c66e64f23ddfaafedcd27d7b8fd0db75c83caea394f270720407bdb0f4203a4d4d49f2f84b4f3a10b]
W[0]: [5a856ffe0c9c680312a0847a56efa48f230da440d435ef8a6b2f5a5c5e140476]
W[1]: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
```
- Sum Composition Secret Key, t = 0:
```
Height: 2
Binary configuration: 0
Right Seed:    [46508e16037e4a4ae3e1b60d5ccf327b808561e7d374a45a6f3bc5b44588158d]
Left Witness:  [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
Right Witness: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
Height: 1
Binary configuration: 0
Right Seed:    [2beb10fbe777095fc2532e61aee21bf33d74917e48ceeb11167fb9e2b9727a44]
Left Witness:  [a5bef7f1979ed0d776fed04c50c27c221b2f834b369744b4b84bc10e742fd396]
Right Witness: [5a856ffe0c9c680312a0847a56efa48f230da440d435ef8a6b2f5a5c5e140476]
Height: 0
Ed25519 Secret Key:       [aa7a50d1a4b2c2a0664e0467062889fa1690fe349347d7c88fb6f877c8d88351]
Ed25519 Verification Key: [7b3060f42759972ae50b70521f9f920587ba1aaa9434fa4e059da40f4aa53f94]
```
- Sigma t = 1:
```
Verification Key: [9bef5555cb073c4b675fd182ca6d78dcfe19364dbeae5283a1888b42fbe55e3d]
Sigma: [099a205e1152bf98ded60373921a32dfe9a9f28fbfc09364bf533f7bef35d5e6c4fb000fb539bcae2a5913ef3c844d466b69c6f2e52c46bafe3275da53cc520a]
W[0]: [a5bef7f1979ed0d776fed04c50c27c221b2f834b369744b4b84bc10e742fd396]
W[1]: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
```
- Sum Composition Secret Key, t = 1:
```
Height: 2
Binary configuration: 0
Right Seed:    [46508e16037e4a4ae3e1b60d5ccf327b808561e7d374a45a6f3bc5b44588158d]
Left Witness:  [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
Right Witness: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [a5bef7f1979ed0d776fed04c50c27c221b2f834b369744b4b84bc10e742fd396]
Right Witness: [5a856ffe0c9c680312a0847a56efa48f230da440d435ef8a6b2f5a5c5e140476]
Height: 0
Ed25519 Secret Key:       [2beb10fbe777095fc2532e61aee21bf33d74917e48ceeb11167fb9e2b9727a44]
Ed25519 Verification Key: [9bef5555cb073c4b675fd182ca6d78dcfe19364dbeae5283a1888b42fbe55e3d]
```
- Sigma t = 2:
```
Verification Key: [57d6a9536c0250183bc31d4e6fc2388a22fe498e57a6dc8a91fb8508694f6a3d]
Sigma: [2965bae2c6c968ed160523ba886af63f3ca82bd9f8d7ecbf31a8ea0fef8bd95b2afc2a2120c5ae31db2ef29fa322e7f2db31cdf6c0c392bb1be7c9743bba3b0b]
W[0]: [9183ed1e702fc2f4983bc461e551d80df3d21b4eb284448e9e35f8a5691d92da]
W[1]: [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
```
- Sum Composition Secret Key, t = 2:
```
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
Right Witness: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
Height: 1
Binary configuration: 0
Right Seed:    [d3ea29a958eb0a628f655a0820a506c61efbfc5fe5dc0ddd70d0da01d8468170]
Left Witness:  [5b4b52bc5dd65cb4c8e6ab2faa906c595bc607fab3a1f9f17f2ccf5ddcf798a1]
Right Witness: [9183ed1e702fc2f4983bc461e551d80df3d21b4eb284448e9e35f8a5691d92da]
Height: 0
Ed25519 Secret Key:       [cfdfad8312acd5c5ca97a986878cdeb8ee51df60ed0bb4bd969d49628502c11e]
Ed25519 Verification Key: [57d6a9536c0250183bc31d4e6fc2388a22fe498e57a6dc8a91fb8508694f6a3d]
```
- Sigma t = 3:
```
Verification Key: [c3dcdaab1292b810b55db8758258824cd73bf913fc59a2f1038fa707bbaff3b6]
Sigma: [81de65fa1e27a33c006f173b2119aa190882d13034afc2ccd184c4a7e3549fc123bfa85be23438ac47fa22504b3253bf96bce3a1a849e9415e635581056d5f0c]
W[0]: [5b4b52bc5dd65cb4c8e6ab2faa906c595bc607fab3a1f9f17f2ccf5ddcf798a1]
W[1]: [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
```
- Sum Composition Secret Key, t = 3:
```
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [615244e7bd05088fb462ba9e7b995d71129b91b42652c06780b17936eb456461]
Right Witness: [7fcd9f9bd1c918654416cdcd2ed908a0f978c58f2123ae896d9df28b42c59367]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [5b4b52bc5dd65cb4c8e6ab2faa906c595bc607fab3a1f9f17f2ccf5ddcf798a1]
Right Witness: [9183ed1e702fc2f4983bc461e551d80df3d21b4eb284448e9e35f8a5691d92da]
Height: 0
Ed25519 Secret Key:       [d3ea29a958eb0a628f655a0820a506c61efbfc5fe5dc0ddd70d0da01d8468170]
Ed25519 Verification Key: [c3dcdaab1292b810b55db8758258824cd73bf913fc59a2f1038fa707bbaff3b6]
```
## Test Vector - 3
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 2, 5, 7]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
36d37def07d10f7acb1570cca5b56237b3d5700fd4f5e5b5c44d6af09f2c2ffb
```
- h (int):

```3```

- Message (string):
```
"arriving on time and late"
```
- Message (bytes) with `utf-8` encoding:
```
6172726976696e67206f6e2074696d6520616e64206c617465
```
### Outputs
- Sum Composition Verification Key:
```
deafadc6b9aa9a018871b54f5d9bfe6acaa3d1ad82e9fadefa347ae9fbc920e7
```
- Sum Composition Secret Key, t = 0:
```
Height: 3
Binary configuration: 0
Right Seed:    [06a99c2454c27c84972c4853b58715f67fdd12932f7dffa016aed0ca19ba012e]
Left Witness:  [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
Right Witness: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
Height: 2
Binary configuration: 0
Right Seed:    [a9b24f826c9231d90d6027a722c2d9a5e1343ea4fe13c10f5b76eb3f061f7a62]
Left Witness:  [b22e36aad1b810dbcca01681cf9b4273633aa5467d3a36ce215f94f194c9a99b]
Right Witness: [581b77b90035b18faa4ea080cf7d653902d9c9903539f21156c948ec1a39d0fb]
Height: 1
Binary configuration: 0
Right Seed:    [cab37238f7079c32261990fd67bba3954cf5bb1b24ae0252646395f398116b76]
Left Witness:  [fbe097b1066d63a8129cefee098eadeca6bf328574ed21aefc5dd4d7d8cce461]
Right Witness: [a5b68a7fad1976bc2f38a46279eca5624f303236f334663e08bbc876765c4533]
Height: 0
Ed25519 Secret Key:       [12b29d8d9d7ecbbc9c1b29d7d42299fa06133d60ba3ff9a6489ad3d38c99a38c]
Ed25519 Verification Key: [79d37776daaf3a2952bdc9124d7228175f4f6fdd3fe83c42bddd4f61b68df1cc]
```
- Sigma t = 0:
```
Verification Key: [79d37776daaf3a2952bdc9124d7228175f4f6fdd3fe83c42bddd4f61b68df1cc]
Sigma: [bcb07a0e68a5ad2b696b44a56a651a95e65885a6908c8fa92825f9ad510fd84cd4e0d67601cd06d17eae8554f5eac5cca817033b3d011924245589fc047db90d]
W[0]: [a5b68a7fad1976bc2f38a46279eca5624f303236f334663e08bbc876765c4533]
W[1]: [581b77b90035b18faa4ea080cf7d653902d9c9903539f21156c948ec1a39d0fb]
W[2]: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
```
- Sum Composition Secret Key, t = 0:
```
Height: 3
Binary configuration: 0
Right Seed:    [06a99c2454c27c84972c4853b58715f67fdd12932f7dffa016aed0ca19ba012e]
Left Witness:  [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
Right Witness: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
Height: 2
Binary configuration: 0
Right Seed:    [a9b24f826c9231d90d6027a722c2d9a5e1343ea4fe13c10f5b76eb3f061f7a62]
Left Witness:  [b22e36aad1b810dbcca01681cf9b4273633aa5467d3a36ce215f94f194c9a99b]
Right Witness: [581b77b90035b18faa4ea080cf7d653902d9c9903539f21156c948ec1a39d0fb]
Height: 1
Binary configuration: 0
Right Seed:    [cab37238f7079c32261990fd67bba3954cf5bb1b24ae0252646395f398116b76]
Left Witness:  [fbe097b1066d63a8129cefee098eadeca6bf328574ed21aefc5dd4d7d8cce461]
Right Witness: [a5b68a7fad1976bc2f38a46279eca5624f303236f334663e08bbc876765c4533]
Height: 0
Ed25519 Secret Key:       [12b29d8d9d7ecbbc9c1b29d7d42299fa06133d60ba3ff9a6489ad3d38c99a38c]
Ed25519 Verification Key: [79d37776daaf3a2952bdc9124d7228175f4f6fdd3fe83c42bddd4f61b68df1cc]
```
- Sigma t = 2:
```
Verification Key: [8b0126047439415a5dba9e426bce4c1a991d37c5ffa1b43c1172fd6f83503069]
Sigma: [0e95cfa983c878cee7caa3f776cd2e67fd2c6145b2fd2d8fe1bc3a72ec6812e2319a821b805ddd680605638b8571efab78ae6af957359f01b1a5b1db19d12205]
W[0]: [e65e5c7a60a9e849bb1ce1f6ce2f6a5e018e8876f0842846555dc5ca78cdce8f]
W[1]: [b22e36aad1b810dbcca01681cf9b4273633aa5467d3a36ce215f94f194c9a99b]
W[2]: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
```
- Sum Composition Secret Key, t = 2:
```
Height: 3
Binary configuration: 0
Right Seed:    [06a99c2454c27c84972c4853b58715f67fdd12932f7dffa016aed0ca19ba012e]
Left Witness:  [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
Right Witness: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b22e36aad1b810dbcca01681cf9b4273633aa5467d3a36ce215f94f194c9a99b]
Right Witness: [581b77b90035b18faa4ea080cf7d653902d9c9903539f21156c948ec1a39d0fb]
Height: 1
Binary configuration: 0
Right Seed:    [e63fbd8ad08b80a8f2dc043ae5f39cd2c4127d90afbb755cc34b4f2f3f2fc92f]
Left Witness:  [7f9c6da4090a4e47469b2493fc66f7e5c63b9128479846877f619673d011393f]
Right Witness: [e65e5c7a60a9e849bb1ce1f6ce2f6a5e018e8876f0842846555dc5ca78cdce8f]
Height: 0
Ed25519 Secret Key:       [233180aad2bc5bc0fd9ad53f931513c1bba8c154e2e51a3dcae55c7368daffb6]
Ed25519 Verification Key: [8b0126047439415a5dba9e426bce4c1a991d37c5ffa1b43c1172fd6f83503069]
```
- Sigma t = 5:
```
Verification Key: [37a1dcaf5b889bdebf17f8c66a27b83a4a8dcf79fe8b0ab1e26c6852a29a6683]
Sigma: [9ed7112b8a92645c34f3271d181cc29b5a4a4e2bdf90a40abffa5f6020cb56993a880a97e094c2d673fa9a789b10979b17e649a2e9ac0b7bc7bc768404255001]
W[0]: [5e1923f93aff941e5d9a7b259c8589dbe088d4540aa729887781d27905002907]
W[1]: [95e63597096d10330505e0d0c505c46dd0388c4a6cb6f033d060ece90c8ee966]
W[2]: [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
```
- Sum Composition Secret Key, t = 5:
```
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
Right Witness: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
Height: 2
Binary configuration: 0
Right Seed:    [2906f6e054de326e705a175df4b3b865bb79c60509821d833a25c4611b1aa71c]
Left Witness:  [164717632cf3e0016d84dbaa60bd593e3bc50b7dfece3cc1adb79aa99583fc63]
Right Witness: [95e63597096d10330505e0d0c505c46dd0388c4a6cb6f033d060ece90c8ee966]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [5e1923f93aff941e5d9a7b259c8589dbe088d4540aa729887781d27905002907]
Right Witness: [6cc805c000acc015d9ee32204ec55c9e58bb9fbfd10e69a3debf32a258cd663b]
Height: 0
Ed25519 Secret Key:       [10df9d3f022949004651f1a3f916322fcc98e7ab510737ef611fc0aeb29369c2]
Ed25519 Verification Key: [37a1dcaf5b889bdebf17f8c66a27b83a4a8dcf79fe8b0ab1e26c6852a29a6683]
```
- Sigma t = 7:
```
Verification Key: [4fee4bf190c11d0cf7175550343da416928a12bc6d0feb2c889f513d58fd8217]
Sigma: [859a8e078f1f4b21303d33076c4ee0f1d1337bb5441837c66bd68f7518da98192b3c3361c1ece772adea47e09a0a230e814c64a75a6057b51cd0f7909d6c5a06]
W[0]: [a0b175ed12fecdc8b686da7d448101e8e407d8e33687288a638862bf62dd5e25]
W[1]: [164717632cf3e0016d84dbaa60bd593e3bc50b7dfece3cc1adb79aa99583fc63]
W[2]: [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
```
- Sum Composition Secret Key, t = 7:
```
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [2c8b7318be3bcf7963fed0545fcae11ab48d60163487a7cf3e8574c36e5d75e0]
Right Witness: [0ada5190f9f8a7ac5d8ba424dbc29ab4135444bbe459a77c598032d60c8d5b8e]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [164717632cf3e0016d84dbaa60bd593e3bc50b7dfece3cc1adb79aa99583fc63]
Right Witness: [95e63597096d10330505e0d0c505c46dd0388c4a6cb6f033d060ece90c8ee966]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [a0b175ed12fecdc8b686da7d448101e8e407d8e33687288a638862bf62dd5e25]
Right Witness: [9ea952a5dbde1d32dae9dd36d88d0bdb8f8c4a9a869d9be1ddfbba002abf2f66]
Height: 0
Ed25519 Secret Key:       [6fc310071acdd2f85aa2a3be5a5c570c4e383c26ef27b895f1e4251b4178b778]
Ed25519 Verification Key: [4fee4bf190c11d0cf7175550343da416928a12bc6d0feb2c889f513d58fd8217]
```
## Test Vector - 4
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 5, 10, 15]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
351f09534baf61171893903ab6f122b82ff21dd775f3d853fcd52ee91cb40178
```
- h (int):

```4```

- Message (string):
```
"wonder where width went"
```
- Message (bytes) with `utf-8` encoding:
```
776f6e6465722077686572652077696474682077656e74
```
### Outputs
- Sum Composition Verification Key:
```
be127e4da6622de7785a221faa76ad008a0e1cb4f41ca2cd937554cc268ae7ce
```
- Sum Composition Secret Key, t = 0:
```
Height: 4
Binary configuration: 0
Right Seed:    [73b4a2db7ef6ff14c6eeda34af394dad5bcc9dcbe307505429293b37484f71d0]
Left Witness:  [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
Right Witness: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
Height: 3
Binary configuration: 0
Right Seed:    [9b8886fd57b8f59a3552cb1d55b3649abcfb1fe951afac985b31e828f97e3899]
Left Witness:  [46e57576ca928be69a373b957e4f0641a886806f6c87ce0679096daedb311f32]
Right Witness: [640652610bfa34bdc65fed175f6a4997ac2b95aa7e948b6b5df2df5826d62ed9]
Height: 2
Binary configuration: 0
Right Seed:    [4530f34e825260eac5de226140eaa15291e35a897b0a443de9311158680459e3]
Left Witness:  [a835af973ae266588962354b16b3529bd6bae097991f94d06d72bda4b5b4c5c9]
Right Witness: [551c64f9e4bcc5996f15ca8ab54d1f3d7fda472ac2174f9706332abe9940f7e5]
Height: 1
Binary configuration: 0
Right Seed:    [f6b1756ecc23d90b1c5d36e310716509c51b73addb83997fab7fefa61b59c1eb]
Left Witness:  [436bff732016c3f94a80723cf328ea51fd0bc3da49b88a046eda72225c81f932]
Right Witness: [fd2a8bb21fff75a6db541253f5a48e652d882dba3475edabb5145c2d95a7f70e]
Height: 0
Ed25519 Secret Key:       [1b8ae97e228eeae635df7ad1b8b9a1b2e5eef68929111e63722e6f3f16cc7289]
Ed25519 Verification Key: [a9679e07331d0d007dcdc5097b742aa51a3a8b02ca0abd3fb627649fc0eadce7]
```
- Sigma t = 0:
```
Verification Key: [a9679e07331d0d007dcdc5097b742aa51a3a8b02ca0abd3fb627649fc0eadce7]
Sigma: [f0c469c5771b84b88f9dd08e43ef64e976cc0d38cb73b8c9517346106cbc122399f707a4e9aa505652e88da4059a2e52eec3bb6915ac46f6157d3d4c7e61ca00]
W[0]: [fd2a8bb21fff75a6db541253f5a48e652d882dba3475edabb5145c2d95a7f70e]
W[1]: [551c64f9e4bcc5996f15ca8ab54d1f3d7fda472ac2174f9706332abe9940f7e5]
W[2]: [640652610bfa34bdc65fed175f6a4997ac2b95aa7e948b6b5df2df5826d62ed9]
W[3]: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
```
- Sum Composition Secret Key, t = 0:
```
Height: 4
Binary configuration: 0
Right Seed:    [73b4a2db7ef6ff14c6eeda34af394dad5bcc9dcbe307505429293b37484f71d0]
Left Witness:  [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
Right Witness: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
Height: 3
Binary configuration: 0
Right Seed:    [9b8886fd57b8f59a3552cb1d55b3649abcfb1fe951afac985b31e828f97e3899]
Left Witness:  [46e57576ca928be69a373b957e4f0641a886806f6c87ce0679096daedb311f32]
Right Witness: [640652610bfa34bdc65fed175f6a4997ac2b95aa7e948b6b5df2df5826d62ed9]
Height: 2
Binary configuration: 0
Right Seed:    [4530f34e825260eac5de226140eaa15291e35a897b0a443de9311158680459e3]
Left Witness:  [a835af973ae266588962354b16b3529bd6bae097991f94d06d72bda4b5b4c5c9]
Right Witness: [551c64f9e4bcc5996f15ca8ab54d1f3d7fda472ac2174f9706332abe9940f7e5]
Height: 1
Binary configuration: 0
Right Seed:    [f6b1756ecc23d90b1c5d36e310716509c51b73addb83997fab7fefa61b59c1eb]
Left Witness:  [436bff732016c3f94a80723cf328ea51fd0bc3da49b88a046eda72225c81f932]
Right Witness: [fd2a8bb21fff75a6db541253f5a48e652d882dba3475edabb5145c2d95a7f70e]
Height: 0
Ed25519 Secret Key:       [1b8ae97e228eeae635df7ad1b8b9a1b2e5eef68929111e63722e6f3f16cc7289]
Ed25519 Verification Key: [a9679e07331d0d007dcdc5097b742aa51a3a8b02ca0abd3fb627649fc0eadce7]
```
- Sigma t = 5:
```
Verification Key: [f17086c76d2ba3c587f3bbbdf6cb457e2f25b6c7e5f0f7b53916a09991edb19c]
Sigma: [34d93cbd32f654862bdc5005def956f0791226f71b40f19cd1d656c9038ec7fa813426f3a261fec8f6645e5d4a3c8a6627ab8e41db88ba3fa383f6e01972400e]
W[0]: [1729eaa48403f75cc25f678f36467764fb3af1a926e30a6b27efbdaf0cf3d13e]
W[1]: [8ff3f095b1d1f6d6727aa3197c7e3c2e5fb4db14d7b75e6694a40d5e1a757352]
W[2]: [46e57576ca928be69a373b957e4f0641a886806f6c87ce0679096daedb311f32]
W[3]: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
```
- Sum Composition Secret Key, t = 5:
```
Height: 4
Binary configuration: 0
Right Seed:    [73b4a2db7ef6ff14c6eeda34af394dad5bcc9dcbe307505429293b37484f71d0]
Left Witness:  [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
Right Witness: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [46e57576ca928be69a373b957e4f0641a886806f6c87ce0679096daedb311f32]
Right Witness: [640652610bfa34bdc65fed175f6a4997ac2b95aa7e948b6b5df2df5826d62ed9]
Height: 2
Binary configuration: 0
Right Seed:    [f618eb801f3fd37dda9bbc71a8767c7f353b36a0c94d8751798b70cf2ec2f2a5]
Left Witness:  [7e1aadec1bbaab284d0ce214fba9af7c94e8e1fa5d42b2e50e94c95f377dc306]
Right Witness: [8ff3f095b1d1f6d6727aa3197c7e3c2e5fb4db14d7b75e6694a40d5e1a757352]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [1729eaa48403f75cc25f678f36467764fb3af1a926e30a6b27efbdaf0cf3d13e]
Right Witness: [d93e647b529a11268676cec45d940e623ddaab8f0f433f9c26006141b82fc9d5]
Height: 0
Ed25519 Secret Key:       [89aaf81813abdda0febb76e2192d4103baf50203728edd0368340816c29afcea]
Ed25519 Verification Key: [f17086c76d2ba3c587f3bbbdf6cb457e2f25b6c7e5f0f7b53916a09991edb19c]
```
- Sigma t = 10:
```
Verification Key: [57ba0d6fd664d30a5e4186b601c887a8e7fa9c78e50cd3351b704f1a3740a4c1]
Sigma: [d15c37f8c4fae4151fe3fa9ec5574a123dbbac849caa3c2ee124ad438aa8ff7a38eaf6da50940d42e1dff69dacb6977345125773822a8d97109a9029d8efab07]
W[0]: [74a6f25b5a9a99049f12c05abdbe5e852c767dbeb6ca79689b148434de8e3433]
W[1]: [c95a8684e9590035520e33074985b2ab2f14b5f072fc3ad2c450d23bf4a08f58]
W[2]: [215c74ddbd507b6227beaf1a13a53ee843b2fb2edaca856b67590cdb66c6d818]
W[3]: [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
```
- Sum Composition Secret Key, t = 10:
```
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
Right Witness: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
Height: 3
Binary configuration: 0
Right Seed:    [c19d6b0eca2cb4dcde20f5cde3ed83eb4a35fa122f2c8d2a45deadad260dbf96]
Left Witness:  [6d763b9fcf4de3c806d272b022fb48fb29e366de8da178fbf3fc55ddaf4a1e08]
Right Witness: [215c74ddbd507b6227beaf1a13a53ee843b2fb2edaca856b67590cdb66c6d818]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [c95a8684e9590035520e33074985b2ab2f14b5f072fc3ad2c450d23bf4a08f58]
Right Witness: [c1e8395905430673b55c38f6db33ee53c3468254dea74de4deccb8e5f9fa1b33]
Height: 1
Binary configuration: 0
Right Seed:    [95f99572edc35415f2b3d07a25d821e986f786647d740dd260cb1d5d81fbc154]
Left Witness:  [ee7d0cffc59738f6ebb5a82312a3f5035b213bf330219e6884d02025cb120720]
Right Witness: [74a6f25b5a9a99049f12c05abdbe5e852c767dbeb6ca79689b148434de8e3433]
Height: 0
Ed25519 Secret Key:       [717f1b5b4cf9bc7e7b0dd145161a4cd3760e027cdf4380395a267cf678e4d683]
Ed25519 Verification Key: [57ba0d6fd664d30a5e4186b601c887a8e7fa9c78e50cd3351b704f1a3740a4c1]
```
- Sigma t = 15:
```
Verification Key: [7f31b22fd7c0240f48fd6ee684b66e7ef80a73c9fc92a38343c8add30c0c468c]
Sigma: [6796e393202e19a74a20f6d449f0704c1891a4957a42342303bdadc7543e6e298836ab9e1374281f4514ae7794e1273efd0c6f742987fd68296c4d7a07639007]
W[0]: [07e5324bafee617d5bfab36b357bf8bad39e1fdf41cd28bd0881e6dec45b10de]
W[1]: [b0fb6589fe3b694650ec8c847f41b6525ef672632ede69cf0330c630ecd414ec]
W[2]: [6d763b9fcf4de3c806d272b022fb48fb29e366de8da178fbf3fc55ddaf4a1e08]
W[3]: [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
```
- Sum Composition Secret Key, t = 15:
```
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [df602c5c6d0eafd2db7c6de7f0ee0ca72e12579450808c3827fb0cdc42836f63]
Right Witness: [b737aa8e49a4b642a1162e0124a39c3bba4d83fee4d3747816e38482e6d2ae86]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [6d763b9fcf4de3c806d272b022fb48fb29e366de8da178fbf3fc55ddaf4a1e08]
Right Witness: [215c74ddbd507b6227beaf1a13a53ee843b2fb2edaca856b67590cdb66c6d818]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b0fb6589fe3b694650ec8c847f41b6525ef672632ede69cf0330c630ecd414ec]
Right Witness: [f4ca5da685e5d11715aae9d5b102dfb4ac4ae3e2d94d280c91b507d9ecb029b9]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [07e5324bafee617d5bfab36b357bf8bad39e1fdf41cd28bd0881e6dec45b10de]
Right Witness: [cf9dd4c880310d301c49e3ddc80f65e58606d498fa29563fad725cbfc29d6c30]
Height: 0
Ed25519 Secret Key:       [a7a43324111acf0c919eb62770fa455e3f29ef7b62754748008dc4a02d68d4ae]
Ed25519 Verification Key: [7f31b22fd7c0240f48fd6ee684b66e7ef80a73c9fc92a38343c8add30c0c468c]
```
## Test Vector - 5
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 10, 21, 31]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
c77bbf01a20dea8cfbd9acce52134a845c67bfd9b2cfa5c115f3a9c8597dcd03
```
- h (int):

```5```

- Message (string):
```
"me or it - either way you jump off"
```
- Message (bytes) with `utf-8` encoding:
```
6d65206f72206974202d206569746865722077617920796f75206a756d70206f6666
```
### Outputs
- Sum Composition Verification Key:
```
70c0d236d2892d1745b8c0547d93bb8ab48adbf7e4498af5dbc123a3fdf80e21
```
- Sum Composition Secret Key, t = 0:
```
Height: 5
Binary configuration: 0
Right Seed:    [ccc4a0dde44fcefb22405b4ff19977052a1532d3091f955ef3e5abc03645ef01]
Left Witness:  [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
Right Witness: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
Height: 4
Binary configuration: 0
Right Seed:    [5291e4c74409f560e6c61f44af442119b89f3eaea4d64705a89f17e9114f1d7e]
Left Witness:  [0e036b4627a99ce67f9e94452f6837018123b354654129e19f4dbb70429eb891]
Right Witness: [a0d5cedc00c1993ea3bc06c5f8d196a1902266266d51390ef5bc15073a5be086]
Height: 3
Binary configuration: 0
Right Seed:    [faa3f535cbb7a11257088eae8fd4c3a71a28cc7a1daeec2752efbd39e856067d]
Left Witness:  [3645586c95971bd4a70b40fa11a36cb9420fa3dbb07e81a04bba3ab3fabecdaa]
Right Witness: [47803271bc0b85a8bee2e04ad1a2dbe7b66457d04912c65909027f794d971038]
Height: 2
Binary configuration: 0
Right Seed:    [253176cb71bbcdaf71cfc260f9224d09a664f72892b19be6b99dd62c3eb84a11]
Left Witness:  [e7df5c216086530da233ff0a8f79e35ccbf521bea891278593be4930a8e595af]
Right Witness: [3ab1ccf0e083de049cfbe02e037d23ee8173af82531d8b4fd3a6ee2e4881be3d]
Height: 1
Binary configuration: 0
Right Seed:    [ffbe71e0d1364d68a720807ddce89558fbeddbb4bebeac4a772740c8497c7592]
Left Witness:  [abd99fbdf41f2489f9ef65142665a0e153011d04c3139e183ba39138b867ce82]
Right Witness: [2398f25f7637ae13081ba4b7674b9123f54eab960ec751a0166d76dce379b84c]
Height: 0
Ed25519 Secret Key:       [5797a3fff494de10e69e3cf99e553830b3eb84608ab9c8276ca47a3cee9b3da2]
Ed25519 Verification Key: [bfb3bd77c3195566c00779a8a3be98e48687efb9fe0703fef255188abe3e8c86]
```
- Sigma t = 0:
```
Verification Key: [bfb3bd77c3195566c00779a8a3be98e48687efb9fe0703fef255188abe3e8c86]
Sigma: [97ed7c65fce2ede533ab5476e43e2f627d3dbf2d6f0d8baeb971e7392c291fb10c4ec2b9103b7df5052fb4f7c7df0906d2c14b22770749781f85e95654e30e0b]
W[0]: [2398f25f7637ae13081ba4b7674b9123f54eab960ec751a0166d76dce379b84c]
W[1]: [3ab1ccf0e083de049cfbe02e037d23ee8173af82531d8b4fd3a6ee2e4881be3d]
W[2]: [47803271bc0b85a8bee2e04ad1a2dbe7b66457d04912c65909027f794d971038]
W[3]: [a0d5cedc00c1993ea3bc06c5f8d196a1902266266d51390ef5bc15073a5be086]
W[4]: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
```
- Sum Composition Secret Key, t = 0:
```
Height: 5
Binary configuration: 0
Right Seed:    [ccc4a0dde44fcefb22405b4ff19977052a1532d3091f955ef3e5abc03645ef01]
Left Witness:  [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
Right Witness: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
Height: 4
Binary configuration: 0
Right Seed:    [5291e4c74409f560e6c61f44af442119b89f3eaea4d64705a89f17e9114f1d7e]
Left Witness:  [0e036b4627a99ce67f9e94452f6837018123b354654129e19f4dbb70429eb891]
Right Witness: [a0d5cedc00c1993ea3bc06c5f8d196a1902266266d51390ef5bc15073a5be086]
Height: 3
Binary configuration: 0
Right Seed:    [faa3f535cbb7a11257088eae8fd4c3a71a28cc7a1daeec2752efbd39e856067d]
Left Witness:  [3645586c95971bd4a70b40fa11a36cb9420fa3dbb07e81a04bba3ab3fabecdaa]
Right Witness: [47803271bc0b85a8bee2e04ad1a2dbe7b66457d04912c65909027f794d971038]
Height: 2
Binary configuration: 0
Right Seed:    [253176cb71bbcdaf71cfc260f9224d09a664f72892b19be6b99dd62c3eb84a11]
Left Witness:  [e7df5c216086530da233ff0a8f79e35ccbf521bea891278593be4930a8e595af]
Right Witness: [3ab1ccf0e083de049cfbe02e037d23ee8173af82531d8b4fd3a6ee2e4881be3d]
Height: 1
Binary configuration: 0
Right Seed:    [ffbe71e0d1364d68a720807ddce89558fbeddbb4bebeac4a772740c8497c7592]
Left Witness:  [abd99fbdf41f2489f9ef65142665a0e153011d04c3139e183ba39138b867ce82]
Right Witness: [2398f25f7637ae13081ba4b7674b9123f54eab960ec751a0166d76dce379b84c]
Height: 0
Ed25519 Secret Key:       [5797a3fff494de10e69e3cf99e553830b3eb84608ab9c8276ca47a3cee9b3da2]
Ed25519 Verification Key: [bfb3bd77c3195566c00779a8a3be98e48687efb9fe0703fef255188abe3e8c86]
```
- Sigma t = 10:
```
Verification Key: [2c3893ffb5eaa06b10baab53e2302103210465f4b02a947756040606c6047920]
Sigma: [dd689f98054fb4d85c747a808a196434051a67a52e51c405d49c6153f767ef8586669525a9ebde5a4d5395c220c48fae29e6088a9e8419b38b9189eb9a78d206]
W[0]: [14ec66d47c77c530382146ddffce027a7d14221f336f5ac3fc37cc369c1c19bf]
W[1]: [c8c437996395666af653895d0b1e74b2bd8771bd0c96ec78d2f3a2c6a8ad434f]
W[2]: [0c86200d9fbf50c21a5e03e2804ddacc19cb8b86e6ace577fa7813b39046c405]
W[3]: [0e036b4627a99ce67f9e94452f6837018123b354654129e19f4dbb70429eb891]
W[4]: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
```
- Sum Composition Secret Key, t = 10:
```
Height: 5
Binary configuration: 0
Right Seed:    [ccc4a0dde44fcefb22405b4ff19977052a1532d3091f955ef3e5abc03645ef01]
Left Witness:  [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
Right Witness: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [0e036b4627a99ce67f9e94452f6837018123b354654129e19f4dbb70429eb891]
Right Witness: [a0d5cedc00c1993ea3bc06c5f8d196a1902266266d51390ef5bc15073a5be086]
Height: 3
Binary configuration: 0
Right Seed:    [b6ba3c7d10bc7497b65068ef4e2e552f1713d080e35b398a3a48ca941a5127ca]
Left Witness:  [ec79206fc7eebc19e13da1ba3b39a0c6e000109594fa8e59e288798d98e09469]
Right Witness: [0c86200d9fbf50c21a5e03e2804ddacc19cb8b86e6ace577fa7813b39046c405]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [c8c437996395666af653895d0b1e74b2bd8771bd0c96ec78d2f3a2c6a8ad434f]
Right Witness: [d373bec17c0fa65667d2e12cb92df0bc7e39d6fd96db5ec9139583cd6e44c3a2]
Height: 1
Binary configuration: 0
Right Seed:    [e73bf8c153f09ee90ea26b0159c5553b1b9ee0563c98605046da5abd47e75bbc]
Left Witness:  [edc8ee419ce9f3fd114c2b83b4ec65a4b1c010dc12607d5e91c2b83c576b84b2]
Right Witness: [14ec66d47c77c530382146ddffce027a7d14221f336f5ac3fc37cc369c1c19bf]
Height: 0
Ed25519 Secret Key:       [956207d67884afede60233ab62fa6961681c429e58aae8fa99b23f23d42f3be2]
Ed25519 Verification Key: [2c3893ffb5eaa06b10baab53e2302103210465f4b02a947756040606c6047920]
```
- Sigma t = 21:
```
Verification Key: [d43476ed2380b1b96902bfaec96c1f675ad113bd55d86b506c9a26895a69b496]
Sigma: [cfd4e8a463ee8c32ca3781edeaefc4673b98631ad0b4ddfcf69baf2a5c6749734dea5401395e3c27063d1d44f13f911a7a2b738fd7bdb359ce7b4b99f8b8f90b]
W[0]: [c77f68fe69b444a67b5544d59635dd5391cf065849c5f443705be9f5f080d9f5]
W[1]: [23273d7995ee43d27d4ab9320774707f50b6d2170f1648540167db548d1032ea]
W[2]: [b8439adb5dec5d6c8775cfadfc6568bd3682a08a5d328452b7823ceeff59a984]
W[3]: [8fab6b378cfa4554103345586bdf2db37897c9fdc91e0d378e16bfced6f44d82]
W[4]: [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
```
- Sum Composition Secret Key, t = 21:
```
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
Right Witness: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
Height: 4
Binary configuration: 0
Right Seed:    [12b744719fe379559c3a36b2e9dd4cd957a5e63174dc78ec1ffdde498afefbf9]
Left Witness:  [6056f6e9d54b77c4c4d29b7588881938859bab939a7f7dea21d59804683edbc7]
Right Witness: [8fab6b378cfa4554103345586bdf2db37897c9fdc91e0d378e16bfced6f44d82]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b8439adb5dec5d6c8775cfadfc6568bd3682a08a5d328452b7823ceeff59a984]
Right Witness: [50ae624f79c7be29431b90a2b84516cb3a3785e82e45b123e3ac54afdeb4c1f6]
Height: 2
Binary configuration: 0
Right Seed:    [be24545dd917dcc230c7cd686f81a3dd223038baf004d8d2f888fc540c41e3e0]
Left Witness:  [959cc186bde032e25150b4de3256baf3c3930a79eb4f8b4f437de3089438d27c]
Right Witness: [23273d7995ee43d27d4ab9320774707f50b6d2170f1648540167db548d1032ea]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [c77f68fe69b444a67b5544d59635dd5391cf065849c5f443705be9f5f080d9f5]
Right Witness: [327938e84bc8d9eb09821b1d7663c698424d2874741ae8ce56438828721fc8d2]
Height: 0
Ed25519 Secret Key:       [82cb7ca5e8cae461898741bde61cfa8ab749738f3a9ac27e7421015acd4e1793]
Ed25519 Verification Key: [d43476ed2380b1b96902bfaec96c1f675ad113bd55d86b506c9a26895a69b496]
```
- Sigma t = 31:
```
Verification Key: [decaf6e8f7f6c767b096775950d8f551b47f3975d5ec196d41f521850722d2c2]
Sigma: [c1e8335f8a5667138839f331310b930fddcdd61cf801a4337949e6e9470bec6ca087d26737f5641aa7ff7951abd1ed5fd5bee610763c0ea24aff7ef9dfc37809]
W[0]: [4179e8cf03735b99189a37614801e8f5f608c6bd11878fd24fffc47da7b54dd0]
W[1]: [781125c39719d6c58c554d1b0203aa681db2bedf056c65897fec0faa18c770d9]
W[2]: [9cd7efa15e265d6398ca38b482ac117584c1a8bac10a39415b6fb9462b69d978]
W[3]: [6056f6e9d54b77c4c4d29b7588881938859bab939a7f7dea21d59804683edbc7]
W[4]: [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
```
- Sum Composition Secret Key, t = 31:
```
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [7feb24f2a47efff49217759e3e76af0def79946407710c243c19e0b4f131b326]
Right Witness: [a5ae34468d39e8c5bbf8b9427444f1d507ce5678b5a73d4d2937b0dffe190f3e]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [6056f6e9d54b77c4c4d29b7588881938859bab939a7f7dea21d59804683edbc7]
Right Witness: [8fab6b378cfa4554103345586bdf2db37897c9fdc91e0d378e16bfced6f44d82]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [9cd7efa15e265d6398ca38b482ac117584c1a8bac10a39415b6fb9462b69d978]
Right Witness: [85c7fc0cb0dd1c4c1433c0e019b23705841985856fa6c1dc611e940f76f69af7]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [781125c39719d6c58c554d1b0203aa681db2bedf056c65897fec0faa18c770d9]
Right Witness: [0e2d05259c0ff2e4c5756a536337f05bd54dbce11199f27187099911f2312376]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [4179e8cf03735b99189a37614801e8f5f608c6bd11878fd24fffc47da7b54dd0]
Right Witness: [fc9680222281d7833fad23b46e142bbbb55b506176ef35b22907526f8598a2d3]
Height: 0
Ed25519 Secret Key:       [142ef2d864ccfff7b44b5b2119186ae1d1d09352c4173e9e293eb87edee7c1ff]
Ed25519 Verification Key: [decaf6e8f7f6c767b096775950d8f551b47f3975d5ec196d41f521850722d2c2]
```
## Test Vector - 6
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 21, 42, 63]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
5a7ac1401665872e6cdbfff3a61c5df45c28e88728f29097635e6f0a91b4b47c
```
- h (int):

```6```

- Message (string):
```
"just over that hill: the one one wants one"
```
- Message (bytes) with `utf-8` encoding:
```
6a757374206f76657220746861742068696c6c3a20746865206f6e65206f6e652077616e7473206f6e65
```
### Outputs
- Sum Composition Verification Key:
```
a0c7e14349ab699f9628b705ab24a6727f60959333c667e789cfdc39af0bbe53
```
- Sum Composition Secret Key, t = 0:
```
Height: 6
Binary configuration: 0
Right Seed:    [2277f04dd632082100be9a0a13b4765d024cb76a841c6f72106d7e2b5c4e2b3d]
Left Witness:  [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
Right Witness: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
Height: 5
Binary configuration: 0
Right Seed:    [f44f8bc743e0e8fda5d860334abb857fb41d7e1de73dfbd4ac2775385c3fe70b]
Left Witness:  [eb3bde2a06cdefbe4f11081f13f801bdcb8ef2a3093747543ffa14169eb06f70]
Right Witness: [0e969fbec8bbd9a8141f3dd4aee3d71c3a9f6883b7a2db5e227c22a50729b1ab]
Height: 4
Binary configuration: 0
Right Seed:    [c550b8d04a5fd23f7657b71a2dac6d4993681853f8b39928545274b690e91c42]
Left Witness:  [7fa5a082554b3ea42374589135649492b889f2323c13e0537a12f91ecf1e0a94]
Right Witness: [1ccb56e5d0df4ce113baf59d08f0a3106d6ef69560e8ee3f0e5d318463abf897]
Height: 3
Binary configuration: 0
Right Seed:    [e2d599de9eebd07769876f1e77de99b6ca11158c36ccfc32b650e19b0ed33d0e]
Left Witness:  [a75f9212c2438c370579a1a4dafd227ad8673822328d51f01dce479611e0cf81]
Right Witness: [b691d91d8aab4d46bfb9a366ff7df889bcac878fa237a785cee13f490aa9796e]
Height: 2
Binary configuration: 0
Right Seed:    [87b52b78bf1132c2b8877b77762258eba44b03702bc70ff1087e52de83ad77ad]
Left Witness:  [06d4a2ad90d65fc8f2aabd68c6f47be4b912eeb476b62b8055bbdf9106841e80]
Right Witness: [575d6c35d2725d1c32d6f9b5b532310b9f06ed3345b854d40710d17be9a89608]
Height: 1
Binary configuration: 0
Right Seed:    [00c20336e4ddb53deb4a991427991d92d2b67a1453b7abc6b64caadb8d3c8503]
Left Witness:  [dce5fe8141ea48541be2bce99c7251a9c9c2235e7a0aa654bb1fac8fdc50696b]
Right Witness: [0b125ade7bb094dd3593badc207b6a549058d2da2e7f19023d10364c86ac1a48]
Height: 0
Ed25519 Secret Key:       [b996c8f68d518c06f443a4c432e5e8dd37080ef2abcb64db122dffa92921aa6c]
Ed25519 Verification Key: [49bd1c39676b2c4041841b957aeb6a64cb60008beae186663b2761be4f9df8d4]
```
- Sigma t = 0:
```
Verification Key: [49bd1c39676b2c4041841b957aeb6a64cb60008beae186663b2761be4f9df8d4]
Sigma: [ab114c6e914bcce3b2ae38e4e61d28a67acccddc6442cf6bbb27e5bc4322b45bff605f4c7f1c3eebbe15ae3f64e0f455a6eea8f570981977f5cef31beb447b09]
W[0]: [0b125ade7bb094dd3593badc207b6a549058d2da2e7f19023d10364c86ac1a48]
W[1]: [575d6c35d2725d1c32d6f9b5b532310b9f06ed3345b854d40710d17be9a89608]
W[2]: [b691d91d8aab4d46bfb9a366ff7df889bcac878fa237a785cee13f490aa9796e]
W[3]: [1ccb56e5d0df4ce113baf59d08f0a3106d6ef69560e8ee3f0e5d318463abf897]
W[4]: [0e969fbec8bbd9a8141f3dd4aee3d71c3a9f6883b7a2db5e227c22a50729b1ab]
W[5]: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
```
- Sum Composition Secret Key, t = 0:
```
Height: 6
Binary configuration: 0
Right Seed:    [2277f04dd632082100be9a0a13b4765d024cb76a841c6f72106d7e2b5c4e2b3d]
Left Witness:  [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
Right Witness: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
Height: 5
Binary configuration: 0
Right Seed:    [f44f8bc743e0e8fda5d860334abb857fb41d7e1de73dfbd4ac2775385c3fe70b]
Left Witness:  [eb3bde2a06cdefbe4f11081f13f801bdcb8ef2a3093747543ffa14169eb06f70]
Right Witness: [0e969fbec8bbd9a8141f3dd4aee3d71c3a9f6883b7a2db5e227c22a50729b1ab]
Height: 4
Binary configuration: 0
Right Seed:    [c550b8d04a5fd23f7657b71a2dac6d4993681853f8b39928545274b690e91c42]
Left Witness:  [7fa5a082554b3ea42374589135649492b889f2323c13e0537a12f91ecf1e0a94]
Right Witness: [1ccb56e5d0df4ce113baf59d08f0a3106d6ef69560e8ee3f0e5d318463abf897]
Height: 3
Binary configuration: 0
Right Seed:    [e2d599de9eebd07769876f1e77de99b6ca11158c36ccfc32b650e19b0ed33d0e]
Left Witness:  [a75f9212c2438c370579a1a4dafd227ad8673822328d51f01dce479611e0cf81]
Right Witness: [b691d91d8aab4d46bfb9a366ff7df889bcac878fa237a785cee13f490aa9796e]
Height: 2
Binary configuration: 0
Right Seed:    [87b52b78bf1132c2b8877b77762258eba44b03702bc70ff1087e52de83ad77ad]
Left Witness:  [06d4a2ad90d65fc8f2aabd68c6f47be4b912eeb476b62b8055bbdf9106841e80]
Right Witness: [575d6c35d2725d1c32d6f9b5b532310b9f06ed3345b854d40710d17be9a89608]
Height: 1
Binary configuration: 0
Right Seed:    [00c20336e4ddb53deb4a991427991d92d2b67a1453b7abc6b64caadb8d3c8503]
Left Witness:  [dce5fe8141ea48541be2bce99c7251a9c9c2235e7a0aa654bb1fac8fdc50696b]
Right Witness: [0b125ade7bb094dd3593badc207b6a549058d2da2e7f19023d10364c86ac1a48]
Height: 0
Ed25519 Secret Key:       [b996c8f68d518c06f443a4c432e5e8dd37080ef2abcb64db122dffa92921aa6c]
Ed25519 Verification Key: [49bd1c39676b2c4041841b957aeb6a64cb60008beae186663b2761be4f9df8d4]
```
- Sigma t = 21:
```
Verification Key: [0d376e128b1b8ad68bc6d060876f38ba2363694f35114e126f53b6d99e25a026]
Sigma: [f4648e56e9e2c7e47c40628c22b4f235710b1d856c27e2c09b4dae685f9475b0cbcfce80f802bdfc2b1b769bfa8e8481be46f39064b80fc99ef4396dd5c8f106]
W[0]: [15534f914297fa307abd1ed1852fe8d0381b9d346946531a32ba1330da3769ef]
W[1]: [a21afc4ed6ff90567746ec8c960411bd4b5995e3826aacff24b20929554eea14]
W[2]: [9987ac67685b21245e18cfc360a6f65eaa56c69bae0ad039db47104b33100d23]
W[3]: [80ec2a274674fdc8911f09b66f02a0380ef1082a7d29e082163814fcf868f949]
W[4]: [eb3bde2a06cdefbe4f11081f13f801bdcb8ef2a3093747543ffa14169eb06f70]
W[5]: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
```
- Sum Composition Secret Key, t = 21:
```
Height: 6
Binary configuration: 0
Right Seed:    [2277f04dd632082100be9a0a13b4765d024cb76a841c6f72106d7e2b5c4e2b3d]
Left Witness:  [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
Right Witness: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [eb3bde2a06cdefbe4f11081f13f801bdcb8ef2a3093747543ffa14169eb06f70]
Right Witness: [0e969fbec8bbd9a8141f3dd4aee3d71c3a9f6883b7a2db5e227c22a50729b1ab]
Height: 4
Binary configuration: 0
Right Seed:    [1d886eae4d36f3007210994ff3b96c016239c86c1452d8a54e99717484b771c4]
Left Witness:  [ee436a83aeee213decb8238fbb6d09130f711ab415c0c07266bead7c6486e274]
Right Witness: [80ec2a274674fdc8911f09b66f02a0380ef1082a7d29e082163814fcf868f949]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [9987ac67685b21245e18cfc360a6f65eaa56c69bae0ad039db47104b33100d23]
Right Witness: [b8ca7e0a42cc2261f794f924a157087e0556ce41eee6f6e5c2b3c87da144c9fd]
Height: 2
Binary configuration: 0
Right Seed:    [8d2bf589d63992413b5fc583adb8a6e02b7432ce0405d25e2fba623f77e3b62a]
Left Witness:  [7fe1444d9ee8469fdc1c618ff1e492ffb65ca4472ca29de270449fd801c96ede]
Right Witness: [a21afc4ed6ff90567746ec8c960411bd4b5995e3826aacff24b20929554eea14]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [15534f914297fa307abd1ed1852fe8d0381b9d346946531a32ba1330da3769ef]
Right Witness: [038ca829937b6e4935a09f36adc686096a9736b5ccf15db2c306a62408e44880]
Height: 0
Ed25519 Secret Key:       [edc52e217e6501f0eddf466c1f01ab6fa4bb9173a93abe33eb8c4111b4588565]
Ed25519 Verification Key: [0d376e128b1b8ad68bc6d060876f38ba2363694f35114e126f53b6d99e25a026]
```
- Sigma t = 42:
```
Verification Key: [82d4d9bddda967740f204a1e7b3df0a010a3847260ff949d5108519a99eadd4e]
Sigma: [f191a820478339c23cad63d17584c705d87571daedc9a0117f57f268d6b783b28079a407537c8a3bbd893df19857f37b830e4cd055043bd769c42af3f4688d0f]
W[0]: [abfc30c6f4430ed0e531ce61d7b947153f93455f47fc5a2a6d411b33d33ec22e]
W[1]: [6742ef5cb17f30654ea8d27fc8f775e7184e4f47f9b91453dd0f396fd92f3fff]
W[2]: [8daaf6cc3002b8821d888dabc68042833e70f4d7d3ad9874435a1014442fdece]
W[3]: [1a9edafa59fa9b0d9398f21b2944f06282393d9fcfa631f75a98ea5c2e575e9a]
W[4]: [89b2d61aa75751956d1839a16973347c980358f2151cb80bc55d64555c22b41a]
W[5]: [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
```
- Sum Composition Secret Key, t = 42:
```
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
Right Witness: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
Height: 5
Binary configuration: 0
Right Seed:    [f275f2b5a10019bb1aedf7a3d6198d68eeacb3ca1eb6ed72a01f4adea2490659]
Left Witness:  [741ab03ee4eb17f80b15aa96a5e9c7f324426ab92dd79ae267f52212c8a19cb2]
Right Witness: [89b2d61aa75751956d1839a16973347c980358f2151cb80bc55d64555c22b41a]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [1a9edafa59fa9b0d9398f21b2944f06282393d9fcfa631f75a98ea5c2e575e9a]
Right Witness: [1864c8a0406939d529d6983be242929182abffd4025c8889d8a96f3351624a8d]
Height: 3
Binary configuration: 0
Right Seed:    [e50eb050ebfb005547954fdd569edc5906d50447bdec6195c8a5289b23b7a6d3]
Left Witness:  [b71d2e7d3a7da90a0f2c9c9610274e85ac0d7026cea1067515f66b6593db3fa6]
Right Witness: [8daaf6cc3002b8821d888dabc68042833e70f4d7d3ad9874435a1014442fdece]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [6742ef5cb17f30654ea8d27fc8f775e7184e4f47f9b91453dd0f396fd92f3fff]
Right Witness: [2cd5febbfb4cded348c55fbcfe905d6403383ab622c1fd0e5bc232c8e357f51b]
Height: 1
Binary configuration: 0
Right Seed:    [c03573f3b6679ffd19a5a86f2cc5ced335bf47fcdb39b6433d71f5e0e9398508]
Left Witness:  [6e00a7d9e26d8d6231c54b36f80c16568486aa148015212074e89b4f3213cf9f]
Right Witness: [abfc30c6f4430ed0e531ce61d7b947153f93455f47fc5a2a6d411b33d33ec22e]
Height: 0
Ed25519 Secret Key:       [0464254bfcf68336a9e2021e69eb61a407734dbce993949055b3b134a8120e9a]
Ed25519 Verification Key: [82d4d9bddda967740f204a1e7b3df0a010a3847260ff949d5108519a99eadd4e]
```
- Sigma t = 63:
```
Verification Key: [ac0b31d016409d88e04e0156983afa8e6f03691069149f36df8407bc91ae683a]
Sigma: [9cb97fc3c3803fabcff7d1abbea9da1957d9dcfb2f6038eff64d8a3e2374b2fe7b1d7f0f3e28e5133016b06788ab7b979d375a927dbd3bb604efefc6e0fdaf0d]
W[0]: [4b8531432cf31d9111556fb483b4d916ac1a2267186edf3b311c4cf61ed54f61]
W[1]: [f59147dd4f6bfbfe7df25f49c0f568782c44b58e8939d029837d2e5a4196110f]
W[2]: [7841cc314fc49aa6ca9e56b430d3a30733b78b421685f2dd2f32068473251f58]
W[3]: [2c7de5a0a911f0ec58584bc9705a620b659e73bf3035815860ebc8305d04c1fe]
W[4]: [741ab03ee4eb17f80b15aa96a5e9c7f324426ab92dd79ae267f52212c8a19cb2]
W[5]: [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
```
- Sum Composition Secret Key, t = 63:
```
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [e1c78fc85548d19fa70d6af8b42b0c2e134a6025214c5885fcdd5f85e65b5876]
Right Witness: [51180e9a5efd245e7f331db08b0227d250b316507b66ca5e6e39c7f87583be92]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [741ab03ee4eb17f80b15aa96a5e9c7f324426ab92dd79ae267f52212c8a19cb2]
Right Witness: [89b2d61aa75751956d1839a16973347c980358f2151cb80bc55d64555c22b41a]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [2c7de5a0a911f0ec58584bc9705a620b659e73bf3035815860ebc8305d04c1fe]
Right Witness: [110f53914bafd589d3778044f711d26ac9001dacf55fd0d397321b812585ae69]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [7841cc314fc49aa6ca9e56b430d3a30733b78b421685f2dd2f32068473251f58]
Right Witness: [7f06e54b5c681a686e5670ae13737194d015d3a76e0575880af50dc031cfd311]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [f59147dd4f6bfbfe7df25f49c0f568782c44b58e8939d029837d2e5a4196110f]
Right Witness: [ec2d9bbe2f69730697783f7d49b399676638eddc2a00576a10b5d686086d4d1e]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [4b8531432cf31d9111556fb483b4d916ac1a2267186edf3b311c4cf61ed54f61]
Right Witness: [f4a5b9c1551fa382ab1e3045abb8f21a572eb75d648175726f7a15723200b832]
Height: 0
Ed25519 Secret Key:       [a7dcd75a40d9b9f7925c4fba6dc580ad2fb48578d10b70509e8c7aee1da5c67f]
Ed25519 Verification Key: [ac0b31d016409d88e04e0156983afa8e6f03691069149f36df8407bc91ae683a]
```
## Test Vector - 7
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 42, 85, 127]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
923d7df4b9c2b16e893620667a4a5bf5eb1f255ad0108ee682476bd7f251b5a0
```
- h (int):

```7```

- Message (string):
```
"my legs cramp, my head moves its mouth"
```
- Message (bytes) with `utf-8` encoding:
```
6d79206c656773206372616d702c206d792068656164206d6f76657320697473206d6f757468
```
### Outputs
- Sum Composition Verification Key:
```
4055a74086c7e1ff4e07b534ac6ca8b999c9923270f762b361010f8bc7631081
```
- Sum Composition Secret Key, t = 0:
```
Height: 7
Binary configuration: 0
Right Seed:    [46c34310dc9458e5b2cd91fa4fe7ee1e06c7779d06c2196fbf82ed98078311d9]
Left Witness:  [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
Right Witness: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
Height: 6
Binary configuration: 0
Right Seed:    [493179ab358a01635d2a49ab65799520458e967abbe0d61d5fbeb1c8d8ac4b64]
Left Witness:  [cc521a01bffa7a82c5d5a1981a769012e0274fbefffb3770713e2583678e27e5]
Right Witness: [2236e5d843b1c6e7c9462aef1f70beb611d765d78cf0fdc9618f7731f847191d]
Height: 5
Binary configuration: 0
Right Seed:    [6095a73ae1db1a59f824c208874175a54a54d761a0ed4534136a83cc3a4a5112]
Left Witness:  [07d186b611b167ba49d62530871f155f1c7b7d88f4be1833d2a678f000a6d82a]
Right Witness: [7ab5167621808cc99bde42a789a74d4106c1d99b3e7ef84de85e914737161888]
Height: 4
Binary configuration: 0
Right Seed:    [0501fd34e75054ef775b3d102e0cecf1242be3e7dd1a40f3a55bcbb78eb55e62]
Left Witness:  [660c23263e9e4e7b73974f02a52fd674f0af5081b037dca65ec83f8ff5edc1bd]
Right Witness: [262128b1cbb1f18f4b295ee895ee6aed29d4d430b30c3f8c59a3f8cb678b5061]
Height: 3
Binary configuration: 0
Right Seed:    [6dc8268a54df1f9f7476a6f25a2278db8648d7374d58fd6bed0f1d3197ee57f3]
Left Witness:  [122f3bcff18230db00cb603ac40ffe1341c40ba213085865ed10fd97b74ce386]
Right Witness: [9092feaed0892fdcbba8d51de5e76fd7455003f90e2a5ce6dc0fd84e69138e2a]
Height: 2
Binary configuration: 0
Right Seed:    [1947b5d4ef7beec92fdea82c41cc0dc50b65832359a46e6da44c752bc4c09c99]
Left Witness:  [9eb599070b144b152c30df9460040ef94c5e6baf2bb361df207109aa73179eea]
Right Witness: [d0133ac37bb2434794fd0793f294e60db1ae97dd35079cfd4c0d2a6c376d646e]
Height: 1
Binary configuration: 0
Right Seed:    [9ce7bf898769bf98f97b9fa36466a23e8d768e8c79057f4fe1836d919595285a]
Left Witness:  [931168ed8b04e045986d7aa29b8c3ef80bf69b5129cb8fd36c33a0efc618d7a7]
Right Witness: [cb34826a3cc03f369a1328c9ed8d6ca63858fbc69baa04c12a08fdddc050b018]
Height: 0
Ed25519 Secret Key:       [c607775d1e00178e81ecc807a866bb5bcc822b58bd87eb3a98aa7c016ec4c593]
Ed25519 Verification Key: [aa9a700d60ba96fb76c7c61f9e03a56b51bba36940e3c8eea9481309331bedcd]
```
- Sigma t = 0:
```
Verification Key: [aa9a700d60ba96fb76c7c61f9e03a56b51bba36940e3c8eea9481309331bedcd]
Sigma: [b40f66e74e096a0f09080dc4239d0e6244dfda2dc88ee660d02886c155ef4955f9e728c4ba0bb9121874b69d8d3670f3cc8c4e59269550f7d74f4a60da50200a]
W[0]: [cb34826a3cc03f369a1328c9ed8d6ca63858fbc69baa04c12a08fdddc050b018]
W[1]: [d0133ac37bb2434794fd0793f294e60db1ae97dd35079cfd4c0d2a6c376d646e]
W[2]: [9092feaed0892fdcbba8d51de5e76fd7455003f90e2a5ce6dc0fd84e69138e2a]
W[3]: [262128b1cbb1f18f4b295ee895ee6aed29d4d430b30c3f8c59a3f8cb678b5061]
W[4]: [7ab5167621808cc99bde42a789a74d4106c1d99b3e7ef84de85e914737161888]
W[5]: [2236e5d843b1c6e7c9462aef1f70beb611d765d78cf0fdc9618f7731f847191d]
W[6]: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
```
- Sum Composition Secret Key, t = 0:
```
Height: 7
Binary configuration: 0
Right Seed:    [46c34310dc9458e5b2cd91fa4fe7ee1e06c7779d06c2196fbf82ed98078311d9]
Left Witness:  [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
Right Witness: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
Height: 6
Binary configuration: 0
Right Seed:    [493179ab358a01635d2a49ab65799520458e967abbe0d61d5fbeb1c8d8ac4b64]
Left Witness:  [cc521a01bffa7a82c5d5a1981a769012e0274fbefffb3770713e2583678e27e5]
Right Witness: [2236e5d843b1c6e7c9462aef1f70beb611d765d78cf0fdc9618f7731f847191d]
Height: 5
Binary configuration: 0
Right Seed:    [6095a73ae1db1a59f824c208874175a54a54d761a0ed4534136a83cc3a4a5112]
Left Witness:  [07d186b611b167ba49d62530871f155f1c7b7d88f4be1833d2a678f000a6d82a]
Right Witness: [7ab5167621808cc99bde42a789a74d4106c1d99b3e7ef84de85e914737161888]
Height: 4
Binary configuration: 0
Right Seed:    [0501fd34e75054ef775b3d102e0cecf1242be3e7dd1a40f3a55bcbb78eb55e62]
Left Witness:  [660c23263e9e4e7b73974f02a52fd674f0af5081b037dca65ec83f8ff5edc1bd]
Right Witness: [262128b1cbb1f18f4b295ee895ee6aed29d4d430b30c3f8c59a3f8cb678b5061]
Height: 3
Binary configuration: 0
Right Seed:    [6dc8268a54df1f9f7476a6f25a2278db8648d7374d58fd6bed0f1d3197ee57f3]
Left Witness:  [122f3bcff18230db00cb603ac40ffe1341c40ba213085865ed10fd97b74ce386]
Right Witness: [9092feaed0892fdcbba8d51de5e76fd7455003f90e2a5ce6dc0fd84e69138e2a]
Height: 2
Binary configuration: 0
Right Seed:    [1947b5d4ef7beec92fdea82c41cc0dc50b65832359a46e6da44c752bc4c09c99]
Left Witness:  [9eb599070b144b152c30df9460040ef94c5e6baf2bb361df207109aa73179eea]
Right Witness: [d0133ac37bb2434794fd0793f294e60db1ae97dd35079cfd4c0d2a6c376d646e]
Height: 1
Binary configuration: 0
Right Seed:    [9ce7bf898769bf98f97b9fa36466a23e8d768e8c79057f4fe1836d919595285a]
Left Witness:  [931168ed8b04e045986d7aa29b8c3ef80bf69b5129cb8fd36c33a0efc618d7a7]
Right Witness: [cb34826a3cc03f369a1328c9ed8d6ca63858fbc69baa04c12a08fdddc050b018]
Height: 0
Ed25519 Secret Key:       [c607775d1e00178e81ecc807a866bb5bcc822b58bd87eb3a98aa7c016ec4c593]
Ed25519 Verification Key: [aa9a700d60ba96fb76c7c61f9e03a56b51bba36940e3c8eea9481309331bedcd]
```
- Sigma t = 42:
```
Verification Key: [f9f12c9dc6364fcb747b7798bc67add302536bae236c55821782a567b3621459]
Sigma: [4c7e0042147b96cdbcf20b4e10cd98e7dd0c172505ad2b1c75265fb8c986ac6b39576bb4b98bc9ed1e87bff9d5d3e3e0411f628be286a701ff87c4177c127f0a]
W[0]: [817d6fb459037056da813671b0624dd3961b028888fa5709926a5e660c6cb35f]
W[1]: [b057fafa9d868584e22ab2a6bbf5dfeefe8515760ca53f4d233da36d66d47e33]
W[2]: [97612b1d8ef71adb0c94106e08d18d1e73746864e0ae5037d289b42471d26931]
W[3]: [b38ebdd9db2924bdeb6f282c5edf49a62831c65c45eb804f967151be8416df8e]
W[4]: [ffb8ba3349907a731274cf7af88607540160dd2c2940d20db0fb99ed180681cc]
W[5]: [cc521a01bffa7a82c5d5a1981a769012e0274fbefffb3770713e2583678e27e5]
W[6]: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
```
- Sum Composition Secret Key, t = 42:
```
Height: 7
Binary configuration: 0
Right Seed:    [46c34310dc9458e5b2cd91fa4fe7ee1e06c7779d06c2196fbf82ed98078311d9]
Left Witness:  [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
Right Witness: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [cc521a01bffa7a82c5d5a1981a769012e0274fbefffb3770713e2583678e27e5]
Right Witness: [2236e5d843b1c6e7c9462aef1f70beb611d765d78cf0fdc9618f7731f847191d]
Height: 5
Binary configuration: 0
Right Seed:    [e24e36bf21d3a3b4d3376488cf539e74ea9c8c3fabb2944f2219359587aa6963]
Left Witness:  [50302762b1241a536116d1665044e394ddfcc5833907ea4f485c433f9d40efb3]
Right Witness: [ffb8ba3349907a731274cf7af88607540160dd2c2940d20db0fb99ed180681cc]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b38ebdd9db2924bdeb6f282c5edf49a62831c65c45eb804f967151be8416df8e]
Right Witness: [88be1eb3e9f012d740d2482d44956ee99197e4074b0447e4c255e3db915ea918]
Height: 3
Binary configuration: 0
Right Seed:    [292e07c2c23954544eeda2ed8fbe576ff15370ebe92a48c421332018fc50eab6]
Left Witness:  [e073921f1b289fe209d6081c8a50a08f92672d2ea9c1c6c7b2c8aca23a5b8e92]
Right Witness: [97612b1d8ef71adb0c94106e08d18d1e73746864e0ae5037d289b42471d26931]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b057fafa9d868584e22ab2a6bbf5dfeefe8515760ca53f4d233da36d66d47e33]
Right Witness: [1178494000930e7f2d5872a39c1e607b361be88e60add9f2ce8aca77e8ed0136]
Height: 1
Binary configuration: 0
Right Seed:    [ac7ec535fbf48eb267f098ff45bb1cbb3579be0a4289049c30c77c6621e8713b]
Left Witness:  [f038a16be4240047348e5c6c60518395bc3cb0a083a06d2766ec5b01eabe7630]
Right Witness: [817d6fb459037056da813671b0624dd3961b028888fa5709926a5e660c6cb35f]
Height: 0
Ed25519 Secret Key:       [9f376cdddd1af96d51ded17aaa08b6720fa259568192e4e4e3e49220e268a939]
Ed25519 Verification Key: [f9f12c9dc6364fcb747b7798bc67add302536bae236c55821782a567b3621459]
```
- Sigma t = 85:
```
Verification Key: [f61809bf2bc860000652b031f69b5f7ca4f7b057c3c09b4e2d8025478e137c15]
Sigma: [194266c8db61ca96872315762ac0250936964de48170aab2d63d9e73ec2f49dee6da14ede56820c10228db6c1eb12c78d1af0d5ac9c996bbe42628dc9de42a06]
W[0]: [78c36ddff0f74e2c3ae2572016c71ca3ef98300eea0dbc118d2dfdc51e4b861e]
W[1]: [98704e786f35c99557ac5d8e81b35e0c9056e7beade7bb9036d189b651425c84]
W[2]: [37f21fee363eff5d2b930a0d1e1c200f746ec59c02d0d5f8dcdf9fa32dbd94b7]
W[3]: [b3a1ba40a40195512d8f477d193970db443b70ef845cbc1404f6ccbdf9422671]
W[4]: [9464d8fc2158264e645b6daa599431bce6a4a3613f3b79fcf10c7dacb96de0d2]
W[5]: [9db86c0eceb4dc1836f50358dddedb12ac3fa11e3e166057f5f16bf6aae31dd0]
W[6]: [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
```
- Sum Composition Secret Key, t = 85:
```
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
Right Witness: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
Height: 6
Binary configuration: 0
Right Seed:    [7d80f162c526630d277d1fba929b79b71d00f68ee43d8ae7eba36fb8e3dd6a08]
Left Witness:  [940cfc25c33d0e2d97571a37a39295b5498223518ae18dda79ac92fa1bba6bda]
Right Witness: [9db86c0eceb4dc1836f50358dddedb12ac3fa11e3e166057f5f16bf6aae31dd0]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [9464d8fc2158264e645b6daa599431bce6a4a3613f3b79fcf10c7dacb96de0d2]
Right Witness: [aeac515b31e9c684ddd774df9c83b87fd8067dc7b75e6baf986c1eaf273e7164]
Height: 4
Binary configuration: 0
Right Seed:    [2cfec62b394327763df12c87dcf88f7dbc22bc8c7b6dc9fccd7c7ad031499622]
Left Witness:  [c7dcccbaa763faae02a7fc852843760efb4c3e73cbc88729204a6ffe16b18498]
Right Witness: [b3a1ba40a40195512d8f477d193970db443b70ef845cbc1404f6ccbdf9422671]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [37f21fee363eff5d2b930a0d1e1c200f746ec59c02d0d5f8dcdf9fa32dbd94b7]
Right Witness: [396564115124cdb22a13fa8c64d645a3f2412c793f602f001a07c370c3cc9e63]
Height: 2
Binary configuration: 0
Right Seed:    [79712a0d5eef5b85a0b09f812472309dd04060fa364327c0c642540abff4ae4c]
Left Witness:  [a6dd37f132cab3fa6c3510ba9183c3266bb966c8a611c94e840c87674b27f207]
Right Witness: [98704e786f35c99557ac5d8e81b35e0c9056e7beade7bb9036d189b651425c84]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [78c36ddff0f74e2c3ae2572016c71ca3ef98300eea0dbc118d2dfdc51e4b861e]
Right Witness: [4b8f62a20efa995f2e967525c7dce8ecfd3b24b63e04020a2939ae15820b37aa]
Height: 0
Ed25519 Secret Key:       [31e45344df67a66ff2d03e67d8573e37e0b17f1ccdd2550d92585d8f8b33c4f5]
Ed25519 Verification Key: [f61809bf2bc860000652b031f69b5f7ca4f7b057c3c09b4e2d8025478e137c15]
```
- Sigma t = 127:
```
Verification Key: [3b5c62ac7d48e20bb0fa6c03e565bb53c51907aaf617cbb88f167c2930114ae6]
Sigma: [460b7508ebdf12ce864380d13f643ceddbd9fb4dcb2d0cca594e187cb2e136e4f7b4a0e9baa35e28a07dafe1012140b75c8ad4ddc51042f7fc39390b1e4b9d06]
W[0]: [5fcb438deb8bfa40bce2d0188c516bf650c041b8efcebf4d1a7c25cc34eb9294]
W[1]: [2b43acbcfd412eaca33af8eedc603e7040549b1923d1fe00b0ff6943d16a3b97]
W[2]: [ea21ddf511748a59247cbe591f4e4b4c75bf75724090780295f4a1b9648a9e88]
W[3]: [771d2b62e52a9ba69364cbd0d60e3dd2bb1194d6cfa2be1a62cd4198a77736c3]
W[4]: [244b8b9730cc617d91958fe141c0fb568f1c5bd697ce07a34c336fc474043de3]
W[5]: [940cfc25c33d0e2d97571a37a39295b5498223518ae18dda79ac92fa1bba6bda]
W[6]: [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
```
- Sum Composition Secret Key, t = 127:
```
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [4a215bd760024ca6d2f9737b3ffb0a1ce5a280e4fdefa765fc32b92491573461]
Right Witness: [982b479d889e1a1d5d9e426bd796b8c0c5aa7347728b43cb159aa939d0821a05]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [940cfc25c33d0e2d97571a37a39295b5498223518ae18dda79ac92fa1bba6bda]
Right Witness: [9db86c0eceb4dc1836f50358dddedb12ac3fa11e3e166057f5f16bf6aae31dd0]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [244b8b9730cc617d91958fe141c0fb568f1c5bd697ce07a34c336fc474043de3]
Right Witness: [adccc62fd3a70ae70614d2b268e1a5c9752a1b6333aac567e9c25404ac54a64a]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [771d2b62e52a9ba69364cbd0d60e3dd2bb1194d6cfa2be1a62cd4198a77736c3]
Right Witness: [adc5bdf5f1f96072d9dd684e192e22a251f8333b2a2cc399627e8aec2a0b8c25]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [ea21ddf511748a59247cbe591f4e4b4c75bf75724090780295f4a1b9648a9e88]
Right Witness: [229d13ae44cd2fdd0758f58c714a317a30f86acade44fd45a6af61108e7ee576]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [2b43acbcfd412eaca33af8eedc603e7040549b1923d1fe00b0ff6943d16a3b97]
Right Witness: [3abd02c20d64a5d68cf0274275dc38739da7203df22bee0036ee0bc138a4f54f]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [5fcb438deb8bfa40bce2d0188c516bf650c041b8efcebf4d1a7c25cc34eb9294]
Right Witness: [b4b079f2e3262a63b811eaf5ba5b281bc6bce94e40bf4a12e6b6d408fede7e88]
Height: 0
Ed25519 Secret Key:       [84783774571ef0f67e23000037426c756c00b57a30fcd0b7e191fcc9c58b27dc]
Ed25519 Verification Key: [3b5c62ac7d48e20bb0fa6c03e565bb53c51907aaf617cbb88f167c2930114ae6]
```
## Test Vector - 8
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 85, 170, 255]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
acf1f71f8fa7edcc93cab4cc835b76f685f94d296847799411f28e89d49754a6
```
- h (int):

```8```

- Message (string):
```
"strip language of emotion, end up with operate"
```
- Message (bytes) with `utf-8` encoding:
```
7374726970206c616e6775616765206f6620656d6f74696f6e2c20656e642075702077697468206f706572617465
```
### Outputs
- Sum Composition Verification Key:
```
caba73dd47a1c0e9c1708ef3e3d30276fc3dcc0ba1b7fc17f320c8401bf497a6
```
- Sum Composition Secret Key, t = 0:
```
Height: 8
Binary configuration: 0
Right Seed:    [869f1e12b3c0efa20fc9c1f8db81461a83dcb363564371723e5c9708b0efe922]
Left Witness:  [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
Right Witness: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
Height: 7
Binary configuration: 0
Right Seed:    [f1a1ca5122a874e96b3a08b0d38272af731c043c3e5c8628ea59f89c61943fe4]
Left Witness:  [08cc6d21f530348781cb4a7bfa2f873ae3739244d38bce508ef8a4671dee91dd]
Right Witness: [66dc8b06f43eb11a03e34c21c1daa3f9b23e68540ec03aca9b8fcf1f5f308424]
Height: 6
Binary configuration: 0
Right Seed:    [6e989db7e13dbdf53db8041e3b8b62335ed0badeed8f237a20be061961de142e]
Left Witness:  [efe737a6a847eaef19d4e4fdeab543bc60570c6a1657b7e91b9ffd44af366eae]
Right Witness: [f947711db4cc04eb3f67adecdf0d39d33c004813351fd621d625c2c1e133eea7]
Height: 5
Binary configuration: 0
Right Seed:    [252a6c01b436034e533d26c3371575888963a9f7e98b2910e8b1b7ea2780cd11]
Left Witness:  [1445897d5dabe109a1ac989a02cd1bb723ff1c6797db33144354884ffcd1cfbf]
Right Witness: [8f018a5f28f5e787833efb933c482e1397643bf5d2503c7c97ac0292eae7e393]
Height: 4
Binary configuration: 0
Right Seed:    [cdf2c4bbcd1e0335e8e757a8d187c3e50ebbe46b2293f55641b3861b498250cd]
Left Witness:  [b0e172eca605e3ff0f296add180011d00fb77b7dbfcc723d6cf3249a0adde62f]
Right Witness: [e51c739dcab698c78e64c565a6bf0960fc3319f898256480724d7c796306783f]
Height: 3
Binary configuration: 0
Right Seed:    [a7cfcbf2a6b8e4d237cb1060f778104bf89232086e2f8f0574f50d212084ce5a]
Left Witness:  [20107159ce16aec486f5a456c3bc24b67343f88f44ed1e539ebf4fe1a89dac50]
Right Witness: [81cfaee8d7e5798ff5abb5e7db8eb421a057022c451d2a538c86bb70af7866d7]
Height: 2
Binary configuration: 0
Right Seed:    [8e6c1f7e6ad4e249fceba3c21f807608f167c24d7ef1a724fa1174dec6462381]
Left Witness:  [e18d235df2e521b4b963c14d4077b5dad4c3933d70f1124bc816b497b7465c7e]
Right Witness: [d28e1540e14fc21aff8ce787384f390d6cf6f1e511c2ef8c69a2d8ff987fd781]
Height: 1
Binary configuration: 0
Right Seed:    [c9ac968078cbd9729519b4bf7d42d9855d211817fd2d9b725790b7b8cd5ab771]
Left Witness:  [4325346945704a26edf088c08d3f2fafa1b1eb572378f1b820b720869eb150e7]
Right Witness: [8d3f1857865c5432ed3ff6138fc51721e228dba9ba3c2066db8263c98f2cb89b]
Height: 0
Ed25519 Secret Key:       [0624eb6dd55440e43337224890b76fd858da7ae45a78ad02d4ecb9df6ced2fe5]
Ed25519 Verification Key: [f7e60bcefa3965a480c774d450a1cf4a0b02730969014427661fedc287ce644d]
```
- Sigma t = 0:
```
Verification Key: [f7e60bcefa3965a480c774d450a1cf4a0b02730969014427661fedc287ce644d]
Sigma: [264e0f568cde71232d7fa7543fcd4dd74fc3ab17bd2be97babeef1e05332552404bbc360ca58528ac88a846a3c2544e320664b9d0bde73ecad7d423a51bcf80d]
W[0]: [8d3f1857865c5432ed3ff6138fc51721e228dba9ba3c2066db8263c98f2cb89b]
W[1]: [d28e1540e14fc21aff8ce787384f390d6cf6f1e511c2ef8c69a2d8ff987fd781]
W[2]: [81cfaee8d7e5798ff5abb5e7db8eb421a057022c451d2a538c86bb70af7866d7]
W[3]: [e51c739dcab698c78e64c565a6bf0960fc3319f898256480724d7c796306783f]
W[4]: [8f018a5f28f5e787833efb933c482e1397643bf5d2503c7c97ac0292eae7e393]
W[5]: [f947711db4cc04eb3f67adecdf0d39d33c004813351fd621d625c2c1e133eea7]
W[6]: [66dc8b06f43eb11a03e34c21c1daa3f9b23e68540ec03aca9b8fcf1f5f308424]
W[7]: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
```
- Sum Composition Secret Key, t = 0:
```
Height: 8
Binary configuration: 0
Right Seed:    [869f1e12b3c0efa20fc9c1f8db81461a83dcb363564371723e5c9708b0efe922]
Left Witness:  [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
Right Witness: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
Height: 7
Binary configuration: 0
Right Seed:    [f1a1ca5122a874e96b3a08b0d38272af731c043c3e5c8628ea59f89c61943fe4]
Left Witness:  [08cc6d21f530348781cb4a7bfa2f873ae3739244d38bce508ef8a4671dee91dd]
Right Witness: [66dc8b06f43eb11a03e34c21c1daa3f9b23e68540ec03aca9b8fcf1f5f308424]
Height: 6
Binary configuration: 0
Right Seed:    [6e989db7e13dbdf53db8041e3b8b62335ed0badeed8f237a20be061961de142e]
Left Witness:  [efe737a6a847eaef19d4e4fdeab543bc60570c6a1657b7e91b9ffd44af366eae]
Right Witness: [f947711db4cc04eb3f67adecdf0d39d33c004813351fd621d625c2c1e133eea7]
Height: 5
Binary configuration: 0
Right Seed:    [252a6c01b436034e533d26c3371575888963a9f7e98b2910e8b1b7ea2780cd11]
Left Witness:  [1445897d5dabe109a1ac989a02cd1bb723ff1c6797db33144354884ffcd1cfbf]
Right Witness: [8f018a5f28f5e787833efb933c482e1397643bf5d2503c7c97ac0292eae7e393]
Height: 4
Binary configuration: 0
Right Seed:    [cdf2c4bbcd1e0335e8e757a8d187c3e50ebbe46b2293f55641b3861b498250cd]
Left Witness:  [b0e172eca605e3ff0f296add180011d00fb77b7dbfcc723d6cf3249a0adde62f]
Right Witness: [e51c739dcab698c78e64c565a6bf0960fc3319f898256480724d7c796306783f]
Height: 3
Binary configuration: 0
Right Seed:    [a7cfcbf2a6b8e4d237cb1060f778104bf89232086e2f8f0574f50d212084ce5a]
Left Witness:  [20107159ce16aec486f5a456c3bc24b67343f88f44ed1e539ebf4fe1a89dac50]
Right Witness: [81cfaee8d7e5798ff5abb5e7db8eb421a057022c451d2a538c86bb70af7866d7]
Height: 2
Binary configuration: 0
Right Seed:    [8e6c1f7e6ad4e249fceba3c21f807608f167c24d7ef1a724fa1174dec6462381]
Left Witness:  [e18d235df2e521b4b963c14d4077b5dad4c3933d70f1124bc816b497b7465c7e]
Right Witness: [d28e1540e14fc21aff8ce787384f390d6cf6f1e511c2ef8c69a2d8ff987fd781]
Height: 1
Binary configuration: 0
Right Seed:    [c9ac968078cbd9729519b4bf7d42d9855d211817fd2d9b725790b7b8cd5ab771]
Left Witness:  [4325346945704a26edf088c08d3f2fafa1b1eb572378f1b820b720869eb150e7]
Right Witness: [8d3f1857865c5432ed3ff6138fc51721e228dba9ba3c2066db8263c98f2cb89b]
Height: 0
Ed25519 Secret Key:       [0624eb6dd55440e43337224890b76fd858da7ae45a78ad02d4ecb9df6ced2fe5]
Ed25519 Verification Key: [f7e60bcefa3965a480c774d450a1cf4a0b02730969014427661fedc287ce644d]
```
- Sigma t = 85:
```
Verification Key: [21702fc68dff339c4cdb8434389488548d5ead7382db959ff36a2a15bb80e863]
Sigma: [b0eac79652d76c557ac207eef0da3e615c5876bbc53e3c5fef91398f14a0d01266a4bbef9a15ed95e5810e421668406dd1a374ce508431126e2cbf17afdb0e07]
W[0]: [262d80c0431e25701ba16f7e5c90ada92d47239f4c4c8aae9d2167d187a5e717]
W[1]: [701add95ce1748bac9654e9bacca65befde3e59966b691c556ab3851e090f4e6]
W[2]: [0ed8b37db49ef9db22736da402efdbebe505fec0d07454ecb6b28f43ef010ead]
W[3]: [9ffeafeb13f459c503f48a182445fad9dccd6ec36f6df8408d08c1ad55751fa2]
W[4]: [1b96bffb8404a8aa0921377ef6160e3294eb8adbe3798357e31ab62be037ee02]
W[5]: [b42dfd928f754ea45e8b24d5b6373b90e0fe9ddff8f080f14852c3f417a92e2d]
W[6]: [08cc6d21f530348781cb4a7bfa2f873ae3739244d38bce508ef8a4671dee91dd]
W[7]: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
```
- Sum Composition Secret Key, t = 85:
```
Height: 8
Binary configuration: 0
Right Seed:    [869f1e12b3c0efa20fc9c1f8db81461a83dcb363564371723e5c9708b0efe922]
Left Witness:  [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
Right Witness: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [08cc6d21f530348781cb4a7bfa2f873ae3739244d38bce508ef8a4671dee91dd]
Right Witness: [66dc8b06f43eb11a03e34c21c1daa3f9b23e68540ec03aca9b8fcf1f5f308424]
Height: 6
Binary configuration: 0
Right Seed:    [9953c4263e0db98f5d59246394731a3f6c9dc699e7605c712aa76b2c114ad0e6]
Left Witness:  [8bb31a99ca627208a31c8cb052335e9dfe1a7e8be3be7b6c457514c3fac4d5c5]
Right Witness: [b42dfd928f754ea45e8b24d5b6373b90e0fe9ddff8f080f14852c3f417a92e2d]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [1b96bffb8404a8aa0921377ef6160e3294eb8adbe3798357e31ab62be037ee02]
Right Witness: [d4c94b4727bd64a6288ec303a6dd8f62d96c5e085e611e3b96c5b9dec6fd220d]
Height: 4
Binary configuration: 0
Right Seed:    [2e441366d379773893504d8547960afef29c77a8a73551792970e0e1186155c5]
Left Witness:  [71322a2b9a9bc37f125b0d07f6ca06d48b0914a970fd3531a67bc8933720d3f0]
Right Witness: [9ffeafeb13f459c503f48a182445fad9dccd6ec36f6df8408d08c1ad55751fa2]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [0ed8b37db49ef9db22736da402efdbebe505fec0d07454ecb6b28f43ef010ead]
Right Witness: [230984ab43d1d5880661f92ccaf918db6b064b9890a3bbe7e9d77d1b59324ca6]
Height: 2
Binary configuration: 0
Right Seed:    [4b50dce3345214183d2fd11f152641129220dc2bb52ff52b2f24e120c198f6f3]
Left Witness:  [a6e1bd070930770861129cd613c7834df3655b3dd8056e04d58ec7580bad50d3]
Right Witness: [701add95ce1748bac9654e9bacca65befde3e59966b691c556ab3851e090f4e6]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [262d80c0431e25701ba16f7e5c90ada92d47239f4c4c8aae9d2167d187a5e717]
Right Witness: [b984e3c9e717ceb568f68d76fd672e67ca103ea490cc9a84421e7db7b1c10b3a]
Height: 0
Ed25519 Secret Key:       [b6c9b9fee3f5e1fc78249f729cd11a258a9bf5dd0052dfe801ba9e8d3daf25f9]
Ed25519 Verification Key: [21702fc68dff339c4cdb8434389488548d5ead7382db959ff36a2a15bb80e863]
```
- Sigma t = 170:
```
Verification Key: [94fcba5c88ad7b15a4613bd5d568edcfaafcc5a6ec70f307ba205db0c2c0b550]
Sigma: [c0cc9f74765ca66b534ea819da9d58eeeb153afb1f470e454af0274f9b2d9cc858b9abce4fabceb3f3801bf4bbe1becedaa3cdf029c414e2d1432b03289a250f]
W[0]: [34e7fd0eb30dcb8805396ee25f6ca62c19791dec018d4f1919cdbf0b27faa394]
W[1]: [b4a535faa43ecd3c8b5c635f2922623f004f14f96c2f91815f2bb86945a155d2]
W[2]: [184890a416f541ef788d8526e54ad8a64708872243f5be37772373e2d60b8c6d]
W[3]: [0639265b465b65175a1e9613f44fac3ccdede8d36f628da928226c59cc0d1a33]
W[4]: [5705e44a0a7595c669592b564edca2ec46154264fbb06e8848e44459876b283e]
W[5]: [36fef93ce690af1213d0fd1d12ecd3cbe3ae7bcea513e23ca1bdfaf328ad27ce]
W[6]: [e8f4417ab9bb51a1dbbb1682e3a2db6f99eb9eb211486a207c8c28a2fe492732]
W[7]: [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
```
- Sum Composition Secret Key, t = 170:
```
Height: 8
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
Right Witness: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
Height: 7
Binary configuration: 0
Right Seed:    [ced27864b2f5f0dca198c2799f26307996790414b5df61856f4b2d7fc0792927]
Left Witness:  [a695e806e494ec5f5a1f04f64868709edb2bdd5949fb7801baaa76251a08081e]
Right Witness: [e8f4417ab9bb51a1dbbb1682e3a2db6f99eb9eb211486a207c8c28a2fe492732]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [36fef93ce690af1213d0fd1d12ecd3cbe3ae7bcea513e23ca1bdfaf328ad27ce]
Right Witness: [86ff3df7b9635bf184fb49c9f0cfeb4f2842a54f728a7e7bb7545505f57c99c3]
Height: 5
Binary configuration: 0
Right Seed:    [66f017033d3df2274e0a45d56417a817f516929858af5a751adbddb65e6faeb2]
Left Witness:  [85a329dc48ba0eb508ea91fccd78a296b66b1dcd0c6189aef5a85e925b8aa882]
Right Witness: [5705e44a0a7595c669592b564edca2ec46154264fbb06e8848e44459876b283e]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [0639265b465b65175a1e9613f44fac3ccdede8d36f628da928226c59cc0d1a33]
Right Witness: [8477f91acae6cde07d4b6e28acfbe9cf35764202393dc64ba3b943300a7882b8]
Height: 3
Binary configuration: 0
Right Seed:    [9f105638a53e98aab398714394ca23dcf0319c5b736aa791c92627e259ddc9ec]
Left Witness:  [aaf7432f10d8e44a904fa8d95e8a4a48aaa3111518b319751c4090bf48b08925]
Right Witness: [184890a416f541ef788d8526e54ad8a64708872243f5be37772373e2d60b8c6d]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b4a535faa43ecd3c8b5c635f2922623f004f14f96c2f91815f2bb86945a155d2]
Right Witness: [251289027048412fcc14ecd3666976de580fdda3ff72ff4bbc9eb58a11fa7ea1]
Height: 1
Binary configuration: 0
Right Seed:    [c822c148bfe0e90c92315087eb077adce0bbacdd690e1e731a3d2f98880b3006]
Left Witness:  [9775c12dd3854d18356b89f651338d82c1d9572008aa019f2d877473914f982e]
Right Witness: [34e7fd0eb30dcb8805396ee25f6ca62c19791dec018d4f1919cdbf0b27faa394]
Height: 0
Ed25519 Secret Key:       [35c26ffa7c04673df9aa57570e2bfc95ec1b5aa8c8b0262fd16f5809b9d75390]
Ed25519 Verification Key: [94fcba5c88ad7b15a4613bd5d568edcfaafcc5a6ec70f307ba205db0c2c0b550]
```
- Sigma t = 255:
```
Verification Key: [48d877f96e4e9cb2280ffb57cbd1e6a04650762c9f8968f72399b8909f0cd309]
Sigma: [a9b2db00941cf94fe0f2ab7a2a7a01dfc7734fdb3df01c9e6310c73b0f2be882c741f698774c8da680fc6a37c499ae0d84b03101a93e1a67d3fdc15f0672eb03]
W[0]: [307caa6854cfd8fd1c6493847102049fd1472fc2ea5902cdf72b2de4f4485d63]
W[1]: [cf444b3009f138998208ebd96ed7d8ab1331745bcaba0276add2c9e97ce688c6]
W[2]: [abe4a94f1266c5251480298943469122dc867bb455a20b950c2b978576531d90]
W[3]: [41de0bf3508bf815a8771d7a7871fb12ccd147ea3ca47801ca280a5c268c1d54]
W[4]: [829c61d45a94443bc544a86b553054d8ecc7231a3367e3855e8f89738045bfa6]
W[5]: [49e815540a9aa0fc9bd643dd35e12c57260dbcf7a3246a0b29cac49ce24d8adb]
W[6]: [a695e806e494ec5f5a1f04f64868709edb2bdd5949fb7801baaa76251a08081e]
W[7]: [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
```
- Sum Composition Secret Key, t = 255:
```
Height: 8
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [0aa18cc6bef06001a04c87bc4db01a46da5ffd1a4cf807984a719b71cb3fae38]
Right Witness: [63f0c3e3b26d6db5323fded155fa1bf7966ab0c538c2296c63c103704183eda8]
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [a695e806e494ec5f5a1f04f64868709edb2bdd5949fb7801baaa76251a08081e]
Right Witness: [e8f4417ab9bb51a1dbbb1682e3a2db6f99eb9eb211486a207c8c28a2fe492732]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [49e815540a9aa0fc9bd643dd35e12c57260dbcf7a3246a0b29cac49ce24d8adb]
Right Witness: [3ae99ad0f4b9de9112f5cfc77d8dd0b3d69884aef54404009e7fc8d0fd9072ba]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [829c61d45a94443bc544a86b553054d8ecc7231a3367e3855e8f89738045bfa6]
Right Witness: [b236df21cbbde9e2efa1b0d915377cdadd93b863c8d1bb9ba5c7fcb9d17d2c6c]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [41de0bf3508bf815a8771d7a7871fb12ccd147ea3ca47801ca280a5c268c1d54]
Right Witness: [72b49b402c7f95b8ea4f44a03087aa87bbe1ac09bd6afb8338cc9c86c13704a7]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [abe4a94f1266c5251480298943469122dc867bb455a20b950c2b978576531d90]
Right Witness: [cf2a07812769b5219914b211c0e4b8aad8b164ad94963e681a5665180e274f53]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [cf444b3009f138998208ebd96ed7d8ab1331745bcaba0276add2c9e97ce688c6]
Right Witness: [7ea93714a4cf1d71068ce6f420c389f4dd9453451fc91bbe473dc4b79a8ae2c7]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [307caa6854cfd8fd1c6493847102049fd1472fc2ea5902cdf72b2de4f4485d63]
Right Witness: [41518ec907394e5632ceaf9d237928abe7b24106df199057f2114036ed269474]
Height: 0
Ed25519 Secret Key:       [108d8baf07b8b454fb66105bb071eef3d227db29ec4a1978e4864ef33e5a9150]
Ed25519 Verification Key: [48d877f96e4e9cb2280ffb57cbd1e6a04650762c9f8968f72399b8909f0cd309]
```
## Test Vector - 9
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 170, 341, 511]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
af443cdf4b721d009fe2e0f0656853a8561619bb21b5505e8e7aff901fefe822
```
- h (int):

```9```

- Message (string):
```
"nevertheless, again more"
```
- Message (bytes) with `utf-8` encoding:
```
6e657665727468656c6573732c20616761696e206d6f7265
```
### Outputs
- Sum Composition Verification Key:
```
9ff04167c44254a447239439aa3a47f389dc5c4cc6e7de0a9fe9b36508604b5d
```
- Sum Composition Secret Key, t = 0:
```
Height: 9
Binary configuration: 0
Right Seed:    [5457276efb66cc4e4d32797c0f15830035e1a80822cbe54daa6614b7b24547ec]
Left Witness:  [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
Right Witness: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
Height: 8
Binary configuration: 0
Right Seed:    [0e40e9b2db9c04abee1b487d0f3790a93d024f61c5fd6578738a532016e42ff9]
Left Witness:  [aea6f31de6c03bcff9c3ee67171134a3b1cd44cad6ef36c6cc269348bb06f1d9]
Right Witness: [602f1e29210fbb5e6ce701c31bc45eef523007b9b9bbf308e505786e4f0337a4]
Height: 7
Binary configuration: 0
Right Seed:    [a655a60c1fa82bcbe3a2234e5b8ddaa351a7b54e586c5621562c663b5d93d1d5]
Left Witness:  [de39a2b49878523c69ce453a91836a85be83530fcc2a34a7999c2be9820eb76b]
Right Witness: [d5c9db27ebc1fa1b7512133ac2cb936a61aa8ea372df8e296ef43379a2957e94]
Height: 6
Binary configuration: 0
Right Seed:    [868f22dad181b3addddce9d2c1dd5e8e11832bb81e623bb43a0d0aba63c06695]
Left Witness:  [ab3df4e0548a11e6861602d233fd676ccb7a6cad6b450d77d0300e014fbae823]
Right Witness: [835619f4d0883598419bc821e079c175c43a11ec2572242e6c4ab2da1fbf96b3]
Height: 5
Binary configuration: 0
Right Seed:    [1d84b6a18c2dbc3a6d4299cae16832a25e44333bd65f70dc7faeb3a7946b1f94]
Left Witness:  [0d59f50d1cd37505cb61a6b3b4225c1a167b8aa30886f0c57efd4c1c2376c4dc]
Right Witness: [e9b079962f0ffa8ab71c05a78b32285504946dd7c4a929ca00432c6af097a07d]
Height: 4
Binary configuration: 0
Right Seed:    [fdc725d65d477268ceade7fe0f60605de7d54e8ca75c4ce2937db688567a4f61]
Left Witness:  [98abdc8e9664754a235228f967f61208b95f929cafce54e5338e8489e4378d67]
Right Witness: [06bafa7b32095a65189c00fa9f1b41bb7a07c167bc0662f90b0d0f0d30da06db]
Height: 3
Binary configuration: 0
Right Seed:    [4007bed98feb9d9dc33dde2b0a8a31128836d784fd3963241375d91b95c1122e]
Left Witness:  [d28a9de3831809b411820cc1844c28ae521caefc1f5c63d7c0485618073418a0]
Right Witness: [764b9b197fac8bbedc33213a2dd350212a18b2a94040d0a81a1d84ada55578e0]
Height: 2
Binary configuration: 0
Right Seed:    [13554213fa2cb2644b84b7b10b3055a98097ff4fb970b0031f5774fd36c7c71a]
Left Witness:  [e1e968b07a50750fac0980bd0b0a0401d4d9138e1b57629362824b8304efb42e]
Right Witness: [64c84e76a18688a8553ec1a2f46eead7bf71f1425080c6cb71a8ea6a50bdccb2]
Height: 1
Binary configuration: 0
Right Seed:    [3013a848a9c0e5de77d8c1a2827085bc8c741a8164cd71852dbba95024d8efb8]
Left Witness:  [a3f042c509980961a2e2ad7ec038432e0d426a7ae35778f0fb833c1cd8dd4b03]
Right Witness: [ab49dc1f84d203263f67b0ddd6307366db6520fd9b766ec75808875a1b348408]
Height: 0
Ed25519 Secret Key:       [ec9a2e3faead89f666bfb034c2ef857421c9099ec7d953a1cde3d8b97c2696a7]
Ed25519 Verification Key: [6be62244d4ce9e3708f41b9001f7276f6cf1f577385fa819e6c2a396f683f5dc]
```
- Sigma t = 0:
```
Verification Key: [6be62244d4ce9e3708f41b9001f7276f6cf1f577385fa819e6c2a396f683f5dc]
Sigma: [d544f714972e3f10cda9e903617c192ce14d6098f413de6e077f5ee395e7397915ee6b52d7be86e6847a3a29eb7eaff7dd606bf7cb45ed4462f6c3a6d3407404]
W[0]: [ab49dc1f84d203263f67b0ddd6307366db6520fd9b766ec75808875a1b348408]
W[1]: [64c84e76a18688a8553ec1a2f46eead7bf71f1425080c6cb71a8ea6a50bdccb2]
W[2]: [764b9b197fac8bbedc33213a2dd350212a18b2a94040d0a81a1d84ada55578e0]
W[3]: [06bafa7b32095a65189c00fa9f1b41bb7a07c167bc0662f90b0d0f0d30da06db]
W[4]: [e9b079962f0ffa8ab71c05a78b32285504946dd7c4a929ca00432c6af097a07d]
W[5]: [835619f4d0883598419bc821e079c175c43a11ec2572242e6c4ab2da1fbf96b3]
W[6]: [d5c9db27ebc1fa1b7512133ac2cb936a61aa8ea372df8e296ef43379a2957e94]
W[7]: [602f1e29210fbb5e6ce701c31bc45eef523007b9b9bbf308e505786e4f0337a4]
W[8]: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
```
- Sum Composition Secret Key, t = 0:
```
Height: 9
Binary configuration: 0
Right Seed:    [5457276efb66cc4e4d32797c0f15830035e1a80822cbe54daa6614b7b24547ec]
Left Witness:  [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
Right Witness: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
Height: 8
Binary configuration: 0
Right Seed:    [0e40e9b2db9c04abee1b487d0f3790a93d024f61c5fd6578738a532016e42ff9]
Left Witness:  [aea6f31de6c03bcff9c3ee67171134a3b1cd44cad6ef36c6cc269348bb06f1d9]
Right Witness: [602f1e29210fbb5e6ce701c31bc45eef523007b9b9bbf308e505786e4f0337a4]
Height: 7
Binary configuration: 0
Right Seed:    [a655a60c1fa82bcbe3a2234e5b8ddaa351a7b54e586c5621562c663b5d93d1d5]
Left Witness:  [de39a2b49878523c69ce453a91836a85be83530fcc2a34a7999c2be9820eb76b]
Right Witness: [d5c9db27ebc1fa1b7512133ac2cb936a61aa8ea372df8e296ef43379a2957e94]
Height: 6
Binary configuration: 0
Right Seed:    [868f22dad181b3addddce9d2c1dd5e8e11832bb81e623bb43a0d0aba63c06695]
Left Witness:  [ab3df4e0548a11e6861602d233fd676ccb7a6cad6b450d77d0300e014fbae823]
Right Witness: [835619f4d0883598419bc821e079c175c43a11ec2572242e6c4ab2da1fbf96b3]
Height: 5
Binary configuration: 0
Right Seed:    [1d84b6a18c2dbc3a6d4299cae16832a25e44333bd65f70dc7faeb3a7946b1f94]
Left Witness:  [0d59f50d1cd37505cb61a6b3b4225c1a167b8aa30886f0c57efd4c1c2376c4dc]
Right Witness: [e9b079962f0ffa8ab71c05a78b32285504946dd7c4a929ca00432c6af097a07d]
Height: 4
Binary configuration: 0
Right Seed:    [fdc725d65d477268ceade7fe0f60605de7d54e8ca75c4ce2937db688567a4f61]
Left Witness:  [98abdc8e9664754a235228f967f61208b95f929cafce54e5338e8489e4378d67]
Right Witness: [06bafa7b32095a65189c00fa9f1b41bb7a07c167bc0662f90b0d0f0d30da06db]
Height: 3
Binary configuration: 0
Right Seed:    [4007bed98feb9d9dc33dde2b0a8a31128836d784fd3963241375d91b95c1122e]
Left Witness:  [d28a9de3831809b411820cc1844c28ae521caefc1f5c63d7c0485618073418a0]
Right Witness: [764b9b197fac8bbedc33213a2dd350212a18b2a94040d0a81a1d84ada55578e0]
Height: 2
Binary configuration: 0
Right Seed:    [13554213fa2cb2644b84b7b10b3055a98097ff4fb970b0031f5774fd36c7c71a]
Left Witness:  [e1e968b07a50750fac0980bd0b0a0401d4d9138e1b57629362824b8304efb42e]
Right Witness: [64c84e76a18688a8553ec1a2f46eead7bf71f1425080c6cb71a8ea6a50bdccb2]
Height: 1
Binary configuration: 0
Right Seed:    [3013a848a9c0e5de77d8c1a2827085bc8c741a8164cd71852dbba95024d8efb8]
Left Witness:  [a3f042c509980961a2e2ad7ec038432e0d426a7ae35778f0fb833c1cd8dd4b03]
Right Witness: [ab49dc1f84d203263f67b0ddd6307366db6520fd9b766ec75808875a1b348408]
Height: 0
Ed25519 Secret Key:       [ec9a2e3faead89f666bfb034c2ef857421c9099ec7d953a1cde3d8b97c2696a7]
Ed25519 Verification Key: [6be62244d4ce9e3708f41b9001f7276f6cf1f577385fa819e6c2a396f683f5dc]
```
- Sigma t = 170:
```
Verification Key: [33b018939bf4e68a4021f7eb6a1cbd15a0ee84b510f0df5b0a5f77c1396cb5a8]
Sigma: [df49418eb731be253570b9b11c49d035a756a6567cff6f1a186a8e491d65feaa8dd30ce0f28178b7c537e8f02ef95fbc1a513119dc4fd5da2fcf9046ae372b0d]
W[0]: [036170862099c8c0a239896c30315228a1765914d61324df838388d948459bd1]
W[1]: [834be99a471e4ad61ff98b6de6bac26d563f5df01baede4f5a8cdb8ab2e0a1f8]
W[2]: [82e29d901d2f098f33b560122bd731ab13fc45cb859306ee09ab56554eb17757]
W[3]: [c0d1fb4997a798005a77a9549099386403adb2489592eed8c55245ff35a9ba83]
W[4]: [46e7ea0376732eb68b107cd28c67458e2a0a558f86731fa446c7e948c6112c88]
W[5]: [206331df86b24086099be2ed0a85875080fc141e180415dd3ce952e98812e68d]
W[6]: [c7d005f0e3e6cdd91c17d6b72c29c76612dfa05ba6d6159343aa23b2da3e0954]
W[7]: [aea6f31de6c03bcff9c3ee67171134a3b1cd44cad6ef36c6cc269348bb06f1d9]
W[8]: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
```
- Sum Composition Secret Key, t = 170:
```
Height: 9
Binary configuration: 0
Right Seed:    [5457276efb66cc4e4d32797c0f15830035e1a80822cbe54daa6614b7b24547ec]
Left Witness:  [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
Right Witness: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
Height: 8
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [aea6f31de6c03bcff9c3ee67171134a3b1cd44cad6ef36c6cc269348bb06f1d9]
Right Witness: [602f1e29210fbb5e6ce701c31bc45eef523007b9b9bbf308e505786e4f0337a4]
Height: 7
Binary configuration: 0
Right Seed:    [0db7db7828121b69f333bd0e55eac24baa4c6af4306d09ced1f45025fc11940f]
Left Witness:  [4f48458ab60bd11fea9a7fb9f088694173863ceeb8641b461535eaecdf85b178]
Right Witness: [c7d005f0e3e6cdd91c17d6b72c29c76612dfa05ba6d6159343aa23b2da3e0954]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [206331df86b24086099be2ed0a85875080fc141e180415dd3ce952e98812e68d]
Right Witness: [99d862462b843a228d777b56175340bbe5c4144cfc3014b0cd1a32e627d0d6bb]
Height: 5
Binary configuration: 0
Right Seed:    [0e8bb9d970b26c9d273b39c228f1049b6311dfe443fb7ce271f454fcfb940e5f]
Left Witness:  [542a1cb4f0070efa60050757dcd63700c1f4214a6613d9bab4d269c1891100c6]
Right Witness: [46e7ea0376732eb68b107cd28c67458e2a0a558f86731fa446c7e948c6112c88]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [c0d1fb4997a798005a77a9549099386403adb2489592eed8c55245ff35a9ba83]
Right Witness: [4ba9387d719f8d31219e697799cc56d66c46595a27d25995d9a901dc0ad4c9e3]
Height: 3
Binary configuration: 0
Right Seed:    [ea165c7d0b62f1df58f61b04437514d70539bbd46833f483b8699d07b94a8bd6]
Left Witness:  [47a8cff12b69ca31ceed7c2267f85f1675c17beb69abbc759316f7bb18e9a9a6]
Right Witness: [82e29d901d2f098f33b560122bd731ab13fc45cb859306ee09ab56554eb17757]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [834be99a471e4ad61ff98b6de6bac26d563f5df01baede4f5a8cdb8ab2e0a1f8]
Right Witness: [3279d879530ade0ef0169d38b7e2633d3c2a58251a352757f59d1d1fe4950e5c]
Height: 1
Binary configuration: 0
Right Seed:    [f20f143e191057ee51b0ecaef653f731751ea45026576127eec532d9941d3601]
Left Witness:  [0de5ac24e218e877b12b538fdfe6e61e4497d524fb95995c187376e6e146b4af]
Right Witness: [036170862099c8c0a239896c30315228a1765914d61324df838388d948459bd1]
Height: 0
Ed25519 Secret Key:       [559f5fbde79cf3f6e128c391b17f89e7f2b843afd31395b36ca1091510c75b5d]
Ed25519 Verification Key: [33b018939bf4e68a4021f7eb6a1cbd15a0ee84b510f0df5b0a5f77c1396cb5a8]
```
- Sigma t = 341:
```
Verification Key: [7f0e2a70950268269f5a61358de789a4dbadf196bc95e2add76c500db502244f]
Sigma: [1d0d9f0149029be706e706c65414303e1feb2729f66ebf36f83b0a8bbe48c8889331efb8c3d802a47f4fc5edd6065b67e0eeb7b0c499650c97fd89482dd93e05]
W[0]: [18765f415388a77885d164141ce3be93fdd56439ee737b282ee009b9cd6a7528]
W[1]: [e1157425b61ced91e7c7c4efeb50aba4139f40757f3fcb38ec735b085a767cc7]
W[2]: [35994a27826ae5afb00b320da42d456d0b5ee19f50e1b4440659d16191a0a27c]
W[3]: [d21290c200a714d3941b51444767fd024067eacbac26a6293f7c22bbd3fbe448]
W[4]: [d2cea35bdc7d17ceed248383ef40656d0517af7355712ad00b9345ca0eb24a62]
W[5]: [1d365198d20a5d12f50349dd18a4e93f4710cf9c875cbc32225fd151ab319c97]
W[6]: [829b7a17111b09a2566ea4222cd3b81e4769e9978c92e4f862178b28edb62fe2]
W[7]: [5c57f0063fc2ca90253367cc21f09d9430c1bc001bdf83d08669ef330521f95a]
W[8]: [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
```
- Sum Composition Secret Key, t = 341:
```
Height: 9
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
Right Witness: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
Height: 8
Binary configuration: 0
Right Seed:    [ce6d3463c2f90de1388cbe1e91a261a974ac0ed2abc124c3eb4d3cfb758798cc]
Left Witness:  [f6736c7286910bb1f9b3728ddbb4c8c17142a41b880d9ad08faefec6966c1c9d]
Right Witness: [5c57f0063fc2ca90253367cc21f09d9430c1bc001bdf83d08669ef330521f95a]
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [829b7a17111b09a2566ea4222cd3b81e4769e9978c92e4f862178b28edb62fe2]
Right Witness: [ef2a8129c70adf0564f068c76ebd8594457040f4d04be47e6351461205dbec9d]
Height: 6
Binary configuration: 0
Right Seed:    [f43ad732ae02d59040a15fefe665a70a97d278afd435164f4871470a38b57aa9]
Left Witness:  [1a40b71af42b0342a40cf5f7bc0ff58c6c6010db373875974ec0882352c6729e]
Right Witness: [1d365198d20a5d12f50349dd18a4e93f4710cf9c875cbc32225fd151ab319c97]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [d2cea35bdc7d17ceed248383ef40656d0517af7355712ad00b9345ca0eb24a62]
Right Witness: [60a71660198dfbd7c7d8af91b4cf208226784970f64d5342708b469750e6245c]
Height: 4
Binary configuration: 0
Right Seed:    [862eb8f6d8d92e8135ed191cfa3bb0599cf7518908f65f620d00152a7c9422b9]
Left Witness:  [5bbf1b380a502cd7c66c2ff9916c56db928fca8c414aabde172f770afb549fc8]
Right Witness: [d21290c200a714d3941b51444767fd024067eacbac26a6293f7c22bbd3fbe448]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [35994a27826ae5afb00b320da42d456d0b5ee19f50e1b4440659d16191a0a27c]
Right Witness: [c2b23fccc811e3735f6296b6b7a06683b88db3dc2421de0852bf4213ae984464]
Height: 2
Binary configuration: 0
Right Seed:    [5e378fd9b623e0f4f4eded4b7004c5541b760897e7ea8e9c631341aa434863a4]
Left Witness:  [a86305dea7699e33045b3001e532b50e0fc4255095d53a4f58eb9e046a962a34]
Right Witness: [e1157425b61ced91e7c7c4efeb50aba4139f40757f3fcb38ec735b085a767cc7]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [18765f415388a77885d164141ce3be93fdd56439ee737b282ee009b9cd6a7528]
Right Witness: [4bab7af5c3c332f85b4a014e24f93c45778c8040c9b811b9ff077c77bf3b9cd4]
Height: 0
Ed25519 Secret Key:       [07aca12aae769263b2fe99addd59cf52149e2417dfb083225d7fd085df01215a]
Ed25519 Verification Key: [7f0e2a70950268269f5a61358de789a4dbadf196bc95e2add76c500db502244f]
```
- Sigma t = 511:
```
Verification Key: [4cb73ff4c311732d82b1bc9aef1f1b7ab5e2d29bf47819802df6fdf313c8657a]
Sigma: [3f8961ca3f8517996247b2067674eff508ae2f8e10794da8d23cb2ddee0b243d0ef3476f7583b774b0d75b05cf7c06611faf69855f67c574c76062c9f87da902]
W[0]: [51dfd2ad54dc209747a581cec6dce2543fa7026a004c88369ca03bdf2ada7199]
W[1]: [b9b13fa344f35521b8d65dc7283cf4c234bcff82a42225342fbde87cacd53c2d]
W[2]: [3d2377746a648c0164cc718e73efddb2f5235237b8287be1695e34034e7995c8]
W[3]: [3dc6d1735c48730059a99dacc6f8b5cb10c5b9ecf6d7578408e1a674a4ce22cc]
W[4]: [a7f2fbbaf90b602b2656a0ff9180aaa258ee231f910b957a51e3146dbe31a072]
W[5]: [90384c92468a09f0a53f33b3feb1efa7fe32108782f99430dcd93facea4e5158]
W[6]: [0ae25d6aaeed8e410e34e06b58558ba861aaaa0ee2e407fccc870466f9da9a9b]
W[7]: [f6736c7286910bb1f9b3728ddbb4c8c17142a41b880d9ad08faefec6966c1c9d]
W[8]: [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
```
- Sum Composition Secret Key, t = 511:
```
Height: 9
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [890248945f21710431d1f110abc7ed56df2d23e566b598cbaf30ba4018c33a31]
Right Witness: [981df6c42eea090e0faa8a2bc70ebf948eabb966aecdf08f54e0f934882632ea]
Height: 8
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [f6736c7286910bb1f9b3728ddbb4c8c17142a41b880d9ad08faefec6966c1c9d]
Right Witness: [5c57f0063fc2ca90253367cc21f09d9430c1bc001bdf83d08669ef330521f95a]
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [0ae25d6aaeed8e410e34e06b58558ba861aaaa0ee2e407fccc870466f9da9a9b]
Right Witness: [756a70352adbabb5f55e211c7169b78771a9952c809a0049d36e5a6d59574516]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [90384c92468a09f0a53f33b3feb1efa7fe32108782f99430dcd93facea4e5158]
Right Witness: [cabc23fd30602cb49241b3a9210d6c800012eda34911489e385f8bb89b062a9c]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [a7f2fbbaf90b602b2656a0ff9180aaa258ee231f910b957a51e3146dbe31a072]
Right Witness: [7f68d4433ced43d9e4c111144e59283c01df2ef83c2fd46c1ec3e9d84548e8cb]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [3dc6d1735c48730059a99dacc6f8b5cb10c5b9ecf6d7578408e1a674a4ce22cc]
Right Witness: [10e564630c70e1ef50dfe31ae79330a374d29b0cba1917ebb5e898bf0877aa55]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [3d2377746a648c0164cc718e73efddb2f5235237b8287be1695e34034e7995c8]
Right Witness: [520e4c442d544b27b3b01613eb9af378e1568fbfbaf2c97f4d328f3484c70d59]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [b9b13fa344f35521b8d65dc7283cf4c234bcff82a42225342fbde87cacd53c2d]
Right Witness: [1277886049ee15798b00b271133c076b1fdc910bf50318d711b17b426f5fba2d]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [51dfd2ad54dc209747a581cec6dce2543fa7026a004c88369ca03bdf2ada7199]
Right Witness: [7be3a0a42e7eff3eda16e6559517c1da94f291f5a722a40a61cebd7717b236d2]
Height: 0
Ed25519 Secret Key:       [1d267e0221df2a2575951c0bc2667a03d7865486276d1868b147e72be90d5b13]
Ed25519 Verification Key: [4cb73ff4c311732d82b1bc9aef1f1b7ab5e2d29bf47819802df6fdf313c8657a]
```
## Test Vector - 10
### Description 
 Generate and verify a specified sum composition signature at `t = [0, 341, 682, 1023]` using a provided seed, message, and height
### Inputs
- Seed Bytes:
```
5f99bac5f58604bc6dc2f8bce1603fc58ad27fae6dddfb04a97b2e1d3efb2aa9
```
- h (int):

```10```

- Message (string):
```
"predicate, pontificate, travel long distances and speak truth"
```
- Message (bytes) with `utf-8` encoding:
```
7072656469636174652c20706f6e74696669636174652c2074726176656c206c6f6e672064697374616e63657320616e6420737065616b207472757468
```
### Outputs
- Sum Composition Verification Key:
```
39944eb590c1b62aee6149859f92d91ce2cb757d5ac1c3af2263fb85a2bc1874
```
- Sum Composition Secret Key, t = 0:
```
Height: 10
Binary configuration: 0
Right Seed:    [7b250c384f3376a324544096be1bdef89e66db528df0ebd1b3231d1a5475af58]
Left Witness:  [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
Right Witness: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
Height: 9
Binary configuration: 0
Right Seed:    [b98627e76b8d8e7487649a566312bee505b9726b70483fc019bee7de85f69ecd]
Left Witness:  [18e56f6d6af8adc85256bf5c047544ce2816503f028904e16ffda35813410a12]
Right Witness: [0de1e23b5721fc343fb7447006877ddbaace044d367bbc25803daafd2989c6ac]
Height: 8
Binary configuration: 0
Right Seed:    [49e38086e14833367472d5d57ed270ed505de7ba20fd5c825d268998d8cd0cdb]
Left Witness:  [18e670100f5790a952ea2846602fa3119114ec7076d4a1c8448496693bad32f5]
Right Witness: [a2e0bf9f39995f5f40c3f7593455a21cb87242b0dfa08e135766063ae091a8b2]
Height: 7
Binary configuration: 0
Right Seed:    [0d8b9ff5af18fcebce41feea1cfe612b297e564d8d547a2e73634340fddd9f97]
Left Witness:  [f84a53ca925f8a0411a2b8395f18bf588fecb4df9256906540c2e4104fc5a38f]
Right Witness: [40bd193d32581dcf1fc549ff06696fcc266c01633f335b18239a1da9d4ab1eef]
Height: 6
Binary configuration: 0
Right Seed:    [f0617a18cac6c28db4ec66812acddcd1bdd1b946f974603774eab956a5fb6de5]
Left Witness:  [b76db9c1d833269d0d16b5fd3fd2c080ab877b2d3cc340c7eda0f3ab42342ca3]
Right Witness: [22c09d8f4d771082716ac4ccc251de14e24d36325a3165cb1a9e40be2b3f389a]
Height: 5
Binary configuration: 0
Right Seed:    [44f6d9db2aa1fe480c1a962e39e9f508fed424185ab8e5509ffc5fd6c0ac127d]
Left Witness:  [88ae5c4eb75a70bac8d57a01e7d04593277135d1283bf86477cc3bc1cfd1a701]
Right Witness: [d7ea43dd328447530b3e4174531935ed85a35430828fff32d670199a70a92037]
Height: 4
Binary configuration: 0
Right Seed:    [d94e8702fccf7641af3a2c8a3fff4517491f822b525f62d1d6396176ac79741d]
Left Witness:  [a6e80f8b1d64a8dd94095515b694ddc01d5fa2dd984c59af8c0321b48a3f01b8]
Right Witness: [0e44f84dca51b18827453df00a5e6e3217de064c2e5fa35ab800f0ffe4f7d916]
Height: 3
Binary configuration: 0
Right Seed:    [2dd9d8fbdd0ed47a83bb00de456b40d5848194b8c2b44691e7928e2043696ffd]
Left Witness:  [a97decac0a4a3e1378043d84c5a0b16a33cb879b3718f1f6b92ec437f98c2bb7]
Right Witness: [4b5d5922d31c0d7dc38bddc302c178509845f230fcb9f139c98e3f85fb49a4f5]
Height: 2
Binary configuration: 0
Right Seed:    [249581449b863b94661c7f95d42c0eb6580f7a21b767ce144856796f78bba1b2]
Left Witness:  [f2d8c1eae368eaa8d62fcffa63c85e9deb392de5788ecb9c7e41fa0827c41f9d]
Right Witness: [a50347e0deaa70168440d58ad099d769e759599caeb071322c826d2eb676f54e]
Height: 1
Binary configuration: 0
Right Seed:    [ae1f790ad1dd0d41484e82a8ac1e46cf12892c8d86cf42199b12820a988a3dfd]
Left Witness:  [637ffcceeeaea78747e5a7f722379a37bbd225eb30e4efecda8ccbdc2d92fb39]
Right Witness: [d4aefee71ac47cd88c1ffbea53415526fd2c195eaae7e561b0db2fead574892c]
Height: 0
Ed25519 Secret Key:       [a20ac03d3f5a049a87e193faa14a0ee137b4aa575b478447af16e065989a2cd7]
Ed25519 Verification Key: [9bf002487ba805cdeedf3fab89c0616f9301da7f8d8c7feef87dd2d1d584848f]
```
- Sigma t = 0:
```
Verification Key: [9bf002487ba805cdeedf3fab89c0616f9301da7f8d8c7feef87dd2d1d584848f]
Sigma: [04a361ceca419e8073c51a98fbd673ccb0a0f23efdf473d764da292415d7d71cb86115fa70cc0dd3f2f1f86478d8a02748bb12105dc2203798cc7b6129c38e0d]
W[0]: [d4aefee71ac47cd88c1ffbea53415526fd2c195eaae7e561b0db2fead574892c]
W[1]: [a50347e0deaa70168440d58ad099d769e759599caeb071322c826d2eb676f54e]
W[2]: [4b5d5922d31c0d7dc38bddc302c178509845f230fcb9f139c98e3f85fb49a4f5]
W[3]: [0e44f84dca51b18827453df00a5e6e3217de064c2e5fa35ab800f0ffe4f7d916]
W[4]: [d7ea43dd328447530b3e4174531935ed85a35430828fff32d670199a70a92037]
W[5]: [22c09d8f4d771082716ac4ccc251de14e24d36325a3165cb1a9e40be2b3f389a]
W[6]: [40bd193d32581dcf1fc549ff06696fcc266c01633f335b18239a1da9d4ab1eef]
W[7]: [a2e0bf9f39995f5f40c3f7593455a21cb87242b0dfa08e135766063ae091a8b2]
W[8]: [0de1e23b5721fc343fb7447006877ddbaace044d367bbc25803daafd2989c6ac]
W[9]: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
```
- Sum Composition Secret Key, t = 0:
```
Height: 10
Binary configuration: 0
Right Seed:    [7b250c384f3376a324544096be1bdef89e66db528df0ebd1b3231d1a5475af58]
Left Witness:  [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
Right Witness: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
Height: 9
Binary configuration: 0
Right Seed:    [b98627e76b8d8e7487649a566312bee505b9726b70483fc019bee7de85f69ecd]
Left Witness:  [18e56f6d6af8adc85256bf5c047544ce2816503f028904e16ffda35813410a12]
Right Witness: [0de1e23b5721fc343fb7447006877ddbaace044d367bbc25803daafd2989c6ac]
Height: 8
Binary configuration: 0
Right Seed:    [49e38086e14833367472d5d57ed270ed505de7ba20fd5c825d268998d8cd0cdb]
Left Witness:  [18e670100f5790a952ea2846602fa3119114ec7076d4a1c8448496693bad32f5]
Right Witness: [a2e0bf9f39995f5f40c3f7593455a21cb87242b0dfa08e135766063ae091a8b2]
Height: 7
Binary configuration: 0
Right Seed:    [0d8b9ff5af18fcebce41feea1cfe612b297e564d8d547a2e73634340fddd9f97]
Left Witness:  [f84a53ca925f8a0411a2b8395f18bf588fecb4df9256906540c2e4104fc5a38f]
Right Witness: [40bd193d32581dcf1fc549ff06696fcc266c01633f335b18239a1da9d4ab1eef]
Height: 6
Binary configuration: 0
Right Seed:    [f0617a18cac6c28db4ec66812acddcd1bdd1b946f974603774eab956a5fb6de5]
Left Witness:  [b76db9c1d833269d0d16b5fd3fd2c080ab877b2d3cc340c7eda0f3ab42342ca3]
Right Witness: [22c09d8f4d771082716ac4ccc251de14e24d36325a3165cb1a9e40be2b3f389a]
Height: 5
Binary configuration: 0
Right Seed:    [44f6d9db2aa1fe480c1a962e39e9f508fed424185ab8e5509ffc5fd6c0ac127d]
Left Witness:  [88ae5c4eb75a70bac8d57a01e7d04593277135d1283bf86477cc3bc1cfd1a701]
Right Witness: [d7ea43dd328447530b3e4174531935ed85a35430828fff32d670199a70a92037]
Height: 4
Binary configuration: 0
Right Seed:    [d94e8702fccf7641af3a2c8a3fff4517491f822b525f62d1d6396176ac79741d]
Left Witness:  [a6e80f8b1d64a8dd94095515b694ddc01d5fa2dd984c59af8c0321b48a3f01b8]
Right Witness: [0e44f84dca51b18827453df00a5e6e3217de064c2e5fa35ab800f0ffe4f7d916]
Height: 3
Binary configuration: 0
Right Seed:    [2dd9d8fbdd0ed47a83bb00de456b40d5848194b8c2b44691e7928e2043696ffd]
Left Witness:  [a97decac0a4a3e1378043d84c5a0b16a33cb879b3718f1f6b92ec437f98c2bb7]
Right Witness: [4b5d5922d31c0d7dc38bddc302c178509845f230fcb9f139c98e3f85fb49a4f5]
Height: 2
Binary configuration: 0
Right Seed:    [249581449b863b94661c7f95d42c0eb6580f7a21b767ce144856796f78bba1b2]
Left Witness:  [f2d8c1eae368eaa8d62fcffa63c85e9deb392de5788ecb9c7e41fa0827c41f9d]
Right Witness: [a50347e0deaa70168440d58ad099d769e759599caeb071322c826d2eb676f54e]
Height: 1
Binary configuration: 0
Right Seed:    [ae1f790ad1dd0d41484e82a8ac1e46cf12892c8d86cf42199b12820a988a3dfd]
Left Witness:  [637ffcceeeaea78747e5a7f722379a37bbd225eb30e4efecda8ccbdc2d92fb39]
Right Witness: [d4aefee71ac47cd88c1ffbea53415526fd2c195eaae7e561b0db2fead574892c]
Height: 0
Ed25519 Secret Key:       [a20ac03d3f5a049a87e193faa14a0ee137b4aa575b478447af16e065989a2cd7]
Ed25519 Verification Key: [9bf002487ba805cdeedf3fab89c0616f9301da7f8d8c7feef87dd2d1d584848f]
```
- Sigma t = 341:
```
Verification Key: [73a6aaeffe45d8e2d3b86d67eeb680c989fe962fa2b55e55501b1535184a7f1b]
Sigma: [c79446d4f125d1336abc56818eb549a4f522100b24430531fda94bdecaabe26d32825ec0c138bf87fb1dbd3f0b6793fd83c6a0762249fe354ba83926122e5701]
W[0]: [7a9432d1868a44cb1b90d37c908112631e2c580d63d4ceb70b7f0df857b76b81]
W[1]: [4f8d5e7eabf887a2b2d20bb46d331c83c254094dd42e76f3ac80cdac9bfd1616]
W[2]: [191787f4779da93ba254d3878d585f13064369aa57d4b001f04fb4ee5c0a8ad4]
W[3]: [ed6fbee9f1d2c104299247c840d7999adf7dd91e2d93eff90055a136eb2242f4]
W[4]: [719ba3cff40f293eb1976360376b09f2722f615e03a980b4f7d8f1a16bbd2339]
W[5]: [136240e16c9411228dcc933751ed84539f7597ca2209f6ebcbcaa08bd9cf549f]
W[6]: [bb6489b163c05afdfab6edeb6b64912f07e160ead76bcb58c88bf08f6a6c8e79]
W[7]: [72d090dd9a74cf881c6723b681211c22ccb4d612e995e264b7ab904a4f54f5d6]
W[8]: [18e56f6d6af8adc85256bf5c047544ce2816503f028904e16ffda35813410a12]
W[9]: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
```
- Sum Composition Secret Key, t = 341:
```
Height: 10
Binary configuration: 0
Right Seed:    [7b250c384f3376a324544096be1bdef89e66db528df0ebd1b3231d1a5475af58]
Left Witness:  [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
Right Witness: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
Height: 9
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [18e56f6d6af8adc85256bf5c047544ce2816503f028904e16ffda35813410a12]
Right Witness: [0de1e23b5721fc343fb7447006877ddbaace044d367bbc25803daafd2989c6ac]
Height: 8
Binary configuration: 0
Right Seed:    [facf1427629a2025e3b53345f86690ae56e5b9752fea33448e0c730d4c66c31b]
Left Witness:  [ea746013a93dacc373ba5e0e3c979667e592e385e23736c2fcf9df9b3bb3d524]
Right Witness: [72d090dd9a74cf881c6723b681211c22ccb4d612e995e264b7ab904a4f54f5d6]
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [bb6489b163c05afdfab6edeb6b64912f07e160ead76bcb58c88bf08f6a6c8e79]
Right Witness: [c452a08042c58e2f1604c52a99952095e4e0bcb188dbe693b077759fa73299be]
Height: 6
Binary configuration: 0
Right Seed:    [8020aca7ea26f1085631dd9dc4b59cd8ad963cc1ed69ddcd55a441111d0d017b]
Left Witness:  [7751ec1fc3444d809888c17e2a54bb488a70d9a6dea4c7e02b53a12d0167f598]
Right Witness: [136240e16c9411228dcc933751ed84539f7597ca2209f6ebcbcaa08bd9cf549f]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [719ba3cff40f293eb1976360376b09f2722f615e03a980b4f7d8f1a16bbd2339]
Right Witness: [07d5506512303970fcdbae80347eeef0008ee4c58fc9551cb97b2fdd5509a08e]
Height: 4
Binary configuration: 0
Right Seed:    [20152647fe0dcd3bcc7a80ddfd973d84f5a03202b4d7f64aded2846a64ca1cc5]
Left Witness:  [53deeae144f586c3d7b3d2d8f7662be643145b1999feba4358927ce3f710b430]
Right Witness: [ed6fbee9f1d2c104299247c840d7999adf7dd91e2d93eff90055a136eb2242f4]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [191787f4779da93ba254d3878d585f13064369aa57d4b001f04fb4ee5c0a8ad4]
Right Witness: [951e1e27f5f54c2719f583681bd650816b8b2c61a477b8614ff0dca0080a501a]
Height: 2
Binary configuration: 0
Right Seed:    [7556932143d290246c7bb7476dbe42f4f91f38b226a40bd4bf9c6f81e77ab372]
Left Witness:  [fc515b49d3b3ceaf6610ff9a83e21f599b984a0e1cf1d57e355989a9cafe866b]
Right Witness: [4f8d5e7eabf887a2b2d20bb46d331c83c254094dd42e76f3ac80cdac9bfd1616]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [7a9432d1868a44cb1b90d37c908112631e2c580d63d4ceb70b7f0df857b76b81]
Right Witness: [2555a1e4307d16ceeaf53deb286cc45c02e6b1bd6d49a38363552a2925002316]
Height: 0
Ed25519 Secret Key:       [7a419926cf18fd2721d2a688404df943a918c92a2f65d4668d5fafc5874547da]
Ed25519 Verification Key: [73a6aaeffe45d8e2d3b86d67eeb680c989fe962fa2b55e55501b1535184a7f1b]
```
- Sigma t = 682:
```
Verification Key: [cfed39e1d7272468b6df99f7a822739b90b7f5fb67d08e051eeac3767956275c]
Sigma: [e8d1736f1ffa8811ed8a148d71b568d9a3bf94dde4ff1247bfb670576ab8b9a1d6b13d92c5cef927dee4acf2fca630d37c71421f1e8686a0e95818ccfcbb540a]
W[0]: [bccf9fa832b985b86d47b96f60d1eacd35512369212a9a1474a51ab7af21a1d8]
W[1]: [4859c67de1d22dd7acd7d58ba84b38c34c32299347670eb3fbe4983c9f839d24]
W[2]: [1ed8b644925f17a4147d92a8cf8a359d0fe433cf0ab0501124df4c4e3da2fca1]
W[3]: [00c8d73ec21df123f3dfe9d48234de9496ca1f99cb4241f9155872eea3b634c8]
W[4]: [b9a75e9a67a7da394154a31bd1ababe6c05950264983505298234e614a60ebab]
W[5]: [e48e2d8fb0ac909e9d39ed88d6b51da8b1ae71b346c9ad8b92a2d8f3b077e398]
W[6]: [7ce0753e0334af86628f601759abe7c04aaf425ae82072c506ba04fbbea70ff4]
W[7]: [f9035bb44a93037d26743820a498750872a65cb758780b70c4437d0597c65058]
W[8]: [2b675edd5d75fb8c6c0f1f8e04f1752350a327756cff30c01f83b3c3e7a759d3]
W[9]: [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
```
- Sum Composition Secret Key, t = 682:
```
Height: 10
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
Right Witness: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
Height: 9
Binary configuration: 0
Right Seed:    [8aa710eed4b3432b5f1eb129f513d41cc27ef5e9514ad713125849f667331b45]
Left Witness:  [2e03393dbe1d83bdf8b23caf0e3aa8a78e906f2ca9467c1cb25b364ce4f41a92]
Right Witness: [2b675edd5d75fb8c6c0f1f8e04f1752350a327756cff30c01f83b3c3e7a759d3]
Height: 8
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [f9035bb44a93037d26743820a498750872a65cb758780b70c4437d0597c65058]
Right Witness: [1c1711f7d1f480c5195301020ef19bfa110e93d3c0a771c01cc6a80caad72aee]
Height: 7
Binary configuration: 0
Right Seed:    [a82bd456e557e07ab4f6f504bbbbb08df4fdc668b1aa13a21b3b9d7bb33eb61b]
Left Witness:  [144b1d208c221ad738df7c20ab138bb52ad70f493f45f07689e20c0911400e0d]
Right Witness: [7ce0753e0334af86628f601759abe7c04aaf425ae82072c506ba04fbbea70ff4]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [e48e2d8fb0ac909e9d39ed88d6b51da8b1ae71b346c9ad8b92a2d8f3b077e398]
Right Witness: [3e3bed025b491a59d9b234c9b118fc359024bd3d57cf2e74d418fc5d55a87c6d]
Height: 5
Binary configuration: 0
Right Seed:    [6b0e2d0ae1a638dc4ab1d33b247c11f6507d7068e6e17f450ae3c87904432245]
Left Witness:  [e1a87924694227fb00f95bf1a7c2bc91cd028cff9da9942f4a487d940057c1d8]
Right Witness: [b9a75e9a67a7da394154a31bd1ababe6c05950264983505298234e614a60ebab]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [00c8d73ec21df123f3dfe9d48234de9496ca1f99cb4241f9155872eea3b634c8]
Right Witness: [217a3f3dd0f736bfb98ae4b09f927c7c421df18f25fe23cf18eb57d3c957072a]
Height: 3
Binary configuration: 0
Right Seed:    [6b6c525157ebce60a9d6acb6e5035ac0644173a38f7edc02ee8d95548c5a5e35]
Left Witness:  [a604a9def780ba47d4accdd56ba3a6726e0c52a41bf5c7319ad35a14402067d7]
Right Witness: [1ed8b644925f17a4147d92a8cf8a359d0fe433cf0ab0501124df4c4e3da2fca1]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [4859c67de1d22dd7acd7d58ba84b38c34c32299347670eb3fbe4983c9f839d24]
Right Witness: [5d44af3497d599006250a9c466521a86c413200402a004d51dbe472cfe229ab3]
Height: 1
Binary configuration: 0
Right Seed:    [dd27497783343035a90edde8815537facf578f36a788e7374d998ddfa540aa2e]
Left Witness:  [dd7e19e3c408d50af0a8a952a72b21dcd00e638a8ee2d7085315f1074c171e52]
Right Witness: [bccf9fa832b985b86d47b96f60d1eacd35512369212a9a1474a51ab7af21a1d8]
Height: 0
Ed25519 Secret Key:       [2bfa0f066cc6cab22c2e8bb600f9ef097ae5e12108d88d7b25b3e2c171021599]
Ed25519 Verification Key: [cfed39e1d7272468b6df99f7a822739b90b7f5fb67d08e051eeac3767956275c]
```
- Sigma t = 1023:
```
Verification Key: [6b9e0ecfc517ba0ec129e5c45350fd62aab6a6a8fbe50e9c86856ffa0eca6e00]
Sigma: [2c6a39940ee482f2a92fee83107856717738b2033c639df87bc1550363e5e18c8e2cfcd90e20c4d83958353a9482a30a6e74fd072b6cd8feb2a7e5974922c508]
W[0]: [56a530273016777eebab4dbf696ec567d8cfb1e640f233774b2b408282fd0d13]
W[1]: [ddf086b3ea10373c2794180c20aa54111dd00b3153997b023884103f9d75c563]
W[2]: [cf941a8c2719c8d2b3c47907090d05e73d0a7eac4826e4c426ad665e1a77d3d9]
W[3]: [e4c1802a55cb9f3849254a465eac985ec81f442f2151b10f8e2c578beed9eec3]
W[4]: [c9b4e6986d42038a1bba06fa594fb1fb8102fcd86e806f5690ada146df5bacfb]
W[5]: [cab5a0899a9644b9dcbbb67356f3c5501d35e66129750348c66d3983c2944666]
W[6]: [a1d40e293e83ac276ae12b5e53b1d4e09061a518d38eb80bccf451df7c6a0711]
W[7]: [4057185c904d1e67e74c7384b696cd44516c767ee8e51246483066b24c687963]
W[8]: [2e03393dbe1d83bdf8b23caf0e3aa8a78e906f2ca9467c1cb25b364ce4f41a92]
W[9]: [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
```
- Sum Composition Secret Key, t = 1023:
```
Height: 10
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [fded3b2a093e67126054010c1a1ddef92cdab1427a51ae7d616b49109dec442f]
Right Witness: [9f4cebedb42cb5650b82c0a957461ab033f9b50434b502353c71a4d81d746546]
Height: 9
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [2e03393dbe1d83bdf8b23caf0e3aa8a78e906f2ca9467c1cb25b364ce4f41a92]
Right Witness: [2b675edd5d75fb8c6c0f1f8e04f1752350a327756cff30c01f83b3c3e7a759d3]
Height: 8
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [4057185c904d1e67e74c7384b696cd44516c767ee8e51246483066b24c687963]
Right Witness: [834218f6400bf7c66e9422b15ea28178d4d4c5c363fade37c7a88bf23ee47965]
Height: 7
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [a1d40e293e83ac276ae12b5e53b1d4e09061a518d38eb80bccf451df7c6a0711]
Right Witness: [05afa71e9ed4aec9a41750accb064d5cfc1eb70b87cad08d2fb7d1ca741c7d77]
Height: 6
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [cab5a0899a9644b9dcbbb67356f3c5501d35e66129750348c66d3983c2944666]
Right Witness: [f4cf225211185350fc3f321b28afb3c246211b4bb9d0d31514cac7828d83cb17]
Height: 5
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [c9b4e6986d42038a1bba06fa594fb1fb8102fcd86e806f5690ada146df5bacfb]
Right Witness: [a87f070ae4963ae47c85c46daa3c411bb27499c9eaf37b2ef11a51e9d10f5a6f]
Height: 4
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [e4c1802a55cb9f3849254a465eac985ec81f442f2151b10f8e2c578beed9eec3]
Right Witness: [fbef4b1425a6dfc3db186045fe8a3998fa5424b88457d4617dd6d6ed654db6a6]
Height: 3
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [cf941a8c2719c8d2b3c47907090d05e73d0a7eac4826e4c426ad665e1a77d3d9]
Right Witness: [426b6cb5138c9662c16fe1013b9aee2dcddd2b6632dd4f86afa6d1b933c8bbb3]
Height: 2
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [ddf086b3ea10373c2794180c20aa54111dd00b3153997b023884103f9d75c563]
Right Witness: [67d2a1733f565b914d059ff643d1c132f0a621ebf07358f717cb63e4681452d5]
Height: 1
Binary configuration: 1
Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
Left Witness:  [56a530273016777eebab4dbf696ec567d8cfb1e640f233774b2b408282fd0d13]
Right Witness: [1f4e209c59ae8ecd7134949f724f67542fcf712bb5866870bd4253c7ddfab0d8]
Height: 0
Ed25519 Secret Key:       [05a0c7000227ad6fe123111fdf298694cd5424368f0992ee32be81e46feb33a0]
Ed25519 Verification Key: [6b9e0ecfc517ba0ec129e5c45350fd62aab6a6a8fbe50e9c86856ffa0eca6e00]
```
