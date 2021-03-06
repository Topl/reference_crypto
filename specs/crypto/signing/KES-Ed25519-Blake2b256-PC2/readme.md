## Description
Test vectors for Topl implementation of a two tree product key evolving signature scheme in the construction of [Malkin-Micciancio-Miner](https://cseweb.ucsd.edu/~daniele/papers/MMM.pdf). A full specification including protocol box descriptions is available in this repo.
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
 Generate and verify a specified product composition signature at `t = [0, 1, 2, 3]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
2a6367c85f416ccef46a4521004228f74f24f7b0770ecced07c0dc035135bf6f
```
- h1 (int):

```1```

- h2 (int):

```1```

- Message (string):
```
"it as do be it he me or"
```
- Message (bytes) with `utf-8` encoding:
```
697420617320646f206265206974206865206d65206f72
```
### Outputs
- Product Composition Verification Key:
```
47099c36fc71c2aae79046c65bb5d3f2c79d058bddd346370bfd22c6263d438d
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 1
    Binary configuration: 0
    Right Seed:    [2fc8c0b612d9115edd39a10908f972638dee21095ab477e449ca259b628081bb]
    Left Witness:  [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
    Right Witness: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
    Height: 0
    Ed25519 Secret Key:       [55576ccc3c12598a3d3fb4bd418c4df3105f8f6ca723d21f47a058e3584ec223]
    Ed25519 Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
Sigma 1:
    Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
    Sigma: [e23e79815bf3faa96c786a2e7a22379b0f14d578aec4b2d31c225bd145dfc0b7041fd4a4dfff26f5214a168eccd9f416fdaeba6cf15784cc7451562550904109]
    W[0]: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
Seed:
    af0200b637b63aab28b415260ad9d1aa197c59d95fff073e360eeb2f85b9c2c0
Tau 2:
    Height: 1
    Binary configuration: 0
    Right Seed:    [f1a1f273a994985d277e419fc28affbc8a671c6186f0de881aac1751fe57f958]
    Left Witness:  [a2fc1f14fa2c724cf2972d030fca6f1adf78490018760fa3e3b5ad46279b47e1]
    Right Witness: [07586219db5738b54be24aec04f8f51f1d84a1531860135f9bcc4fbe3bc51a55]
    Height: 0
    Ed25519 Secret Key:       [ea25235b5769e5bd64ddf1e95fc1ba47acceed967a5eee6bf946e29cdd39c9f4]
    Ed25519 Verification Key: [1747b2fffbeccefa8a855bb28af7f7e8937bc5e24972bf49a9ad1cf26168ef54]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
    Sigma: [e23e79815bf3faa96c786a2e7a22379b0f14d578aec4b2d31c225bd145dfc0b7041fd4a4dfff26f5214a168eccd9f416fdaeba6cf15784cc7451562550904109]
    W[0]: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
Sigma 2:
    Verification Key: [1747b2fffbeccefa8a855bb28af7f7e8937bc5e24972bf49a9ad1cf26168ef54]
    Sigma: [4b6fb021e285e7f7408c3c80bd8217e8edcb5623e02f12956d32d9412caa1e995dd1400e3a638280aeba1aed909be2021c48d63dd966be1b52012b5ad392740b]
    W[0]: [07586219db5738b54be24aec04f8f51f1d84a1531860135f9bcc4fbe3bc51a55]
R 2: [d86d2201174bea618cdae1f62f0be718e9cff353dea2d4da710652d2011727a4]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 1
    Binary configuration: 0
    Right Seed:    [2fc8c0b612d9115edd39a10908f972638dee21095ab477e449ca259b628081bb]
    Left Witness:  [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
    Right Witness: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
    Height: 0
    Ed25519 Secret Key:       [55576ccc3c12598a3d3fb4bd418c4df3105f8f6ca723d21f47a058e3584ec223]
    Ed25519 Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
Sigma 1:
    Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
    Sigma: [e23e79815bf3faa96c786a2e7a22379b0f14d578aec4b2d31c225bd145dfc0b7041fd4a4dfff26f5214a168eccd9f416fdaeba6cf15784cc7451562550904109]
    W[0]: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
Seed:
    af0200b637b63aab28b415260ad9d1aa197c59d95fff073e360eeb2f85b9c2c0
Tau 2:
    Height: 1
    Binary configuration: 0
    Right Seed:    [f1a1f273a994985d277e419fc28affbc8a671c6186f0de881aac1751fe57f958]
    Left Witness:  [a2fc1f14fa2c724cf2972d030fca6f1adf78490018760fa3e3b5ad46279b47e1]
    Right Witness: [07586219db5738b54be24aec04f8f51f1d84a1531860135f9bcc4fbe3bc51a55]
    Height: 0
    Ed25519 Secret Key:       [ea25235b5769e5bd64ddf1e95fc1ba47acceed967a5eee6bf946e29cdd39c9f4]
    Ed25519 Verification Key: [1747b2fffbeccefa8a855bb28af7f7e8937bc5e24972bf49a9ad1cf26168ef54]
```
- Sigma t = 1:
```
Sigma 1:
    Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
    Sigma: [e23e79815bf3faa96c786a2e7a22379b0f14d578aec4b2d31c225bd145dfc0b7041fd4a4dfff26f5214a168eccd9f416fdaeba6cf15784cc7451562550904109]
    W[0]: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
Sigma 2:
    Verification Key: [d21551b12cf35d9b6022742352d6d5574b4f07f2cbab7f4cff25e43028b46aba]
    Sigma: [0517a4e29b8196ddfc1761fa2224b70cfc1b1b80b96faed4826a0aee80dfb1da770fe310fdf5cd596f5ad34920e6eff15fe02d5fa4fbae79e2d3db1fee68cb02]
    W[0]: [a2fc1f14fa2c724cf2972d030fca6f1adf78490018760fa3e3b5ad46279b47e1]
R 2: [d86d2201174bea618cdae1f62f0be718e9cff353dea2d4da710652d2011727a4]
```
Product Composition Secret Key, t = 1:
```
Tau 1:
    Height: 1
    Binary configuration: 0
    Right Seed:    [2fc8c0b612d9115edd39a10908f972638dee21095ab477e449ca259b628081bb]
    Left Witness:  [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
    Right Witness: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
    Height: 0
    Ed25519 Secret Key:       [55576ccc3c12598a3d3fb4bd418c4df3105f8f6ca723d21f47a058e3584ec223]
    Ed25519 Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
Sigma 1:
    Verification Key: [d1a38e6db07062c9c58036c537d1c999b6fc8b60c51feeede25afda66ee36395]
    Sigma: [e23e79815bf3faa96c786a2e7a22379b0f14d578aec4b2d31c225bd145dfc0b7041fd4a4dfff26f5214a168eccd9f416fdaeba6cf15784cc7451562550904109]
    W[0]: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
Seed:
    af0200b637b63aab28b415260ad9d1aa197c59d95fff073e360eeb2f85b9c2c0
Tau 2:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a2fc1f14fa2c724cf2972d030fca6f1adf78490018760fa3e3b5ad46279b47e1]
    Right Witness: [07586219db5738b54be24aec04f8f51f1d84a1531860135f9bcc4fbe3bc51a55]
    Height: 0
    Ed25519 Secret Key:       [f1a1f273a994985d277e419fc28affbc8a671c6186f0de881aac1751fe57f958]
    Ed25519 Verification Key: [d21551b12cf35d9b6022742352d6d5574b4f07f2cbab7f4cff25e43028b46aba]
```
- Sigma t = 2:
```
Sigma 1:
    Verification Key: [4e66fe180d5cd03c1593d2295cb21e4fbbca8d0c5fe7dbf3372a9ee6f9f1f8ae]
    Sigma: [e69d7a6ae2164e20487400d4fb10d96a2fdb37501462bb5baf7a3cc0682f7eae95aab47c5eb6a9772a77768627a36641a47c92baca75cdde404e9bfae0301d02]
    W[0]: [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
Sigma 2:
    Verification Key: [ec4a9f15574d260f9c41b0c847c08237a3f590e21bd9267bc72f25d1476ba338]
    Sigma: [7851eac4378709e78f8fc0cf17ddc7b6883670a31d1fb5fdd45b1f3a656988cd60d13c7b93095f9ce4b0e5c48dd79282761e542bfa187ff7c09619af5c7ef305]
    W[0]: [d21e09026215b55fc6c295a7fb239f3c37b558a5a19cdcb10fefc9b65201d8df]
R 2: [4f9618b4e9bdfecb43d5038cee3f1eea092a29244ee7d36da3d1a828efe8efdb]
```
Product Composition Secret Key, t = 2:
```
Tau 1:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
    Right Witness: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [4e66fe180d5cd03c1593d2295cb21e4fbbca8d0c5fe7dbf3372a9ee6f9f1f8ae]
Sigma 1:
    Verification Key: [4e66fe180d5cd03c1593d2295cb21e4fbbca8d0c5fe7dbf3372a9ee6f9f1f8ae]
    Sigma: [e69d7a6ae2164e20487400d4fb10d96a2fdb37501462bb5baf7a3cc0682f7eae95aab47c5eb6a9772a77768627a36641a47c92baca75cdde404e9bfae0301d02]
    W[0]: [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
Seed:
    272651eb4dacb102109154158a1442257fb6f78648bdeae7989fd8f4c612f567
Tau 2:
    Height: 1
    Binary configuration: 0
    Right Seed:    [d41b3736803c20e519c02666749c9212a954cb0994291e95c4b10f3fb4b2935d]
    Left Witness:  [af810b4355fc79ca2e1b27285a6dde3b725404b3937c7e120c499415375e79d8]
    Right Witness: [d21e09026215b55fc6c295a7fb239f3c37b558a5a19cdcb10fefc9b65201d8df]
    Height: 0
    Ed25519 Secret Key:       [04990a1d084b4b6e592e1b7e756254f03e72641ca5d56492aec82ce40f42b963]
    Ed25519 Verification Key: [ec4a9f15574d260f9c41b0c847c08237a3f590e21bd9267bc72f25d1476ba338]
```
- Sigma t = 3:
```
Sigma 1:
    Verification Key: [4e66fe180d5cd03c1593d2295cb21e4fbbca8d0c5fe7dbf3372a9ee6f9f1f8ae]
    Sigma: [e69d7a6ae2164e20487400d4fb10d96a2fdb37501462bb5baf7a3cc0682f7eae95aab47c5eb6a9772a77768627a36641a47c92baca75cdde404e9bfae0301d02]
    W[0]: [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
Sigma 2:
    Verification Key: [be533ba32cdc053b51218abc6ce3ebe66a9c0aa6f8be97930d9abe0b370d264e]
    Sigma: [1fd2812b224d955f2444d1d8988704c83cee284c1f023b4f9696ef2d0c19db69c75379e3a470658c67cb308dcc72f3c2e89825be9363cae3e0c91020f495e90f]
    W[0]: [af810b4355fc79ca2e1b27285a6dde3b725404b3937c7e120c499415375e79d8]
R 2: [4f9618b4e9bdfecb43d5038cee3f1eea092a29244ee7d36da3d1a828efe8efdb]
```
Product Composition Secret Key, t = 3:
```
Tau 1:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
    Right Witness: [babb43bba46bb63fc0d7f0c460733f1835b23ec59cbf89b42b8ee5090616ba2e]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [4e66fe180d5cd03c1593d2295cb21e4fbbca8d0c5fe7dbf3372a9ee6f9f1f8ae]
Sigma 1:
    Verification Key: [4e66fe180d5cd03c1593d2295cb21e4fbbca8d0c5fe7dbf3372a9ee6f9f1f8ae]
    Sigma: [e69d7a6ae2164e20487400d4fb10d96a2fdb37501462bb5baf7a3cc0682f7eae95aab47c5eb6a9772a77768627a36641a47c92baca75cdde404e9bfae0301d02]
    W[0]: [9417bf4a4456a865a92ec1cc0c50bf0f90d1f1c09f79ab80485a48ca975375e1]
Seed:
    272651eb4dacb102109154158a1442257fb6f78648bdeae7989fd8f4c612f567
Tau 2:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [af810b4355fc79ca2e1b27285a6dde3b725404b3937c7e120c499415375e79d8]
    Right Witness: [d21e09026215b55fc6c295a7fb239f3c37b558a5a19cdcb10fefc9b65201d8df]
    Height: 0
    Ed25519 Secret Key:       [d41b3736803c20e519c02666749c9212a954cb0994291e95c4b10f3fb4b2935d]
    Ed25519 Verification Key: [be533ba32cdc053b51218abc6ce3ebe66a9c0aa6f8be97930d9abe0b370d264e]
```
## Test Vector - 2
### Description 
 Generate and verify a specified product composition signature at `t = [0, 2, 4, 6]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
38c2775bc7e6866e69c6acd5e12ee366fd57f7df1b30e200cae610ec4ecf378c
```
- h1 (int):

```1```

- h2 (int):

```2```

- Message (string):
```
"in a short while craft - not much to do about it"
```
- Message (bytes) with `utf-8` encoding:
```
696e20612073686f7274207768696c65206372616674202d206e6f74206d75636820746f20646f2061626f7574206974
```
### Outputs
- Product Composition Verification Key:
```
56d4f5dc6bfe518c9b6898222c1bfc97e93f760ec48df07704369bc306884bdd
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 1
    Binary configuration: 0
    Right Seed:    [63cd4026d707c99d0e6faaf300963540275a5446c39454bec64e8a582b429233]
    Left Witness:  [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
    Right Witness: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
    Height: 0
    Ed25519 Secret Key:       [797ec460bd8298a21ab9d04c0cace497d7552eb483f772ef713e1ce90c89eab3]
    Ed25519 Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
Sigma 1:
    Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
    Sigma: [0860e791a13f1a996339054810b531ae7e7fc8a67336829dbe7698f3cd7e2f1334a020f0ff366a60e83f1968df726cd3d07c0343da1f003d588add43662fab0b]
    W[0]: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
Seed:
    9a795a3291945a4e814937a79a45e6f4473214aef80d60c7eed70d87c9aa3a52
Tau 2:
    Height: 2
    Binary configuration: 0
    Right Seed:    [14c8de0480acc4fa3aac58893675b9932455e76a4bbb0cd26e3bef1b13a80876]
    Left Witness:  [9b0df1a883f526ef04b80ea74031ac17781ec0954f7796e782c315d4617b9f8b]
    Right Witness: [37ce2848ce72147cc9a42268034c2a781168b932fae3a92964795dd993fe30ca]
    Height: 1
    Binary configuration: 0
    Right Seed:    [c510b37bc0a6b7183a527ec098acea9de5ae9f853e84ec7bbb407c89c5cd0966]
    Left Witness:  [2da6eb233a4843c7782d27924738457a22fb8ff5363b57c54d2f734f22dfc0c5]
    Right Witness: [7fbea3be88d776943503ea05a9698e9b43d221f9d4a7f65ee62ecea21381859c]
    Height: 0
    Ed25519 Secret Key:       [2322d709478474b16dfc681ee27aa51dfed98a9b2ddae7fe420586bb927d0765]
    Ed25519 Verification Key: [9705690aef09bbbf05255024892366952a9f71a9c671ad3f4138043dce5f6793]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
    Sigma: [0860e791a13f1a996339054810b531ae7e7fc8a67336829dbe7698f3cd7e2f1334a020f0ff366a60e83f1968df726cd3d07c0343da1f003d588add43662fab0b]
    W[0]: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
Sigma 2:
    Verification Key: [9705690aef09bbbf05255024892366952a9f71a9c671ad3f4138043dce5f6793]
    Sigma: [fe5433ccec7b16d829acafdf3a495771fea4e2a82885a8a89b71a2cfee1db724914e5f8acd4c52e9547059154c5a5ebadde374eae2fdcb546df49941a0780e0d]
    W[0]: [7fbea3be88d776943503ea05a9698e9b43d221f9d4a7f65ee62ecea21381859c]
    W[1]: [37ce2848ce72147cc9a42268034c2a781168b932fae3a92964795dd993fe30ca]
R 2: [42c2e48e9fb057643092f93e9285ef51b993cc4b9724ffef429ade875010555b]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 1
    Binary configuration: 0
    Right Seed:    [63cd4026d707c99d0e6faaf300963540275a5446c39454bec64e8a582b429233]
    Left Witness:  [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
    Right Witness: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
    Height: 0
    Ed25519 Secret Key:       [797ec460bd8298a21ab9d04c0cace497d7552eb483f772ef713e1ce90c89eab3]
    Ed25519 Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
Sigma 1:
    Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
    Sigma: [0860e791a13f1a996339054810b531ae7e7fc8a67336829dbe7698f3cd7e2f1334a020f0ff366a60e83f1968df726cd3d07c0343da1f003d588add43662fab0b]
    W[0]: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
Seed:
    9a795a3291945a4e814937a79a45e6f4473214aef80d60c7eed70d87c9aa3a52
Tau 2:
    Height: 2
    Binary configuration: 0
    Right Seed:    [14c8de0480acc4fa3aac58893675b9932455e76a4bbb0cd26e3bef1b13a80876]
    Left Witness:  [9b0df1a883f526ef04b80ea74031ac17781ec0954f7796e782c315d4617b9f8b]
    Right Witness: [37ce2848ce72147cc9a42268034c2a781168b932fae3a92964795dd993fe30ca]
    Height: 1
    Binary configuration: 0
    Right Seed:    [c510b37bc0a6b7183a527ec098acea9de5ae9f853e84ec7bbb407c89c5cd0966]
    Left Witness:  [2da6eb233a4843c7782d27924738457a22fb8ff5363b57c54d2f734f22dfc0c5]
    Right Witness: [7fbea3be88d776943503ea05a9698e9b43d221f9d4a7f65ee62ecea21381859c]
    Height: 0
    Ed25519 Secret Key:       [2322d709478474b16dfc681ee27aa51dfed98a9b2ddae7fe420586bb927d0765]
    Ed25519 Verification Key: [9705690aef09bbbf05255024892366952a9f71a9c671ad3f4138043dce5f6793]
```
- Sigma t = 2:
```
Sigma 1:
    Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
    Sigma: [0860e791a13f1a996339054810b531ae7e7fc8a67336829dbe7698f3cd7e2f1334a020f0ff366a60e83f1968df726cd3d07c0343da1f003d588add43662fab0b]
    W[0]: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
Sigma 2:
    Verification Key: [3841939979fc0bd3f99f4aa16d6784c2645e61717e26e8ef546c4c5161c94eea]
    Sigma: [20c90ce415ad35966203e763aeb52abc163117ebb6e22ceb9c2fb7cecdeec899c34fa00c9ccc56667586667dcb96f24a014456f98857cf5508a96dae2dfb4b04]
    W[0]: [855282b123c25f86405d5508dbad51480c80ab4eded37c3ae59705bcbbd36c6a]
    W[1]: [9b0df1a883f526ef04b80ea74031ac17781ec0954f7796e782c315d4617b9f8b]
R 2: [42c2e48e9fb057643092f93e9285ef51b993cc4b9724ffef429ade875010555b]
```
Product Composition Secret Key, t = 2:
```
Tau 1:
    Height: 1
    Binary configuration: 0
    Right Seed:    [63cd4026d707c99d0e6faaf300963540275a5446c39454bec64e8a582b429233]
    Left Witness:  [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
    Right Witness: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
    Height: 0
    Ed25519 Secret Key:       [797ec460bd8298a21ab9d04c0cace497d7552eb483f772ef713e1ce90c89eab3]
    Ed25519 Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
Sigma 1:
    Verification Key: [5b9fe44c021bdd9c3b34f600efdd73c795fccd0604a124ca8a3d4d24a2a20b88]
    Sigma: [0860e791a13f1a996339054810b531ae7e7fc8a67336829dbe7698f3cd7e2f1334a020f0ff366a60e83f1968df726cd3d07c0343da1f003d588add43662fab0b]
    W[0]: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
Seed:
    9a795a3291945a4e814937a79a45e6f4473214aef80d60c7eed70d87c9aa3a52
Tau 2:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9b0df1a883f526ef04b80ea74031ac17781ec0954f7796e782c315d4617b9f8b]
    Right Witness: [37ce2848ce72147cc9a42268034c2a781168b932fae3a92964795dd993fe30ca]
    Height: 1
    Binary configuration: 0
    Right Seed:    [b7a529a8f5c6c3a985415394bae8296d51340448849f412d424e1c84def19f6a]
    Left Witness:  [485081847dcf06b4c90f77e719c2cdd16630f7a62dc375c95af2895591c7030d]
    Right Witness: [855282b123c25f86405d5508dbad51480c80ab4eded37c3ae59705bcbbd36c6a]
    Height: 0
    Ed25519 Secret Key:       [d338018ea2479d98583c8afc93ef51e1fd952cfeee4309538af97cccf810da0c]
    Ed25519 Verification Key: [3841939979fc0bd3f99f4aa16d6784c2645e61717e26e8ef546c4c5161c94eea]
```
- Sigma t = 4:
```
Sigma 1:
    Verification Key: [9077780e7a816f81b2be94b9cbed9248db8ce03545819387496047c6ad251f09]
    Sigma: [cb7af65595938758f60009dbc7312c87baef3f8f88a6babc01e392538ec331ef20766992bc91b52bedd4a2f021bbd9e10f6cd8548dd9048e56b9579cf975fe06]
    W[0]: [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
Sigma 2:
    Verification Key: [bb640ed46e13cf24f5dcbb1af1fdccb71e506e239c3c2c4258cb38a13d00d248]
    Sigma: [0377b3e58df3f2b64718a0ad0d1fe146d79b0be361131c7aa965b6448dffcc8391f804f2956a762f63e9f2f4fca308d09baf4f7b70f6b27a5d358f78c7603109]
    W[0]: [4928f7904341021fc080c2bdb8b45094661ddd6ad3655dc9b44ec5f1096d606d]
    W[1]: [652c7e4997aa62a06addd75ad8a5c9d54dc9479bbb1f1045c5e5246c83318b92]
R 2: [e6cc585ccec0d6d27aadacaea854fe921c6f0ccf5009a506570e7f2b8f704bac]
```
Product Composition Secret Key, t = 4:
```
Tau 1:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
    Right Witness: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [9077780e7a816f81b2be94b9cbed9248db8ce03545819387496047c6ad251f09]
Sigma 1:
    Verification Key: [9077780e7a816f81b2be94b9cbed9248db8ce03545819387496047c6ad251f09]
    Sigma: [cb7af65595938758f60009dbc7312c87baef3f8f88a6babc01e392538ec331ef20766992bc91b52bedd4a2f021bbd9e10f6cd8548dd9048e56b9579cf975fe06]
    W[0]: [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
Seed:
    d82ab9526323833262ac56f65860f38faa433ff6129c24f033e6ea786fd6db6b
Tau 2:
    Height: 2
    Binary configuration: 0
    Right Seed:    [d1a3e0d9876b252a66497a3b505bef73d74e79095684fdbad6054ceaae219645]
    Left Witness:  [330daba116c2337d0b5414cc46a73506d709416c61554722b78b0b66e765443b]
    Right Witness: [652c7e4997aa62a06addd75ad8a5c9d54dc9479bbb1f1045c5e5246c83318b92]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f29a1d9b02ac1de50fd9e485a24978de366f0325f189c39d6c856fb805872dea]
    Left Witness:  [745ce360e80f694405c14cfc6b2d27ed18e1f4f3616da7bae5025c495931a450]
    Right Witness: [4928f7904341021fc080c2bdb8b45094661ddd6ad3655dc9b44ec5f1096d606d]
    Height: 0
    Ed25519 Secret Key:       [d8aea7132f85108e03fa2e46033b628dc4c4d894dcf48a087b660d5cf523fcd5]
    Ed25519 Verification Key: [bb640ed46e13cf24f5dcbb1af1fdccb71e506e239c3c2c4258cb38a13d00d248]
```
- Sigma t = 6:
```
Sigma 1:
    Verification Key: [9077780e7a816f81b2be94b9cbed9248db8ce03545819387496047c6ad251f09]
    Sigma: [cb7af65595938758f60009dbc7312c87baef3f8f88a6babc01e392538ec331ef20766992bc91b52bedd4a2f021bbd9e10f6cd8548dd9048e56b9579cf975fe06]
    W[0]: [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
Sigma 2:
    Verification Key: [d7cab746d246b5fc21b40b8778e377456a62d03636e10a0228856d61453c7595]
    Sigma: [78eeeff16ea30306c64bf176cbac97005a35d88855f9f2ff283b990a45545297ba355644471d63fc6b5c21b5f26262db5d6317a45643383b9adfbe3f9ce0d504]
    W[0]: [9d1f9f9d03b6ed90710c7eaf2d9156a3b34a290d7baf79e775b417336a4415d1]
    W[1]: [330daba116c2337d0b5414cc46a73506d709416c61554722b78b0b66e765443b]
R 2: [e6cc585ccec0d6d27aadacaea854fe921c6f0ccf5009a506570e7f2b8f704bac]
```
Product Composition Secret Key, t = 6:
```
Tau 1:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
    Right Witness: [377b3bd79d099313a59dbac4fcb74cd9b45bfe6e32030e90c8f4a1dfae3bc986]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [9077780e7a816f81b2be94b9cbed9248db8ce03545819387496047c6ad251f09]
Sigma 1:
    Verification Key: [9077780e7a816f81b2be94b9cbed9248db8ce03545819387496047c6ad251f09]
    Sigma: [cb7af65595938758f60009dbc7312c87baef3f8f88a6babc01e392538ec331ef20766992bc91b52bedd4a2f021bbd9e10f6cd8548dd9048e56b9579cf975fe06]
    W[0]: [9ec328f26f8a298c8dfd365d513301b316c09f423f111c4ab3cc84277bb1bafc]
Seed:
    d82ab9526323833262ac56f65860f38faa433ff6129c24f033e6ea786fd6db6b
Tau 2:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [330daba116c2337d0b5414cc46a73506d709416c61554722b78b0b66e765443b]
    Right Witness: [652c7e4997aa62a06addd75ad8a5c9d54dc9479bbb1f1045c5e5246c83318b92]
    Height: 1
    Binary configuration: 0
    Right Seed:    [c32eb1c5e9bcd3d96243e6371f52781a4f6ac6dac6976f26544c99d31f5dbecb]
    Left Witness:  [3726a93ad80a90eb8ef9abb49cfd954b7658fd5eb14d65e1b9b57d77253321dc]
    Right Witness: [9d1f9f9d03b6ed90710c7eaf2d9156a3b34a290d7baf79e775b417336a4415d1]
    Height: 0
    Ed25519 Secret Key:       [57185fdef1032136515d53e1b104acbace7d9b590465c9b11a72c8943f02c7a4]
    Ed25519 Verification Key: [d7cab746d246b5fc21b40b8778e377456a62d03636e10a0228856d61453c7595]
```
## Test Vector - 3
### Description 
 Generate and verify a specified product composition signature at `t = [1, 3, 5, 7]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
450daa6ca8aefdba78c142a659c438d1347e76e11e665237c9aae429f175789f
```
- h1 (int):

```2```

- h2 (int):

```1```

- Message (string):
```
"turn a single letter - it becomes a bird or later"
```
- Message (bytes) with `utf-8` encoding:
```
7475726e20612073696e676c65206c6574746572202d206974206265636f6d657320612062697264206f72206c61746572
```
### Outputs
- Product Composition Verification Key:
```
74d3dc1319f1369d0149ef5229a07f7b5d057a3e30424e078da26b6df834640d
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 2
    Binary configuration: 0
    Right Seed:    [3823456895bb5329952d5eef4d0a2ef603001d9aaadebefe52bab83405ae2cba]
    Left Witness:  [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
    Right Witness: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f1901ff41f257e415381d1f410955f9f4a334eab99145e57fe1853759e6bc583]
    Left Witness:  [4a127e3e2b43565538c05ad7076748e9c0cee288018334d705f064894ab9a41e]
    Right Witness: [b21f6d6dc22977a73fa86a66d1ddf05b7e6b0ea9da2ac491778d053daef39bc6]
    Height: 0
    Ed25519 Secret Key:       [70b1133de89197bed7df88fb13f8ae77cd976a4d6d5836d62a965f68caef1659]
    Ed25519 Verification Key: [f51de133e7d8f7b4790bc8c2db4fd557dc0da824447b60e47c57d8e06f7e1d41]
Sigma 1:
    Verification Key: [f51de133e7d8f7b4790bc8c2db4fd557dc0da824447b60e47c57d8e06f7e1d41]
    Sigma: [3cd33a45dd2386fe0ac4e0dd7ed22eb1c7c5019a9fb274fc955903be9d6641fd65c615eec1f5e9b4087a3f79c8a55b95b3b37c42eeda4768a544f6e29b6a7105]
    W[0]: [b21f6d6dc22977a73fa86a66d1ddf05b7e6b0ea9da2ac491778d053daef39bc6]
    W[1]: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
Seed:
    3331144bd8d5ec608d14672f98e4c9175d41966bbe5e8d3a37d56cd593a7fbe4
Tau 2:
    Height: 1
    Binary configuration: 0
    Right Seed:    [525644742be0493d4029ba696517afb1d12a20cc2eaa94827b2821c2a3bc9434]
    Left Witness:  [da115d8fd2f79f5819509db22417667f1aa4490b71e1bb2a99f6a185d380df0e]
    Right Witness: [1c5f85d2919421dee4f21901f98d5eaab56f091549670c3194cdb3c8dc207f3d]
    Height: 0
    Ed25519 Secret Key:       [6b6aab55d44c3000c372e614751e9c356b417f8a4ed70759b6e0c7ba53adc9d4]
    Ed25519 Verification Key: [bcfa0326251d83ac1cdf3b6029673d0be9608c822bf6d00245481bd5caf7b1f6]
```
- Sigma t = 1:
```
Sigma 1:
    Verification Key: [f51de133e7d8f7b4790bc8c2db4fd557dc0da824447b60e47c57d8e06f7e1d41]
    Sigma: [3cd33a45dd2386fe0ac4e0dd7ed22eb1c7c5019a9fb274fc955903be9d6641fd65c615eec1f5e9b4087a3f79c8a55b95b3b37c42eeda4768a544f6e29b6a7105]
    W[0]: [b21f6d6dc22977a73fa86a66d1ddf05b7e6b0ea9da2ac491778d053daef39bc6]
    W[1]: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
Sigma 2:
    Verification Key: [48b7b1379d58e0b6cf33c1d240d1a1ae38cf56cf7f259509e11bed0d199a15a2]
    Sigma: [94a26397daf003127a1d795bfba0a0829c448479df00d8f99f76fc2fc9fe4fec350f7741e04353048d7dd47d28abaaa904ab10b1616c924aa14dcf727a350a0b]
    W[0]: [da115d8fd2f79f5819509db22417667f1aa4490b71e1bb2a99f6a185d380df0e]
R 2: [deedcfcb2fac9e445bb03977e2423361d2b6d87d8cb2f39ace46dadfc3299cd9]
```
Product Composition Secret Key, t = 1:
```
Tau 1:
    Height: 2
    Binary configuration: 0
    Right Seed:    [3823456895bb5329952d5eef4d0a2ef603001d9aaadebefe52bab83405ae2cba]
    Left Witness:  [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
    Right Witness: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f1901ff41f257e415381d1f410955f9f4a334eab99145e57fe1853759e6bc583]
    Left Witness:  [4a127e3e2b43565538c05ad7076748e9c0cee288018334d705f064894ab9a41e]
    Right Witness: [b21f6d6dc22977a73fa86a66d1ddf05b7e6b0ea9da2ac491778d053daef39bc6]
    Height: 0
    Ed25519 Secret Key:       [70b1133de89197bed7df88fb13f8ae77cd976a4d6d5836d62a965f68caef1659]
    Ed25519 Verification Key: [f51de133e7d8f7b4790bc8c2db4fd557dc0da824447b60e47c57d8e06f7e1d41]
Sigma 1:
    Verification Key: [f51de133e7d8f7b4790bc8c2db4fd557dc0da824447b60e47c57d8e06f7e1d41]
    Sigma: [3cd33a45dd2386fe0ac4e0dd7ed22eb1c7c5019a9fb274fc955903be9d6641fd65c615eec1f5e9b4087a3f79c8a55b95b3b37c42eeda4768a544f6e29b6a7105]
    W[0]: [b21f6d6dc22977a73fa86a66d1ddf05b7e6b0ea9da2ac491778d053daef39bc6]
    W[1]: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
Seed:
    3331144bd8d5ec608d14672f98e4c9175d41966bbe5e8d3a37d56cd593a7fbe4
Tau 2:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [da115d8fd2f79f5819509db22417667f1aa4490b71e1bb2a99f6a185d380df0e]
    Right Witness: [1c5f85d2919421dee4f21901f98d5eaab56f091549670c3194cdb3c8dc207f3d]
    Height: 0
    Ed25519 Secret Key:       [525644742be0493d4029ba696517afb1d12a20cc2eaa94827b2821c2a3bc9434]
    Ed25519 Verification Key: [48b7b1379d58e0b6cf33c1d240d1a1ae38cf56cf7f259509e11bed0d199a15a2]
```
- Sigma t = 3:
```
Sigma 1:
    Verification Key: [3cc93037196a6f9cb79fec9604a69af4fde2ed9ec905148073bca84169d9146b]
    Sigma: [600295ba73124ed8a4443359adf1b45f85232d5f7d6c7ae67b5f09c44d2349dbe949dc302aee12920fbceba428b8e39a9975ee6301a6131eb011da4c2304700d]
    W[0]: [4a127e3e2b43565538c05ad7076748e9c0cee288018334d705f064894ab9a41e]
    W[1]: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
Sigma 2:
    Verification Key: [46fb38ce7bc9a3754418560ee5e850fb9af2da99795d16f250b00428b5760bb0]
    Sigma: [80dc82e18cdc0e54adfff50dda29611fb0cecd2597bdb2f936ca6f30e852c93d99388a99565667017c4fbd72d414df356e2fb363411d72f6a7448f4e07f43b04]
    W[0]: [8f2b04db04d1fcfc38391250fdd13b8621b62423084a489c1401a6f9e3ffe0f5]
R 2: [a112acbf7a72644c2e74b364409744ee34dc2c7f84eb0a99a5af9a6baa851163]
```
Product Composition Secret Key, t = 3:
```
Tau 1:
    Height: 2
    Binary configuration: 0
    Right Seed:    [3823456895bb5329952d5eef4d0a2ef603001d9aaadebefe52bab83405ae2cba]
    Left Witness:  [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
    Right Witness: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [4a127e3e2b43565538c05ad7076748e9c0cee288018334d705f064894ab9a41e]
    Right Witness: [b21f6d6dc22977a73fa86a66d1ddf05b7e6b0ea9da2ac491778d053daef39bc6]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [3cc93037196a6f9cb79fec9604a69af4fde2ed9ec905148073bca84169d9146b]
Sigma 1:
    Verification Key: [3cc93037196a6f9cb79fec9604a69af4fde2ed9ec905148073bca84169d9146b]
    Sigma: [600295ba73124ed8a4443359adf1b45f85232d5f7d6c7ae67b5f09c44d2349dbe949dc302aee12920fbceba428b8e39a9975ee6301a6131eb011da4c2304700d]
    W[0]: [4a127e3e2b43565538c05ad7076748e9c0cee288018334d705f064894ab9a41e]
    W[1]: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
Seed:
    9c8a1fa32fb5d8a75533b916e73616b29dbdfec66f5310967a284da34a0081eb
Tau 2:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [8f2b04db04d1fcfc38391250fdd13b8621b62423084a489c1401a6f9e3ffe0f5]
    Right Witness: [9ed3885747e624de70b679e42ecee1fc4e22d7a58079c9ddb06b0ec6a6779dae]
    Height: 0
    Ed25519 Secret Key:       [a87213e2beb14e28d55c1542d376e1558779478bbec61347db1c13819d40bbc3]
    Ed25519 Verification Key: [46fb38ce7bc9a3754418560ee5e850fb9af2da99795d16f250b00428b5760bb0]
```
- Sigma t = 5:
```
Sigma 1:
    Verification Key: [459d6fba233ad916b9d74bc07b4820d5055423079e28eeb798c305e6295e82c3]
    Sigma: [fb5180c093045ea779393752018487a59e4bc9a0b6dee0f74c980ef2aace789f14d5bd82f03c160c9a9195bf1854ff7b5ac4abed8cf7b602853aafac801d9f06]
    W[0]: [bc820f64dc8dce378cd10bea0c8a1f806c86b99d8684842fb331e90b5c4d8fb0]
    W[1]: [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
Sigma 2:
    Verification Key: [198e0e28ab19b8aeab5eb4b11bc5e27457842164b4074945387fb025c8343ec4]
    Sigma: [26602caca9b69271c4cfd25b3c5aa45fb8430ac6ebc0bc8f59620d2637cfa3e368fc27943d2a4b7c3f9284c425673b78c506667bd2646db6da7af1066a344202]
    W[0]: [b6d54f7126ac52aa5737a713a5ef796b381a802a8a7fdca80ae20024b73dc676]
R 2: [86799e1b092036bed0ddb206b192ece76ce2f43447e52bb1932dcefcd41abb55]
```
Product Composition Secret Key, t = 5:
```
Tau 1:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
    Right Witness: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
    Height: 1
    Binary configuration: 0
    Right Seed:    [0d6daa1ad3c595d6ba9c0328fa021067ccbe18d8c495127a6b6ad7ccae9f225a]
    Left Witness:  [7158920099352e213b5c9d696e74393f72f1a71126aa831d04c6da61c51647c3]
    Right Witness: [bc820f64dc8dce378cd10bea0c8a1f806c86b99d8684842fb331e90b5c4d8fb0]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [459d6fba233ad916b9d74bc07b4820d5055423079e28eeb798c305e6295e82c3]
Sigma 1:
    Verification Key: [459d6fba233ad916b9d74bc07b4820d5055423079e28eeb798c305e6295e82c3]
    Sigma: [fb5180c093045ea779393752018487a59e4bc9a0b6dee0f74c980ef2aace789f14d5bd82f03c160c9a9195bf1854ff7b5ac4abed8cf7b602853aafac801d9f06]
    W[0]: [bc820f64dc8dce378cd10bea0c8a1f806c86b99d8684842fb331e90b5c4d8fb0]
    W[1]: [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
Seed:
    f5a41d2b81fe840c2b51dd078ab84d9ce313a0f60c1600a9502000915a76a97a
Tau 2:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b6d54f7126ac52aa5737a713a5ef796b381a802a8a7fdca80ae20024b73dc676]
    Right Witness: [56ec4465f5a1d1c8a48b94deee7ed3866d8e805172b9df44cd91380fb963d456]
    Height: 0
    Ed25519 Secret Key:       [d5ea955a0596e16eb35f016f65a5b9ad4d9a53290c1d44ac587178174ee50a68]
    Ed25519 Verification Key: [198e0e28ab19b8aeab5eb4b11bc5e27457842164b4074945387fb025c8343ec4]
```
- Sigma t = 7:
```
Sigma 1:
    Verification Key: [7b082ecba5a1a18654d8c74e2c0748f521481376f500f47906f80e7c845e1503]
    Sigma: [fe9ebb1a0392e67c7b26561f9bb5c37e9aaf3a9083ab8634fb1359fb889b394a2b13d635036748fe37fee88b75804bc04d2e60bfdaf95e8a86f6f4af17166a06]
    W[0]: [7158920099352e213b5c9d696e74393f72f1a71126aa831d04c6da61c51647c3]
    W[1]: [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
Sigma 2:
    Verification Key: [bf6aff9ba35ff856d7852b66bed6fa7f08641a073f1a01d684443ad93b01abb1]
    Sigma: [e7f42394a7805b37def9e22deafd3d8e46f7b1e3411a384db68a7f9b47e97deca0a897a276cd4c52efd3133576e5ca2616d1b95e42a6eb016a173c9f3cc24b0e]
    W[0]: [15a5d481a00773d8976efb933abcadd186acac1365c71f07a72b4021a2845b23]
R 2: [41197c9607ef13853df64ac31c8378eb503af995eb829d457a87d32b11fd85b6]
```
Product Composition Secret Key, t = 7:
```
Tau 1:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
    Right Witness: [91b5dbb3ae9c2d4aad0434490af4003a371ab53e5d6635f9575c0bbd77658de6]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7158920099352e213b5c9d696e74393f72f1a71126aa831d04c6da61c51647c3]
    Right Witness: [bc820f64dc8dce378cd10bea0c8a1f806c86b99d8684842fb331e90b5c4d8fb0]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [7b082ecba5a1a18654d8c74e2c0748f521481376f500f47906f80e7c845e1503]
Sigma 1:
    Verification Key: [7b082ecba5a1a18654d8c74e2c0748f521481376f500f47906f80e7c845e1503]
    Sigma: [fe9ebb1a0392e67c7b26561f9bb5c37e9aaf3a9083ab8634fb1359fb889b394a2b13d635036748fe37fee88b75804bc04d2e60bfdaf95e8a86f6f4af17166a06]
    W[0]: [7158920099352e213b5c9d696e74393f72f1a71126aa831d04c6da61c51647c3]
    W[1]: [137bb3f95c0139dd95a7126615c9893651cc6d47c479de3c14380671f26dc939]
Seed:
    521dafafe440ffda858e98ed2ab31ece987229a2afd72ec94763ca8cd582d34a
Tau 2:
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [15a5d481a00773d8976efb933abcadd186acac1365c71f07a72b4021a2845b23]
    Right Witness: [61b335de292b16587432cefe765e24099206dc0dd51130d29a2d68a9746a18a4]
    Height: 0
    Ed25519 Secret Key:       [97fd4701cc25ba80112dedb4c192469564f304ed7fb9e906f7a16e20e99b3f49]
    Ed25519 Verification Key: [bf6aff9ba35ff856d7852b66bed6fa7f08641a073f1a01d684443ad93b01abb1]
```
## Test Vector - 4
### Description 
 Generate and verify a specified product composition signature at `t = [0, 5, 10, 15]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
cbf5a7f7f8b807b5bc588b3c54e46fb20b680325890aa85c44ee360f99a0c483
```
- h1 (int):

```2```

- h2 (int):

```2```

- Message (string):
```
"a string pulled out of a word endlessly, never snaps"
```
- Message (bytes) with `utf-8` encoding:
```
6120737472696e672070756c6c6564206f7574206f66206120776f726420656e646c6573736c792c206e6576657220736e617073
```
### Outputs
- Product Composition Verification Key:
```
e3050f622e37604a05532f3a9840de1da0bb6dfddc667b62de6dbe4baaea53e3
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 2
    Binary configuration: 0
    Right Seed:    [5ebbb8aa79a064fc5c1f6e02d336fa61644bc5c4b80bf3290462ceb6045a75a1]
    Left Witness:  [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
    Right Witness: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
    Height: 1
    Binary configuration: 0
    Right Seed:    [c2a3cd8d64f647847bd19fe843b9813aa95217695f413c9ca88173cde3e3303d]
    Left Witness:  [f87bd7029be7dd9af465daec161b77971c9f46ee3e2e6e4b0019b2c2d2e13e8b]
    Right Witness: [8d4a0ce8ec0578634b19960288372f3580beeaeea051ee1f8dc6ae0ef2398e54]
    Height: 0
    Ed25519 Secret Key:       [ff23476e904fb7ebcc7b58818ff8e605960b23c2666810295b80d6b86aa3426c]
    Ed25519 Verification Key: [2c56933618a2a11c026a937dce7bb2bab93cc98ee77a5a95dc33c20881975fb2]
Sigma 1:
    Verification Key: [2c56933618a2a11c026a937dce7bb2bab93cc98ee77a5a95dc33c20881975fb2]
    Sigma: [631c9ca2b3ca9154bc6abf80f612de4a45f16ec415b1d5f68d94a546805c25ff000d83f6d10ca2073bfd298a64fd815f1e64ac035a2e56d2e4763097fd7add0b]
    W[0]: [8d4a0ce8ec0578634b19960288372f3580beeaeea051ee1f8dc6ae0ef2398e54]
    W[1]: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
Seed:
    f4f9e851b66a93e951a640c28b27aa14e406b305840b0eaef70801205635b314
Tau 2:
    Height: 2
    Binary configuration: 0
    Right Seed:    [92355e0a3eabc25050e4cad8fa745d5d08ac89006a1078992d2ae23ce4a8ddd5]
    Left Witness:  [479348b6d38a1cb205013387e8de418e52690b96234c502bcda040e6390d76ea]
    Right Witness: [7b75db1b012c029398e58cbd7e4a543dc1058772948d4124f548fe688133fc0f]
    Height: 1
    Binary configuration: 0
    Right Seed:    [9524c0af531349fb4bd608552d0ece6b054121ce454d77d4ebc9e6d784339edc]
    Left Witness:  [14ba4b26ed9cfd594aa5606f007b9c5f9a217dfee10ff26e70a385a63c4a5a2c]
    Right Witness: [d5d87e3caf3dee6e6c612d7ce015055ec108bba193f022a55627ebdc4f96706f]
    Height: 0
    Ed25519 Secret Key:       [3dafe4321f0ac5032ef3ef00bd25105cb22b62fbb060807c298cfd7a2769e3c1]
    Ed25519 Verification Key: [cf2ac69d0a67cf619da27e2192f0916f2f92e7164d302b5b358a01273ade173b]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [2c56933618a2a11c026a937dce7bb2bab93cc98ee77a5a95dc33c20881975fb2]
    Sigma: [631c9ca2b3ca9154bc6abf80f612de4a45f16ec415b1d5f68d94a546805c25ff000d83f6d10ca2073bfd298a64fd815f1e64ac035a2e56d2e4763097fd7add0b]
    W[0]: [8d4a0ce8ec0578634b19960288372f3580beeaeea051ee1f8dc6ae0ef2398e54]
    W[1]: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
Sigma 2:
    Verification Key: [cf2ac69d0a67cf619da27e2192f0916f2f92e7164d302b5b358a01273ade173b]
    Sigma: [9ce5122961c4e8b58db4227ed181d4c4dbaf112a34696772115738c655ba7d95b7d381a24f35e75c5746d53de93b795ffc00f317280df8359b6f9285231b8201]
    W[0]: [d5d87e3caf3dee6e6c612d7ce015055ec108bba193f022a55627ebdc4f96706f]
    W[1]: [7b75db1b012c029398e58cbd7e4a543dc1058772948d4124f548fe688133fc0f]
R 2: [0981adaabf382160a8c77c430a4d5a746f8287671604d860ebcc73fecc94343b]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 2
    Binary configuration: 0
    Right Seed:    [5ebbb8aa79a064fc5c1f6e02d336fa61644bc5c4b80bf3290462ceb6045a75a1]
    Left Witness:  [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
    Right Witness: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
    Height: 1
    Binary configuration: 0
    Right Seed:    [c2a3cd8d64f647847bd19fe843b9813aa95217695f413c9ca88173cde3e3303d]
    Left Witness:  [f87bd7029be7dd9af465daec161b77971c9f46ee3e2e6e4b0019b2c2d2e13e8b]
    Right Witness: [8d4a0ce8ec0578634b19960288372f3580beeaeea051ee1f8dc6ae0ef2398e54]
    Height: 0
    Ed25519 Secret Key:       [ff23476e904fb7ebcc7b58818ff8e605960b23c2666810295b80d6b86aa3426c]
    Ed25519 Verification Key: [2c56933618a2a11c026a937dce7bb2bab93cc98ee77a5a95dc33c20881975fb2]
Sigma 1:
    Verification Key: [2c56933618a2a11c026a937dce7bb2bab93cc98ee77a5a95dc33c20881975fb2]
    Sigma: [631c9ca2b3ca9154bc6abf80f612de4a45f16ec415b1d5f68d94a546805c25ff000d83f6d10ca2073bfd298a64fd815f1e64ac035a2e56d2e4763097fd7add0b]
    W[0]: [8d4a0ce8ec0578634b19960288372f3580beeaeea051ee1f8dc6ae0ef2398e54]
    W[1]: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
Seed:
    f4f9e851b66a93e951a640c28b27aa14e406b305840b0eaef70801205635b314
Tau 2:
    Height: 2
    Binary configuration: 0
    Right Seed:    [92355e0a3eabc25050e4cad8fa745d5d08ac89006a1078992d2ae23ce4a8ddd5]
    Left Witness:  [479348b6d38a1cb205013387e8de418e52690b96234c502bcda040e6390d76ea]
    Right Witness: [7b75db1b012c029398e58cbd7e4a543dc1058772948d4124f548fe688133fc0f]
    Height: 1
    Binary configuration: 0
    Right Seed:    [9524c0af531349fb4bd608552d0ece6b054121ce454d77d4ebc9e6d784339edc]
    Left Witness:  [14ba4b26ed9cfd594aa5606f007b9c5f9a217dfee10ff26e70a385a63c4a5a2c]
    Right Witness: [d5d87e3caf3dee6e6c612d7ce015055ec108bba193f022a55627ebdc4f96706f]
    Height: 0
    Ed25519 Secret Key:       [3dafe4321f0ac5032ef3ef00bd25105cb22b62fbb060807c298cfd7a2769e3c1]
    Ed25519 Verification Key: [cf2ac69d0a67cf619da27e2192f0916f2f92e7164d302b5b358a01273ade173b]
```
- Sigma t = 5:
```
Sigma 1:
    Verification Key: [282c4e4f4f44d18f50982bc725be80337cb9d4e2b44d690d55bfed5dd7ee5765]
    Sigma: [33bca76006fe8f19da4278bd83a92ad29b829d159f7c6feece3069567b3b372808166389e540fdb2a3f0d4b476d80c4cec82e2571cdbb4536465eab24571e30e]
    W[0]: [f87bd7029be7dd9af465daec161b77971c9f46ee3e2e6e4b0019b2c2d2e13e8b]
    W[1]: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
Sigma 2:
    Verification Key: [d84d2c341e6b5b55bb21091c6d53c3367376200068bad5c38f0f4ba41212ba97]
    Sigma: [68697afe1fa07ab861e62019ad6046cdb46fb653817d0442b0b350e4b639f12d6c27e228c5d7900381ff4dd021a4b23c89cd75d1dacbf44b0ae9cacc6c04170c]
    W[0]: [a5e2626038449d723d49be411665be26bbf44b58f0acd7a9fd15f1252d674ad7]
    W[1]: [f7817101879a8940593bb5b0265942f2cc71996468780a30f99b270a53bcc1c2]
R 2: [f00c94ab9f40057e308b42de02ede3ab27499371c432c5535cc6667cc091cf02]
```
Product Composition Secret Key, t = 5:
```
Tau 1:
    Height: 2
    Binary configuration: 0
    Right Seed:    [5ebbb8aa79a064fc5c1f6e02d336fa61644bc5c4b80bf3290462ceb6045a75a1]
    Left Witness:  [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
    Right Witness: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f87bd7029be7dd9af465daec161b77971c9f46ee3e2e6e4b0019b2c2d2e13e8b]
    Right Witness: [8d4a0ce8ec0578634b19960288372f3580beeaeea051ee1f8dc6ae0ef2398e54]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [282c4e4f4f44d18f50982bc725be80337cb9d4e2b44d690d55bfed5dd7ee5765]
Sigma 1:
    Verification Key: [282c4e4f4f44d18f50982bc725be80337cb9d4e2b44d690d55bfed5dd7ee5765]
    Sigma: [33bca76006fe8f19da4278bd83a92ad29b829d159f7c6feece3069567b3b372808166389e540fdb2a3f0d4b476d80c4cec82e2571cdbb4536465eab24571e30e]
    W[0]: [f87bd7029be7dd9af465daec161b77971c9f46ee3e2e6e4b0019b2c2d2e13e8b]
    W[1]: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
Seed:
    2427d24f9cf13c36ea3109f34e9b3aa4cec652a112fcbb613c61d695a42a9b49
Tau 2:
    Height: 2
    Binary configuration: 0
    Right Seed:    [13d6529931023c7f4cc412138d662a13050542b11688659a2cbb5b3dfb504e0c]
    Left Witness:  [49339f733231744879beafb6d7226ba848e1f47f378a1eeb046f4247042885bb]
    Right Witness: [f7817101879a8940593bb5b0265942f2cc71996468780a30f99b270a53bcc1c2]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a5e2626038449d723d49be411665be26bbf44b58f0acd7a9fd15f1252d674ad7]
    Right Witness: [1f2e86c794baa14cfcb5256ea6609127da242a946d2fe3cffe02a0625b913cff]
    Height: 0
    Ed25519 Secret Key:       [66d99fe56f516ad02d1f279a240c2972a0a79289614284eac438e84b1daeae99]
    Ed25519 Verification Key: [d84d2c341e6b5b55bb21091c6d53c3367376200068bad5c38f0f4ba41212ba97]
```
- Sigma t = 10:
```
Sigma 1:
    Verification Key: [757c98f27cb7feb38b1b28d6e445a072ddc0a5e803cb3776779d0ea0b2962093]
    Sigma: [1f230333d39f0370c25fcdd2fb23942b09d2668f9d4077fde8ceee007b2a2d640ec8846e63c26c5d59f5513ad5b3ebb7992d098e539a6710fadda7a3c4585a0d]
    W[0]: [0839201549e759c358618c6e5ec91612211b7d066b90a6d8fc82b315dbc42bcd]
    W[1]: [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
Sigma 2:
    Verification Key: [d1957ba36686a69f47e176a352128cc6281c9bfe4712a935df11994e4d9eec1d]
    Sigma: [e1ac53ccb5a1dde07c17240f150f753ce19141d1ba805dc1ca886fa7c421a4871b25ec71f516f603eb85d5c8335fae4e1e3b243589616da06b8635d8ef79620b]
    W[0]: [bfc3bc84429f922563e73fd72e20797e15806c749a17a4bbf3648c9d4ef000a7]
    W[1]: [476821ed21d5f1ed7371e99a203700b308bd0a8fd2a2742e8f38ad62489c5dcb]
R 2: [f78f562cc3687e10358f67b713aa5e025d96e29cab4e53a521364b50938b146c]
```
Product Composition Secret Key, t = 10:
```
Tau 1:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
    Right Witness: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
    Height: 1
    Binary configuration: 0
    Right Seed:    [d29ac741c2381317fd7672a82bf2450be120e4852d186aa02aae8849d67c07bc]
    Left Witness:  [2fea432763055da30976aefc5a71ce7cb629e0b2decda4add244852e2c7c0009]
    Right Witness: [0839201549e759c358618c6e5ec91612211b7d066b90a6d8fc82b315dbc42bcd]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [757c98f27cb7feb38b1b28d6e445a072ddc0a5e803cb3776779d0ea0b2962093]
Sigma 1:
    Verification Key: [757c98f27cb7feb38b1b28d6e445a072ddc0a5e803cb3776779d0ea0b2962093]
    Sigma: [1f230333d39f0370c25fcdd2fb23942b09d2668f9d4077fde8ceee007b2a2d640ec8846e63c26c5d59f5513ad5b3ebb7992d098e539a6710fadda7a3c4585a0d]
    W[0]: [0839201549e759c358618c6e5ec91612211b7d066b90a6d8fc82b315dbc42bcd]
    W[1]: [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
Seed:
    bba60291bbb99a85e0e0f29fc4c69c091c35d2507a04e541b5f20d900aa8f9eb
Tau 2:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [476821ed21d5f1ed7371e99a203700b308bd0a8fd2a2742e8f38ad62489c5dcb]
    Right Witness: [cf7979092d7281c659e223267e664e523b9d21983c77f04bb17657afb8b9d4ac]
    Height: 1
    Binary configuration: 0
    Right Seed:    [2c49025fa586bf7b3ac25a100ff564dbf68c6aa060614b08745143255a928c0d]
    Left Witness:  [98343afc7024587b8cfe8a7c9dd1e2a97de27538fc83983d520e891a57a5af29]
    Right Witness: [bfc3bc84429f922563e73fd72e20797e15806c749a17a4bbf3648c9d4ef000a7]
    Height: 0
    Ed25519 Secret Key:       [9dd5284422cccba6750527813181ba4da6c698c683db5cd98e04dcfa2a3bb182]
    Ed25519 Verification Key: [d1957ba36686a69f47e176a352128cc6281c9bfe4712a935df11994e4d9eec1d]
```
- Sigma t = 15:
```
Sigma 1:
    Verification Key: [df15213e0dc7fc0d4119922acc2f3f8cf5772615534bb30944e330a00f43778b]
    Sigma: [524c8eaa6add002e6e13d138d0fc8e8ebb9e85c7ac502bb43502632761e5521eff78b7360b42e21ccd25e46ea6ca59fda4ed521e9b2f851ea1450c8acdae270b]
    W[0]: [2fea432763055da30976aefc5a71ce7cb629e0b2decda4add244852e2c7c0009]
    W[1]: [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
Sigma 2:
    Verification Key: [a2b49b0bc62ab98c64e965bca61c02c91923d651bb65ce92a814523445889888]
    Sigma: [09e6365035e00a650e66893da09a6e32778ef4129f8541c7bffc1448ab91cfd204f65c8078ef7aea769b3ef1dae6979d3988f904df7b1c2822b76739cf76f00f]
    W[0]: [5899b296c3fd5a15f9e00d54bf8bbd12329d4db38d587d0ac5e3038e298fbabe]
    W[1]: [097a120b5535bb352bf964fd20b741116d70f5eb34c0a2bb8883888ab701516b]
R 2: [6437dc07114792cd1009b46fd7b100032c7991c456875c133533069308ea2894]
```
Product Composition Secret Key, t = 15:
```
Tau 1:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
    Right Witness: [3e1267045aeb5ed4f3e2ff5d9d846ab36293a72907aec90e7ca05f2d7325d159]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [2fea432763055da30976aefc5a71ce7cb629e0b2decda4add244852e2c7c0009]
    Right Witness: [0839201549e759c358618c6e5ec91612211b7d066b90a6d8fc82b315dbc42bcd]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [df15213e0dc7fc0d4119922acc2f3f8cf5772615534bb30944e330a00f43778b]
Sigma 1:
    Verification Key: [df15213e0dc7fc0d4119922acc2f3f8cf5772615534bb30944e330a00f43778b]
    Sigma: [524c8eaa6add002e6e13d138d0fc8e8ebb9e85c7ac502bb43502632761e5521eff78b7360b42e21ccd25e46ea6ca59fda4ed521e9b2f851ea1450c8acdae270b]
    W[0]: [2fea432763055da30976aefc5a71ce7cb629e0b2decda4add244852e2c7c0009]
    W[1]: [5bd9f2be21473982e1a8bf7af92948532de9ffecee7a615ac9d404388d8b59b9]
Seed:
    d193c3f885297dc8a1e3901a252080b8e8a4289d50cc85fcf5eb44ea12403f72
Tau 2:
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [097a120b5535bb352bf964fd20b741116d70f5eb34c0a2bb8883888ab701516b]
    Right Witness: [6937c447f422a2c5587d2cb9a5d1481a9c6f48da9a3d38f67dfbd469db8600eb]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5899b296c3fd5a15f9e00d54bf8bbd12329d4db38d587d0ac5e3038e298fbabe]
    Right Witness: [b0ec778da951624a7d8a4e4c09487a78fa3354461ff3573383448216fc94f4fa]
    Height: 0
    Ed25519 Secret Key:       [9cef0b538e2e68c09599d887d9b444bf0dfcf28f0888c080572973c352df08a7]
    Ed25519 Verification Key: [a2b49b0bc62ab98c64e965bca61c02c91923d651bb65ce92a814523445889888]
```
## Test Vector - 5
### Description 
 Generate and verify a specified product composition signature at `t = [0, 21, 42, 63]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
50c3e574fa16956b384f9c46ecf976a0eb42fd82b9e8be381d5a24b3697d9e6d
```
- h1 (int):

```3```

- h2 (int):

```3```

- Message (string):
```
"disabled and detained, probably dispelled"
```
- Message (bytes) with `utf-8` encoding:
```
64697361626c656420616e642064657461696e65642c2070726f6261626c792064697370656c6c6564
```
### Outputs
- Product Composition Verification Key:
```
e290c6600ce59025b705362b725c522d52c749167516213a73272e6861ef5dce
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 3
    Binary configuration: 0
    Right Seed:    [7960b148986958219f1ae3bf3a17fd95521369ab98e56224a184fe4831680b7d]
    Left Witness:  [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
    Right Witness: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
    Height: 2
    Binary configuration: 0
    Right Seed:    [8cdac8da0e2faacbf3a76ce318e9dd9b7497bd2d292e975f9f85c52c6a12ac64]
    Left Witness:  [4abc0c96474b57f6d82c74a11a88112d20160392b837172bed957c9c4052d0a1]
    Right Witness: [cfeb55b068dc7842e4a9b5bfbab5a2f12ba803b1f26f6e58d45fda790b91c910]
    Height: 1
    Binary configuration: 0
    Right Seed:    [72ea02d87939c566e742649da9c988ed73a08082d947ff431000f18721b7d5a2]
    Left Witness:  [2f31b4183a76fcd0302a2299dc4f13604afc0bf0bc65df548ce80eb193fb1d3e]
    Right Witness: [7557bdc2b80dacdfc6f50ff7153c0121f6bc0928fa03a25016d6f29f075bb41e]
    Height: 0
    Ed25519 Secret Key:       [2929738b61c6e619ab071e3cea139d160831d3cc8e7d578039e27f62135a65f5]
    Ed25519 Verification Key: [11b542df6036003b84c4f6af7bcc6bf4890a92fb503e4c44344703a3d9a56616]
Sigma 1:
    Verification Key: [11b542df6036003b84c4f6af7bcc6bf4890a92fb503e4c44344703a3d9a56616]
    Sigma: [1f72de09d38cffb4aee83fa4b6ff3e0b2b11bd0072fa83ebeac8dbcad5a6132a3017fbeba19bf9e83a6882ef4af80d564da9ff412d4686051b17351ec4c8a200]
    W[0]: [7557bdc2b80dacdfc6f50ff7153c0121f6bc0928fa03a25016d6f29f075bb41e]
    W[1]: [cfeb55b068dc7842e4a9b5bfbab5a2f12ba803b1f26f6e58d45fda790b91c910]
    W[2]: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
Seed:
    2e04d95c9a444e3a231ff56571f12364efa6addb0cddac27d72e4ff5581dd376
Tau 2:
    Height: 3
    Binary configuration: 0
    Right Seed:    [8aaaf14867ba39efd1719271e222be616fadd14d1a1ba9e5a7fd0ddd75068da5]
    Left Witness:  [18a9064df1c26d30adf0f108bbbae725eb496ce1fbd2e7049d03814e80c25229]
    Right Witness: [a6aab8f3954f8adafc89df1e9ed6f0b160dda3d73a6a34cae4566eb3161d7d95]
    Height: 2
    Binary configuration: 0
    Right Seed:    [c40ae8be793c28e3905becc964e91c1de39ecaf09546d06ae86a38bab8dcc11e]
    Left Witness:  [076e438de42b6942df8eedea274fd3cd2220e7bb0b03ddae009bdbd0c87cba84]
    Right Witness: [07ded1379fcda41b5214a607487616e22c863fd86ba17b85943a608046f43761]
    Height: 1
    Binary configuration: 0
    Right Seed:    [a0209e383cc1719430270aa394ad0fe391401fbdc18e8d1e1396509004040085]
    Left Witness:  [7e4ff87b63f753c0b0afd4f34b36624942a7738cfb83773be52d5e896db20df3]
    Right Witness: [51435e6993cdf9fcddc7da914e7cea2076e64f09037e5609f2a4711b814861fe]
    Height: 0
    Ed25519 Secret Key:       [17023af318c06725d3e7d615a711db900e4089cf3ad9bcd44a9f9657d02e7a91]
    Ed25519 Verification Key: [643119fe671768ecac4a7fa999a7b6719d02eea1de127f9564c68566702a96be]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [11b542df6036003b84c4f6af7bcc6bf4890a92fb503e4c44344703a3d9a56616]
    Sigma: [1f72de09d38cffb4aee83fa4b6ff3e0b2b11bd0072fa83ebeac8dbcad5a6132a3017fbeba19bf9e83a6882ef4af80d564da9ff412d4686051b17351ec4c8a200]
    W[0]: [7557bdc2b80dacdfc6f50ff7153c0121f6bc0928fa03a25016d6f29f075bb41e]
    W[1]: [cfeb55b068dc7842e4a9b5bfbab5a2f12ba803b1f26f6e58d45fda790b91c910]
    W[2]: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
Sigma 2:
    Verification Key: [643119fe671768ecac4a7fa999a7b6719d02eea1de127f9564c68566702a96be]
    Sigma: [63ff2586a56c909309a5c71d4bb4a738920381a516411bda045b02f78b04f670189df367d781ed491d195571a63e1a4baadf34a879a02a1c3fb00dcaf7603e0c]
    W[0]: [51435e6993cdf9fcddc7da914e7cea2076e64f09037e5609f2a4711b814861fe]
    W[1]: [07ded1379fcda41b5214a607487616e22c863fd86ba17b85943a608046f43761]
    W[2]: [a6aab8f3954f8adafc89df1e9ed6f0b160dda3d73a6a34cae4566eb3161d7d95]
R 2: [1766bf6233df5efb27cb9a626477668a93479ebd84fd55fb7041a7a29c93d6c2]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 3
    Binary configuration: 0
    Right Seed:    [7960b148986958219f1ae3bf3a17fd95521369ab98e56224a184fe4831680b7d]
    Left Witness:  [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
    Right Witness: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
    Height: 2
    Binary configuration: 0
    Right Seed:    [8cdac8da0e2faacbf3a76ce318e9dd9b7497bd2d292e975f9f85c52c6a12ac64]
    Left Witness:  [4abc0c96474b57f6d82c74a11a88112d20160392b837172bed957c9c4052d0a1]
    Right Witness: [cfeb55b068dc7842e4a9b5bfbab5a2f12ba803b1f26f6e58d45fda790b91c910]
    Height: 1
    Binary configuration: 0
    Right Seed:    [72ea02d87939c566e742649da9c988ed73a08082d947ff431000f18721b7d5a2]
    Left Witness:  [2f31b4183a76fcd0302a2299dc4f13604afc0bf0bc65df548ce80eb193fb1d3e]
    Right Witness: [7557bdc2b80dacdfc6f50ff7153c0121f6bc0928fa03a25016d6f29f075bb41e]
    Height: 0
    Ed25519 Secret Key:       [2929738b61c6e619ab071e3cea139d160831d3cc8e7d578039e27f62135a65f5]
    Ed25519 Verification Key: [11b542df6036003b84c4f6af7bcc6bf4890a92fb503e4c44344703a3d9a56616]
Sigma 1:
    Verification Key: [11b542df6036003b84c4f6af7bcc6bf4890a92fb503e4c44344703a3d9a56616]
    Sigma: [1f72de09d38cffb4aee83fa4b6ff3e0b2b11bd0072fa83ebeac8dbcad5a6132a3017fbeba19bf9e83a6882ef4af80d564da9ff412d4686051b17351ec4c8a200]
    W[0]: [7557bdc2b80dacdfc6f50ff7153c0121f6bc0928fa03a25016d6f29f075bb41e]
    W[1]: [cfeb55b068dc7842e4a9b5bfbab5a2f12ba803b1f26f6e58d45fda790b91c910]
    W[2]: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
Seed:
    2e04d95c9a444e3a231ff56571f12364efa6addb0cddac27d72e4ff5581dd376
Tau 2:
    Height: 3
    Binary configuration: 0
    Right Seed:    [8aaaf14867ba39efd1719271e222be616fadd14d1a1ba9e5a7fd0ddd75068da5]
    Left Witness:  [18a9064df1c26d30adf0f108bbbae725eb496ce1fbd2e7049d03814e80c25229]
    Right Witness: [a6aab8f3954f8adafc89df1e9ed6f0b160dda3d73a6a34cae4566eb3161d7d95]
    Height: 2
    Binary configuration: 0
    Right Seed:    [c40ae8be793c28e3905becc964e91c1de39ecaf09546d06ae86a38bab8dcc11e]
    Left Witness:  [076e438de42b6942df8eedea274fd3cd2220e7bb0b03ddae009bdbd0c87cba84]
    Right Witness: [07ded1379fcda41b5214a607487616e22c863fd86ba17b85943a608046f43761]
    Height: 1
    Binary configuration: 0
    Right Seed:    [a0209e383cc1719430270aa394ad0fe391401fbdc18e8d1e1396509004040085]
    Left Witness:  [7e4ff87b63f753c0b0afd4f34b36624942a7738cfb83773be52d5e896db20df3]
    Right Witness: [51435e6993cdf9fcddc7da914e7cea2076e64f09037e5609f2a4711b814861fe]
    Height: 0
    Ed25519 Secret Key:       [17023af318c06725d3e7d615a711db900e4089cf3ad9bcd44a9f9657d02e7a91]
    Ed25519 Verification Key: [643119fe671768ecac4a7fa999a7b6719d02eea1de127f9564c68566702a96be]
```
- Sigma t = 21:
```
Sigma 1:
    Verification Key: [a006b5e71a16e51781c4185ceb738914b21bcb38544ecbe63407ba5bc888541c]
    Sigma: [1f76f27fbc6953151309e7b09d4d4c691ff7a8d4e1cfac164588942573107086f37739b3db1f06d4c629d1d6154e0d5cf352abb27be3a98b66c810cbda744c07]
    W[0]: [c7521a93e407b29a24ec8df7c3cbc07352ed3f1e2f684933c0ba6b5322162eff]
    W[1]: [4abc0c96474b57f6d82c74a11a88112d20160392b837172bed957c9c4052d0a1]
    W[2]: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
Sigma 2:
    Verification Key: [66faac397e9563745f2623a1825c90366cc7971d0b1a0c87f3722685caae6a2d]
    Sigma: [ae143f5c4b255b1448ec72263d9e6a4b5fea972501adafb2351daddad84dd32a299fb5519e290b57ea15ae9c62fc6494de8cd2f2bfff0989baffb4866566a10b]
    W[0]: [fc6dd766522c4be77222ce112588f731e17ea37b61f3b5b908dab761c6676bd9]
    W[1]: [3146459cc09e66e9a32e251e620c8f264581134bbcd8a81d3aa94e2017d02158]
    W[2]: [1245106090fa427604bbecaab61d9c157c8a1462955ff9986058845cc99c7311]
R 2: [9cc2d6121dc44f6afb2d1d4d2163af8c8262d6c93770f33e947facada5906fa9]
```
Product Composition Secret Key, t = 21:
```
Tau 1:
    Height: 3
    Binary configuration: 0
    Right Seed:    [7960b148986958219f1ae3bf3a17fd95521369ab98e56224a184fe4831680b7d]
    Left Witness:  [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
    Right Witness: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [4abc0c96474b57f6d82c74a11a88112d20160392b837172bed957c9c4052d0a1]
    Right Witness: [cfeb55b068dc7842e4a9b5bfbab5a2f12ba803b1f26f6e58d45fda790b91c910]
    Height: 1
    Binary configuration: 0
    Right Seed:    [9e04b4252ac067763dd938286c940df12c1e2d7cc560944f61ead52d7343cf6c]
    Left Witness:  [90872ea1174466d1b004ce8ccd81c026193833259c87ce2be7a98f74c9650f5d]
    Right Witness: [c7521a93e407b29a24ec8df7c3cbc07352ed3f1e2f684933c0ba6b5322162eff]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [a006b5e71a16e51781c4185ceb738914b21bcb38544ecbe63407ba5bc888541c]
Sigma 1:
    Verification Key: [a006b5e71a16e51781c4185ceb738914b21bcb38544ecbe63407ba5bc888541c]
    Sigma: [1f76f27fbc6953151309e7b09d4d4c691ff7a8d4e1cfac164588942573107086f37739b3db1f06d4c629d1d6154e0d5cf352abb27be3a98b66c810cbda744c07]
    W[0]: [c7521a93e407b29a24ec8df7c3cbc07352ed3f1e2f684933c0ba6b5322162eff]
    W[1]: [4abc0c96474b57f6d82c74a11a88112d20160392b837172bed957c9c4052d0a1]
    W[2]: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
Seed:
    a88c73cf016e0094e4214daad4fd1364c6ee8a9f49403d6286140a843dfd5694
Tau 2:
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [1245106090fa427604bbecaab61d9c157c8a1462955ff9986058845cc99c7311]
    Right Witness: [892213785f37f9e1c8366c8c5d0b834734376ec267e9cfe21ff3cd643cf444d3]
    Height: 2
    Binary configuration: 0
    Right Seed:    [25c4b9ae8b51c081467e8bad9097e416a9736c7d2c85698aba0f5e4b0261d3aa]
    Left Witness:  [29a3c5e3a8188f5be57acb09a6b76440b23db69bdb59f160e1267ef39939a471]
    Right Witness: [3146459cc09e66e9a32e251e620c8f264581134bbcd8a81d3aa94e2017d02158]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [fc6dd766522c4be77222ce112588f731e17ea37b61f3b5b908dab761c6676bd9]
    Right Witness: [e8c051586366a5c28e32c27c70572def57e900b83bc1feff99ab9ef126fb25b9]
    Height: 0
    Ed25519 Secret Key:       [29e3e6b41ccbb4af1d334514d133edfc216190f9ff0c709bd684e3778a7844e2]
    Ed25519 Verification Key: [66faac397e9563745f2623a1825c90366cc7971d0b1a0c87f3722685caae6a2d]
```
- Sigma t = 42:
```
Sigma 1:
    Verification Key: [a3be6fd324fcb51afe38c6ce4cf97273b06a4836896da1868234f823c4b24477]
    Sigma: [c59c276e385b036d7e3911fb957f2db972bf8010f1ba09e52f7cf9d20dda03c801adc5918d73b1c05763f6abe0a2503ce7c67870f0dad891d199ee5f33e6b707]
    W[0]: [fe82b54e078c986aa9c25a0e914463c8b8361692221c8a2716c6dc3d746fd08b]
    W[1]: [b02c889de52f5ce59b7778a771631a0ffa4b99419c4a2078102be8a4465aac6e]
    W[2]: [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
Sigma 2:
    Verification Key: [9a33868bad6a3713b54962d42e4a17b135845281cdf8786ac100865e2ceb6d14]
    Sigma: [376d8cfea55f0275f24b02e020222be2170aec07cfb1249855ca7d0ffa35393b6c0bb977cc167095c8f4de3574b773c278e888b4cc2b1c4e9da8b6fa7ec92303]
    W[0]: [bcbecf84e3bc0f4d482dee450e19efbe579e3f1121e7e8a24a746c416e327e97]
    W[1]: [3044d1d9a57616e8ed109dc37a585d5add07dddd4a0ff0e2e110deb162c5bc36]
    W[2]: [7c414edab64a076d47ce39d28bc3b76952e0c552f1b4baaf6460e56d00429019]
R 2: [e1b233d3e9969137ce9d7684316135ef76a2fe507692cf1f1528f6abfc756892]
```
Product Composition Secret Key, t = 42:
```
Tau 1:
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
    Right Witness: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
    Height: 2
    Binary configuration: 0
    Right Seed:    [46b3d84aad52ba256269df8e2397fb6f8f2e79d80984416e8fd5bb33fa93414f]
    Left Witness:  [2e15e54671daf8576d5b2d9d38708b2d2601a038192018984d19f11bf72702e4]
    Right Witness: [b02c889de52f5ce59b7778a771631a0ffa4b99419c4a2078102be8a4465aac6e]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [fe82b54e078c986aa9c25a0e914463c8b8361692221c8a2716c6dc3d746fd08b]
    Right Witness: [37eb63299e1be20b236dc6a53d69b563754df31f6c3476b536a0f632f4dd32ce]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [a3be6fd324fcb51afe38c6ce4cf97273b06a4836896da1868234f823c4b24477]
Sigma 1:
    Verification Key: [a3be6fd324fcb51afe38c6ce4cf97273b06a4836896da1868234f823c4b24477]
    Sigma: [c59c276e385b036d7e3911fb957f2db972bf8010f1ba09e52f7cf9d20dda03c801adc5918d73b1c05763f6abe0a2503ce7c67870f0dad891d199ee5f33e6b707]
    W[0]: [fe82b54e078c986aa9c25a0e914463c8b8361692221c8a2716c6dc3d746fd08b]
    W[1]: [b02c889de52f5ce59b7778a771631a0ffa4b99419c4a2078102be8a4465aac6e]
    W[2]: [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
Seed:
    9e38d15bad1f738f104f222b154fe0c65b4b96adb5eb12d73dd2aac8b6988b72
Tau 2:
    Height: 3
    Binary configuration: 0
    Right Seed:    [8932b91679ea96c9762be582fcce76dcf40ee6202f4d3b8ac4855f57bb0e9f3e]
    Left Witness:  [3a6e156fe18596051004cc55b5308f0be60d8e9953312f0590470e9c2dceb423]
    Right Witness: [7c414edab64a076d47ce39d28bc3b76952e0c552f1b4baaf6460e56d00429019]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [3044d1d9a57616e8ed109dc37a585d5add07dddd4a0ff0e2e110deb162c5bc36]
    Right Witness: [16ecc52eef3746f34288a3251148cb97cc9bce44841b909285db3a8b500b3d97]
    Height: 1
    Binary configuration: 0
    Right Seed:    [d4977768a5a4b8c25fefaf1a14778a3d96eb52f1f0a739597e5e51e8532ef054]
    Left Witness:  [c49424723624efb20f807e08915d00b6c2c29ed97db3a7cd7225aea839af1348]
    Right Witness: [bcbecf84e3bc0f4d482dee450e19efbe579e3f1121e7e8a24a746c416e327e97]
    Height: 0
    Ed25519 Secret Key:       [7dedd5db901c98ababdb90101df2aa1874b62d2d59a74aa377e1158058814c34]
    Ed25519 Verification Key: [9a33868bad6a3713b54962d42e4a17b135845281cdf8786ac100865e2ceb6d14]
```
- Sigma t = 63:
```
Sigma 1:
    Verification Key: [84e857556ab0f306d9ccaf07951f0b9a4326d8f470d2761465f076cf9afc3bda]
    Sigma: [2b981e6768d0e2bb83cf7b640e34861fd57f47e018c610bef691a1a7a6529a5505bb4ac7f598f057bd91c0d69265077c8d5da3ed35e1964af4bda4907ea66b0b]
    W[0]: [85a8aed9dc95730edf357a850ab80090c142b93058dd0b8e5f3cd3319a60ab9f]
    W[1]: [2e15e54671daf8576d5b2d9d38708b2d2601a038192018984d19f11bf72702e4]
    W[2]: [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
Sigma 2:
    Verification Key: [9ebeebb407842ae0f67d9aee5ffabc32a8e6a1bd7810c4da995a578529565e29]
    Sigma: [07329c9802f10e01783fa5ed9081673098effdcca4ee45d6fb5788c1129cb8f0f7370e9078e8c58aed2aea4de95e72ec7a213d74104739c415dac77cb47e2501]
    W[0]: [05d621aa665d76e25c5f535a5a15b09e46c4aabc744de1801c2749f9f52a95c0]
    W[1]: [bc0225bcc28bed4ccc43c3a4910c2ad3e2d62894ebdb9ba67190df085858934d]
    W[2]: [f18710ea9ac9e6ca20070beddbcd7ed0b1608aa10116a98a197b8639cdbcc337]
R 2: [1b9972beb1238eee1f032c48a026244e407f19d63c34baef8348ac996fcac9d7]
```
Product Composition Secret Key, t = 63:
```
Tau 1:
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
    Right Witness: [3326b87fe172fea589f79de8ba7bea0b0f288ede17c3c2433dd2cc9c5ec01570]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [2e15e54671daf8576d5b2d9d38708b2d2601a038192018984d19f11bf72702e4]
    Right Witness: [b02c889de52f5ce59b7778a771631a0ffa4b99419c4a2078102be8a4465aac6e]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [85a8aed9dc95730edf357a850ab80090c142b93058dd0b8e5f3cd3319a60ab9f]
    Right Witness: [aadfd3fb7dc12b491b89338c3d5a4395d56f627893a91cea402d2c1bf163eb7e]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [84e857556ab0f306d9ccaf07951f0b9a4326d8f470d2761465f076cf9afc3bda]
Sigma 1:
    Verification Key: [84e857556ab0f306d9ccaf07951f0b9a4326d8f470d2761465f076cf9afc3bda]
    Sigma: [2b981e6768d0e2bb83cf7b640e34861fd57f47e018c610bef691a1a7a6529a5505bb4ac7f598f057bd91c0d69265077c8d5da3ed35e1964af4bda4907ea66b0b]
    W[0]: [85a8aed9dc95730edf357a850ab80090c142b93058dd0b8e5f3cd3319a60ab9f]
    W[1]: [2e15e54671daf8576d5b2d9d38708b2d2601a038192018984d19f11bf72702e4]
    W[2]: [33d94f87778d5204ceb3b8e3b3768600627a1b6ad66d078e1a3541bd4fcda649]
Seed:
    d28799166f3ff947b2008aa4a44575adfe6ee941ec491e60706069b01d0f00ca
Tau 2:
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f18710ea9ac9e6ca20070beddbcd7ed0b1608aa10116a98a197b8639cdbcc337]
    Right Witness: [1a78ce3fea8965804f34e92cc06b680424566315e5c823b8d42eb562fb01003d]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [bc0225bcc28bed4ccc43c3a4910c2ad3e2d62894ebdb9ba67190df085858934d]
    Right Witness: [7bb89fda73f3eece2976a179e528c9c150b0b4e50df3cc4a7fe22513271cec15]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [05d621aa665d76e25c5f535a5a15b09e46c4aabc744de1801c2749f9f52a95c0]
    Right Witness: [c9b8047460fa7cc357b73974c61dcf5dc13f9a18d49536be73651dbe6f8d68a5]
    Height: 0
    Ed25519 Secret Key:       [b8e2330334693ee0cfca3835b5247383dfca8324895f98ffadc8bdf90ee259b6]
    Ed25519 Verification Key: [9ebeebb407842ae0f67d9aee5ffabc32a8e6a1bd7810c4da995a578529565e29]
```
## Test Vector - 6
### Description 
 Generate and verify a specified product composition signature at `t = [0, 85, 170, 255]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
768f9760f74bab4f56fa46b7030525f227368d553c1b6de57026b675bdd6295a
```
- h1 (int):

```4```

- h2 (int):

```4```

- Message (string):
```
"place it on a stump"
```
- Message (bytes) with `utf-8` encoding:
```
706c616365206974206f6e2061207374756d70
```
### Outputs
- Product Composition Verification Key:
```
3cef287de1467276a6527f3af9f2e199aaf0efa1d0f801cc69cd7e340580fd89
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 4
    Binary configuration: 0
    Right Seed:    [e781753461ecb4afecb94997a8473a45f6261fd78fef170d6557a3a69140ca55]
    Left Witness:  [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
    Right Witness: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
    Height: 3
    Binary configuration: 0
    Right Seed:    [9f1790e73555146ae174495f356243f3c3c10596ff442c6a5a3cd87a0777b94f]
    Left Witness:  [f1a7b96bf5fc14b1414d0d2d421352533bf7d84a07fb58d5e0859624343b4709]
    Right Witness: [e0227b25fdc6cc314e2bd448a16aaef620e298636cd2ea1689e07ef52a9410d8]
    Height: 2
    Binary configuration: 0
    Right Seed:    [ca45d6710abad3b14eea26c840300bd15603518c5160a6c1c94b8e1bde622b36]
    Left Witness:  [e7d0c668e7ce3819f4867dc23cc11a60bc30fe2a3fd66ca1c300187a678b2e4a]
    Right Witness: [013342ac9e9a817cdb95081a4c67aa811f533dc96cea98d1987933b9a380c5c7]
    Height: 1
    Binary configuration: 0
    Right Seed:    [ee610d33dc203942e06eb25443115d9f1253cd1bf5bf0dbbf5b5c36565e11ce8]
    Left Witness:  [ad3e85980bd3f8158d04170fc4a622ff3091cb6fa78fca07148d8e3b716b5718]
    Right Witness: [6f669100cf05ed7eb9754b97383d0ce20d4c6d7c981fe8d3c9e4f5745bd2540a]
    Height: 0
    Ed25519 Secret Key:       [756fa22d868acc5ade229436501451f03358fc157a1169f001c40928070de544]
    Ed25519 Verification Key: [f64479747e24327798515d552f55b63c757cf76eba98be1ba9159328e6457058]
Sigma 1:
    Verification Key: [f64479747e24327798515d552f55b63c757cf76eba98be1ba9159328e6457058]
    Sigma: [a1ab61140e6ae483fd2659a9aee6fc8c377fc48fbed5888fa6e2952c4b3dd1b80ffe88ccce315b73c7eaf03fc65fd81f11508b33e584dc7ce4efda471d015d03]
    W[0]: [6f669100cf05ed7eb9754b97383d0ce20d4c6d7c981fe8d3c9e4f5745bd2540a]
    W[1]: [013342ac9e9a817cdb95081a4c67aa811f533dc96cea98d1987933b9a380c5c7]
    W[2]: [e0227b25fdc6cc314e2bd448a16aaef620e298636cd2ea1689e07ef52a9410d8]
    W[3]: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
Seed:
    6dc9bde3368f2fa81752a32ab4c9e894d639eea05e7890ab52b3f2aa8ac905a5
Tau 2:
    Height: 4
    Binary configuration: 0
    Right Seed:    [4c995c91de39d26106e6359d5824437c3cd3331949ad410403937aa8d870162f]
    Left Witness:  [2f75758f0a8c1aec373e867ac901a84b7175fbe39bc081dcfe457c0c009c67f3]
    Right Witness: [de623ebf130a41f2c91b7954bc7a9640ef798f916ffa6743aa39b5c8806657dd]
    Height: 3
    Binary configuration: 0
    Right Seed:    [5993416ad5ee890f2e06aafe7277a8c3ef59cfaf626b9ff23ae291607089ab05]
    Left Witness:  [24982284f2bed54b3030fed75ca8e1840144d49002a85d66a0a20f1faf734ca8]
    Right Witness: [11b5b37bcd0cde7291640f4a2b021ea6e9cec7e77643c1fac0cd86f623a212d8]
    Height: 2
    Binary configuration: 0
    Right Seed:    [ac582ec43235b0f70d5e9847a8f66bd18adc248bc16704c2680add154176f142]
    Left Witness:  [51b60c4dd8ee65366c27719068b8eaf8a269247ef3a55ba3feada5b45f7e8abf]
    Right Witness: [f43933c9f93bcf3e95d480ff9d12fbc9680ea07e42d649da22cede104bc37c75]
    Height: 1
    Binary configuration: 0
    Right Seed:    [27bec3f7c1d17973e6003483cdc9006e34edce3f6c335ebbab2b273191e77612]
    Left Witness:  [43212e8ea8923b20e8db9589a47147ba0dc8fd52250e9865d82801eb59d1cc67]
    Right Witness: [7c00e956549a87f6da1ad464879fbc39645e7c5269140274ea43b15842a016ce]
    Height: 0
    Ed25519 Secret Key:       [03451261730ca6dcef21a9ea14f74dc3fbae5afc52dad7dd22b073c209d8d98a]
    Ed25519 Verification Key: [68c5e70d09acfa348c860c07396512ec899e3c06800c684c375e020c8d672603]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [f64479747e24327798515d552f55b63c757cf76eba98be1ba9159328e6457058]
    Sigma: [a1ab61140e6ae483fd2659a9aee6fc8c377fc48fbed5888fa6e2952c4b3dd1b80ffe88ccce315b73c7eaf03fc65fd81f11508b33e584dc7ce4efda471d015d03]
    W[0]: [6f669100cf05ed7eb9754b97383d0ce20d4c6d7c981fe8d3c9e4f5745bd2540a]
    W[1]: [013342ac9e9a817cdb95081a4c67aa811f533dc96cea98d1987933b9a380c5c7]
    W[2]: [e0227b25fdc6cc314e2bd448a16aaef620e298636cd2ea1689e07ef52a9410d8]
    W[3]: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
Sigma 2:
    Verification Key: [68c5e70d09acfa348c860c07396512ec899e3c06800c684c375e020c8d672603]
    Sigma: [33094d4886c203d8ecb452d9b9c338a665d6dade3449e263d9d7f3e62a7540530f4ece37bedd97e776008cccaec23b78566f2a9a8f4da6e8758f0fc9e8686303]
    W[0]: [7c00e956549a87f6da1ad464879fbc39645e7c5269140274ea43b15842a016ce]
    W[1]: [f43933c9f93bcf3e95d480ff9d12fbc9680ea07e42d649da22cede104bc37c75]
    W[2]: [11b5b37bcd0cde7291640f4a2b021ea6e9cec7e77643c1fac0cd86f623a212d8]
    W[3]: [de623ebf130a41f2c91b7954bc7a9640ef798f916ffa6743aa39b5c8806657dd]
R 2: [f3481270fa91ba14b07f9b9a09a8ff25de3cc87ad7e5548de7c9425951ae1286]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 4
    Binary configuration: 0
    Right Seed:    [e781753461ecb4afecb94997a8473a45f6261fd78fef170d6557a3a69140ca55]
    Left Witness:  [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
    Right Witness: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
    Height: 3
    Binary configuration: 0
    Right Seed:    [9f1790e73555146ae174495f356243f3c3c10596ff442c6a5a3cd87a0777b94f]
    Left Witness:  [f1a7b96bf5fc14b1414d0d2d421352533bf7d84a07fb58d5e0859624343b4709]
    Right Witness: [e0227b25fdc6cc314e2bd448a16aaef620e298636cd2ea1689e07ef52a9410d8]
    Height: 2
    Binary configuration: 0
    Right Seed:    [ca45d6710abad3b14eea26c840300bd15603518c5160a6c1c94b8e1bde622b36]
    Left Witness:  [e7d0c668e7ce3819f4867dc23cc11a60bc30fe2a3fd66ca1c300187a678b2e4a]
    Right Witness: [013342ac9e9a817cdb95081a4c67aa811f533dc96cea98d1987933b9a380c5c7]
    Height: 1
    Binary configuration: 0
    Right Seed:    [ee610d33dc203942e06eb25443115d9f1253cd1bf5bf0dbbf5b5c36565e11ce8]
    Left Witness:  [ad3e85980bd3f8158d04170fc4a622ff3091cb6fa78fca07148d8e3b716b5718]
    Right Witness: [6f669100cf05ed7eb9754b97383d0ce20d4c6d7c981fe8d3c9e4f5745bd2540a]
    Height: 0
    Ed25519 Secret Key:       [756fa22d868acc5ade229436501451f03358fc157a1169f001c40928070de544]
    Ed25519 Verification Key: [f64479747e24327798515d552f55b63c757cf76eba98be1ba9159328e6457058]
Sigma 1:
    Verification Key: [f64479747e24327798515d552f55b63c757cf76eba98be1ba9159328e6457058]
    Sigma: [a1ab61140e6ae483fd2659a9aee6fc8c377fc48fbed5888fa6e2952c4b3dd1b80ffe88ccce315b73c7eaf03fc65fd81f11508b33e584dc7ce4efda471d015d03]
    W[0]: [6f669100cf05ed7eb9754b97383d0ce20d4c6d7c981fe8d3c9e4f5745bd2540a]
    W[1]: [013342ac9e9a817cdb95081a4c67aa811f533dc96cea98d1987933b9a380c5c7]
    W[2]: [e0227b25fdc6cc314e2bd448a16aaef620e298636cd2ea1689e07ef52a9410d8]
    W[3]: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
Seed:
    6dc9bde3368f2fa81752a32ab4c9e894d639eea05e7890ab52b3f2aa8ac905a5
Tau 2:
    Height: 4
    Binary configuration: 0
    Right Seed:    [4c995c91de39d26106e6359d5824437c3cd3331949ad410403937aa8d870162f]
    Left Witness:  [2f75758f0a8c1aec373e867ac901a84b7175fbe39bc081dcfe457c0c009c67f3]
    Right Witness: [de623ebf130a41f2c91b7954bc7a9640ef798f916ffa6743aa39b5c8806657dd]
    Height: 3
    Binary configuration: 0
    Right Seed:    [5993416ad5ee890f2e06aafe7277a8c3ef59cfaf626b9ff23ae291607089ab05]
    Left Witness:  [24982284f2bed54b3030fed75ca8e1840144d49002a85d66a0a20f1faf734ca8]
    Right Witness: [11b5b37bcd0cde7291640f4a2b021ea6e9cec7e77643c1fac0cd86f623a212d8]
    Height: 2
    Binary configuration: 0
    Right Seed:    [ac582ec43235b0f70d5e9847a8f66bd18adc248bc16704c2680add154176f142]
    Left Witness:  [51b60c4dd8ee65366c27719068b8eaf8a269247ef3a55ba3feada5b45f7e8abf]
    Right Witness: [f43933c9f93bcf3e95d480ff9d12fbc9680ea07e42d649da22cede104bc37c75]
    Height: 1
    Binary configuration: 0
    Right Seed:    [27bec3f7c1d17973e6003483cdc9006e34edce3f6c335ebbab2b273191e77612]
    Left Witness:  [43212e8ea8923b20e8db9589a47147ba0dc8fd52250e9865d82801eb59d1cc67]
    Right Witness: [7c00e956549a87f6da1ad464879fbc39645e7c5269140274ea43b15842a016ce]
    Height: 0
    Ed25519 Secret Key:       [03451261730ca6dcef21a9ea14f74dc3fbae5afc52dad7dd22b073c209d8d98a]
    Ed25519 Verification Key: [68c5e70d09acfa348c860c07396512ec899e3c06800c684c375e020c8d672603]
```
- Sigma t = 85:
```
Sigma 1:
    Verification Key: [19f5224ed6c6ac6fd7f6a532491befb22b29164a3af74c33bd78dcefe0f5e68b]
    Sigma: [55788caf92e501bc5dc3bacc08aa898c0d3b88c84c835193e29d4dd33e1dddfde5b042bcbc8d76b8fabc524c034cdc1a158afaded22e6abccf886c5d8148d806]
    W[0]: [5c4d66136f7b09228f6cfbf1bc8c30cd4b247d4456df869d591ddff1130f40eb]
    W[1]: [d67d7e5745c1bea953b1d21131d792295db7f6eef4684e5ecc3c6f75f1a2b5a4]
    W[2]: [f1a7b96bf5fc14b1414d0d2d421352533bf7d84a07fb58d5e0859624343b4709]
    W[3]: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
Sigma 2:
    Verification Key: [cd77c681303d3c3e83094c0dc825bce88395ec4a6eab4a9ce84d7cb0944c3061]
    Sigma: [155cb33ba2ae0e71d5f30730701cb8cb0639462044eedcdba75dac8dd58221fe514d6e0a0058240b13291a731f4b7440e2967f7aaf7ec124608f0eced07ed206]
    W[0]: [45e713f37f42f8dbe0b853e212d8fd3104a4ffc128aaabae49e2abfaeae68d09]
    W[1]: [4b651acd0fab5573a2fed3be1d11cb46d680d63ca687756c557c0bc5824b2723]
    W[2]: [6d0f9e5306bc153a4a63485af566cd420625f38f4c2f909e9256390ca18769f2]
    W[3]: [4d4e98f9c98c53cb6b37af3a3b5dd51d127523fd1673efe43e3e92b68da4dee0]
R 2: [71a9a67b198968f8e6d5d96e7249acf7a11731c13be1709693b8c83dd97d1a7c]
```
Product Composition Secret Key, t = 85:
```
Tau 1:
    Height: 4
    Binary configuration: 0
    Right Seed:    [e781753461ecb4afecb94997a8473a45f6261fd78fef170d6557a3a69140ca55]
    Left Witness:  [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
    Right Witness: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f1a7b96bf5fc14b1414d0d2d421352533bf7d84a07fb58d5e0859624343b4709]
    Right Witness: [e0227b25fdc6cc314e2bd448a16aaef620e298636cd2ea1689e07ef52a9410d8]
    Height: 2
    Binary configuration: 0
    Right Seed:    [54d10a2bd0cf11dded3f509941212870e6d4f940902e9cca748bc54b2055c7b1]
    Left Witness:  [e5cc48d270133fde59bc64d39504bd5ad57c5261f5ea34e871990e9a2e2f7475]
    Right Witness: [d67d7e5745c1bea953b1d21131d792295db7f6eef4684e5ecc3c6f75f1a2b5a4]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5c4d66136f7b09228f6cfbf1bc8c30cd4b247d4456df869d591ddff1130f40eb]
    Right Witness: [6256516657d4f97667e1ebdf899756a39d6578f48249fdece6ead08e93df0043]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [19f5224ed6c6ac6fd7f6a532491befb22b29164a3af74c33bd78dcefe0f5e68b]
Sigma 1:
    Verification Key: [19f5224ed6c6ac6fd7f6a532491befb22b29164a3af74c33bd78dcefe0f5e68b]
    Sigma: [55788caf92e501bc5dc3bacc08aa898c0d3b88c84c835193e29d4dd33e1dddfde5b042bcbc8d76b8fabc524c034cdc1a158afaded22e6abccf886c5d8148d806]
    W[0]: [5c4d66136f7b09228f6cfbf1bc8c30cd4b247d4456df869d591ddff1130f40eb]
    W[1]: [d67d7e5745c1bea953b1d21131d792295db7f6eef4684e5ecc3c6f75f1a2b5a4]
    W[2]: [f1a7b96bf5fc14b1414d0d2d421352533bf7d84a07fb58d5e0859624343b4709]
    W[3]: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
Seed:
    8bba45a219cd212097ef60d275f2df3148ef848a91bdef24bb90d496be4e3a90
Tau 2:
    Height: 4
    Binary configuration: 0
    Right Seed:    [f85d7cd4630684d6f1cf1de625df020b34ae97f0c8239559efca2310d634178d]
    Left Witness:  [2f67dbbcc219e32233804216fc330bb694c5215db4dc62adc89adf99057e55a5]
    Right Witness: [4d4e98f9c98c53cb6b37af3a3b5dd51d127523fd1673efe43e3e92b68da4dee0]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [6d0f9e5306bc153a4a63485af566cd420625f38f4c2f909e9256390ca18769f2]
    Right Witness: [9e788eeb57c2542e8efee7c9487c44b6fcba8a591176a6857f9196135bb6ddee]
    Height: 2
    Binary configuration: 0
    Right Seed:    [7ace7c3d8e3e7ef99e4833fac6074cbc23792be189304a5190540dc107a03b91]
    Left Witness:  [1e3014b273fcbae4f48cb9e904e5af44b543b9ff23d173c7964dce5a31df8e86]
    Right Witness: [4b651acd0fab5573a2fed3be1d11cb46d680d63ca687756c557c0bc5824b2723]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [45e713f37f42f8dbe0b853e212d8fd3104a4ffc128aaabae49e2abfaeae68d09]
    Right Witness: [ebeb2d1b5279763f43df3def888f24c86455ee21ba914cec5fb51a4d12e5e7a1]
    Height: 0
    Ed25519 Secret Key:       [cee76653078945c1387f325784f63871b7e1a384927548d2fb9a76ba50ffc01b]
    Ed25519 Verification Key: [cd77c681303d3c3e83094c0dc825bce88395ec4a6eab4a9ce84d7cb0944c3061]
```
- Sigma t = 170:
```
Sigma 1:
    Verification Key: [331d7fd62ee1f723ee6b09a9d9133ea2d2233208ba7ae16ac533238c30e08c24]
    Sigma: [f50517b1b587f29d88f7a526d5a138e40641fda340a2bfa5fc14d143dd195e2c7a28175e67376dadaf453feb46eb3aec1c92bdcc93e495c22ea399ec7a4b1103]
    W[0]: [4a25db497738e68aa6e27156b36db3f2e58ef5180bb543df4a88b360a96d6b5e]
    W[1]: [d928875a9ebef33d1f0e8d296b2db8f52428cae04fbab7c677dd5d7be5040cd1]
    W[2]: [93255f57d3deb85b3b9c9fbb09ff110c56f72e394823c7ebbde7e7cccf8eb2f8]
    W[3]: [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
Sigma 2:
    Verification Key: [183c3810ed99dda75f5f7aebcae99e06f0897ff7c5a27dc1cf0c32ab9c4de992]
    Sigma: [fe56a0a89f166621a17d33176733ef88e5a2e16d257a188e96a69ecb85ee8607a212385a9eeb84e9d66a053f1906efcd9753294d2e9f1ac16a4b14dbe9a6d605]
    W[0]: [606a3022034ef39b31edfb87877db8945d9d4bde4446049b5146ab204676bcc2]
    W[1]: [f199c5f85b4e1acc18870d48efa2362f59bb00600b179707cd38b9c810a7c115]
    W[2]: [a62a0f2f68fc607ffd8bb9c82f5dafad4c138d3c4db7e338a515b80b93405c88]
    W[3]: [95c5adb410133f3bcb668d6a082afb686ab188828ab80f28448b3555200a9607]
R 2: [4e535a39457f44fe3d390a825d96ee2ddf825c69eeee6a796c1ebb582ab396d4]
```
Product Composition Secret Key, t = 170:
```
Tau 1:
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
    Right Witness: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
    Height: 3
    Binary configuration: 0
    Right Seed:    [94431ea637d193868523856b3caec12acb0e2267c76af037b0fc9054f90f602e]
    Left Witness:  [9037281ef3026f47fb7aaac7a42de9decd50dae59b011279203d2519690b2d49]
    Right Witness: [93255f57d3deb85b3b9c9fbb09ff110c56f72e394823c7ebbde7e7cccf8eb2f8]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d928875a9ebef33d1f0e8d296b2db8f52428cae04fbab7c677dd5d7be5040cd1]
    Right Witness: [e3bfe28d780cbad69b3479cd2a6e7ad88ee0c0833eb285cf7121741669f87dde]
    Height: 1
    Binary configuration: 0
    Right Seed:    [4f0c9d5fa093b3fe8f0a1afee486de4fb577059c840203735573f008a2b2cea3]
    Left Witness:  [dced6417f8b3a1397c9b5e7bd88352da55e1139bec0028f1129b5467dc2f05b2]
    Right Witness: [4a25db497738e68aa6e27156b36db3f2e58ef5180bb543df4a88b360a96d6b5e]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [331d7fd62ee1f723ee6b09a9d9133ea2d2233208ba7ae16ac533238c30e08c24]
Sigma 1:
    Verification Key: [331d7fd62ee1f723ee6b09a9d9133ea2d2233208ba7ae16ac533238c30e08c24]
    Sigma: [f50517b1b587f29d88f7a526d5a138e40641fda340a2bfa5fc14d143dd195e2c7a28175e67376dadaf453feb46eb3aec1c92bdcc93e495c22ea399ec7a4b1103]
    W[0]: [4a25db497738e68aa6e27156b36db3f2e58ef5180bb543df4a88b360a96d6b5e]
    W[1]: [d928875a9ebef33d1f0e8d296b2db8f52428cae04fbab7c677dd5d7be5040cd1]
    W[2]: [93255f57d3deb85b3b9c9fbb09ff110c56f72e394823c7ebbde7e7cccf8eb2f8]
    W[3]: [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
Seed:
    9dee94f41e1605dc0c65c1311037470e198237da9f46301c389a97bd02d3586c
Tau 2:
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [95c5adb410133f3bcb668d6a082afb686ab188828ab80f28448b3555200a9607]
    Right Witness: [c77d829c4b356e1e0b6c7f49f2a885a0ddd8067b8e84e643540608bc2406b0c9]
    Height: 3
    Binary configuration: 0
    Right Seed:    [7b08789d18296225dcca3f0dcb4d7127a09eb937551f940abb30dd10de2f1432]
    Left Witness:  [9b4ef5c7a83eb1b6b836b220f97486a6f8aa20b9acba4b9accf29b76d11ee93d]
    Right Witness: [a62a0f2f68fc607ffd8bb9c82f5dafad4c138d3c4db7e338a515b80b93405c88]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f199c5f85b4e1acc18870d48efa2362f59bb00600b179707cd38b9c810a7c115]
    Right Witness: [7d08e3198f1386671c9deab0d152a042eb956ccf6ad2689a27623d36d5393b2f]
    Height: 1
    Binary configuration: 0
    Right Seed:    [6dc5dbe82db59817f1a6e3f2b47602f0d3c9e91acc6dcaeaa8482eacb0f3ea52]
    Left Witness:  [2019c82ee4960cf5a66898d4100813266cd0d115c9094242db4940418e99ec8e]
    Right Witness: [606a3022034ef39b31edfb87877db8945d9d4bde4446049b5146ab204676bcc2]
    Height: 0
    Ed25519 Secret Key:       [b44277c76c48a59c197dd15dd50e707f3372ee4034d9160d7bb41df9b8cde8ce]
    Ed25519 Verification Key: [183c3810ed99dda75f5f7aebcae99e06f0897ff7c5a27dc1cf0c32ab9c4de992]
```
- Sigma t = 255:
```
Sigma 1:
    Verification Key: [e63ca6a8c884701fefadada34f497e8fe55dad7b1ea9ce289dd07e7feaddfa99]
    Sigma: [fc1fe972eedd257172d6688275825402ba45909ddf37cd8b370ad6c7f6aa4c4cff78c2270d8f263cafb223bd97782c855f31664939ea483b2d3141f604748807]
    W[0]: [7723b587ac5eb1ab13df1ade867b69986e564c6d4d0e65273fe0251269e9da68]
    W[1]: [915399d653da23cf71c7fee6c986c30f6d4f4492c66e1d27e8e9a650c36f3905]
    W[2]: [9037281ef3026f47fb7aaac7a42de9decd50dae59b011279203d2519690b2d49]
    W[3]: [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
Sigma 2:
    Verification Key: [81ebb81987fd94f3ddcbb9313ea015b9e7c7964ffaef31f5768d5afd8cf7e3a7]
    Sigma: [b298337b3a75599d1c07db124a7c590f0d6f0f1a136a5a330bda69694cca40307168a356ce18f1cda5c58a3c0ac3ab25c1a73fcdc52d218037ef6707e528cd09]
    W[0]: [98d2d4bd487f365b3d9d54dbfb69a40d04b8fb21894fd38bc1781761567cc185]
    W[1]: [b5e3b9a3eed371f46df4cefc967d52207122d16931c653fd3221b1fdc498bf44]
    W[2]: [ca0134974d44630224a2fd51466dd38da368061674fded23f734c2d87d17a534]
    W[3]: [44f7df5be1b100c408f2907e3f5cc3cfa8ac6bf1decb78524370dae886a5edd0]
R 2: [aca697561776ad3751c5a16ae176aca59d309486f2dd70b7b6632c3f0a5ce652]
```
Product Composition Secret Key, t = 255:
```
Tau 1:
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
    Right Witness: [3eb00d5169d07be9cfe6684a7798ecc3af0fb196dd0d108dfa2bbf051a37e061]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9037281ef3026f47fb7aaac7a42de9decd50dae59b011279203d2519690b2d49]
    Right Witness: [93255f57d3deb85b3b9c9fbb09ff110c56f72e394823c7ebbde7e7cccf8eb2f8]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [915399d653da23cf71c7fee6c986c30f6d4f4492c66e1d27e8e9a650c36f3905]
    Right Witness: [00eae5886b6db14eb7f0238e48a6f3ad9fc6b80124b7aec2daea5c4a9836a369]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7723b587ac5eb1ab13df1ade867b69986e564c6d4d0e65273fe0251269e9da68]
    Right Witness: [1808d39c101b3ed8b89ebbff9ab5c561238c99aa30c0c7d6f42a7e073b0bc01a]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [e63ca6a8c884701fefadada34f497e8fe55dad7b1ea9ce289dd07e7feaddfa99]
Sigma 1:
    Verification Key: [e63ca6a8c884701fefadada34f497e8fe55dad7b1ea9ce289dd07e7feaddfa99]
    Sigma: [fc1fe972eedd257172d6688275825402ba45909ddf37cd8b370ad6c7f6aa4c4cff78c2270d8f263cafb223bd97782c855f31664939ea483b2d3141f604748807]
    W[0]: [7723b587ac5eb1ab13df1ade867b69986e564c6d4d0e65273fe0251269e9da68]
    W[1]: [915399d653da23cf71c7fee6c986c30f6d4f4492c66e1d27e8e9a650c36f3905]
    W[2]: [9037281ef3026f47fb7aaac7a42de9decd50dae59b011279203d2519690b2d49]
    W[3]: [d51207e5a59e22e6a55584766942a433426dd1582a2aeaaa749b63cfba8fc436]
Seed:
    fa5606351eecfb5d28b66019a2f25589cfb27ee7158e1ddb5a6b7ca36c289e55
Tau 2:
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [44f7df5be1b100c408f2907e3f5cc3cfa8ac6bf1decb78524370dae886a5edd0]
    Right Witness: [15fac3a800d91ce2f013656faf1939675e32e0df1496efd0c8ea797e3dbab137]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [ca0134974d44630224a2fd51466dd38da368061674fded23f734c2d87d17a534]
    Right Witness: [87e6595c410b4d16d92951e562b11a5d700b56af3befaaea3fa2d25cdda9388c]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b5e3b9a3eed371f46df4cefc967d52207122d16931c653fd3221b1fdc498bf44]
    Right Witness: [956f66206ffea429ef4a89f46722ba91035ad4b5013753276a2a1c896f37f9cb]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [98d2d4bd487f365b3d9d54dbfb69a40d04b8fb21894fd38bc1781761567cc185]
    Right Witness: [bffc59593e4e603e9fdc42755f43d01a93d67b3ae8bd969da42d8a660922fa64]
    Height: 0
    Ed25519 Secret Key:       [eb42b9305ee23695f9bdcb5dd7210bd16abade18c39a554392a649e4adfd91b7]
    Ed25519 Verification Key: [81ebb81987fd94f3ddcbb9313ea015b9e7c7964ffaef31f5768d5afd8cf7e3a7]
```
## Test Vector - 7
### Description 
 Generate and verify a specified product composition signature at `t = [0, 341, 682, 1023]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
9c26e3a734a3cb1e0a54d801662469fed30c4b88cbe1544856134b3457728b45
```
- h1 (int):

```5```

- h2 (int):

```5```

- Message (string):
```
"nature speaks to those who disappear into it"
```
- Message (bytes) with `utf-8` encoding:
```
6e617475726520737065616b7320746f2074686f73652077686f2064697361707065617220696e746f206974
```
### Outputs
- Product Composition Verification Key:
```
7a89d035cea964b9fe438952a9ce614f5c82d1be3bc156bed6ec3503f2dbee06
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 5
    Binary configuration: 0
    Right Seed:    [5e45cb18ecd6ffba3fb6bc01470fd632bd4ea3bad111f619847befc9ccd75aee]
    Left Witness:  [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
    Right Witness: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
    Height: 4
    Binary configuration: 0
    Right Seed:    [56c82557f372a46a5e0471fa2dace363afd2484e2e8efb3b60d3428a559a5e65]
    Left Witness:  [693987c27c635c09d1852b08cc227389fdee4a45078dc840d7e7c1535861e1fb]
    Right Witness: [2ea4710ecd84176f6b0d789b60ae24fe705941ae40551f51c890cd55d0446207]
    Height: 3
    Binary configuration: 0
    Right Seed:    [a44707e8b111c44189804a74d2a0e5e97b971130aef2ee08589a8aa7d7b69150]
    Left Witness:  [d299633afbbaab776e48e81bd328e68c4e07bb1d4d1a41bd9bee035912e4ef43]
    Right Witness: [60d121cb554a7cd1d96174b4e064fd4cd1a3a56d8d3f55cd47c60398ff945efb]
    Height: 2
    Binary configuration: 0
    Right Seed:    [0f2d374e03c196a6473b5e15d0e581e31a847546216aed005f01207a2967f0a0]
    Left Witness:  [d308dddaf256db49e1e41469da7fd054ea4944e375943bbdc8c01bcbdba310ad]
    Right Witness: [dcca83c069d2f15fd4eef3189a04284c3d73f6f7e4c92ab6869ad0e852ebbe78]
    Height: 1
    Binary configuration: 0
    Right Seed:    [bc6c01febc75a3683bd9a7a35c51e9968bc46704f580a5586ea8cb3151289e30]
    Left Witness:  [0e9b464b13a2f5f6585eab160d4c96b0e74ed7dc0e8a5bee1657153c8355a76d]
    Right Witness: [a24ff972b6ad1302122fb9c2802f66818daabb165cf1ba1aabf49598cfb11ff6]
    Height: 0
    Ed25519 Secret Key:       [8a44fd50ffa16086b3a74bbed204f65d3119d172089489742d8cd4c7f77dea25]
    Ed25519 Verification Key: [edbc0a91e8deede4b290ca4d0cbb37fa545fa2c0daa620c75d932e255288621b]
Sigma 1:
    Verification Key: [edbc0a91e8deede4b290ca4d0cbb37fa545fa2c0daa620c75d932e255288621b]
    Sigma: [b97c8c94b76f9600ce56b5a8a035c9662e1b2f3100a0ab7d9f1bb17fabeca5f13bc4fd6341fdb0dfeab4ed582f799360f6b7b2a8f492b06abfa42e27eefdfe0d]
    W[0]: [a24ff972b6ad1302122fb9c2802f66818daabb165cf1ba1aabf49598cfb11ff6]
    W[1]: [dcca83c069d2f15fd4eef3189a04284c3d73f6f7e4c92ab6869ad0e852ebbe78]
    W[2]: [60d121cb554a7cd1d96174b4e064fd4cd1a3a56d8d3f55cd47c60398ff945efb]
    W[3]: [2ea4710ecd84176f6b0d789b60ae24fe705941ae40551f51c890cd55d0446207]
    W[4]: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
Seed:
    6fdfeae8eef08d774e2058fb62c0e2fec6d02ea1768973bf02831476be47946e
Tau 2:
    Height: 5
    Binary configuration: 0
    Right Seed:    [43f05d73a5e48b053aaa0b703e4d7d6dd9d70d11d2605f41c5db46c54e05b1b0]
    Left Witness:  [77b0826115166e6eaf768cf70164797875129a793d2279f1bcdfac11027c0dd5]
    Right Witness: [563d72ed62f6715b4e234f61b1f451e81dbac73843ed8fda3a632caaa96c1c59]
    Height: 4
    Binary configuration: 0
    Right Seed:    [551d6c3771fa1bf1e64157a683c1cc746cd5cb0b7fe5518ca742541bfe7f823c]
    Left Witness:  [26aac1bf05374519315993ce52d4baa27044205a3a97a737dbb6b9585632106f]
    Right Witness: [f5251ef47b4ae6a407630a859ad388254e70292b2e1651c089280d4fbb55da1e]
    Height: 3
    Binary configuration: 0
    Right Seed:    [40014e6f7ae9dd2f7995b507010c53cd46fb5e38ff7be4edc367e9af95f441a4]
    Left Witness:  [4021f51760f306ec3cfaf6d9563a3809c407fff669f8d86fd0e2617c10922ccc]
    Right Witness: [6f8b202c41a516ee0f0b82b51d407048b4b3c3f38eb97c7dbaf155eaefb6aa1f]
    Height: 2
    Binary configuration: 0
    Right Seed:    [204fb187b59eab3a6b10c680a9cd00899fb051a3f01c63e0d3d4c3bce07a4a69]
    Left Witness:  [3786925f6078da00ba6b3ae31ab4101cf3c3d05f1cab7b683c1535b1e5266562]
    Right Witness: [9bdf32c4a24deb210bb7a650d216c5c46721ef2aad00297732f494c82faff544]
    Height: 1
    Binary configuration: 0
    Right Seed:    [139b7b8938ef7c34d83392793ab09dc3762609e7c9003a2600be41f4948a3bd4]
    Left Witness:  [b0230340059562b6aebbed98d944801c8865cef160366cd48609a82231b60941]
    Right Witness: [0df4660f0cc17096bdb7de3613bcf4be45aeb5c18f7e89f1f8f52a058acdec91]
    Height: 0
    Ed25519 Secret Key:       [8dc16022c16821a2bbde516c7802b55cc5f28303c99f44936dd396f4482ef225]
    Ed25519 Verification Key: [1a4dbd918318ba9170eb058e8d12cfad3a975ca616f81c373c7a346ff1c03146]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [edbc0a91e8deede4b290ca4d0cbb37fa545fa2c0daa620c75d932e255288621b]
    Sigma: [b97c8c94b76f9600ce56b5a8a035c9662e1b2f3100a0ab7d9f1bb17fabeca5f13bc4fd6341fdb0dfeab4ed582f799360f6b7b2a8f492b06abfa42e27eefdfe0d]
    W[0]: [a24ff972b6ad1302122fb9c2802f66818daabb165cf1ba1aabf49598cfb11ff6]
    W[1]: [dcca83c069d2f15fd4eef3189a04284c3d73f6f7e4c92ab6869ad0e852ebbe78]
    W[2]: [60d121cb554a7cd1d96174b4e064fd4cd1a3a56d8d3f55cd47c60398ff945efb]
    W[3]: [2ea4710ecd84176f6b0d789b60ae24fe705941ae40551f51c890cd55d0446207]
    W[4]: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
Sigma 2:
    Verification Key: [1a4dbd918318ba9170eb058e8d12cfad3a975ca616f81c373c7a346ff1c03146]
    Sigma: [c3bf0d5d1a0fc663b99bcf9c5be088f4cf245660fb0f17e0a99278f88663e0251178cb956997ac84f89cabc1ea6741eb259afe318f899158209f192998beb00f]
    W[0]: [0df4660f0cc17096bdb7de3613bcf4be45aeb5c18f7e89f1f8f52a058acdec91]
    W[1]: [9bdf32c4a24deb210bb7a650d216c5c46721ef2aad00297732f494c82faff544]
    W[2]: [6f8b202c41a516ee0f0b82b51d407048b4b3c3f38eb97c7dbaf155eaefb6aa1f]
    W[3]: [f5251ef47b4ae6a407630a859ad388254e70292b2e1651c089280d4fbb55da1e]
    W[4]: [563d72ed62f6715b4e234f61b1f451e81dbac73843ed8fda3a632caaa96c1c59]
R 2: [ed62a9ea16331012f123bb24249454d40164324019084dc117260d740812e5e3]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 5
    Binary configuration: 0
    Right Seed:    [5e45cb18ecd6ffba3fb6bc01470fd632bd4ea3bad111f619847befc9ccd75aee]
    Left Witness:  [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
    Right Witness: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
    Height: 4
    Binary configuration: 0
    Right Seed:    [56c82557f372a46a5e0471fa2dace363afd2484e2e8efb3b60d3428a559a5e65]
    Left Witness:  [693987c27c635c09d1852b08cc227389fdee4a45078dc840d7e7c1535861e1fb]
    Right Witness: [2ea4710ecd84176f6b0d789b60ae24fe705941ae40551f51c890cd55d0446207]
    Height: 3
    Binary configuration: 0
    Right Seed:    [a44707e8b111c44189804a74d2a0e5e97b971130aef2ee08589a8aa7d7b69150]
    Left Witness:  [d299633afbbaab776e48e81bd328e68c4e07bb1d4d1a41bd9bee035912e4ef43]
    Right Witness: [60d121cb554a7cd1d96174b4e064fd4cd1a3a56d8d3f55cd47c60398ff945efb]
    Height: 2
    Binary configuration: 0
    Right Seed:    [0f2d374e03c196a6473b5e15d0e581e31a847546216aed005f01207a2967f0a0]
    Left Witness:  [d308dddaf256db49e1e41469da7fd054ea4944e375943bbdc8c01bcbdba310ad]
    Right Witness: [dcca83c069d2f15fd4eef3189a04284c3d73f6f7e4c92ab6869ad0e852ebbe78]
    Height: 1
    Binary configuration: 0
    Right Seed:    [bc6c01febc75a3683bd9a7a35c51e9968bc46704f580a5586ea8cb3151289e30]
    Left Witness:  [0e9b464b13a2f5f6585eab160d4c96b0e74ed7dc0e8a5bee1657153c8355a76d]
    Right Witness: [a24ff972b6ad1302122fb9c2802f66818daabb165cf1ba1aabf49598cfb11ff6]
    Height: 0
    Ed25519 Secret Key:       [8a44fd50ffa16086b3a74bbed204f65d3119d172089489742d8cd4c7f77dea25]
    Ed25519 Verification Key: [edbc0a91e8deede4b290ca4d0cbb37fa545fa2c0daa620c75d932e255288621b]
Sigma 1:
    Verification Key: [edbc0a91e8deede4b290ca4d0cbb37fa545fa2c0daa620c75d932e255288621b]
    Sigma: [b97c8c94b76f9600ce56b5a8a035c9662e1b2f3100a0ab7d9f1bb17fabeca5f13bc4fd6341fdb0dfeab4ed582f799360f6b7b2a8f492b06abfa42e27eefdfe0d]
    W[0]: [a24ff972b6ad1302122fb9c2802f66818daabb165cf1ba1aabf49598cfb11ff6]
    W[1]: [dcca83c069d2f15fd4eef3189a04284c3d73f6f7e4c92ab6869ad0e852ebbe78]
    W[2]: [60d121cb554a7cd1d96174b4e064fd4cd1a3a56d8d3f55cd47c60398ff945efb]
    W[3]: [2ea4710ecd84176f6b0d789b60ae24fe705941ae40551f51c890cd55d0446207]
    W[4]: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
Seed:
    6fdfeae8eef08d774e2058fb62c0e2fec6d02ea1768973bf02831476be47946e
Tau 2:
    Height: 5
    Binary configuration: 0
    Right Seed:    [43f05d73a5e48b053aaa0b703e4d7d6dd9d70d11d2605f41c5db46c54e05b1b0]
    Left Witness:  [77b0826115166e6eaf768cf70164797875129a793d2279f1bcdfac11027c0dd5]
    Right Witness: [563d72ed62f6715b4e234f61b1f451e81dbac73843ed8fda3a632caaa96c1c59]
    Height: 4
    Binary configuration: 0
    Right Seed:    [551d6c3771fa1bf1e64157a683c1cc746cd5cb0b7fe5518ca742541bfe7f823c]
    Left Witness:  [26aac1bf05374519315993ce52d4baa27044205a3a97a737dbb6b9585632106f]
    Right Witness: [f5251ef47b4ae6a407630a859ad388254e70292b2e1651c089280d4fbb55da1e]
    Height: 3
    Binary configuration: 0
    Right Seed:    [40014e6f7ae9dd2f7995b507010c53cd46fb5e38ff7be4edc367e9af95f441a4]
    Left Witness:  [4021f51760f306ec3cfaf6d9563a3809c407fff669f8d86fd0e2617c10922ccc]
    Right Witness: [6f8b202c41a516ee0f0b82b51d407048b4b3c3f38eb97c7dbaf155eaefb6aa1f]
    Height: 2
    Binary configuration: 0
    Right Seed:    [204fb187b59eab3a6b10c680a9cd00899fb051a3f01c63e0d3d4c3bce07a4a69]
    Left Witness:  [3786925f6078da00ba6b3ae31ab4101cf3c3d05f1cab7b683c1535b1e5266562]
    Right Witness: [9bdf32c4a24deb210bb7a650d216c5c46721ef2aad00297732f494c82faff544]
    Height: 1
    Binary configuration: 0
    Right Seed:    [139b7b8938ef7c34d83392793ab09dc3762609e7c9003a2600be41f4948a3bd4]
    Left Witness:  [b0230340059562b6aebbed98d944801c8865cef160366cd48609a82231b60941]
    Right Witness: [0df4660f0cc17096bdb7de3613bcf4be45aeb5c18f7e89f1f8f52a058acdec91]
    Height: 0
    Ed25519 Secret Key:       [8dc16022c16821a2bbde516c7802b55cc5f28303c99f44936dd396f4482ef225]
    Ed25519 Verification Key: [1a4dbd918318ba9170eb058e8d12cfad3a975ca616f81c373c7a346ff1c03146]
```
- Sigma t = 341:
```
Sigma 1:
    Verification Key: [bb5d8906aa529893d2ada6ee2e27c9bdc94ec15332569d32f2ea9dfae2ece6d6]
    Sigma: [56eb16113ccff0b493ff3c4ecfe019f4469fee00e29312f0855f679b832fe7813ec23df59faaab8475d8e2b2a54c6914a55a83c872bca69a37bbc03025f51c0e]
    W[0]: [8f41c3e3177ab8ed7bb1df10949b6694019445744aa5c9c56da37a1471661789]
    W[1]: [d85d6168c4bb8f0b4e1b86acd6270a74aab2f46b0f1ce32a0be6f379df5a76fe]
    W[2]: [1c57fe57585bb224ec2869be2f23ba48bfc3259c4d63601f34d9c48506f472f2]
    W[3]: [693987c27c635c09d1852b08cc227389fdee4a45078dc840d7e7c1535861e1fb]
    W[4]: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
Sigma 2:
    Verification Key: [1840fd86119f4a4c7c41a18d8deb57bb5a3226535bfca0c5de56e2bf26247e93]
    Sigma: [10855683daed1205ae715536fde58071295cc49ab49e852edfd9c97e9d6f90cce14e3afde4ca55c322ce9e8969b23688fcea7b3571f113e3d6bd8dc524d41f02]
    W[0]: [b68dbc76effd030879272925e9cbe61ac339a4c248fd0b9ea3cec0e35e03f1fa]
    W[1]: [60ed28c610be13c8cbca50b8b718e8defdebf9be2f3d75482d9b420794b93326]
    W[2]: [62e4b7772c481d507322828c85c6b97c0af8cd234843d1488b7bc8824f3d1fbc]
    W[3]: [645b0568bc62f7482abf6423834871db7ab49bfb8a1a178eecdbc71308f65b82]
    W[4]: [16625fae1b5c705bba5bc5e55b9b2bc4e9d737245e441a7a3da3bb50c7da9922]
R 2: [0151a233680378a7174bfbbd37f25522e057fcf0fe5792f8194e74719d24343b]
```
Product Composition Secret Key, t = 341:
```
Tau 1:
    Height: 5
    Binary configuration: 0
    Right Seed:    [5e45cb18ecd6ffba3fb6bc01470fd632bd4ea3bad111f619847befc9ccd75aee]
    Left Witness:  [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
    Right Witness: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [693987c27c635c09d1852b08cc227389fdee4a45078dc840d7e7c1535861e1fb]
    Right Witness: [2ea4710ecd84176f6b0d789b60ae24fe705941ae40551f51c890cd55d0446207]
    Height: 3
    Binary configuration: 0
    Right Seed:    [553a45d2bf68aaf45a3db8f380d0f1b4d1a0ca301ded61949fd1962c173b5466]
    Left Witness:  [1f0f876c20a5fc47414725b0db8f384d1869fcb1f61b52a97be7d7841b5cdcc8]
    Right Witness: [1c57fe57585bb224ec2869be2f23ba48bfc3259c4d63601f34d9c48506f472f2]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d85d6168c4bb8f0b4e1b86acd6270a74aab2f46b0f1ce32a0be6f379df5a76fe]
    Right Witness: [ba58d9dab4cf9c1b10f2a7c48a256dc7e4fa61259987ac88cbd7ffa3e6edf10e]
    Height: 1
    Binary configuration: 0
    Right Seed:    [08c5da22f5f12add5fa520dc20cd4d6dd6ea4b3eda6e001c6b047319d2ecf9e8]
    Left Witness:  [54b9380eab5769da5a5451ef92f201aeabfe31507110631a55f162c41cd3697a]
    Right Witness: [8f41c3e3177ab8ed7bb1df10949b6694019445744aa5c9c56da37a1471661789]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [bb5d8906aa529893d2ada6ee2e27c9bdc94ec15332569d32f2ea9dfae2ece6d6]
Sigma 1:
    Verification Key: [bb5d8906aa529893d2ada6ee2e27c9bdc94ec15332569d32f2ea9dfae2ece6d6]
    Sigma: [56eb16113ccff0b493ff3c4ecfe019f4469fee00e29312f0855f679b832fe7813ec23df59faaab8475d8e2b2a54c6914a55a83c872bca69a37bbc03025f51c0e]
    W[0]: [8f41c3e3177ab8ed7bb1df10949b6694019445744aa5c9c56da37a1471661789]
    W[1]: [d85d6168c4bb8f0b4e1b86acd6270a74aab2f46b0f1ce32a0be6f379df5a76fe]
    W[2]: [1c57fe57585bb224ec2869be2f23ba48bfc3259c4d63601f34d9c48506f472f2]
    W[3]: [693987c27c635c09d1852b08cc227389fdee4a45078dc840d7e7c1535861e1fb]
    W[4]: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
Seed:
    72199d212cb74ee6ea4cb6856582900866232c08f9c09cec4b7c6feaba1b454f
Tau 2:
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [16625fae1b5c705bba5bc5e55b9b2bc4e9d737245e441a7a3da3bb50c7da9922]
    Right Witness: [ff004a4e9e640c3bda14c869a7be9af3b151fe4c78974bb499179cd05f781050]
    Height: 4
    Binary configuration: 0
    Right Seed:    [404fe56aa18ba23631b84a115ab51b94e4191d49d33c824bfa5d54abdf392f36]
    Left Witness:  [7b25581ca8646eba852323b20ddafb98ef1c8c84dcdacdd0417e1ea5302b2599]
    Right Witness: [645b0568bc62f7482abf6423834871db7ab49bfb8a1a178eecdbc71308f65b82]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [62e4b7772c481d507322828c85c6b97c0af8cd234843d1488b7bc8824f3d1fbc]
    Right Witness: [f6715017c19c51ebc5a6635a74def8f3ea56e65b19f14127d94ce36a929209b6]
    Height: 2
    Binary configuration: 0
    Right Seed:    [8e33a9161284c74fdf38e9f3baead6371a4cc4e6de200580862fe4bff3e7a285]
    Left Witness:  [19427bf6bdc9f9eabbe197ba6bd7a434855f40ad0e90725c94a1c18859f6edce]
    Right Witness: [60ed28c610be13c8cbca50b8b718e8defdebf9be2f3d75482d9b420794b93326]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b68dbc76effd030879272925e9cbe61ac339a4c248fd0b9ea3cec0e35e03f1fa]
    Right Witness: [4f7587fcf73d90b3988f97ebfe8f101c9be9f96c529f93bc90bdb4c55e089883]
    Height: 0
    Ed25519 Secret Key:       [f315de7d6e17c67d5419a5f1047f990f9437806c5f2bdab804280e696f3ca431]
    Ed25519 Verification Key: [1840fd86119f4a4c7c41a18d8deb57bb5a3226535bfca0c5de56e2bf26247e93]
```
- Sigma t = 682:
```
Sigma 1:
    Verification Key: [860635e6c7b1907b685765c298fad1340cf03b30b2d92ad84f25397f8974096b]
    Sigma: [71b05ce367ac7d3c2dbffd2e251308536963f2fd82a0ec55ddd3eca0fa7861e8a720640e10f6ffe01964f95dab900257255e620b1443ea4cbff90d2d41488401]
    W[0]: [ec96f29824bbe95840d5023894c9776c60534cecdee74602bfa450b90cb1bfe9]
    W[1]: [60949a23ff455c9e66f0b1715f1fded4588c6d0697b6c10455002c9f40309b32]
    W[2]: [b5059ebc943665613414781647cfa2dff29f5ba7209f5e4abee4355120bd4006]
    W[3]: [3d099a7fa1e6ae0db7894dae705a1143918407ff8e522b6838f174e16be0c82d]
    W[4]: [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
Sigma 2:
    Verification Key: [bc9d44d0a449dd4e2f9daeff6a78d3799e5d9e0a95f59205afa5f867ef6c532a]
    Sigma: [fe7f45f463635c8695cd33e78f9d8b40d6141b1c5cc642c6d912447a3a3f65590b6cf3711c8b4d79d3226310772afe8f4bcf8584a942837ed384b098d0b24005]
    W[0]: [eb67dcbc2a7119684e4319eebd7fbad4348790645f80ac97cae1a77926ae54b7]
    W[1]: [2e0e20c401c3441263bd8973b54a8ee49491f698149d5ee39db70f3925f78233]
    W[2]: [d3d310aa042831bdabc16b882b8b78cb860da226d89afd263855a4f4720952eb]
    W[3]: [1f91d7a30ea66a905244f1c1e975c96afcd7683978a1121755cde43b2846f00c]
    W[4]: [779010db7b8b7aa7e02480c4c39bc9eb5b1cd77d53e2864510c7e8bc0e44f1e9]
R 2: [de0e2362dc8d0be5a13b8e314ee8cb63395b303576bf927e9add9f2edd3ac5f8]
```
Product Composition Secret Key, t = 682:
```
Tau 1:
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
    Right Witness: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
    Height: 4
    Binary configuration: 0
    Right Seed:    [7a16346839c0fe57ce49263a86ac1c39b860c97cd9311a5510adc3a580a4e884]
    Left Witness:  [ff62250deeee182274f9363ce9fb98db8422e5fec38725669ec21184408d41cf]
    Right Witness: [3d099a7fa1e6ae0db7894dae705a1143918407ff8e522b6838f174e16be0c82d]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b5059ebc943665613414781647cfa2dff29f5ba7209f5e4abee4355120bd4006]
    Right Witness: [358c0618c228af6e17e17e2029ebb792809bf2e7e5abd9613a584cfb68b0f70e]
    Height: 2
    Binary configuration: 0
    Right Seed:    [f5a11e8a6f3a173c4130b9151e13677a4ed0446a9f4e075fe1d5059e47769b19]
    Left Witness:  [c25c20a1cd2c4fa34cff309d7a68f16b5aec4c8b5578ac44314bf93626ec727a]
    Right Witness: [60949a23ff455c9e66f0b1715f1fded4588c6d0697b6c10455002c9f40309b32]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [ec96f29824bbe95840d5023894c9776c60534cecdee74602bfa450b90cb1bfe9]
    Right Witness: [0b2e2e099aa1987dd3f92d88d48465883ce550277d15eea5afc135dfd40c674d]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [860635e6c7b1907b685765c298fad1340cf03b30b2d92ad84f25397f8974096b]
Sigma 1:
    Verification Key: [860635e6c7b1907b685765c298fad1340cf03b30b2d92ad84f25397f8974096b]
    Sigma: [71b05ce367ac7d3c2dbffd2e251308536963f2fd82a0ec55ddd3eca0fa7861e8a720640e10f6ffe01964f95dab900257255e620b1443ea4cbff90d2d41488401]
    W[0]: [ec96f29824bbe95840d5023894c9776c60534cecdee74602bfa450b90cb1bfe9]
    W[1]: [60949a23ff455c9e66f0b1715f1fded4588c6d0697b6c10455002c9f40309b32]
    W[2]: [b5059ebc943665613414781647cfa2dff29f5ba7209f5e4abee4355120bd4006]
    W[3]: [3d099a7fa1e6ae0db7894dae705a1143918407ff8e522b6838f174e16be0c82d]
    W[4]: [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
Seed:
    046841b9b2193df8b2fa2490903af0b9f574f4ce44d98e1b21e26495d0a417a1
Tau 2:
    Height: 5
    Binary configuration: 0
    Right Seed:    [e9225ef67bac1e44bd56ff539c1d4138ed28575dfcd4881cdfbbcf0f1c3f418a]
    Left Witness:  [a9e353126f540f2b0b522d89f72618659a89c6d7f04bfca4ef2091fa5bb4899a]
    Right Witness: [779010db7b8b7aa7e02480c4c39bc9eb5b1cd77d53e2864510c7e8bc0e44f1e9]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [1f91d7a30ea66a905244f1c1e975c96afcd7683978a1121755cde43b2846f00c]
    Right Witness: [6c1314d1fc45461a6e76404f503c8832c1dd474f09a3059c334bb8dd75ad1027]
    Height: 3
    Binary configuration: 0
    Right Seed:    [3a1dcf666f9d26422ce95d952de10c37e1044fbef8d13c8606fa9519251c9cbc]
    Left Witness:  [cb86b189c4c78c7adffbf0cb0cdb4ecf4967da5b8025140d0baeda778cfc2cdd]
    Right Witness: [d3d310aa042831bdabc16b882b8b78cb860da226d89afd263855a4f4720952eb]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [2e0e20c401c3441263bd8973b54a8ee49491f698149d5ee39db70f3925f78233]
    Right Witness: [43d0899fd23d50a60af0778189a65a140543c0d8b79fdff74fa42921056e0c61]
    Height: 1
    Binary configuration: 0
    Right Seed:    [0780885139317947137af72ad80c54dbedf1414cadba96bfbf410ea83f0b4697]
    Left Witness:  [8e4dcdfa0aedebee3748670da3bb085274ca1c5debb50ab58be31eb363ce8e99]
    Right Witness: [eb67dcbc2a7119684e4319eebd7fbad4348790645f80ac97cae1a77926ae54b7]
    Height: 0
    Ed25519 Secret Key:       [122fd081614ef00532f2e2b21707c4f10aae5bcb731706c54f20129a5fdb6652]
    Ed25519 Verification Key: [bc9d44d0a449dd4e2f9daeff6a78d3799e5d9e0a95f59205afa5f867ef6c532a]
```
- Sigma t = 1023:
```
Sigma 1:
    Verification Key: [6994d0b6af0078d628a761cf7267ca24a88de035bbfbeb5b8b0994a5dea6b064]
    Sigma: [dfaa9296bfb18e380323418afd3617a7dec72e012279580bb881f60ac0bec250e1a1496ee2dfe416473d2bf57e241d54cc6c06d436aba4f49f46c88beb651c0b]
    W[0]: [a7e27070128e81ed4e10248703942c7c9b7f625242d032cbebfce2554d5fb2f6]
    W[1]: [2be8202c9ddf88745ab76421c285a0acf4faa08895879f86ae533ace3989658f]
    W[2]: [98e139cd0711e6f051819450a63755baad896f9e18b6e74550bf45ca6850cf24]
    W[3]: [ff62250deeee182274f9363ce9fb98db8422e5fec38725669ec21184408d41cf]
    W[4]: [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
Sigma 2:
    Verification Key: [2f026619cbeaae67495c9d19fe87968cea787f8c05a0f3bdaf29ef15a6ba5912]
    Sigma: [b3dfc6afbeb0ae8760216c07f1c443988419e3faa70351e570136f16f2c62d4d627fd59e290ad364263e641b37932e1aee27fd9ad33a1387ea014b40029cc303]
    W[0]: [cd0d081e7069e0e2358ee27a7fd8ea66e5c7f4491f8739dff262c7512f7e0ecb]
    W[1]: [622a2ca91be8ca7d4e0e279e2be235e429afede29ca98098679ffac7eb0445f2]
    W[2]: [0ca76e4b8f988d3a7248d87d980b30619f149e21499237eb124e2f26cd555bdc]
    W[3]: [a673c7c68e6039db024e6239f0ea34599406e8eb1461c24db3ceeec1de67cd31]
    W[4]: [a377f90858e4857f3bd162ac577de0d5438956c80ac86fd14fdf143dc806fe01]
R 2: [0985cbb9465146934cce2b8077e8120078ed73fb59777553e568baa7bb63ff05]
```
Product Composition Secret Key, t = 1023:
```
Tau 1:
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
    Right Witness: [d8347fa5647dd588273786c92fc50ea1adf16847ccb4cecb3c53c8eabd12895e]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [ff62250deeee182274f9363ce9fb98db8422e5fec38725669ec21184408d41cf]
    Right Witness: [3d099a7fa1e6ae0db7894dae705a1143918407ff8e522b6838f174e16be0c82d]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [98e139cd0711e6f051819450a63755baad896f9e18b6e74550bf45ca6850cf24]
    Right Witness: [cd380f1da673c5cd976780b0e8e1eaafe28e2800c7600a4ee2014c433edcc8f6]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [2be8202c9ddf88745ab76421c285a0acf4faa08895879f86ae533ace3989658f]
    Right Witness: [3f3c13270c9697b4b127f85035041dc7915bb1f116b3395fa4eaa4d1bc4dacf6]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a7e27070128e81ed4e10248703942c7c9b7f625242d032cbebfce2554d5fb2f6]
    Right Witness: [207a96afcc0d0442f73d8559276fd5c60a634066d4f0c8b98abc0e147de6d8c4]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [6994d0b6af0078d628a761cf7267ca24a88de035bbfbeb5b8b0994a5dea6b064]
Sigma 1:
    Verification Key: [6994d0b6af0078d628a761cf7267ca24a88de035bbfbeb5b8b0994a5dea6b064]
    Sigma: [dfaa9296bfb18e380323418afd3617a7dec72e012279580bb881f60ac0bec250e1a1496ee2dfe416473d2bf57e241d54cc6c06d436aba4f49f46c88beb651c0b]
    W[0]: [a7e27070128e81ed4e10248703942c7c9b7f625242d032cbebfce2554d5fb2f6]
    W[1]: [2be8202c9ddf88745ab76421c285a0acf4faa08895879f86ae533ace3989658f]
    W[2]: [98e139cd0711e6f051819450a63755baad896f9e18b6e74550bf45ca6850cf24]
    W[3]: [ff62250deeee182274f9363ce9fb98db8422e5fec38725669ec21184408d41cf]
    W[4]: [a9b4f437d58059e3b597fa89b95573b873ac545ec903e4d8cb970b48d0185751]
Seed:
    ef044cc0ff542358bea25dab4d6476c578055aa38724a16ae01ca6696dc46adc
Tau 2:
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a377f90858e4857f3bd162ac577de0d5438956c80ac86fd14fdf143dc806fe01]
    Right Witness: [bf32409d4e47013077d83326bcd9bd55caae45e14600ec973e76c1879ac7a7be]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a673c7c68e6039db024e6239f0ea34599406e8eb1461c24db3ceeec1de67cd31]
    Right Witness: [96097b1bd75211c3b85f0d9d56cea2396b174e0ecbc9a41e14fa07364feb920a]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [0ca76e4b8f988d3a7248d87d980b30619f149e21499237eb124e2f26cd555bdc]
    Right Witness: [c6e25e6f312eb44dbc639cca3a14c2b9823fc7229748f77192c9d5b3ddaddf88]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [622a2ca91be8ca7d4e0e279e2be235e429afede29ca98098679ffac7eb0445f2]
    Right Witness: [506393231aeb533bc53b519ac6d847d90e9becd2b253cfb3c466cf9ad529a3ef]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [cd0d081e7069e0e2358ee27a7fd8ea66e5c7f4491f8739dff262c7512f7e0ecb]
    Right Witness: [351ce10b84cd79d48534df9d85d3ae2ec180a42f76c72eb4d842e566f5d8be7d]
    Height: 0
    Ed25519 Secret Key:       [2add52095742166c4fa37d3277e2e645bdae76c5b8996ffda96c7f43ac578079]
    Ed25519 Verification Key: [2f026619cbeaae67495c9d19fe87968cea787f8c05a0f3bdaf29ef15a6ba5912]
```
## Test Vector - 8
### Description 
 Generate and verify a specified product composition signature at `t = [0, 1365, 2730, 4095]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
d47c163f7e7483cba6ec576958b4995778c41f7ad09f0ae3eb1aecaecf1c5fba
```
- h1 (int):

```6```

- h2 (int):

```6```

- Message (string):
```
"all the images my eyes have seen now memory?"
```
- Message (bytes) with `utf-8` encoding:
```
616c6c2074686520696d61676573206d7920657965732068617665207365656e206e6f77206d656d6f72793f
```
### Outputs
- Product Composition Verification Key:
```
8c779b9304f7369add28edd70f043b459d8d18572a31f424716339c4eb75db25
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 6
    Binary configuration: 0
    Right Seed:    [8d9b9d88f07211e2cd3a74f03117467b796560cea661b530e1e8f52d8e3c4f51]
    Left Witness:  [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
    Right Witness: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
    Height: 5
    Binary configuration: 0
    Right Seed:    [f60c4b80dc2abfd698bb1521ab73f4ec2904747bc396d0a3b8c347a4904297ba]
    Left Witness:  [edd8de6309cca307ccdc4e91831068f544a72f9f64951d498a1f860a6598c0a6]
    Right Witness: [3be4ffcf122fbe1334044f39a4096f4eadf342b180b2b9d87baa42fd903ecc0f]
    Height: 4
    Binary configuration: 0
    Right Seed:    [17330c736aa4c2914348771025bffec5aaaad68f5d9753cd91f8b40fe75957bf]
    Left Witness:  [8a48fcdf6c5cdcb3106c460b4873265845637e5674d703bf434794f63a8b8f70]
    Right Witness: [650b2b74f2bff4e424a2053952c33c77a7d68a585ae8385640882769d18c67fb]
    Height: 3
    Binary configuration: 0
    Right Seed:    [dc1f09ad5276f16396ea183d4ded8efd8ed97011b48aae411ebb2241e8e17db7]
    Left Witness:  [e63dcd502ea0e65821e7564feba015f8f4b1e4a8059c9e561237cbf3876f5b1d]
    Right Witness: [28b16ecc4ebc4e8014ddd9b41a6f6ed9b27c14fa68db05ab37b45ebb653e1729]
    Height: 2
    Binary configuration: 0
    Right Seed:    [6e84a16d05d30daa4c61b93eca9cd5d6441c7a1e62eeadb4c29a9286ca82fc9f]
    Left Witness:  [3f41161e2c9ca3f54ace878dfeec0d6957f0dfaa6eb6280e7a550b0f3b6afc3f]
    Right Witness: [f2c0ea911bcff878be634437eb028f33a329e46e8423c7262ba8c94268fb537d]
    Height: 1
    Binary configuration: 0
    Right Seed:    [62d5c794f66ef6be68f957b37b851291c771d2743d6996e7bca012e6a23896cd]
    Left Witness:  [23d39cc3d69df0e6fefe2db0fff6d8309afd02639e660f8834560e9bed4db748]
    Right Witness: [6e247383a57e1d03a6bc58b57bbce483231aac16a9df9bb22846cec1cf52e673]
    Height: 0
    Ed25519 Secret Key:       [2369d05b6a63e207a9a2f6f28e0d8602e4e38274f1a84d35b2a3f5faf9843cf8]
    Ed25519 Verification Key: [10b414abf5b299bdb5a7245c8c3d21bb8ae96a6e64bbc74dc81ae509f91eb29e]
Sigma 1:
    Verification Key: [10b414abf5b299bdb5a7245c8c3d21bb8ae96a6e64bbc74dc81ae509f91eb29e]
    Sigma: [91ac27a9a4d67d8c15c2ff81f230d9b793830040d27f88a0c53bea398b8b68b62234af05a5cbc1e8c2ceafd285cf7d11b6acd87f6de7573fafa7871582cfe506]
    W[0]: [6e247383a57e1d03a6bc58b57bbce483231aac16a9df9bb22846cec1cf52e673]
    W[1]: [f2c0ea911bcff878be634437eb028f33a329e46e8423c7262ba8c94268fb537d]
    W[2]: [28b16ecc4ebc4e8014ddd9b41a6f6ed9b27c14fa68db05ab37b45ebb653e1729]
    W[3]: [650b2b74f2bff4e424a2053952c33c77a7d68a585ae8385640882769d18c67fb]
    W[4]: [3be4ffcf122fbe1334044f39a4096f4eadf342b180b2b9d87baa42fd903ecc0f]
    W[5]: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
Seed:
    f1f0be5c49bf2e4d71e4c5321da57baeb5053e8e9a7ad04a77b0b073d53df1e5
Tau 2:
    Height: 6
    Binary configuration: 0
    Right Seed:    [62c02b76925395c6d35a044b3580609b5a56e80c30210ef35d841a51530ca060]
    Left Witness:  [7c0e7be05078fad48e4d25415c4de44fe197c6d0c359ba1390f8b40d1e9a43ad]
    Right Witness: [dc6bc2cfec3875b21c8066a8df164116ca62d6b90adb7aeb15058e409a7808cc]
    Height: 5
    Binary configuration: 0
    Right Seed:    [60782f745d8c31c0d41b0283d764ca792c750856b35981cdff88faf8a8d27100]
    Left Witness:  [4f0e726fb09a0c648c443404e8cd018bbd4d238d2492c1baf8caf1f9f491862d]
    Right Witness: [e9ad9d3d7d13d96fc19e9cd5796d8d747d80785066378ef35ade85ee338fd819]
    Height: 4
    Binary configuration: 0
    Right Seed:    [d2ca09bd20f54fc1e95d334963fffc91956745c0d0166521c722cacc8f98d500]
    Left Witness:  [51db9946ae447ffada0da0ad637e9c8326e59a78a093373a47fc6db15b2f6a0c]
    Right Witness: [e50e5ef6267f1e3ae3c8cf9709b47e26eb1f96326861d6208c652202d481a138]
    Height: 3
    Binary configuration: 0
    Right Seed:    [95d0f745fc5b2d0f5c5034543a290ec501446a091c7553fe3f720ffad8b99657]
    Left Witness:  [89f938c144febe16f80fe81a4179ab21a335b9d01e2487ec6119bc47a8a837c7]
    Right Witness: [84351a1b24f02d814656eba0c45bb51f79bd6f880839da53818e1e22c9771fc0]
    Height: 2
    Binary configuration: 0
    Right Seed:    [eed6805dc2bb07115359cb1e210895dbef393d86687fde73187377ade117deef]
    Left Witness:  [fa9d0218595113f11cd168658c9eb2bb7791595e44114e08a544bab04f2f4b26]
    Right Witness: [c62186465eaa34145b6f3fb2264adc1dd93d3bdf932f329ded89dfe240fa4078]
    Height: 1
    Binary configuration: 0
    Right Seed:    [1f89b9cf60ea0feb278bf502bea041e3f16777f563ae634a002210c5bf5c9336]
    Left Witness:  [9acbefedf0c6175a90f2fce5a53a5a7f24c265c32cec286ec90d9e50d2d8797f]
    Right Witness: [af8c1cce5f742faf71840395d677bc23aaad6c334b169e639a086a44aeb26393]
    Height: 0
    Ed25519 Secret Key:       [c63d59f15f924c02c83c2a87f96ee39345ad04dc789dd2165e988f744c220a45]
    Ed25519 Verification Key: [c1d3d42cacf05dd6a0dd9f85bf2e82f51734ac31037f4625695b656bf45cb974]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [10b414abf5b299bdb5a7245c8c3d21bb8ae96a6e64bbc74dc81ae509f91eb29e]
    Sigma: [91ac27a9a4d67d8c15c2ff81f230d9b793830040d27f88a0c53bea398b8b68b62234af05a5cbc1e8c2ceafd285cf7d11b6acd87f6de7573fafa7871582cfe506]
    W[0]: [6e247383a57e1d03a6bc58b57bbce483231aac16a9df9bb22846cec1cf52e673]
    W[1]: [f2c0ea911bcff878be634437eb028f33a329e46e8423c7262ba8c94268fb537d]
    W[2]: [28b16ecc4ebc4e8014ddd9b41a6f6ed9b27c14fa68db05ab37b45ebb653e1729]
    W[3]: [650b2b74f2bff4e424a2053952c33c77a7d68a585ae8385640882769d18c67fb]
    W[4]: [3be4ffcf122fbe1334044f39a4096f4eadf342b180b2b9d87baa42fd903ecc0f]
    W[5]: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
Sigma 2:
    Verification Key: [c1d3d42cacf05dd6a0dd9f85bf2e82f51734ac31037f4625695b656bf45cb974]
    Sigma: [f5fa047743a7d1a09413b5dbfc936bbee5b7420fd70babdc95580c93dc14e5f22e3ee5c1c38483d94851acc6b0ce9c7ea022910a0a7b132d717994b6430c7b0e]
    W[0]: [af8c1cce5f742faf71840395d677bc23aaad6c334b169e639a086a44aeb26393]
    W[1]: [c62186465eaa34145b6f3fb2264adc1dd93d3bdf932f329ded89dfe240fa4078]
    W[2]: [84351a1b24f02d814656eba0c45bb51f79bd6f880839da53818e1e22c9771fc0]
    W[3]: [e50e5ef6267f1e3ae3c8cf9709b47e26eb1f96326861d6208c652202d481a138]
    W[4]: [e9ad9d3d7d13d96fc19e9cd5796d8d747d80785066378ef35ade85ee338fd819]
    W[5]: [dc6bc2cfec3875b21c8066a8df164116ca62d6b90adb7aeb15058e409a7808cc]
R 2: [6bd176397fe5a18adcf5e8cfaca6cc2f401e0565ec1eafcd73b726fbbceb39da]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 6
    Binary configuration: 0
    Right Seed:    [8d9b9d88f07211e2cd3a74f03117467b796560cea661b530e1e8f52d8e3c4f51]
    Left Witness:  [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
    Right Witness: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
    Height: 5
    Binary configuration: 0
    Right Seed:    [f60c4b80dc2abfd698bb1521ab73f4ec2904747bc396d0a3b8c347a4904297ba]
    Left Witness:  [edd8de6309cca307ccdc4e91831068f544a72f9f64951d498a1f860a6598c0a6]
    Right Witness: [3be4ffcf122fbe1334044f39a4096f4eadf342b180b2b9d87baa42fd903ecc0f]
    Height: 4
    Binary configuration: 0
    Right Seed:    [17330c736aa4c2914348771025bffec5aaaad68f5d9753cd91f8b40fe75957bf]
    Left Witness:  [8a48fcdf6c5cdcb3106c460b4873265845637e5674d703bf434794f63a8b8f70]
    Right Witness: [650b2b74f2bff4e424a2053952c33c77a7d68a585ae8385640882769d18c67fb]
    Height: 3
    Binary configuration: 0
    Right Seed:    [dc1f09ad5276f16396ea183d4ded8efd8ed97011b48aae411ebb2241e8e17db7]
    Left Witness:  [e63dcd502ea0e65821e7564feba015f8f4b1e4a8059c9e561237cbf3876f5b1d]
    Right Witness: [28b16ecc4ebc4e8014ddd9b41a6f6ed9b27c14fa68db05ab37b45ebb653e1729]
    Height: 2
    Binary configuration: 0
    Right Seed:    [6e84a16d05d30daa4c61b93eca9cd5d6441c7a1e62eeadb4c29a9286ca82fc9f]
    Left Witness:  [3f41161e2c9ca3f54ace878dfeec0d6957f0dfaa6eb6280e7a550b0f3b6afc3f]
    Right Witness: [f2c0ea911bcff878be634437eb028f33a329e46e8423c7262ba8c94268fb537d]
    Height: 1
    Binary configuration: 0
    Right Seed:    [62d5c794f66ef6be68f957b37b851291c771d2743d6996e7bca012e6a23896cd]
    Left Witness:  [23d39cc3d69df0e6fefe2db0fff6d8309afd02639e660f8834560e9bed4db748]
    Right Witness: [6e247383a57e1d03a6bc58b57bbce483231aac16a9df9bb22846cec1cf52e673]
    Height: 0
    Ed25519 Secret Key:       [2369d05b6a63e207a9a2f6f28e0d8602e4e38274f1a84d35b2a3f5faf9843cf8]
    Ed25519 Verification Key: [10b414abf5b299bdb5a7245c8c3d21bb8ae96a6e64bbc74dc81ae509f91eb29e]
Sigma 1:
    Verification Key: [10b414abf5b299bdb5a7245c8c3d21bb8ae96a6e64bbc74dc81ae509f91eb29e]
    Sigma: [91ac27a9a4d67d8c15c2ff81f230d9b793830040d27f88a0c53bea398b8b68b62234af05a5cbc1e8c2ceafd285cf7d11b6acd87f6de7573fafa7871582cfe506]
    W[0]: [6e247383a57e1d03a6bc58b57bbce483231aac16a9df9bb22846cec1cf52e673]
    W[1]: [f2c0ea911bcff878be634437eb028f33a329e46e8423c7262ba8c94268fb537d]
    W[2]: [28b16ecc4ebc4e8014ddd9b41a6f6ed9b27c14fa68db05ab37b45ebb653e1729]
    W[3]: [650b2b74f2bff4e424a2053952c33c77a7d68a585ae8385640882769d18c67fb]
    W[4]: [3be4ffcf122fbe1334044f39a4096f4eadf342b180b2b9d87baa42fd903ecc0f]
    W[5]: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
Seed:
    f1f0be5c49bf2e4d71e4c5321da57baeb5053e8e9a7ad04a77b0b073d53df1e5
Tau 2:
    Height: 6
    Binary configuration: 0
    Right Seed:    [62c02b76925395c6d35a044b3580609b5a56e80c30210ef35d841a51530ca060]
    Left Witness:  [7c0e7be05078fad48e4d25415c4de44fe197c6d0c359ba1390f8b40d1e9a43ad]
    Right Witness: [dc6bc2cfec3875b21c8066a8df164116ca62d6b90adb7aeb15058e409a7808cc]
    Height: 5
    Binary configuration: 0
    Right Seed:    [60782f745d8c31c0d41b0283d764ca792c750856b35981cdff88faf8a8d27100]
    Left Witness:  [4f0e726fb09a0c648c443404e8cd018bbd4d238d2492c1baf8caf1f9f491862d]
    Right Witness: [e9ad9d3d7d13d96fc19e9cd5796d8d747d80785066378ef35ade85ee338fd819]
    Height: 4
    Binary configuration: 0
    Right Seed:    [d2ca09bd20f54fc1e95d334963fffc91956745c0d0166521c722cacc8f98d500]
    Left Witness:  [51db9946ae447ffada0da0ad637e9c8326e59a78a093373a47fc6db15b2f6a0c]
    Right Witness: [e50e5ef6267f1e3ae3c8cf9709b47e26eb1f96326861d6208c652202d481a138]
    Height: 3
    Binary configuration: 0
    Right Seed:    [95d0f745fc5b2d0f5c5034543a290ec501446a091c7553fe3f720ffad8b99657]
    Left Witness:  [89f938c144febe16f80fe81a4179ab21a335b9d01e2487ec6119bc47a8a837c7]
    Right Witness: [84351a1b24f02d814656eba0c45bb51f79bd6f880839da53818e1e22c9771fc0]
    Height: 2
    Binary configuration: 0
    Right Seed:    [eed6805dc2bb07115359cb1e210895dbef393d86687fde73187377ade117deef]
    Left Witness:  [fa9d0218595113f11cd168658c9eb2bb7791595e44114e08a544bab04f2f4b26]
    Right Witness: [c62186465eaa34145b6f3fb2264adc1dd93d3bdf932f329ded89dfe240fa4078]
    Height: 1
    Binary configuration: 0
    Right Seed:    [1f89b9cf60ea0feb278bf502bea041e3f16777f563ae634a002210c5bf5c9336]
    Left Witness:  [9acbefedf0c6175a90f2fce5a53a5a7f24c265c32cec286ec90d9e50d2d8797f]
    Right Witness: [af8c1cce5f742faf71840395d677bc23aaad6c334b169e639a086a44aeb26393]
    Height: 0
    Ed25519 Secret Key:       [c63d59f15f924c02c83c2a87f96ee39345ad04dc789dd2165e988f744c220a45]
    Ed25519 Verification Key: [c1d3d42cacf05dd6a0dd9f85bf2e82f51734ac31037f4625695b656bf45cb974]
```
- Sigma t = 1365:
```
Sigma 1:
    Verification Key: [192688ecc0a75284b82f953ba4a22900da69c7fba7b9899a3fc393c165a6b50b]
    Sigma: [8a1184eb0ea77cfa7200740322335452e7d1426753c2e80a05204558f51b9e2bf858af8b45eb00a365f69221e58a49305b00b9f7fdd29ee2f9f75beea024b50e]
    W[0]: [b8a4991f2541152e37df64a111ec5105042874674033c101892a30b8fa42085f]
    W[1]: [f8aa4440d95d91bbaacefb3008cbbc82419ccf6b40d46c3795883df8863f67a7]
    W[2]: [cc472d54fd940aec897a0e50633fbc72a65f531567eb3a6b9bad3cc9f8825cc5]
    W[3]: [18a0306e49a2932c93fb93222049e10c758b0c08008f2df2b6b9403493f64a06]
    W[4]: [edd8de6309cca307ccdc4e91831068f544a72f9f64951d498a1f860a6598c0a6]
    W[5]: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
Sigma 2:
    Verification Key: [1acbce3f7b5e658fd98c154ad99ea20ea93c95919b7b0663ff8e11545fae7b21]
    Sigma: [15d92b5f18885f559f7f114c1a244f983504710b5601a1f8c665400673496e9f95660e004c2b41d043f1e8e9ea124c5eddf4871444703b768f5bca2e4ac2000e]
    W[0]: [ef9c715960b42b760da2b6ec3ca2698625c87d10a08cf46460abdfd74e3a8735]
    W[1]: [e5605f0d2421333e05251974bb5103e1afbbc1b5ffc7297bae11cfdee51f303d]
    W[2]: [1377d82552056f940972430d765a950ba22a72779b048a454091a84dd41d619a]
    W[3]: [71310f02730bacd2ae2c8f57000cdd6d05ae7c8f8bcfed350e0b476530ffe521]
    W[4]: [d142b1b047841a913f6393f0f589caa0f9f6e7ff006de1feb64f714486f2a85a]
    W[5]: [ed890eb5a788732266abb0a956a7478d66b1c51caf344936a9e03c69032f0ded]
R 2: [a869823714a9b5710e667c9a60331e3d6de047f08a7c704d9693b7039ac50feb]
```
Product Composition Secret Key, t = 1365:
```
Tau 1:
    Height: 6
    Binary configuration: 0
    Right Seed:    [8d9b9d88f07211e2cd3a74f03117467b796560cea661b530e1e8f52d8e3c4f51]
    Left Witness:  [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
    Right Witness: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [edd8de6309cca307ccdc4e91831068f544a72f9f64951d498a1f860a6598c0a6]
    Right Witness: [3be4ffcf122fbe1334044f39a4096f4eadf342b180b2b9d87baa42fd903ecc0f]
    Height: 4
    Binary configuration: 0
    Right Seed:    [6209a582c0ccd06e943be1a1d4b5fe8fd58555293a0465d4baebb68c0c00c6d9]
    Left Witness:  [f43db534c836f336969c6931d084158fa54d3f971f3df80d80c5ae7bf7b49f76]
    Right Witness: [18a0306e49a2932c93fb93222049e10c758b0c08008f2df2b6b9403493f64a06]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [cc472d54fd940aec897a0e50633fbc72a65f531567eb3a6b9bad3cc9f8825cc5]
    Right Witness: [7d10ef7cac40dbca562822a431cf26ea6089f0a83993afa51be6843e084cbe9b]
    Height: 2
    Binary configuration: 0
    Right Seed:    [36ebe11b6350890442fb2e3e55ca8615692425dcd50afd2b2477766f0ea3f9fb]
    Left Witness:  [e19a22b4b98ec5421dc4e9e60a225085e04d06cf82c1360fa01b7cf5635dd8bc]
    Right Witness: [f8aa4440d95d91bbaacefb3008cbbc82419ccf6b40d46c3795883df8863f67a7]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b8a4991f2541152e37df64a111ec5105042874674033c101892a30b8fa42085f]
    Right Witness: [4116eed422bf493e0ae13a2e70e29a93c8770dd8ef1e06e4ad1ef1d7e40fd4ea]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [192688ecc0a75284b82f953ba4a22900da69c7fba7b9899a3fc393c165a6b50b]
Sigma 1:
    Verification Key: [192688ecc0a75284b82f953ba4a22900da69c7fba7b9899a3fc393c165a6b50b]
    Sigma: [8a1184eb0ea77cfa7200740322335452e7d1426753c2e80a05204558f51b9e2bf858af8b45eb00a365f69221e58a49305b00b9f7fdd29ee2f9f75beea024b50e]
    W[0]: [b8a4991f2541152e37df64a111ec5105042874674033c101892a30b8fa42085f]
    W[1]: [f8aa4440d95d91bbaacefb3008cbbc82419ccf6b40d46c3795883df8863f67a7]
    W[2]: [cc472d54fd940aec897a0e50633fbc72a65f531567eb3a6b9bad3cc9f8825cc5]
    W[3]: [18a0306e49a2932c93fb93222049e10c758b0c08008f2df2b6b9403493f64a06]
    W[4]: [edd8de6309cca307ccdc4e91831068f544a72f9f64951d498a1f860a6598c0a6]
    W[5]: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
Seed:
    32095ddafb14e0ae65bb069d646b434ce39da2a663d5472c9f0ac2648be19253
Tau 2:
    Height: 6
    Binary configuration: 0
    Right Seed:    [1493e636bbc3932777b2fd6fecdb51d23302e1d6d994e6863ac50c2af9de3bff]
    Left Witness:  [3393d1949eb7208525c3c911ae5e7d588e4b50c7df5bac86ee664c4a092d9194]
    Right Witness: [ed890eb5a788732266abb0a956a7478d66b1c51caf344936a9e03c69032f0ded]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d142b1b047841a913f6393f0f589caa0f9f6e7ff006de1feb64f714486f2a85a]
    Right Witness: [bcf5ee6a4c540050a08da5e955f62fb539a813ff0ceff3bf24ff71bff60e7241]
    Height: 4
    Binary configuration: 0
    Right Seed:    [9149f24083f03f2caad97ea038e828013b5766f285bec3b0edfd5a639103e20f]
    Left Witness:  [38d47ca8817413434f24becb007db75bf6424e4124799024bc00e520affa1822]
    Right Witness: [71310f02730bacd2ae2c8f57000cdd6d05ae7c8f8bcfed350e0b476530ffe521]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [1377d82552056f940972430d765a950ba22a72779b048a454091a84dd41d619a]
    Right Witness: [68a045dbc71d06e3cd64e8a4ceb7e5623a1cf75bcb8df6288fa2dfbe4e80a9b9]
    Height: 2
    Binary configuration: 0
    Right Seed:    [9d18c6b96c228cb30a6f4e4e524adaa2274c93cfdb84240022a82c6ecdb8f210]
    Left Witness:  [a10d956fbcf2653894c49ca3b44a94138b3be1ae83dcf437b55e16f7bf14d464]
    Right Witness: [e5605f0d2421333e05251974bb5103e1afbbc1b5ffc7297bae11cfdee51f303d]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [ef9c715960b42b760da2b6ec3ca2698625c87d10a08cf46460abdfd74e3a8735]
    Right Witness: [3b1b835b0e57af17aa56b60c72f8c30ffecbba03c7b398b40c9a9d0803fbd4b3]
    Height: 0
    Ed25519 Secret Key:       [409cfdc9739e4ed2814774d0efe9e1217fafc3af98a280616b44640ee49fe469]
    Ed25519 Verification Key: [1acbce3f7b5e658fd98c154ad99ea20ea93c95919b7b0663ff8e11545fae7b21]
```
- Sigma t = 2730:
```
Sigma 1:
    Verification Key: [c29e539919d1fa7246e0a05da106b6f599e48fd4570d0d934a27a8df3d2d0d50]
    Sigma: [b54cedc8738a71038fd8b853fcf3ed42a283abef65ae7b0b278eb3130bacb8fe7730ce874227597cd4046037aa4fcd05f70c6dad433e259ff5141b4b2886f200]
    W[0]: [7db774d953ed17ee7300f8e1d6ae89d7dc415fa47ceecdb5f1f0ecb25fd2c817]
    W[1]: [5fa8eb5d3149c036be8ae75e1808b4bf5caf9af2033cc87e2fa63a1d0df5e745]
    W[2]: [4ebd22dc216c6a73537d08d2029202a3ac558c823b425ba1809b312aa2cddf13]
    W[3]: [265ad8b6e1bc1aa802f8012aec7fce5256bd85c08384994c00ef5c8384dabb41]
    W[4]: [b2dc47595139254d3bc84d61af3b1be28c8fff43f89e04811e54580327d2b5b8]
    W[5]: [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
Sigma 2:
    Verification Key: [c7f9fc5fc25721387b2908dacc457d72bb8620cee58458d18ed1dfbf2062fa26]
    Sigma: [222ae35337b6e6d3e3809d58e8d97456260b46789d2e5f1afe0ff5e8c8cfe40656f9af1f620c336fc56a0ccc8a4a68ba01a373557cdf10a4dc129ec5262ad907]
    W[0]: [e626cb6d5331515e18b7df0358b1fe73676c462e5a5cd0f0b0c267c9fd2bf354]
    W[1]: [90f418ac21994f1e8ce61aa838f9653d329f3214caa5f31435e7bc7b7920d945]
    W[2]: [d96fe3126f8faec1185366e0a78457a8bd7384c72c275d7b9c1fe007a068c5f6]
    W[3]: [34397e727b02bd6243291c555d3f10befcf0ebb2bbef1f5a66964b1756596031]
    W[4]: [74a5c6a60e60584433cf715a3a51fa3f2b0bd19e05bbaf2c18a7b89b89e0cba3]
    W[5]: [da846364528c0d88629b474827a4a94d34b0259ad600c255da904b234b94a13a]
R 2: [c90630c0f2ee0c92610f4730c18bdaa022e739ea0e51078565732c4bf00251dd]
```
Product Composition Secret Key, t = 2730:
```
Tau 1:
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
    Right Witness: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
    Height: 5
    Binary configuration: 0
    Right Seed:    [2285f076ef8eca7fb761af64145496624d012e1bf32bd3ca053dad4d4c79cfa2]
    Left Witness:  [be023d2e7086ae9fb96047316cbac5132515452be71247e0ca3f1b132a061295]
    Right Witness: [b2dc47595139254d3bc84d61af3b1be28c8fff43f89e04811e54580327d2b5b8]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [265ad8b6e1bc1aa802f8012aec7fce5256bd85c08384994c00ef5c8384dabb41]
    Right Witness: [01ec3824183d271f5b31475956352ae12ce90d42feced469bdfea843f59366c4]
    Height: 3
    Binary configuration: 0
    Right Seed:    [32cf0f98984d9a0887bd5d8a12548c21ef5a4c252e21db6f7da37b5e1d77b90b]
    Left Witness:  [c5a7b0a4a8391b721c8b2a342810bff418a040e06440fbc8d0d5a513d7bc1535]
    Right Witness: [4ebd22dc216c6a73537d08d2029202a3ac558c823b425ba1809b312aa2cddf13]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5fa8eb5d3149c036be8ae75e1808b4bf5caf9af2033cc87e2fa63a1d0df5e745]
    Right Witness: [bd70b053e824b0a6c23b74205f97fbb2b478e027615c800a49240f341687d424]
    Height: 1
    Binary configuration: 0
    Right Seed:    [2b52b813a5ae2256c8eaf0cc6dd06ac6e384065e742e214748518ea7a660018c]
    Left Witness:  [a145a981acebe6a089845f5317cbe4c42defd248bf4c3f80a36ac744c2bae862]
    Right Witness: [7db774d953ed17ee7300f8e1d6ae89d7dc415fa47ceecdb5f1f0ecb25fd2c817]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [c29e539919d1fa7246e0a05da106b6f599e48fd4570d0d934a27a8df3d2d0d50]
Sigma 1:
    Verification Key: [c29e539919d1fa7246e0a05da106b6f599e48fd4570d0d934a27a8df3d2d0d50]
    Sigma: [b54cedc8738a71038fd8b853fcf3ed42a283abef65ae7b0b278eb3130bacb8fe7730ce874227597cd4046037aa4fcd05f70c6dad433e259ff5141b4b2886f200]
    W[0]: [7db774d953ed17ee7300f8e1d6ae89d7dc415fa47ceecdb5f1f0ecb25fd2c817]
    W[1]: [5fa8eb5d3149c036be8ae75e1808b4bf5caf9af2033cc87e2fa63a1d0df5e745]
    W[2]: [4ebd22dc216c6a73537d08d2029202a3ac558c823b425ba1809b312aa2cddf13]
    W[3]: [265ad8b6e1bc1aa802f8012aec7fce5256bd85c08384994c00ef5c8384dabb41]
    W[4]: [b2dc47595139254d3bc84d61af3b1be28c8fff43f89e04811e54580327d2b5b8]
    W[5]: [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
Seed:
    0e3543505d77e2bb603253e00186490ac99e0b3c457ff81d221118b5d7292ba2
Tau 2:
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [da846364528c0d88629b474827a4a94d34b0259ad600c255da904b234b94a13a]
    Right Witness: [fa7373707e386af3d89230b84d70a136986eec779d1e00482e981f2230a24e6e]
    Height: 5
    Binary configuration: 0
    Right Seed:    [70cbaf2ec77a1881946a440f13a07b6aa8a0f4fa216068ebc84bdb46cae97341]
    Left Witness:  [248f6d05ea097221cc65edafedd99a63dff4c4878cc37e63106ed630ab08bdcb]
    Right Witness: [74a5c6a60e60584433cf715a3a51fa3f2b0bd19e05bbaf2c18a7b89b89e0cba3]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [34397e727b02bd6243291c555d3f10befcf0ebb2bbef1f5a66964b1756596031]
    Right Witness: [f5dd79cc8ca28ec27d7c442eeef4edd2f841b4b0b35f4fc7fecfb2666fc85c0f]
    Height: 3
    Binary configuration: 0
    Right Seed:    [358c3ef388002f17a726f1bfb592654e8b3ad0cd7fb12fab4476dd815bd060b6]
    Left Witness:  [2a575b70cb889bf6675ecaac90dd8a9de37d79f9735f82900fc8eaf897d13a96]
    Right Witness: [d96fe3126f8faec1185366e0a78457a8bd7384c72c275d7b9c1fe007a068c5f6]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [90f418ac21994f1e8ce61aa838f9653d329f3214caa5f31435e7bc7b7920d945]
    Right Witness: [bc6ad0d01d3907f4d91254d1ee3cee49898065bf6cf1f8e2ed331a35774ceb7a]
    Height: 1
    Binary configuration: 0
    Right Seed:    [eab684f9f392425b88ba166b2f7a5cfb76bd2e1f2b26503f40cb4e5d2660eb98]
    Left Witness:  [fd4b71f04b0f4223f0524608d7bbec06611473bf49dbf2e200ea81d1ddbec02c]
    Right Witness: [e626cb6d5331515e18b7df0358b1fe73676c462e5a5cd0f0b0c267c9fd2bf354]
    Height: 0
    Ed25519 Secret Key:       [3f83abccdef109186a2dfb7ee0b4136dd225cf325552431828a90c310731339e]
    Ed25519 Verification Key: [c7f9fc5fc25721387b2908dacc457d72bb8620cee58458d18ed1dfbf2062fa26]
```
- Sigma t = 4095:
```
Sigma 1:
    Verification Key: [e0281e4901d6aa02e41aa356bf5e41ff7bd46ff5685b49566ab4cf4cac693883]
    Sigma: [ff798c91017ef40b99335a62c2703f09bdc6de405054dd27a581f61e42938e8e7c003224a30bc532d47b4ec6e85acc9db97d0329f1e7b6949744bcb632eebc0b]
    W[0]: [9491e1708df043e259befe71acf477d03696cbd21192b51a980c258deb8d9e0c]
    W[1]: [72399c2e95fdc005fa1e3bacea7a19c2103802b24026da5922963b8d8da4b612]
    W[2]: [0e33f95fb6eef3e17736ef7cf2a3c4a06445d7843e6f68a3124de943ac527e2d]
    W[3]: [01fdcb0b11bf755a42310e7c8c78cfcf0c7cc8a74a091826dbcd335a37cd5977]
    W[4]: [be023d2e7086ae9fb96047316cbac5132515452be71247e0ca3f1b132a061295]
    W[5]: [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
Sigma 2:
    Verification Key: [042454dc7a822ae1695f23f5c4c6e783f6900130b7a3b2f718be86be0c24ebf8]
    Sigma: [c6a6ee2ea9d7b377a13d3e036e1ee766c12151beed413959c944a483c1244a0494674c33eff19259a218028cc49276be86b4807efd1072c513ea5b5ee8276c08]
    W[0]: [97aca62d2f9116bd0220918eb5711a84378a1fead3f9c94994152f4ed8275df2]
    W[1]: [d103abd5ce21e284bc1e0bee5997c97880d445b501b1400c7f776533d586a6a9]
    W[2]: [cd64bda31432ccf0b8698b058a023640ee9142429cc5736fd409f43b45753a12]
    W[3]: [532c5d8185c1afa1beb8e063a1fab65ffc26f71a78dad3847a6331d3bbe48dc8]
    W[4]: [bb7129523d2105046f700bbdad4ffeded6e77e5b80af6849538dc307a5b9c8d2]
    W[5]: [ac68c5c1455477351dd4cea62d217e8ee1a203b5a1b087f5c6b9af5d36498252]
R 2: [038c0d22e71d7c98d7fa09fd6289f7b92f3d0cd85ef439a527d932adb56ff2b2]
```
Product Composition Secret Key, t = 4095:
```
Tau 1:
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
    Right Witness: [e14a55f6822fa84bbaa21760fc32f04b64cfca286a2fa7f463f84670380d1f6a]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [be023d2e7086ae9fb96047316cbac5132515452be71247e0ca3f1b132a061295]
    Right Witness: [b2dc47595139254d3bc84d61af3b1be28c8fff43f89e04811e54580327d2b5b8]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [01fdcb0b11bf755a42310e7c8c78cfcf0c7cc8a74a091826dbcd335a37cd5977]
    Right Witness: [6f5ef8869a741e0b1adf164c848d935df98d692c1d22b0a0ee7c7d23593b18ad]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [0e33f95fb6eef3e17736ef7cf2a3c4a06445d7843e6f68a3124de943ac527e2d]
    Right Witness: [95355efe1988b08120a5d3dedbb7857fc6f15cb8a0b1eef1550ee56d10d99cc4]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [72399c2e95fdc005fa1e3bacea7a19c2103802b24026da5922963b8d8da4b612]
    Right Witness: [80811b6319b040613ce1a0f864cd95db868ccb435e10117ae4c55548b907ec8f]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9491e1708df043e259befe71acf477d03696cbd21192b51a980c258deb8d9e0c]
    Right Witness: [2700feb9ee3bbc7e7fa1d688c7197bf9ae1b6f3bcc385533f7cc977bc0066389]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [e0281e4901d6aa02e41aa356bf5e41ff7bd46ff5685b49566ab4cf4cac693883]
Sigma 1:
    Verification Key: [e0281e4901d6aa02e41aa356bf5e41ff7bd46ff5685b49566ab4cf4cac693883]
    Sigma: [ff798c91017ef40b99335a62c2703f09bdc6de405054dd27a581f61e42938e8e7c003224a30bc532d47b4ec6e85acc9db97d0329f1e7b6949744bcb632eebc0b]
    W[0]: [9491e1708df043e259befe71acf477d03696cbd21192b51a980c258deb8d9e0c]
    W[1]: [72399c2e95fdc005fa1e3bacea7a19c2103802b24026da5922963b8d8da4b612]
    W[2]: [0e33f95fb6eef3e17736ef7cf2a3c4a06445d7843e6f68a3124de943ac527e2d]
    W[3]: [01fdcb0b11bf755a42310e7c8c78cfcf0c7cc8a74a091826dbcd335a37cd5977]
    W[4]: [be023d2e7086ae9fb96047316cbac5132515452be71247e0ca3f1b132a061295]
    W[5]: [9e1f7077955f72583ffe6329b18ab40a2fe34d2bb75cd3c9b2f97cde10f793f6]
Seed:
    15c4fcbeafe2f6df1d2fefaafe85d6af8f1b051278da3bc122c452bed34817e7
Tau 2:
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [ac68c5c1455477351dd4cea62d217e8ee1a203b5a1b087f5c6b9af5d36498252]
    Right Witness: [676f015960d13be3de0bc753962cc2d3c1b5d047a7fc94f747bace5efe963d41]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [bb7129523d2105046f700bbdad4ffeded6e77e5b80af6849538dc307a5b9c8d2]
    Right Witness: [37e639c12c291ea4179065117e509b6b5002d980ae032db640fb508885d717ac]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [532c5d8185c1afa1beb8e063a1fab65ffc26f71a78dad3847a6331d3bbe48dc8]
    Right Witness: [4992bcd524718e6685064780d61e2126a55f2e621ddcfb6b994d4bbd982bfe60]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [cd64bda31432ccf0b8698b058a023640ee9142429cc5736fd409f43b45753a12]
    Right Witness: [9e671350315ffb07bd7627f5d4c0cbf74ce3e99bf5634e7c96dfdd08b84049ec]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d103abd5ce21e284bc1e0bee5997c97880d445b501b1400c7f776533d586a6a9]
    Right Witness: [ed8a3f0035a1d96047af522c2d553bb53c674adc3597fc0f3c9e1b542b169685]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [97aca62d2f9116bd0220918eb5711a84378a1fead3f9c94994152f4ed8275df2]
    Right Witness: [0b037dc5a49936a797066bb7a3b8215ea3829036bddbcc2ec746a845ab3acf65]
    Height: 0
    Ed25519 Secret Key:       [934359c2b03cc8f98d09598974a46ec4e1b0b46c0d351b3e7d30900a24cd031c]
    Ed25519 Verification Key: [042454dc7a822ae1695f23f5c4c6e783f6900130b7a3b2f718be86be0c24ebf8]
```
## Test Vector - 9
### Description 
 Generate and verify a specified product composition signature at `t = [0, 5461, 10922, 16383]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
195624a047d662cb2062da152f2d55ba7b05a3747589ec4358ab8d0a328d4cb2
```
- h1 (int):

```7```

- h2 (int):

```7```

- Message (string):
```
"limited potential so must rely on hope or help"
```
- Message (bytes) with `utf-8` encoding:
```
6c696d6974656420706f74656e7469616c20736f206d7573742072656c79206f6e20686f7065206f722068656c70
```
### Outputs
- Product Composition Verification Key:
```
6255bc97b2a83d393cbb1b3449e8b7fb5b1d7a3852665291a51362c5d16a1b9f
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 7
    Binary configuration: 0
    Right Seed:    [ca7a1adcd560cd2cdb8f831522664b43aa8f53d73da688fde85d5a7fb2cff6f2]
    Left Witness:  [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
    Right Witness: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
    Height: 6
    Binary configuration: 0
    Right Seed:    [3010a020b74700532c1b705a583134049c7ce034fc1258f538462e3e014bbfbf]
    Left Witness:  [8d216e159cabb2eaeaacc1a1f8674f1cdf30415529ab6fcad8e1c2c5ac7425ed]
    Right Witness: [f66246868676907ba3d33c227e6a257f14c0d37c58002ad17c55f6adb3b3e619]
    Height: 5
    Binary configuration: 0
    Right Seed:    [4cc6e19900506903385a2e9c7f0332b65290d8d35c71e7e3f3e594c5e8180cb8]
    Left Witness:  [95f0d6c79ec7eea4158ebe2b7a1fd29d10ef3cbf008ca335b46e6633c873cf5d]
    Right Witness: [df0011083b767f16ab106627272ea164c53192ea0601b099193a75271ec3f99c]
    Height: 4
    Binary configuration: 0
    Right Seed:    [8290b120cf001faf3392b92a7c12293ed2681825214b6e96f9adee17ac5ca9d2]
    Left Witness:  [2fe6371a035f06b51e52049721c4a54e26dd1d957183947030c10d35fc53a7c0]
    Right Witness: [f40126a06c28e33e3f0d565ba9eee23e124df11b56d69379b2b85d2625e1216e]
    Height: 3
    Binary configuration: 0
    Right Seed:    [2d3dfe9c0600c52d1e183bcadd38553bddf69f26e13dbfaab7b5df238fa21600]
    Left Witness:  [cb47cbee8d4136281e08170475a57a4018650a43008856babd650447fd7b2c45]
    Right Witness: [bbbe1598a1972d16bc91d7851b821a3895fb221978461fdc741b487f4efc10dc]
    Height: 2
    Binary configuration: 0
    Right Seed:    [41f0d2e62f72f614e9aeee1a541b031cb7bf3c4bfe1bd8f2176363ddad655a5b]
    Left Witness:  [3bc50538f55e790a38843554885cfca344cdf64b66013cec30408c82f9bf1c36]
    Right Witness: [006b5f2ae244ec96ae0ba16f35cd68b43cb214e5fb1f02a3511ef7371391cb71]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f97b01fc5bad6ecb26e7a766c5383a71415b5f87d5f8bb5d84b6fa07415f2c70]
    Left Witness:  [0d58039ccc0791a84fad8a46a8d3621d1018e09250292d1a5d7b8cb4640c5de2]
    Right Witness: [2153d48b54de22a6e4f5d33ad9ee58ae24ed7325124e7f753db6d94a49b5ba21]
    Height: 0
    Ed25519 Secret Key:       [62100e3399324cf5bda1158ae7b9b8b5e61fdaf2160b0905d3026b5dc50fe6f4]
    Ed25519 Verification Key: [53a3d50b722ba1b3998f31a0537955ddf797532d8c188a8d89c305b122b96eb8]
Sigma 1:
    Verification Key: [53a3d50b722ba1b3998f31a0537955ddf797532d8c188a8d89c305b122b96eb8]
    Sigma: [56f6509b372b27cfdfa391cb35f9830f93236106e7fc44c3a6438949e6780491c7d90db50f4a43ad9f81194342a13d57817fc79df0ed79e1925ba409ff5c8501]
    W[0]: [2153d48b54de22a6e4f5d33ad9ee58ae24ed7325124e7f753db6d94a49b5ba21]
    W[1]: [006b5f2ae244ec96ae0ba16f35cd68b43cb214e5fb1f02a3511ef7371391cb71]
    W[2]: [bbbe1598a1972d16bc91d7851b821a3895fb221978461fdc741b487f4efc10dc]
    W[3]: [f40126a06c28e33e3f0d565ba9eee23e124df11b56d69379b2b85d2625e1216e]
    W[4]: [df0011083b767f16ab106627272ea164c53192ea0601b099193a75271ec3f99c]
    W[5]: [f66246868676907ba3d33c227e6a257f14c0d37c58002ad17c55f6adb3b3e619]
    W[6]: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
Seed:
    dd9519bbe9ce95b5356ba241720513165983d296c05d77d21e59ff3f8b353ddc
Tau 2:
    Height: 7
    Binary configuration: 0
    Right Seed:    [71725e6fc70005e30f19a1c08dfb6747cf580befce433311e42560c676178635]
    Left Witness:  [f93b88991f3d045c1917d71e00d529ec2ab330a482551c4154453d87bd3630bc]
    Right Witness: [74d32cae321da85df9faf9391012af4e2fa29dd075c253f758fea7bba13acab5]
    Height: 6
    Binary configuration: 0
    Right Seed:    [6809e546368c3d5aff7fd9e9c00443c1ce093690d86e228191d969f26868a6ed]
    Left Witness:  [dc390c83ca2d16205efac0b729f6d6c4ef7ddb1d2d84dbdfd99547abb5eeeea0]
    Right Witness: [d62837424cb912e84038db1a5c9f1cf3d2cab31b7544e876f31a2463380a3fd7]
    Height: 5
    Binary configuration: 0
    Right Seed:    [cf4f125a6ba829e65fadaff7805c594b1ad6715fc9bbc32c5d30685727b7e219]
    Left Witness:  [0b95a7226c4dafeb19797462803d5833490c7c223631604da383536b7c82f760]
    Right Witness: [deb6571bc85ec1bbe787c0eafe128b8c873d485498b91b94f3aff1efb0fd07d8]
    Height: 4
    Binary configuration: 0
    Right Seed:    [ff495b30f519aeadf66e7931fd4502e0089aa8923e8eec3768067399fec1eb8d]
    Left Witness:  [a8e30aa1dbf8cd61078c6b439e291f72c1798f17a1b85d11745817ee1f18d129]
    Right Witness: [0554b151fe4c78c5b7685b1c3ad6f2d9468b4140098259a9a4be90005a12959f]
    Height: 3
    Binary configuration: 0
    Right Seed:    [b678e01635540484e928d00c3df4321991c817a3eade59b4e455683fd79bdd32]
    Left Witness:  [97d0bd57671bb958a1c0c9d3eab2d46fc0dc7946c4aea5c0e112e7a2314dbb88]
    Right Witness: [aed5a11fa4b74d9d7186cff9b890cb4b6eb657188a408599819ae9061188e476]
    Height: 2
    Binary configuration: 0
    Right Seed:    [74cc6f56b90f9e09b9c2ab321cd609cd1247503c65b4cd58bfc9a7ca006c0632]
    Left Witness:  [0f4ff32c95874769c2df205c27ca334890c3e2c3194ea9201bab2a82d184ada0]
    Right Witness: [572be45ec5ff0120208501f546a7bd28c0b337320b7efd21909b29d8e8601462]
    Height: 1
    Binary configuration: 0
    Right Seed:    [3e90a8166b062b25b6e9cec0a113e4aad54c659431eed3775d0f9ff51647877c]
    Left Witness:  [591dcbd428450970f7b3cf54bef17cfb9c1c074368f2d6b194a1bad375bf2dbf]
    Right Witness: [f37d634baa3ef69a201e738f4122dbffba204377b7d741f626ad4d6b0d1fa7fd]
    Height: 0
    Ed25519 Secret Key:       [196ef5c43c9bf562e76769c5f960ed3fc2bafd26026b7641b1bcc430d245c6d3]
    Ed25519 Verification Key: [6d26853298744f6e97bae7e44b9fe990a1fcf275105a8fdba5a87f3640463054]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [53a3d50b722ba1b3998f31a0537955ddf797532d8c188a8d89c305b122b96eb8]
    Sigma: [56f6509b372b27cfdfa391cb35f9830f93236106e7fc44c3a6438949e6780491c7d90db50f4a43ad9f81194342a13d57817fc79df0ed79e1925ba409ff5c8501]
    W[0]: [2153d48b54de22a6e4f5d33ad9ee58ae24ed7325124e7f753db6d94a49b5ba21]
    W[1]: [006b5f2ae244ec96ae0ba16f35cd68b43cb214e5fb1f02a3511ef7371391cb71]
    W[2]: [bbbe1598a1972d16bc91d7851b821a3895fb221978461fdc741b487f4efc10dc]
    W[3]: [f40126a06c28e33e3f0d565ba9eee23e124df11b56d69379b2b85d2625e1216e]
    W[4]: [df0011083b767f16ab106627272ea164c53192ea0601b099193a75271ec3f99c]
    W[5]: [f66246868676907ba3d33c227e6a257f14c0d37c58002ad17c55f6adb3b3e619]
    W[6]: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
Sigma 2:
    Verification Key: [6d26853298744f6e97bae7e44b9fe990a1fcf275105a8fdba5a87f3640463054]
    Sigma: [040b0714ee981afc579aaea439cb655d3b5b1953b83b8503d11bbee9d6b3a55e655c41f316ef55c960c1b54aa2964ec59f66489b98c1039af2beb704b538b30b]
    W[0]: [f37d634baa3ef69a201e738f4122dbffba204377b7d741f626ad4d6b0d1fa7fd]
    W[1]: [572be45ec5ff0120208501f546a7bd28c0b337320b7efd21909b29d8e8601462]
    W[2]: [aed5a11fa4b74d9d7186cff9b890cb4b6eb657188a408599819ae9061188e476]
    W[3]: [0554b151fe4c78c5b7685b1c3ad6f2d9468b4140098259a9a4be90005a12959f]
    W[4]: [deb6571bc85ec1bbe787c0eafe128b8c873d485498b91b94f3aff1efb0fd07d8]
    W[5]: [d62837424cb912e84038db1a5c9f1cf3d2cab31b7544e876f31a2463380a3fd7]
    W[6]: [74d32cae321da85df9faf9391012af4e2fa29dd075c253f758fea7bba13acab5]
R 2: [dcccb8163221966dbd5cc9522281a1121cefb83f2670561b7632a031c2317056]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 7
    Binary configuration: 0
    Right Seed:    [ca7a1adcd560cd2cdb8f831522664b43aa8f53d73da688fde85d5a7fb2cff6f2]
    Left Witness:  [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
    Right Witness: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
    Height: 6
    Binary configuration: 0
    Right Seed:    [3010a020b74700532c1b705a583134049c7ce034fc1258f538462e3e014bbfbf]
    Left Witness:  [8d216e159cabb2eaeaacc1a1f8674f1cdf30415529ab6fcad8e1c2c5ac7425ed]
    Right Witness: [f66246868676907ba3d33c227e6a257f14c0d37c58002ad17c55f6adb3b3e619]
    Height: 5
    Binary configuration: 0
    Right Seed:    [4cc6e19900506903385a2e9c7f0332b65290d8d35c71e7e3f3e594c5e8180cb8]
    Left Witness:  [95f0d6c79ec7eea4158ebe2b7a1fd29d10ef3cbf008ca335b46e6633c873cf5d]
    Right Witness: [df0011083b767f16ab106627272ea164c53192ea0601b099193a75271ec3f99c]
    Height: 4
    Binary configuration: 0
    Right Seed:    [8290b120cf001faf3392b92a7c12293ed2681825214b6e96f9adee17ac5ca9d2]
    Left Witness:  [2fe6371a035f06b51e52049721c4a54e26dd1d957183947030c10d35fc53a7c0]
    Right Witness: [f40126a06c28e33e3f0d565ba9eee23e124df11b56d69379b2b85d2625e1216e]
    Height: 3
    Binary configuration: 0
    Right Seed:    [2d3dfe9c0600c52d1e183bcadd38553bddf69f26e13dbfaab7b5df238fa21600]
    Left Witness:  [cb47cbee8d4136281e08170475a57a4018650a43008856babd650447fd7b2c45]
    Right Witness: [bbbe1598a1972d16bc91d7851b821a3895fb221978461fdc741b487f4efc10dc]
    Height: 2
    Binary configuration: 0
    Right Seed:    [41f0d2e62f72f614e9aeee1a541b031cb7bf3c4bfe1bd8f2176363ddad655a5b]
    Left Witness:  [3bc50538f55e790a38843554885cfca344cdf64b66013cec30408c82f9bf1c36]
    Right Witness: [006b5f2ae244ec96ae0ba16f35cd68b43cb214e5fb1f02a3511ef7371391cb71]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f97b01fc5bad6ecb26e7a766c5383a71415b5f87d5f8bb5d84b6fa07415f2c70]
    Left Witness:  [0d58039ccc0791a84fad8a46a8d3621d1018e09250292d1a5d7b8cb4640c5de2]
    Right Witness: [2153d48b54de22a6e4f5d33ad9ee58ae24ed7325124e7f753db6d94a49b5ba21]
    Height: 0
    Ed25519 Secret Key:       [62100e3399324cf5bda1158ae7b9b8b5e61fdaf2160b0905d3026b5dc50fe6f4]
    Ed25519 Verification Key: [53a3d50b722ba1b3998f31a0537955ddf797532d8c188a8d89c305b122b96eb8]
Sigma 1:
    Verification Key: [53a3d50b722ba1b3998f31a0537955ddf797532d8c188a8d89c305b122b96eb8]
    Sigma: [56f6509b372b27cfdfa391cb35f9830f93236106e7fc44c3a6438949e6780491c7d90db50f4a43ad9f81194342a13d57817fc79df0ed79e1925ba409ff5c8501]
    W[0]: [2153d48b54de22a6e4f5d33ad9ee58ae24ed7325124e7f753db6d94a49b5ba21]
    W[1]: [006b5f2ae244ec96ae0ba16f35cd68b43cb214e5fb1f02a3511ef7371391cb71]
    W[2]: [bbbe1598a1972d16bc91d7851b821a3895fb221978461fdc741b487f4efc10dc]
    W[3]: [f40126a06c28e33e3f0d565ba9eee23e124df11b56d69379b2b85d2625e1216e]
    W[4]: [df0011083b767f16ab106627272ea164c53192ea0601b099193a75271ec3f99c]
    W[5]: [f66246868676907ba3d33c227e6a257f14c0d37c58002ad17c55f6adb3b3e619]
    W[6]: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
Seed:
    dd9519bbe9ce95b5356ba241720513165983d296c05d77d21e59ff3f8b353ddc
Tau 2:
    Height: 7
    Binary configuration: 0
    Right Seed:    [71725e6fc70005e30f19a1c08dfb6747cf580befce433311e42560c676178635]
    Left Witness:  [f93b88991f3d045c1917d71e00d529ec2ab330a482551c4154453d87bd3630bc]
    Right Witness: [74d32cae321da85df9faf9391012af4e2fa29dd075c253f758fea7bba13acab5]
    Height: 6
    Binary configuration: 0
    Right Seed:    [6809e546368c3d5aff7fd9e9c00443c1ce093690d86e228191d969f26868a6ed]
    Left Witness:  [dc390c83ca2d16205efac0b729f6d6c4ef7ddb1d2d84dbdfd99547abb5eeeea0]
    Right Witness: [d62837424cb912e84038db1a5c9f1cf3d2cab31b7544e876f31a2463380a3fd7]
    Height: 5
    Binary configuration: 0
    Right Seed:    [cf4f125a6ba829e65fadaff7805c594b1ad6715fc9bbc32c5d30685727b7e219]
    Left Witness:  [0b95a7226c4dafeb19797462803d5833490c7c223631604da383536b7c82f760]
    Right Witness: [deb6571bc85ec1bbe787c0eafe128b8c873d485498b91b94f3aff1efb0fd07d8]
    Height: 4
    Binary configuration: 0
    Right Seed:    [ff495b30f519aeadf66e7931fd4502e0089aa8923e8eec3768067399fec1eb8d]
    Left Witness:  [a8e30aa1dbf8cd61078c6b439e291f72c1798f17a1b85d11745817ee1f18d129]
    Right Witness: [0554b151fe4c78c5b7685b1c3ad6f2d9468b4140098259a9a4be90005a12959f]
    Height: 3
    Binary configuration: 0
    Right Seed:    [b678e01635540484e928d00c3df4321991c817a3eade59b4e455683fd79bdd32]
    Left Witness:  [97d0bd57671bb958a1c0c9d3eab2d46fc0dc7946c4aea5c0e112e7a2314dbb88]
    Right Witness: [aed5a11fa4b74d9d7186cff9b890cb4b6eb657188a408599819ae9061188e476]
    Height: 2
    Binary configuration: 0
    Right Seed:    [74cc6f56b90f9e09b9c2ab321cd609cd1247503c65b4cd58bfc9a7ca006c0632]
    Left Witness:  [0f4ff32c95874769c2df205c27ca334890c3e2c3194ea9201bab2a82d184ada0]
    Right Witness: [572be45ec5ff0120208501f546a7bd28c0b337320b7efd21909b29d8e8601462]
    Height: 1
    Binary configuration: 0
    Right Seed:    [3e90a8166b062b25b6e9cec0a113e4aad54c659431eed3775d0f9ff51647877c]
    Left Witness:  [591dcbd428450970f7b3cf54bef17cfb9c1c074368f2d6b194a1bad375bf2dbf]
    Right Witness: [f37d634baa3ef69a201e738f4122dbffba204377b7d741f626ad4d6b0d1fa7fd]
    Height: 0
    Ed25519 Secret Key:       [196ef5c43c9bf562e76769c5f960ed3fc2bafd26026b7641b1bcc430d245c6d3]
    Ed25519 Verification Key: [6d26853298744f6e97bae7e44b9fe990a1fcf275105a8fdba5a87f3640463054]
```
- Sigma t = 5461:
```
Sigma 1:
    Verification Key: [015d1f02cdd55e0b1e2e6aac5f0def162b2a906d1c0cc376abecf5218ca6af2b]
    Sigma: [8ade652751b62f28f3caf203fb90e39be750263cdd41c2417baf0827ac164565194ea5511a26dad8998a97dbaf34c6140cda3c68e5bfb2a940fe53504e62f50b]
    W[0]: [0f88e9f992b0e7f5548ba1fc97f64af1ae43fa35563cfa32ec1d473cf5767e03]
    W[1]: [0ea0b89b532f8b5708873f77d68d9669c74a3e0fef1619c3d80ac6e0bc91d2f5]
    W[2]: [233b1a4e6c6b0313cee3d7028592e4e8d903f62e12c24e598da8f60b7b631dc9]
    W[3]: [6e4937a0b6252163e6bae7db3b23f1c11c500ccf47a20c8efd4c9ad15ed46ac1]
    W[4]: [d0a6123ff60482926e1d6432478871f85818045ff7c27b4906d22a86e2a23696]
    W[5]: [8d216e159cabb2eaeaacc1a1f8674f1cdf30415529ab6fcad8e1c2c5ac7425ed]
    W[6]: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
Sigma 2:
    Verification Key: [90ba47f0e0c12b5f6b901ea8896f25175dca896bc7f42ba624a950957ca16563]
    Sigma: [c66f3df1a3123f09c5db8ecd2ae7be79fc0897ffa6983155346c0b19e494296171549a5956e919b203039dad688e49a4bbe228c91ec9c6c4601ae8670d570f0e]
    W[0]: [7bbc4228f3f24189b359ac2eb6d94e55776ad298ec2a9667e67e32d2e5ba60da]
    W[1]: [a47891fcb4fe0bf3ba44659db7378df4bcbc11c3b0cd7b380f5f659ccd1db8de]
    W[2]: [85c8a6887c3addc46f7d8d781237a869ab94f66c24997286973e4c31f2417cd8]
    W[3]: [613d81caa293cb5a0825922bbb992bf89fc6f96b73f200be17758deead7f0856]
    W[4]: [355cd18b84011203e93b87ee967a2de84ec8d422936c5dd8c77828987fbdad66]
    W[5]: [83e3b5b93e5843415ceae260abd661ddc9114bb1e2dd4c7466ce453bda35c62f]
    W[6]: [0ac3d0e0dfa2cc9d59cebd4f36042c8dfef8eaf59ecfffab3a8b54dcafa8d712]
R 2: [f1c5e2393bc5f50c23ca89ac3130afc2eb029e534bbd24a7c661b6849f2f43ac]
```
Product Composition Secret Key, t = 5461:
```
Tau 1:
    Height: 7
    Binary configuration: 0
    Right Seed:    [ca7a1adcd560cd2cdb8f831522664b43aa8f53d73da688fde85d5a7fb2cff6f2]
    Left Witness:  [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
    Right Witness: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [8d216e159cabb2eaeaacc1a1f8674f1cdf30415529ab6fcad8e1c2c5ac7425ed]
    Right Witness: [f66246868676907ba3d33c227e6a257f14c0d37c58002ad17c55f6adb3b3e619]
    Height: 5
    Binary configuration: 0
    Right Seed:    [eff26a83db9bd4e1be159e3f35e393e457e84d3e0bf8faeaed54d4f8a5ab8414]
    Left Witness:  [e4e33c2d99cf58709457134510bc5cef2ade72fa01a1752cc9735894304b0365]
    Right Witness: [d0a6123ff60482926e1d6432478871f85818045ff7c27b4906d22a86e2a23696]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [6e4937a0b6252163e6bae7db3b23f1c11c500ccf47a20c8efd4c9ad15ed46ac1]
    Right Witness: [b350f3b47c5a1a6b0977f55e0589ee9536d7aedb71ceb9903e3d178cfebc0bc8]
    Height: 3
    Binary configuration: 0
    Right Seed:    [976b4e8394e67b08eff2939d2c3c93664bdc5a722072c1ea42312396f81f0acf]
    Left Witness:  [cb0e03789dcb9fe28eefbcf5023b2f2fba0a563045a3101e39d25134f46b5b37]
    Right Witness: [233b1a4e6c6b0313cee3d7028592e4e8d903f62e12c24e598da8f60b7b631dc9]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [0ea0b89b532f8b5708873f77d68d9669c74a3e0fef1619c3d80ac6e0bc91d2f5]
    Right Witness: [853e8462136438d1b307a9d3188dd0a4198e9a991e539b3ecd41439a796d533c]
    Height: 1
    Binary configuration: 0
    Right Seed:    [6d490f91c43b131d16642c60060170c25f914924e099fea117d3ebb50be67cfd]
    Left Witness:  [cef1a62699aa61dce7935a3c08fd41eccb7b464507d8c9066e833e0f7b2c196f]
    Right Witness: [0f88e9f992b0e7f5548ba1fc97f64af1ae43fa35563cfa32ec1d473cf5767e03]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [015d1f02cdd55e0b1e2e6aac5f0def162b2a906d1c0cc376abecf5218ca6af2b]
Sigma 1:
    Verification Key: [015d1f02cdd55e0b1e2e6aac5f0def162b2a906d1c0cc376abecf5218ca6af2b]
    Sigma: [8ade652751b62f28f3caf203fb90e39be750263cdd41c2417baf0827ac164565194ea5511a26dad8998a97dbaf34c6140cda3c68e5bfb2a940fe53504e62f50b]
    W[0]: [0f88e9f992b0e7f5548ba1fc97f64af1ae43fa35563cfa32ec1d473cf5767e03]
    W[1]: [0ea0b89b532f8b5708873f77d68d9669c74a3e0fef1619c3d80ac6e0bc91d2f5]
    W[2]: [233b1a4e6c6b0313cee3d7028592e4e8d903f62e12c24e598da8f60b7b631dc9]
    W[3]: [6e4937a0b6252163e6bae7db3b23f1c11c500ccf47a20c8efd4c9ad15ed46ac1]
    W[4]: [d0a6123ff60482926e1d6432478871f85818045ff7c27b4906d22a86e2a23696]
    W[5]: [8d216e159cabb2eaeaacc1a1f8674f1cdf30415529ab6fcad8e1c2c5ac7425ed]
    W[6]: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
Seed:
    ba00502633c715bad6b8f47f0b6e9464825fcc4caeca7b485e09cdb0a7096f41
Tau 2:
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [0ac3d0e0dfa2cc9d59cebd4f36042c8dfef8eaf59ecfffab3a8b54dcafa8d712]
    Right Witness: [562cd1bd78113558f0f8adaace1f7f7785eb69a318d0be6be57396180d9674fc]
    Height: 6
    Binary configuration: 0
    Right Seed:    [c22adcec39fd56b427b8ce8d140e1a4bba88cb3f475bab34e8a8d51a57d36427]
    Left Witness:  [5823789f480c9590222582f340517194ef0b38eaedd35e967d1be47b160fdb31]
    Right Witness: [83e3b5b93e5843415ceae260abd661ddc9114bb1e2dd4c7466ce453bda35c62f]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [355cd18b84011203e93b87ee967a2de84ec8d422936c5dd8c77828987fbdad66]
    Right Witness: [6d00b8f534dcfdce53e1a9c640932e54c69e3122523df9681884e07e236abb1b]
    Height: 4
    Binary configuration: 0
    Right Seed:    [cd6dffbbeb697591a3dc9d8f4dc42691db7596ae8e3605af3f075f616e6f273d]
    Left Witness:  [8a49f84e56e21687691669494e88a308de86086c9bf4c140a4d8d61710f29435]
    Right Witness: [613d81caa293cb5a0825922bbb992bf89fc6f96b73f200be17758deead7f0856]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [85c8a6887c3addc46f7d8d781237a869ab94f66c24997286973e4c31f2417cd8]
    Right Witness: [1227ea6c8933ddd95f675042df471d04637cb0dfbfd465b3181fd7300fb59323]
    Height: 2
    Binary configuration: 0
    Right Seed:    [3480d2544c87ecbbadda5ba9eece4e13488d7a23b293282963b7d580c67a1cc3]
    Left Witness:  [e41ef81bd48464f0f1d487b16f88a37eb21196abbe6300d1e530b5082a6cd17a]
    Right Witness: [a47891fcb4fe0bf3ba44659db7378df4bcbc11c3b0cd7b380f5f659ccd1db8de]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7bbc4228f3f24189b359ac2eb6d94e55776ad298ec2a9667e67e32d2e5ba60da]
    Right Witness: [3bfd53e674350dab81ef9efb4a333dbd724af33d5e3f05bf9def34c7c8c538a2]
    Height: 0
    Ed25519 Secret Key:       [7bcce31e95db45d9a8356dc981aaebd7b20e89250eafa90ce8a8226ecd4723be]
    Ed25519 Verification Key: [90ba47f0e0c12b5f6b901ea8896f25175dca896bc7f42ba624a950957ca16563]
```
- Sigma t = 10922:
```
Sigma 1:
    Verification Key: [583a3594d9027163dcf6d6d4feb0b7e3b2348eb7d0829361bc66e8f3a3d67ce4]
    Sigma: [5830ea8c12e065a3498671fb9a4719cf708b81da73dc3fb4efc47da9783e394fae8d59078133f119efec1d56018b3659ab333b9b68e50f07aca806ef1926f302]
    W[0]: [5d774192390fc405f9ef3927b9cc87d858cef0837121f7ecbeb9194b8ae923b5]
    W[1]: [2162d1ffff4f2d3779838e3d1449c0a4b439e07f7a3f70be3d2963d6fc3fe874]
    W[2]: [d33296ba9340809a602a7b1f2ca6345910b36def3b8365cf5039971a5799a912]
    W[3]: [4b17b6766287f16da1373613cdfe15ec3022955c8653dcc5fbad4172d2125a94]
    W[4]: [5df192d039f8edd0671e2096417e631e72e81097749ea921e962462bdb48b281]
    W[5]: [099a303142ba2c4f6d47d2d48c69de96536f006269fc4f5769d45b99e8d7a7b1]
    W[6]: [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
Sigma 2:
    Verification Key: [bda6cd2ac0b1bd7c59b285d85ec718d9a63bf1ce0d2971f7bf9c4788c70deef4]
    Sigma: [8bc646b222b39df7ad8ef62a1e744d56b0a5c13925b0d8ba87df51d97d6da70fd13feca003a5013eabcaea851fd51decdde72f2181534b32909adbc754024204]
    W[0]: [84fad4e2b78ddc07d070e9fd2a0a3bf7bc9e7bc017179d432c193a49736ce35e]
    W[1]: [b118080d2d85d95189b9c089ed28f8e1e3866be787493439594b2266e9421596]
    W[2]: [e240f6d33dca2784f9fa12d6515bc61c7ac5961b258f64c92a58720337f7c5dd]
    W[3]: [e55876d683df031e779d30366d9a7d7c1091edef520da2c3fec8e7ab02cd1489]
    W[4]: [7da1fd10f6520dc902fc895cf115a35089a14c15907c2785cb52a5f1762e8493]
    W[5]: [9f122857ed5f1e0aa99b3c047c72d0af66ad4b2df7bdcb0a4e4589cd83c4ef79]
    W[6]: [fc773d69d90922273655d5c7aacf52e505e71e9268570a0b8f7d1d3fbfd698c5]
R 2: [a7ef3ba4baf7fdd662e8e60724c9106cec4e17edf36f3ee346ca9a14dbb5a02a]
```
Product Composition Secret Key, t = 10922:
```
Tau 1:
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
    Right Witness: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
    Height: 6
    Binary configuration: 0
    Right Seed:    [08213de8b92e8fcfc71186a26421ed24f241d01c7d5921d3f7ea5058edcfd376]
    Left Witness:  [105392d27affa14a019a4cee64d255ae4b43f3e42962e8afbf0a50b5e57cecd7]
    Right Witness: [099a303142ba2c4f6d47d2d48c69de96536f006269fc4f5769d45b99e8d7a7b1]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5df192d039f8edd0671e2096417e631e72e81097749ea921e962462bdb48b281]
    Right Witness: [ccabb9b369ac735a43e5eb4c639f4489a04f9dd628e2d6e74f720025f4a95215]
    Height: 4
    Binary configuration: 0
    Right Seed:    [cfe5c70dd40bcbfcece74e4e69c6f1fc6338483401c1deefdef163ed41eb9521]
    Left Witness:  [8781cc9ecdd704276230c8d903874c98495458cb7423d2cc34b3cabe17444bd9]
    Right Witness: [4b17b6766287f16da1373613cdfe15ec3022955c8653dcc5fbad4172d2125a94]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d33296ba9340809a602a7b1f2ca6345910b36def3b8365cf5039971a5799a912]
    Right Witness: [5b5d6d875f9956512ef112c7ee90bb715740fa5ff291fb499d51771655e98a40]
    Height: 2
    Binary configuration: 0
    Right Seed:    [1796609a247ec07f987785faf62f28023821f505dad48cf136389255b174ceb2]
    Left Witness:  [bb50bd7a76c3a832f1dd554c2cd022dfc15f52cca96080b935736082a4073458]
    Right Witness: [2162d1ffff4f2d3779838e3d1449c0a4b439e07f7a3f70be3d2963d6fc3fe874]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5d774192390fc405f9ef3927b9cc87d858cef0837121f7ecbeb9194b8ae923b5]
    Right Witness: [755c8a48ce17a83c5c3d9ba9d92b4eb931593508677d7d59e4b9a00f1f9e2d0c]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [583a3594d9027163dcf6d6d4feb0b7e3b2348eb7d0829361bc66e8f3a3d67ce4]
Sigma 1:
    Verification Key: [583a3594d9027163dcf6d6d4feb0b7e3b2348eb7d0829361bc66e8f3a3d67ce4]
    Sigma: [5830ea8c12e065a3498671fb9a4719cf708b81da73dc3fb4efc47da9783e394fae8d59078133f119efec1d56018b3659ab333b9b68e50f07aca806ef1926f302]
    W[0]: [5d774192390fc405f9ef3927b9cc87d858cef0837121f7ecbeb9194b8ae923b5]
    W[1]: [2162d1ffff4f2d3779838e3d1449c0a4b439e07f7a3f70be3d2963d6fc3fe874]
    W[2]: [d33296ba9340809a602a7b1f2ca6345910b36def3b8365cf5039971a5799a912]
    W[3]: [4b17b6766287f16da1373613cdfe15ec3022955c8653dcc5fbad4172d2125a94]
    W[4]: [5df192d039f8edd0671e2096417e631e72e81097749ea921e962462bdb48b281]
    W[5]: [099a303142ba2c4f6d47d2d48c69de96536f006269fc4f5769d45b99e8d7a7b1]
    W[6]: [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
Seed:
    3c22b634b7a03c01f3c99bbf59929de413089db4046c23f0fc7913339ad78755
Tau 2:
    Height: 7
    Binary configuration: 0
    Right Seed:    [8e6bb14b6b4b0854be597c00bd4029cdd00ae9fc6720d7a2f813b2f0f8d89206]
    Left Witness:  [dd88074d03739077e9b23e44af6c2b9564db1ef8975fce46ea2e1eedda6f86d6]
    Right Witness: [fc773d69d90922273655d5c7aacf52e505e71e9268570a0b8f7d1d3fbfd698c5]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9f122857ed5f1e0aa99b3c047c72d0af66ad4b2df7bdcb0a4e4589cd83c4ef79]
    Right Witness: [a6992c81bd0904eaa69ca8f3b62b8fab4adefa6277edd903a410112150cb9d59]
    Height: 5
    Binary configuration: 0
    Right Seed:    [2bff7a98cc465ee205735f1726214a72e21d9da3f64c04a174167b1bd7486be7]
    Left Witness:  [05df5007bba0cc971fbb700fd460c335b2dda8c7601173fa3c3dd28bfcd513ca]
    Right Witness: [7da1fd10f6520dc902fc895cf115a35089a14c15907c2785cb52a5f1762e8493]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [e55876d683df031e779d30366d9a7d7c1091edef520da2c3fec8e7ab02cd1489]
    Right Witness: [88af41f8c0c8a11b4d7cb9d4538808e4337efb96c54ea8e9040791c95c3d392f]
    Height: 3
    Binary configuration: 0
    Right Seed:    [a5fb2a37753af5f33efb72bd296c7fb33d1e5bfc0298fa5787913dcc909a1098]
    Left Witness:  [8a160d48c72ee0969b8108baed41eab7c688a30db362aab40b52324b8fffc448]
    Right Witness: [e240f6d33dca2784f9fa12d6515bc61c7ac5961b258f64c92a58720337f7c5dd]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b118080d2d85d95189b9c089ed28f8e1e3866be787493439594b2266e9421596]
    Right Witness: [68eb85d047fc2c611f906a4a8337eabd862ac9a2fd364680c2f060971c20df8c]
    Height: 1
    Binary configuration: 0
    Right Seed:    [bdb58353def4c75b5181d79fdf5f547aaa489bb1ee51518871d91a121edb8f8b]
    Left Witness:  [678cf836061d6644d3f7440f80c87d4ed58b1eb063a3e144b7381cdb0b834c62]
    Right Witness: [84fad4e2b78ddc07d070e9fd2a0a3bf7bc9e7bc017179d432c193a49736ce35e]
    Height: 0
    Ed25519 Secret Key:       [56b3e3289ab8ad7d9a5e4e961fa3d69db3ae2b8cafb02ff6694539115779dfec]
    Ed25519 Verification Key: [bda6cd2ac0b1bd7c59b285d85ec718d9a63bf1ce0d2971f7bf9c4788c70deef4]
```
- Sigma t = 16383:
```
Sigma 1:
    Verification Key: [be53ca809f14a98d15462ef91a0949f2644a6518e025d72177a653676c9d47c2]
    Sigma: [7fbf263ae746654fd7d338483e92eac9e54b3f4f314caecd943fa669bd2a39ed0410d59a580e4928090ce08eac9dba1c44185d9436fd4257ba00d9eedcd66305]
    W[0]: [6ca9494a4f0053b9f44b58c99e488e5fd82a372b07e902284e3cb05030434f22]
    W[1]: [7d1a3a11fb6d0e3dda19378c199eecd72bb806cabf7207de3d4204492fbeca69]
    W[2]: [f2ae38404b6295b7afcc4a683fd9fbc5f9ce48076a2fad538805c7b0f4189356]
    W[3]: [fbfda4cecfaf96c27e61b21cf399d733fe58e2184e562b558d6b2de9992d2b11]
    W[4]: [133fa0cb56ff12c7ab70b454fa2ea4cba8f8d648b4efc429887d4058d1dc0c87]
    W[5]: [105392d27affa14a019a4cee64d255ae4b43f3e42962e8afbf0a50b5e57cecd7]
    W[6]: [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
Sigma 2:
    Verification Key: [a8aa59b8c49555e616f9b97bbcb03fc0f67dff84e960b4a6c8f98addecf53030]
    Sigma: [90d86d287b823db00495da19604e2b67bec1a827ac7811bfbb1efa85c0a5f2c6d73d43fb7a07af78470db68f41181df477c008cc1c1cb4a0772df36fba42b40a]
    W[0]: [628396c498ffd37f2e4ffd514edab39377aa5d1b4d293977277d4b73c022f3d3]
    W[1]: [2188f50efc84145afa9953fcd0f90c142278059137a2ed6213131122a00be652]
    W[2]: [7a6306db77b1c052ce5f794d8906b9943b3e2f964097d79f2a180b4953f75e3f]
    W[3]: [805d8fbe8531c62fc05a5727547eceb985fc7c3941bdb01768f04b2b0914542a]
    W[4]: [cfcdc3eac3870b111666cb3857b6c9b4174e1624915a3b9eaeafdc048a1a649f]
    W[5]: [f8ececbc33b5fda16052b3cea0688bd7d8c26ddb2e509c43a9c1ffb6ccf91458]
    W[6]: [11726d173febca7d6db8438f683cc796cd0f885f3ca37d43935fb55ca76aead7]
R 2: [05278249d0d29d4e1ca71a474cb7dcc979b5163a48132eaffcf02f9d27a4650b]
```
Product Composition Secret Key, t = 16383:
```
Tau 1:
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
    Right Witness: [3826a0ce6317771d29d7c3d18732330f34aad0c2afaadc890bb24181b06c89cc]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [105392d27affa14a019a4cee64d255ae4b43f3e42962e8afbf0a50b5e57cecd7]
    Right Witness: [099a303142ba2c4f6d47d2d48c69de96536f006269fc4f5769d45b99e8d7a7b1]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [133fa0cb56ff12c7ab70b454fa2ea4cba8f8d648b4efc429887d4058d1dc0c87]
    Right Witness: [0da9ca944589819af6e7422319d1ec60db274551ce3f96da92057f2eb0e33536]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [fbfda4cecfaf96c27e61b21cf399d733fe58e2184e562b558d6b2de9992d2b11]
    Right Witness: [108cacb1f1ff1f9d7aeed3e4157cf87e93f4b9c3caba9feed75e9977cb30eb7a]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f2ae38404b6295b7afcc4a683fd9fbc5f9ce48076a2fad538805c7b0f4189356]
    Right Witness: [2f8a0a8c39c728693469c4c9f8bee7741bf1abee04d297e918ff004f459cbbda]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7d1a3a11fb6d0e3dda19378c199eecd72bb806cabf7207de3d4204492fbeca69]
    Right Witness: [0ebf5360f3d500e786b2561aefc1c2878b4ffe63f0b61812586403304b3dbf53]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [6ca9494a4f0053b9f44b58c99e488e5fd82a372b07e902284e3cb05030434f22]
    Right Witness: [679cac132a86a8df5984934038971d4d93e2a24ed310adfa51ec7a2a983a4fc3]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [be53ca809f14a98d15462ef91a0949f2644a6518e025d72177a653676c9d47c2]
Sigma 1:
    Verification Key: [be53ca809f14a98d15462ef91a0949f2644a6518e025d72177a653676c9d47c2]
    Sigma: [7fbf263ae746654fd7d338483e92eac9e54b3f4f314caecd943fa669bd2a39ed0410d59a580e4928090ce08eac9dba1c44185d9436fd4257ba00d9eedcd66305]
    W[0]: [6ca9494a4f0053b9f44b58c99e488e5fd82a372b07e902284e3cb05030434f22]
    W[1]: [7d1a3a11fb6d0e3dda19378c199eecd72bb806cabf7207de3d4204492fbeca69]
    W[2]: [f2ae38404b6295b7afcc4a683fd9fbc5f9ce48076a2fad538805c7b0f4189356]
    W[3]: [fbfda4cecfaf96c27e61b21cf399d733fe58e2184e562b558d6b2de9992d2b11]
    W[4]: [133fa0cb56ff12c7ab70b454fa2ea4cba8f8d648b4efc429887d4058d1dc0c87]
    W[5]: [105392d27affa14a019a4cee64d255ae4b43f3e42962e8afbf0a50b5e57cecd7]
    W[6]: [7cbc13c0b96cc52b85e74b76e51b97043d1ee74d56990c8aa1183f9d3995f7f7]
Seed:
    b0f2eeb2ca827b2a3c83c9d68b5ff7b767deddffe081bce0f4ae1f952f8859c9
Tau 2:
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [11726d173febca7d6db8438f683cc796cd0f885f3ca37d43935fb55ca76aead7]
    Right Witness: [241d2e73b30372d801714729663e5b780df382c858b28f114e0474c72a0f67fe]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f8ececbc33b5fda16052b3cea0688bd7d8c26ddb2e509c43a9c1ffb6ccf91458]
    Right Witness: [781e9a52a9fb630ae4179a76695a3bdb7f0ed3035dfd2c2a0b075b5066abb9ef]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [cfcdc3eac3870b111666cb3857b6c9b4174e1624915a3b9eaeafdc048a1a649f]
    Right Witness: [b6c531feb79ca6d059b4180af51c01d2c88f6c99a33d68551f8239d7f5610631]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [805d8fbe8531c62fc05a5727547eceb985fc7c3941bdb01768f04b2b0914542a]
    Right Witness: [22b50479133848480974a3a07f14aa2e7976943a9c94f00d2629a747eb086555]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7a6306db77b1c052ce5f794d8906b9943b3e2f964097d79f2a180b4953f75e3f]
    Right Witness: [aa470ee7b1a056f4a9aa6a80be013ff3ddddf7fda9cc21926bede6346bb6eb02]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [2188f50efc84145afa9953fcd0f90c142278059137a2ed6213131122a00be652]
    Right Witness: [98a94fad1b59cc5a18ac2a6f1e04c0e45c262640cd86647bd4c64dbe8f50cb05]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [628396c498ffd37f2e4ffd514edab39377aa5d1b4d293977277d4b73c022f3d3]
    Right Witness: [dc0d8ba418cae4aa3b109918830fff94aabd6c227a89bb33dd8344c4fedc2d89]
    Height: 0
    Ed25519 Secret Key:       [996313a2389ab7fdf9333987e620d3bdd0875eb7653b8cb913005f4e5c81175c]
    Ed25519 Verification Key: [a8aa59b8c49555e616f9b97bbcb03fc0f67dff84e960b4a6c8f98addecf53030]
```
## Test Vector - 10
### Description 
 Generate and verify a specified product composition signature at `t = [0, 21845, 43690, 65535]` using a provided seed, message, and heights of the two trees
### Inputs
- Seed Bytes:
```
89d93bec2d392950fe1478559d1ba41d7ede8ad00171db9e03e086f75a98a378
```
- h1 (int):

```8```

- h2 (int):

```8```

- Message (string):
```
"olfactory workers on break"
```
- Message (bytes) with `utf-8` encoding:
```
6f6c666163746f727920776f726b657273206f6e20627265616b
```
### Outputs
- Product Composition Verification Key:
```
098e6fc4f6a8fc1ed597a7d06ca68244c306be7cbef368cd07887bfbc816cf36
```
- Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 8
    Binary configuration: 0
    Right Seed:    [74c93386cce96f628cb2a84f81ccd77f8a41050c10205d436177acc9203537c2]
    Left Witness:  [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
    Right Witness: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
    Height: 7
    Binary configuration: 0
    Right Seed:    [7d02091f9e55feed483387b172971700ff76556aa66c131121be3cdfc47fc1ff]
    Left Witness:  [7b990c0f2f97a41365f9804df8631da584e3bc705c48874480b950c51ac1c02e]
    Right Witness: [7a22a7e698d3c1cf2b3293f7c468e54a720adc8eb566438050370e1178fe5ed3]
    Height: 6
    Binary configuration: 0
    Right Seed:    [f897a12075446a5da67a8181b41053e4446465652b35749c2b30410c6a6e890b]
    Left Witness:  [263220ab61484e34cba3303609e6f82e1bd54502adda0c47a769385a868ddd64]
    Right Witness: [7e8a1f8b1c12d03937d8e79050f2edc3e7a33f96f7608ec2f896ee04738f093e]
    Height: 5
    Binary configuration: 0
    Right Seed:    [124a95a99d0e99de6782dda9085b83ffa0e5fcb4326ed078fdcb7a0e0567c845]
    Left Witness:  [c9f23e8c1d583816243a62d6af4a3bc9c2e1b9ba75729e712719e4c608bc12fb]
    Right Witness: [7b73efd250646b986b58b422d4920b5f6acaed7cfbdf9e15fb8ff9fd6c57f7a0]
    Height: 4
    Binary configuration: 0
    Right Seed:    [c7ad1b4eaeb10b2ab76456a36c6264372de3a8847ecc7e1e08fc336d4817dd15]
    Left Witness:  [b95330dcd59b38089a5ea78e058b034a57ae3b233c1fd1e44452a66d141e0d0f]
    Right Witness: [241db0dd1bd32978f950f1f35a50660e108aa4fdf68fd75acf06e3c59b891317]
    Height: 3
    Binary configuration: 0
    Right Seed:    [aad8f8cf1b22b5ed8026a3490fdc920aa30dad4dec8d4d2b4e23f2a498c2f4c2]
    Left Witness:  [b69b509c73757a42b6bb5b8dbe17174bf4024102ce3d83fc64d57d5142fd1e87]
    Right Witness: [534016cd11e3de883ec5062996d27096897a4d50dfb2bc32e4f0c1703e87b1ef]
    Height: 2
    Binary configuration: 0
    Right Seed:    [8345fb9057e573c3a08257ac0a3438911c4f7cdb6031b9efb486cc618ed45301]
    Left Witness:  [ab1de01fd0f43515bd2207361cd1fa3507474c6b3572a6a49a34c76313f68ef8]
    Right Witness: [751a4fd84caf9c63553436bd52068ae04f254cb0f0f3d959e962ad0a933de543]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f08fd349f4ab6b9a96b3809c49af6a90b31fb33f794eb7b4cdd1dac326b6de7e]
    Left Witness:  [8fe422d9865960519c98aae0d21960cf5c0f2c0bdf34ac1657827c9971e1cd85]
    Right Witness: [da76b54630204ccce4c6ab9a339a4facec8b98fa179443101f8008003683c34e]
    Height: 0
    Ed25519 Secret Key:       [a2d8545edb9c67ca943b2ca1ce531569c5ca075ce6ae8e887b7fd8a0be149b6e]
    Ed25519 Verification Key: [1ac2f5becffd35f7f8d515d3e027e1258da290a812f31b26e1fdfa8e1d590b52]
Sigma 1:
    Verification Key: [1ac2f5becffd35f7f8d515d3e027e1258da290a812f31b26e1fdfa8e1d590b52]
    Sigma: [71fad1ffd544c21aa996e3bd5c99262a961a2808fb5ba5c6552f4c8cbdfeedbe7fbb50afe2a8c0b95f6d6c3fbea28df9d611b802493c96e686f71dd99f9af40a]
    W[0]: [da76b54630204ccce4c6ab9a339a4facec8b98fa179443101f8008003683c34e]
    W[1]: [751a4fd84caf9c63553436bd52068ae04f254cb0f0f3d959e962ad0a933de543]
    W[2]: [534016cd11e3de883ec5062996d27096897a4d50dfb2bc32e4f0c1703e87b1ef]
    W[3]: [241db0dd1bd32978f950f1f35a50660e108aa4fdf68fd75acf06e3c59b891317]
    W[4]: [7b73efd250646b986b58b422d4920b5f6acaed7cfbdf9e15fb8ff9fd6c57f7a0]
    W[5]: [7e8a1f8b1c12d03937d8e79050f2edc3e7a33f96f7608ec2f896ee04738f093e]
    W[6]: [7a22a7e698d3c1cf2b3293f7c468e54a720adc8eb566438050370e1178fe5ed3]
    W[7]: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
Seed:
    0ad78c28b151dc3f422cae68314c2a7b8c1d9feeaeafc82593798b2cd6330d79
Tau 2:
    Height: 8
    Binary configuration: 0
    Right Seed:    [c1b98fd8f8d55b63b1d225f2b1f14a773f074263da2b0b4bc1d08043f8ad9d38]
    Left Witness:  [6e0e3fd68a413bca596440df3bbe2f617c9fa947173d661bb6c0aaed891352f9]
    Right Witness: [459d718a64fca74f132f00381d228f746d027906808e945d2bdbeb7c46a9bdef]
    Height: 7
    Binary configuration: 0
    Right Seed:    [b28bcf46a7d686d4aabc7e9944a130e774f03f32b78e22bbd06e840b107ba0ec]
    Left Witness:  [e096c36e9a3e3f1943ef8b157c2a399093a5e70482766d45694801d3ed734ce2]
    Right Witness: [b649707ccb98fc06ede0f6e6630a3872420092a26967a2e45c56d460a5e88a98]
    Height: 6
    Binary configuration: 0
    Right Seed:    [e60511faa905a468751e98e8ac279ec383c891bfc6ff8c5a6dcd26348b9839be]
    Left Witness:  [894bdd456ed1dd2cb442d9722451af9915ba027aa141572da338d1400fc6ba79]
    Right Witness: [710ca2f89466d8ff9f557935c9780a0d93dc7d8dc01f889e6839aee8cac717fe]
    Height: 5
    Binary configuration: 0
    Right Seed:    [e77351779c9b03ced760e9aae4abe916e43885fbf25f090161ca1bf2732c70c5]
    Left Witness:  [e2de4ad8172c387293220362015a116cf889ec207e5e187b0fe0a7a070af6eb7]
    Right Witness: [9138ebd7bc5e20c3f559410120d0108f69a6965741ffd20b73ac9723f48a512c]
    Height: 4
    Binary configuration: 0
    Right Seed:    [a633e652460486c7dc0abf76cc7a567f64681c907dccdcd5e46b9dcaade75026]
    Left Witness:  [403b5d964685dd6bdd68488e7e52450c855d774ca4516e81a41257747200f99a]
    Right Witness: [b3049baf3230ec7fea9b1cf564d53b25abc0973c292c8c313c59d1bc5995a1e1]
    Height: 3
    Binary configuration: 0
    Right Seed:    [745acd09cbaeba08376bbe4d4d3cca6591bef911812b14c964ef6cd203a51a22]
    Left Witness:  [66fb162cd1efa56709371145a58f8424f53fbc6f99ede5abe1c5b9ddf5b7ad6a]
    Right Witness: [847c9a30430b603413198c09efe82837554525560d9bbe942c5ec5cb11c1d1a7]
    Height: 2
    Binary configuration: 0
    Right Seed:    [1435841d528c477a48af165029d9e813e7538d5b2f63037cec36904616fe0738]
    Left Witness:  [e5eacaa8d40c6949e338f4ab87403180b371f5411573a16328ba82943185566d]
    Right Witness: [f1f7d81a53453eb56dbe07ee923841879d1fefadcd9d2a0d957cca9816a79da5]
    Height: 1
    Binary configuration: 0
    Right Seed:    [40a4442277975aa55daac179b8016a94a20bbd75b665e54672325ce2ff1f07cc]
    Left Witness:  [6c7e1d70e25215bf377dcc4d28fa867eea65dfd7885ed600f6695e9541453642]
    Right Witness: [6dfa2e947567a856bdaeedfdf8572d5dc0450d6cb69145fa616f9629d8a3b021]
    Height: 0
    Ed25519 Secret Key:       [ef58f6f21d8106ef2f91c217dc71918342c049e139baa8383912700e01dcda2d]
    Ed25519 Verification Key: [83e353b3ef113f2548fc4b9c2f00d7aaaf524e51058f94ba3818fc725bc7de2a]
```
- Sigma t = 0:
```
Sigma 1:
    Verification Key: [1ac2f5becffd35f7f8d515d3e027e1258da290a812f31b26e1fdfa8e1d590b52]
    Sigma: [71fad1ffd544c21aa996e3bd5c99262a961a2808fb5ba5c6552f4c8cbdfeedbe7fbb50afe2a8c0b95f6d6c3fbea28df9d611b802493c96e686f71dd99f9af40a]
    W[0]: [da76b54630204ccce4c6ab9a339a4facec8b98fa179443101f8008003683c34e]
    W[1]: [751a4fd84caf9c63553436bd52068ae04f254cb0f0f3d959e962ad0a933de543]
    W[2]: [534016cd11e3de883ec5062996d27096897a4d50dfb2bc32e4f0c1703e87b1ef]
    W[3]: [241db0dd1bd32978f950f1f35a50660e108aa4fdf68fd75acf06e3c59b891317]
    W[4]: [7b73efd250646b986b58b422d4920b5f6acaed7cfbdf9e15fb8ff9fd6c57f7a0]
    W[5]: [7e8a1f8b1c12d03937d8e79050f2edc3e7a33f96f7608ec2f896ee04738f093e]
    W[6]: [7a22a7e698d3c1cf2b3293f7c468e54a720adc8eb566438050370e1178fe5ed3]
    W[7]: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
Sigma 2:
    Verification Key: [83e353b3ef113f2548fc4b9c2f00d7aaaf524e51058f94ba3818fc725bc7de2a]
    Sigma: [dd90211c49d421bf60614b679aadc6d0b10fba93a1dc28080ed6dd85579239382fa9a65f717c36ec9493c22dcbcd9347b5ce89d72cde6112ce9d67e9fcb79e06]
    W[0]: [6dfa2e947567a856bdaeedfdf8572d5dc0450d6cb69145fa616f9629d8a3b021]
    W[1]: [f1f7d81a53453eb56dbe07ee923841879d1fefadcd9d2a0d957cca9816a79da5]
    W[2]: [847c9a30430b603413198c09efe82837554525560d9bbe942c5ec5cb11c1d1a7]
    W[3]: [b3049baf3230ec7fea9b1cf564d53b25abc0973c292c8c313c59d1bc5995a1e1]
    W[4]: [9138ebd7bc5e20c3f559410120d0108f69a6965741ffd20b73ac9723f48a512c]
    W[5]: [710ca2f89466d8ff9f557935c9780a0d93dc7d8dc01f889e6839aee8cac717fe]
    W[6]: [b649707ccb98fc06ede0f6e6630a3872420092a26967a2e45c56d460a5e88a98]
    W[7]: [459d718a64fca74f132f00381d228f746d027906808e945d2bdbeb7c46a9bdef]
R 2: [3e0bd5fc406cb92e70b4ad8ca8c47f8eebe3de3c00f7fc050a0888db9f591f55]
```
Product Composition Secret Key, t = 0:
```
Tau 1:
    Height: 8
    Binary configuration: 0
    Right Seed:    [74c93386cce96f628cb2a84f81ccd77f8a41050c10205d436177acc9203537c2]
    Left Witness:  [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
    Right Witness: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
    Height: 7
    Binary configuration: 0
    Right Seed:    [7d02091f9e55feed483387b172971700ff76556aa66c131121be3cdfc47fc1ff]
    Left Witness:  [7b990c0f2f97a41365f9804df8631da584e3bc705c48874480b950c51ac1c02e]
    Right Witness: [7a22a7e698d3c1cf2b3293f7c468e54a720adc8eb566438050370e1178fe5ed3]
    Height: 6
    Binary configuration: 0
    Right Seed:    [f897a12075446a5da67a8181b41053e4446465652b35749c2b30410c6a6e890b]
    Left Witness:  [263220ab61484e34cba3303609e6f82e1bd54502adda0c47a769385a868ddd64]
    Right Witness: [7e8a1f8b1c12d03937d8e79050f2edc3e7a33f96f7608ec2f896ee04738f093e]
    Height: 5
    Binary configuration: 0
    Right Seed:    [124a95a99d0e99de6782dda9085b83ffa0e5fcb4326ed078fdcb7a0e0567c845]
    Left Witness:  [c9f23e8c1d583816243a62d6af4a3bc9c2e1b9ba75729e712719e4c608bc12fb]
    Right Witness: [7b73efd250646b986b58b422d4920b5f6acaed7cfbdf9e15fb8ff9fd6c57f7a0]
    Height: 4
    Binary configuration: 0
    Right Seed:    [c7ad1b4eaeb10b2ab76456a36c6264372de3a8847ecc7e1e08fc336d4817dd15]
    Left Witness:  [b95330dcd59b38089a5ea78e058b034a57ae3b233c1fd1e44452a66d141e0d0f]
    Right Witness: [241db0dd1bd32978f950f1f35a50660e108aa4fdf68fd75acf06e3c59b891317]
    Height: 3
    Binary configuration: 0
    Right Seed:    [aad8f8cf1b22b5ed8026a3490fdc920aa30dad4dec8d4d2b4e23f2a498c2f4c2]
    Left Witness:  [b69b509c73757a42b6bb5b8dbe17174bf4024102ce3d83fc64d57d5142fd1e87]
    Right Witness: [534016cd11e3de883ec5062996d27096897a4d50dfb2bc32e4f0c1703e87b1ef]
    Height: 2
    Binary configuration: 0
    Right Seed:    [8345fb9057e573c3a08257ac0a3438911c4f7cdb6031b9efb486cc618ed45301]
    Left Witness:  [ab1de01fd0f43515bd2207361cd1fa3507474c6b3572a6a49a34c76313f68ef8]
    Right Witness: [751a4fd84caf9c63553436bd52068ae04f254cb0f0f3d959e962ad0a933de543]
    Height: 1
    Binary configuration: 0
    Right Seed:    [f08fd349f4ab6b9a96b3809c49af6a90b31fb33f794eb7b4cdd1dac326b6de7e]
    Left Witness:  [8fe422d9865960519c98aae0d21960cf5c0f2c0bdf34ac1657827c9971e1cd85]
    Right Witness: [da76b54630204ccce4c6ab9a339a4facec8b98fa179443101f8008003683c34e]
    Height: 0
    Ed25519 Secret Key:       [a2d8545edb9c67ca943b2ca1ce531569c5ca075ce6ae8e887b7fd8a0be149b6e]
    Ed25519 Verification Key: [1ac2f5becffd35f7f8d515d3e027e1258da290a812f31b26e1fdfa8e1d590b52]
Sigma 1:
    Verification Key: [1ac2f5becffd35f7f8d515d3e027e1258da290a812f31b26e1fdfa8e1d590b52]
    Sigma: [71fad1ffd544c21aa996e3bd5c99262a961a2808fb5ba5c6552f4c8cbdfeedbe7fbb50afe2a8c0b95f6d6c3fbea28df9d611b802493c96e686f71dd99f9af40a]
    W[0]: [da76b54630204ccce4c6ab9a339a4facec8b98fa179443101f8008003683c34e]
    W[1]: [751a4fd84caf9c63553436bd52068ae04f254cb0f0f3d959e962ad0a933de543]
    W[2]: [534016cd11e3de883ec5062996d27096897a4d50dfb2bc32e4f0c1703e87b1ef]
    W[3]: [241db0dd1bd32978f950f1f35a50660e108aa4fdf68fd75acf06e3c59b891317]
    W[4]: [7b73efd250646b986b58b422d4920b5f6acaed7cfbdf9e15fb8ff9fd6c57f7a0]
    W[5]: [7e8a1f8b1c12d03937d8e79050f2edc3e7a33f96f7608ec2f896ee04738f093e]
    W[6]: [7a22a7e698d3c1cf2b3293f7c468e54a720adc8eb566438050370e1178fe5ed3]
    W[7]: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
Seed:
    0ad78c28b151dc3f422cae68314c2a7b8c1d9feeaeafc82593798b2cd6330d79
Tau 2:
    Height: 8
    Binary configuration: 0
    Right Seed:    [c1b98fd8f8d55b63b1d225f2b1f14a773f074263da2b0b4bc1d08043f8ad9d38]
    Left Witness:  [6e0e3fd68a413bca596440df3bbe2f617c9fa947173d661bb6c0aaed891352f9]
    Right Witness: [459d718a64fca74f132f00381d228f746d027906808e945d2bdbeb7c46a9bdef]
    Height: 7
    Binary configuration: 0
    Right Seed:    [b28bcf46a7d686d4aabc7e9944a130e774f03f32b78e22bbd06e840b107ba0ec]
    Left Witness:  [e096c36e9a3e3f1943ef8b157c2a399093a5e70482766d45694801d3ed734ce2]
    Right Witness: [b649707ccb98fc06ede0f6e6630a3872420092a26967a2e45c56d460a5e88a98]
    Height: 6
    Binary configuration: 0
    Right Seed:    [e60511faa905a468751e98e8ac279ec383c891bfc6ff8c5a6dcd26348b9839be]
    Left Witness:  [894bdd456ed1dd2cb442d9722451af9915ba027aa141572da338d1400fc6ba79]
    Right Witness: [710ca2f89466d8ff9f557935c9780a0d93dc7d8dc01f889e6839aee8cac717fe]
    Height: 5
    Binary configuration: 0
    Right Seed:    [e77351779c9b03ced760e9aae4abe916e43885fbf25f090161ca1bf2732c70c5]
    Left Witness:  [e2de4ad8172c387293220362015a116cf889ec207e5e187b0fe0a7a070af6eb7]
    Right Witness: [9138ebd7bc5e20c3f559410120d0108f69a6965741ffd20b73ac9723f48a512c]
    Height: 4
    Binary configuration: 0
    Right Seed:    [a633e652460486c7dc0abf76cc7a567f64681c907dccdcd5e46b9dcaade75026]
    Left Witness:  [403b5d964685dd6bdd68488e7e52450c855d774ca4516e81a41257747200f99a]
    Right Witness: [b3049baf3230ec7fea9b1cf564d53b25abc0973c292c8c313c59d1bc5995a1e1]
    Height: 3
    Binary configuration: 0
    Right Seed:    [745acd09cbaeba08376bbe4d4d3cca6591bef911812b14c964ef6cd203a51a22]
    Left Witness:  [66fb162cd1efa56709371145a58f8424f53fbc6f99ede5abe1c5b9ddf5b7ad6a]
    Right Witness: [847c9a30430b603413198c09efe82837554525560d9bbe942c5ec5cb11c1d1a7]
    Height: 2
    Binary configuration: 0
    Right Seed:    [1435841d528c477a48af165029d9e813e7538d5b2f63037cec36904616fe0738]
    Left Witness:  [e5eacaa8d40c6949e338f4ab87403180b371f5411573a16328ba82943185566d]
    Right Witness: [f1f7d81a53453eb56dbe07ee923841879d1fefadcd9d2a0d957cca9816a79da5]
    Height: 1
    Binary configuration: 0
    Right Seed:    [40a4442277975aa55daac179b8016a94a20bbd75b665e54672325ce2ff1f07cc]
    Left Witness:  [6c7e1d70e25215bf377dcc4d28fa867eea65dfd7885ed600f6695e9541453642]
    Right Witness: [6dfa2e947567a856bdaeedfdf8572d5dc0450d6cb69145fa616f9629d8a3b021]
    Height: 0
    Ed25519 Secret Key:       [ef58f6f21d8106ef2f91c217dc71918342c049e139baa8383912700e01dcda2d]
    Ed25519 Verification Key: [83e353b3ef113f2548fc4b9c2f00d7aaaf524e51058f94ba3818fc725bc7de2a]
```
- Sigma t = 21845:
```
Sigma 1:
    Verification Key: [0ad6dc6cad601b9fdc42472cc1ac9581493a2ee981e27b6b6bfe1a77e4da1eed]
    Sigma: [1f5638706e05285387eb467c9601fea11e228af7cd75077fabc30e7c8a79d76561f4439f2dabf0466c6415268ca3853f5bffa72418baee57b7da6dd530bb4d06]
    W[0]: [b143c965cad672635ca884f5668e20899e5ceb6f3d391b6ebbaab31b80602518]
    W[1]: [11a19266de49384659a7a86ce4ee0e83144a3dc1e44ec953470f26111b615404]
    W[2]: [a3e850a8274caf1417ae8ffc2e3f6c0544905af52fbc167b01c1ed8c8f4219a8]
    W[3]: [deb89e497459d9a8a772893a3830e7008928fb844f85bc97578644f74204e337]
    W[4]: [5f9cade426cf72a1ea71819ff38cc901b4019cd1108feb020fa5fc643a113500]
    W[5]: [07bcf85b204b0468b41657e01e27222b60ee6fbffdb16375da42736fcaf8e859]
    W[6]: [7b990c0f2f97a41365f9804df8631da584e3bc705c48874480b950c51ac1c02e]
    W[7]: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
Sigma 2:
    Verification Key: [5c9f3c7ce0c73feb0770e0727fce11cc2773ea430f7f6b1ee85edf993a00b8a7]
    Sigma: [8583e3099e0928ba4ab83379fb032c688db0b875a73b831be2a3ea38b66918ca5338a59b8d53bf5feb40dedf0cc9f773106d796b28365e8cecd0b2039c37f70e]
    W[0]: [71bbe712f3b06f726e70d285ee3b9044580c39bb4588820501188a0fd3d3a287]
    W[1]: [56e6d22fc18c288f4cd708b8c0024f9c66369e50eaedad750d81f13ab7e61824]
    W[2]: [5b03ab508973a7ed6918d416fe339a2a11c1bf34b44311ea3c74721290e9e9f7]
    W[3]: [340d42cbabee26bad4dcf2a28ac5fc7173cba753bb0a2fb52d0a843996a3f9a4]
    W[4]: [a651f94904c44647f6ebf522eedcb579d296f5b5b05a843372517bbed4cb4f58]
    W[5]: [29fcf918861ad110879c09956f9073ea6670c0cf71835e9d964030bfaa9413f4]
    W[6]: [df00c8ae687863512d9ea191efd816a9afffd8e0a6069bb7a667875fc010dd25]
    W[7]: [4f80ba61b7b2f77e1b2bec048f8b642350049de20a579ae26f773f7de32c056a]
R 2: [07186c3955ded48687fd5e2d44dd5306d332f256d4a8b9aab434b496122b1187]
```
Product Composition Secret Key, t = 21845:
```
Tau 1:
    Height: 8
    Binary configuration: 0
    Right Seed:    [74c93386cce96f628cb2a84f81ccd77f8a41050c10205d436177acc9203537c2]
    Left Witness:  [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
    Right Witness: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [7b990c0f2f97a41365f9804df8631da584e3bc705c48874480b950c51ac1c02e]
    Right Witness: [7a22a7e698d3c1cf2b3293f7c468e54a720adc8eb566438050370e1178fe5ed3]
    Height: 6
    Binary configuration: 0
    Right Seed:    [780cbb4f03744dba7094443fa773fc97f98bea371d552cf5e30e9fd130ddcb33]
    Left Witness:  [973f43951f0f744708b3c7702b29b66a04ef0cb11e9c627de722c7c102d6c5ce]
    Right Witness: [07bcf85b204b0468b41657e01e27222b60ee6fbffdb16375da42736fcaf8e859]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5f9cade426cf72a1ea71819ff38cc901b4019cd1108feb020fa5fc643a113500]
    Right Witness: [cfbc680114daf903b387261677dbcdaa69808d004c1dd9fccd5d275681308f76]
    Height: 4
    Binary configuration: 0
    Right Seed:    [8ddcedb1c1b2fa1ab298487eeebcdf960e63865d326025a158d9350b5d0aed22]
    Left Witness:  [85d9cb2396c4c74226c13b6cc3a772514015a75e533383df7870dd5ecf2ab332]
    Right Witness: [deb89e497459d9a8a772893a3830e7008928fb844f85bc97578644f74204e337]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a3e850a8274caf1417ae8ffc2e3f6c0544905af52fbc167b01c1ed8c8f4219a8]
    Right Witness: [3cb7311b5aad05a4fbffb06c0d1256bc1de5b26993b481ada0911acf8d178c35]
    Height: 2
    Binary configuration: 0
    Right Seed:    [d817a8587504afaf48973b5a79355ee01bf994d673afccc65c0011accfe59214]
    Left Witness:  [2fc5b4b7a09a10b5ff68ddfff7f1ef353fefa434ef5fc86b08661e4730c503b7]
    Right Witness: [11a19266de49384659a7a86ce4ee0e83144a3dc1e44ec953470f26111b615404]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b143c965cad672635ca884f5668e20899e5ceb6f3d391b6ebbaab31b80602518]
    Right Witness: [f0f10325253e4859ca5f56a3defb33cd3eaebfaf2498d21de7f8df313b63e8d1]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [0ad6dc6cad601b9fdc42472cc1ac9581493a2ee981e27b6b6bfe1a77e4da1eed]
Sigma 1:
    Verification Key: [0ad6dc6cad601b9fdc42472cc1ac9581493a2ee981e27b6b6bfe1a77e4da1eed]
    Sigma: [1f5638706e05285387eb467c9601fea11e228af7cd75077fabc30e7c8a79d76561f4439f2dabf0466c6415268ca3853f5bffa72418baee57b7da6dd530bb4d06]
    W[0]: [b143c965cad672635ca884f5668e20899e5ceb6f3d391b6ebbaab31b80602518]
    W[1]: [11a19266de49384659a7a86ce4ee0e83144a3dc1e44ec953470f26111b615404]
    W[2]: [a3e850a8274caf1417ae8ffc2e3f6c0544905af52fbc167b01c1ed8c8f4219a8]
    W[3]: [deb89e497459d9a8a772893a3830e7008928fb844f85bc97578644f74204e337]
    W[4]: [5f9cade426cf72a1ea71819ff38cc901b4019cd1108feb020fa5fc643a113500]
    W[5]: [07bcf85b204b0468b41657e01e27222b60ee6fbffdb16375da42736fcaf8e859]
    W[6]: [7b990c0f2f97a41365f9804df8631da584e3bc705c48874480b950c51ac1c02e]
    W[7]: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
Seed:
    6a6a55dff0f867f1f962a5380cf4292ece6c199922bf8af96a0d91e071cfc29c
Tau 2:
    Height: 8
    Binary configuration: 0
    Right Seed:    [0b6fc4a342d2483e289a438e45734ad05c7118a23ddfa214f80371e69be51e42]
    Left Witness:  [bae0b978fa9f980675a8853bb2155d65ce44ffff34237a1ee4b56d5e61aa165a]
    Right Witness: [4f80ba61b7b2f77e1b2bec048f8b642350049de20a579ae26f773f7de32c056a]
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [df00c8ae687863512d9ea191efd816a9afffd8e0a6069bb7a667875fc010dd25]
    Right Witness: [0c25877fd052dd8d95a58d410e69f4289311cd90de816f09b0ad3ae621c9d037]
    Height: 6
    Binary configuration: 0
    Right Seed:    [08e4fbcb3bdac5a7e9e9f28c216644584af713ed3715e5c36a28d3e3b0462e0d]
    Left Witness:  [fc4c4827166c7a38a4a4e9452f90afcfb0c3b41684c8b37c8a0f17f6ee36e86f]
    Right Witness: [29fcf918861ad110879c09956f9073ea6670c0cf71835e9d964030bfaa9413f4]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [a651f94904c44647f6ebf522eedcb579d296f5b5b05a843372517bbed4cb4f58]
    Right Witness: [5fb579eda6714a95446bb1c9eee47cac46eacfc5232df58d9c44a3da82e519da]
    Height: 4
    Binary configuration: 0
    Right Seed:    [bc492a33b0d2eb8efc19b2d62e04c113d58c5f1e2699918f4d124695e29b871a]
    Left Witness:  [f7ff835101c94e705773b81dcf82ee1796ed3f6d838b5366e830d84e2aa07f4d]
    Right Witness: [340d42cbabee26bad4dcf2a28ac5fc7173cba753bb0a2fb52d0a843996a3f9a4]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5b03ab508973a7ed6918d416fe339a2a11c1bf34b44311ea3c74721290e9e9f7]
    Right Witness: [daebb3294d2dcb2f59b6eeba4140e7a2c3de9bdf7d4c6512eca698a5ebff1e79]
    Height: 2
    Binary configuration: 0
    Right Seed:    [40c160fea1271d08ca718bc55ea6746268aca780626c2f8b7ee370200348159f]
    Left Witness:  [f39f4a6b21bdcff8275e1a1331bd08be054577bef7c23e2e13cdca6cbc5484ae]
    Right Witness: [56e6d22fc18c288f4cd708b8c0024f9c66369e50eaedad750d81f13ab7e61824]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [71bbe712f3b06f726e70d285ee3b9044580c39bb4588820501188a0fd3d3a287]
    Right Witness: [d081f737c7e2614a436bd9461313eed43b57aa52f8e2796c1cdb25d6e1eb752a]
    Height: 0
    Ed25519 Secret Key:       [03a01b372aabe42ad63285b8045cb7ff9005d1294d0f362b894bbe264b2e9ffe]
    Ed25519 Verification Key: [5c9f3c7ce0c73feb0770e0727fce11cc2773ea430f7f6b1ee85edf993a00b8a7]
```
- Sigma t = 43690:
```
Sigma 1:
    Verification Key: [affa268c27c340f563f8a3c759c2395bed6d2ae2286ed292cc563d79550ff4bb]
    Sigma: [83f30508b73e0aa29b66fe21520566d8c17c211a544c11cac620c0a0a88b13e71f2e571e625c64bebc317cb3090685e32545dc789c882a44f0c3c07f7a8aa709]
    W[0]: [ae8415a816802a5d9c163e1509ee2933d2670ec74388114d9dfe22247a2ef8bc]
    W[1]: [394587c62d13105059c7d43a4c214830f30f525021f4e424b5598f03053e2b00]
    W[2]: [c9503192c3b37f61f45e55a2139b89b459ecafcb24573c9b5528be65f1333840]
    W[3]: [d5631e45076036eb0a232988074e714701056ca4aa89b4fec111b6344a289478]
    W[4]: [06306ba7031523c62fa46064056249e2a30b1bf8c4c5914dd52e356a540132b1]
    W[5]: [944ac57dd83d1dbb34545b280c24cd021f085894a18769e95480d7b01b8b294f]
    W[6]: [afe557fcbecf9f77cc933b880b2c79d919d292e40660c76dca9c47b710e81bea]
    W[7]: [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
Sigma 2:
    Verification Key: [58fc22cf26ccfe1f1c342fc4dce0983485055254f8189e1a0501c20223476cc9]
    Sigma: [ed9e0e2943696f903c81ff7023e3478b7687e2c0aa9b82a98d9926aaa63fce320c81b502ac6256bc01f9e171920bc59b27d42117f070aee10368b251307e7800]
    W[0]: [f38d767ea19b8b671cdf6671ecfdc562e77ba4eab3ff71606d9ab28b5ee9be16]
    W[1]: [15826b7e02bbdf687c3fdc39717ee802c30c1af997f75042bd10fec73e904791]
    W[2]: [1b13a2393fb489dfb40377be79771fe912dbdbb7150c2986c6cbdc73c39866f0]
    W[3]: [ca76b741d9c56c4359f076d26cf782cc8d8f3b192502a096b51ad0c57c47e6a2]
    W[4]: [794d4429e7a6a46b76ee0fbe13f62852ae342c329b38f23e275eb3505c40c207]
    W[5]: [90eccd0dd50ade31771ee598c817b56dc9f5fbfd3aa4c37e62fbb27d5a47c262]
    W[6]: [156ca396660cf9beaf0ed1b1f194fef371f6f706aa418167564c704e9f216eab]
    W[7]: [65a5bbd1abe61abecf63fa9d3c703d33d248cbbcd36f7a85966fea740202eb74]
R 2: [528f96bdb6a3056801565c1a3530a3f8c603f941e437d009e13e04ab1bc14755]
```
Product Composition Secret Key, t = 43690:
```
Tau 1:
    Height: 8
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
    Right Witness: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
    Height: 7
    Binary configuration: 0
    Right Seed:    [21bdd2217e1bb0c806d62b34fe7e50d6ac508fc7ec33257f411fa4fe409ee01d]
    Left Witness:  [668e35cdadc67b993f8a9efa11be57e5cda0e0e6bf391d5495d70b9d31dd7588]
    Right Witness: [afe557fcbecf9f77cc933b880b2c79d919d292e40660c76dca9c47b710e81bea]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [944ac57dd83d1dbb34545b280c24cd021f085894a18769e95480d7b01b8b294f]
    Right Witness: [733e07c755e6d0b3939924e654ba1cc25fc0a7dd116f5acbd478870838e1efcb]
    Height: 5
    Binary configuration: 0
    Right Seed:    [1aa113c8637d1bf0833a5c6d7c55efbe2dd390996dbd09da1faa53b3ae6c19a8]
    Left Witness:  [c020149e7eb51897f100026f45641bd3e34c332a04a60962affc0083fee25a59]
    Right Witness: [06306ba7031523c62fa46064056249e2a30b1bf8c4c5914dd52e356a540132b1]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d5631e45076036eb0a232988074e714701056ca4aa89b4fec111b6344a289478]
    Right Witness: [9b614fab7706a5195b745ca3bd7230d29d619b88f09e67cd6438ee1bc54def27]
    Height: 3
    Binary configuration: 0
    Right Seed:    [61e788f71e4c8328972cc16b1c4ecbdd524105e77edc70c8944aa4e54ba3435a]
    Left Witness:  [349b9c2d9627e813bd08f8a837cab585716ac2ceafb7c3dbeaec639e03ece018]
    Right Witness: [c9503192c3b37f61f45e55a2139b89b459ecafcb24573c9b5528be65f1333840]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [394587c62d13105059c7d43a4c214830f30f525021f4e424b5598f03053e2b00]
    Right Witness: [efb1b93d9494a6f1da2c483acf1fe52bb16f2ef3c6ae2af848cb08243d03d70d]
    Height: 1
    Binary configuration: 0
    Right Seed:    [b0e300c245cbe3bf6e4edd85adcfe510536b88bf89d10dde4323ecbf0623346d]
    Left Witness:  [3cd144300b929968163e98399dc45558205f2d221536d8290dae9d477b58788a]
    Right Witness: [ae8415a816802a5d9c163e1509ee2933d2670ec74388114d9dfe22247a2ef8bc]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [affa268c27c340f563f8a3c759c2395bed6d2ae2286ed292cc563d79550ff4bb]
Sigma 1:
    Verification Key: [affa268c27c340f563f8a3c759c2395bed6d2ae2286ed292cc563d79550ff4bb]
    Sigma: [83f30508b73e0aa29b66fe21520566d8c17c211a544c11cac620c0a0a88b13e71f2e571e625c64bebc317cb3090685e32545dc789c882a44f0c3c07f7a8aa709]
    W[0]: [ae8415a816802a5d9c163e1509ee2933d2670ec74388114d9dfe22247a2ef8bc]
    W[1]: [394587c62d13105059c7d43a4c214830f30f525021f4e424b5598f03053e2b00]
    W[2]: [c9503192c3b37f61f45e55a2139b89b459ecafcb24573c9b5528be65f1333840]
    W[3]: [d5631e45076036eb0a232988074e714701056ca4aa89b4fec111b6344a289478]
    W[4]: [06306ba7031523c62fa46064056249e2a30b1bf8c4c5914dd52e356a540132b1]
    W[5]: [944ac57dd83d1dbb34545b280c24cd021f085894a18769e95480d7b01b8b294f]
    W[6]: [afe557fcbecf9f77cc933b880b2c79d919d292e40660c76dca9c47b710e81bea]
    W[7]: [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
Seed:
    7d97a342de665416e01dbe850ec24fc82440c2568c55ce581611d105237bcb06
Tau 2:
    Height: 8
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [65a5bbd1abe61abecf63fa9d3c703d33d248cbbcd36f7a85966fea740202eb74]
    Right Witness: [8a5e11ca638b8bbacd3f536878872382063ab920768162991e1327301f63d850]
    Height: 7
    Binary configuration: 0
    Right Seed:    [d78873feca8f78298761337b16d00b0b8c355466136c6f3ab6f090c7e811630f]
    Left Witness:  [3eb8bdbffe951ab96c8658a4d3373964156c4aa9fc578ed978267e3cb894880b]
    Right Witness: [156ca396660cf9beaf0ed1b1f194fef371f6f706aa418167564c704e9f216eab]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [90eccd0dd50ade31771ee598c817b56dc9f5fbfd3aa4c37e62fbb27d5a47c262]
    Right Witness: [1a66b0004735aaeccc3e7d7e5f29048d28b99a9dc5ebcd9b10bed3bfb586d7ec]
    Height: 5
    Binary configuration: 0
    Right Seed:    [62473960805a74c2e737ac71728100e622415c6a33049098040680d43a5b6c59]
    Left Witness:  [6b5e64d59b0f17178ccee2c11c21e558b4c44e8a802f9148394b2b40b47a9bd8]
    Right Witness: [794d4429e7a6a46b76ee0fbe13f62852ae342c329b38f23e275eb3505c40c207]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [ca76b741d9c56c4359f076d26cf782cc8d8f3b192502a096b51ad0c57c47e6a2]
    Right Witness: [0fec8ff1035b3399c0926652d7246f9fd9fad9c868cfec7435c8c48b905e426c]
    Height: 3
    Binary configuration: 0
    Right Seed:    [e955b47e70e916333deb3ae6ebc3500e8ba5c202d6854318a5c25160892a3f99]
    Left Witness:  [d82b730a2616bc43597054f17c03affb77efec2b618136d946e1f4e792510b60]
    Right Witness: [1b13a2393fb489dfb40377be79771fe912dbdbb7150c2986c6cbdc73c39866f0]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [15826b7e02bbdf687c3fdc39717ee802c30c1af997f75042bd10fec73e904791]
    Right Witness: [59434344aa25c3a9165132a96842e76575dfd914d58c16379eb6944342c3ffed]
    Height: 1
    Binary configuration: 0
    Right Seed:    [14419085addd4740e5b3df7a3839d5dd6122a58236df61a539768640d1ab85cb]
    Left Witness:  [370d150620ab4f398692021780228f065b1cdd87e38c996bffe96e5e3aee0825]
    Right Witness: [f38d767ea19b8b671cdf6671ecfdc562e77ba4eab3ff71606d9ab28b5ee9be16]
    Height: 0
    Ed25519 Secret Key:       [32efc8b8038099d9bd38e53aa5491c6acaee75bf978f3d60a7a8d3157c2775ac]
    Ed25519 Verification Key: [58fc22cf26ccfe1f1c342fc4dce0983485055254f8189e1a0501c20223476cc9]
```
- Sigma t = 65535:
```
Sigma 1:
    Verification Key: [8efd4961b94185b774080d8d73e854d6da041e8a8740ca939a7b985131cd9af7]
    Sigma: [599510b9f0756c08dcc206e2ce23139b746cc58d5f6291904a7860c0b95478f673755c59c578930a0cb82e224443ac8dcb069b2f305fc1db6160cb12f9c5d209]
    W[0]: [cf19b592b3ad51d61aa20b456a6f511733f1d66227273eba1dc6529d54061cb5]
    W[1]: [b8ce88cf5a5eae81fff7422109a62db516c39d61243d1256cfceaae6dd8714af]
    W[2]: [5727ed843e553dfa32e4df015cd1836b59bd4d8bc54d4173cf023cdee8ed306f]
    W[3]: [f503f7d57187dcc951bb11eb87b1dc22e9a68e1e5e00452b47e919c27402c014]
    W[4]: [03c257b2b6dc3492de2530c5359b5f15e3b222b520a118d665e80d27d6217214]
    W[5]: [1064bb76a9712fd0028dd487728cd624b452eba63415efd3997e72cf33deec69]
    W[6]: [668e35cdadc67b993f8a9efa11be57e5cda0e0e6bf391d5495d70b9d31dd7588]
    W[7]: [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
Sigma 2:
    Verification Key: [906714b5583cd2006c17719af3be4a0208c821dbc4a09a45eb5c16af55b21db8]
    Sigma: [4e871a75074adb99564752f73603b88da4a0dc5ea9ab7e57c14a3d69bb43f694dc6728ad4ee6db9ca1d937a51f86cdc2ebaa7a261f279ecdb4f10ab146725f0c]
    W[0]: [9e7ce610f7cb7a9f1deb790863ac4a218927e6d4d5a991e861ed07f9c79f666c]
    W[1]: [aa873a4859c44def535e914287ed262ea3ced128008d36a0d0d6b3df8ff8517c]
    W[2]: [f907416961030fabe366ba926b97a9752f568a62fd1de95c61b83f87ab027252]
    W[3]: [f5a02136816c52ef95e6a4e4eea6ca632e93e96479cff59eec6fc83853bbb8b0]
    W[4]: [8365970698170ab80c5c0cd59ca0b25fc19533444bb232c0e171729abf292ade]
    W[5]: [d79947ba7fae57bf8c982e9ddad90ec681a576203574ed387f2f52ab7234617d]
    W[6]: [253205b551d5c9264ab0844e1204146e78ea45a13793c6527ee8c3b70a2b3f1b]
    W[7]: [48fc3de3e1f8dc48057bcdda5d155b577a4f4c20ec8f375112e6056516f345b1]
R 2: [8d89e9f4993691d5bf1998c32b8c8f22b70958351f79cf1368292e914e40df9e]
```
Product Composition Secret Key, t = 65535:
```
Tau 1:
    Height: 8
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
    Right Witness: [82a5642cd19f6246b3b69c26b69eccb327956050a05cf75d3c00d2cf7b9fa8f1]
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [668e35cdadc67b993f8a9efa11be57e5cda0e0e6bf391d5495d70b9d31dd7588]
    Right Witness: [afe557fcbecf9f77cc933b880b2c79d919d292e40660c76dca9c47b710e81bea]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [1064bb76a9712fd0028dd487728cd624b452eba63415efd3997e72cf33deec69]
    Right Witness: [c6a61d627050eddadc4dbc6a419cb24f760f2fbbd6e8705f0b264591b0241c10]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [03c257b2b6dc3492de2530c5359b5f15e3b222b520a118d665e80d27d6217214]
    Right Witness: [b2f2058179b692a5843c5c22a0eae92df2870a3e084faad9866b85de447fe3eb]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f503f7d57187dcc951bb11eb87b1dc22e9a68e1e5e00452b47e919c27402c014]
    Right Witness: [197b2f00147db5fec8593c05d437d5e195ad16faaaaec8b9eb9ba5218cd251af]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [5727ed843e553dfa32e4df015cd1836b59bd4d8bc54d4173cf023cdee8ed306f]
    Right Witness: [601067c536a477cc440fdcfa3fa21627eef5e42c91383ba462ac4d889bccbaf3]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [b8ce88cf5a5eae81fff7422109a62db516c39d61243d1256cfceaae6dd8714af]
    Right Witness: [a9b93c326082c8ecf07264a541669ca62aa88f50d0acb57b5ec90f7ccf8bf80d]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [cf19b592b3ad51d61aa20b456a6f511733f1d66227273eba1dc6529d54061cb5]
    Right Witness: [656da45f89158ab71b23dd279661ce1918896405a4d3dc5a73df40302c838acd]
    Height: 0
    Ed25519 Secret Key:       [0000000000000000000000000000000000000000000000000000000000000000]
    Ed25519 Verification Key: [8efd4961b94185b774080d8d73e854d6da041e8a8740ca939a7b985131cd9af7]
Sigma 1:
    Verification Key: [8efd4961b94185b774080d8d73e854d6da041e8a8740ca939a7b985131cd9af7]
    Sigma: [599510b9f0756c08dcc206e2ce23139b746cc58d5f6291904a7860c0b95478f673755c59c578930a0cb82e224443ac8dcb069b2f305fc1db6160cb12f9c5d209]
    W[0]: [cf19b592b3ad51d61aa20b456a6f511733f1d66227273eba1dc6529d54061cb5]
    W[1]: [b8ce88cf5a5eae81fff7422109a62db516c39d61243d1256cfceaae6dd8714af]
    W[2]: [5727ed843e553dfa32e4df015cd1836b59bd4d8bc54d4173cf023cdee8ed306f]
    W[3]: [f503f7d57187dcc951bb11eb87b1dc22e9a68e1e5e00452b47e919c27402c014]
    W[4]: [03c257b2b6dc3492de2530c5359b5f15e3b222b520a118d665e80d27d6217214]
    W[5]: [1064bb76a9712fd0028dd487728cd624b452eba63415efd3997e72cf33deec69]
    W[6]: [668e35cdadc67b993f8a9efa11be57e5cda0e0e6bf391d5495d70b9d31dd7588]
    W[7]: [0969dd98544b2cbfe4082682c3040687d0c4c78c912629246a05ffb896d7aa20]
Seed:
    bf1149b0ab1489bbc9b1af795e3f971f80922d5be6a5268dc3e56fd0a5f430f9
Tau 2:
    Height: 8
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [48fc3de3e1f8dc48057bcdda5d155b577a4f4c20ec8f375112e6056516f345b1]
    Right Witness: [b67063c590934e94dd7768dc755729dda512c6af2763da912375cc39ac9a2617]
    Height: 7
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [253205b551d5c9264ab0844e1204146e78ea45a13793c6527ee8c3b70a2b3f1b]
    Right Witness: [66f307eca606c4ece10ecd528104675cff1f8bf79041b28a4fc593eb7f0fdb94]
    Height: 6
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [d79947ba7fae57bf8c982e9ddad90ec681a576203574ed387f2f52ab7234617d]
    Right Witness: [bbf906a63577b7b74b5307162bc4625e6e91356535e73e0132dbe2c540b2da27]
    Height: 5
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [8365970698170ab80c5c0cd59ca0b25fc19533444bb232c0e171729abf292ade]
    Right Witness: [68e4f8f2c02f5e95fda0e8a31d94a46daab635b6aef5d5bc304ff426a788301b]
    Height: 4
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f5a02136816c52ef95e6a4e4eea6ca632e93e96479cff59eec6fc83853bbb8b0]
    Right Witness: [18794673cfe48509720a674c3c413234f3918bed21341b9728c1e1828a06c8ab]
    Height: 3
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [f907416961030fabe366ba926b97a9752f568a62fd1de95c61b83f87ab027252]
    Right Witness: [a0e796adfde578e95cf052474c3a9848872e3adb074dfa7e8c3b6d3451962ef3]
    Height: 2
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [aa873a4859c44def535e914287ed262ea3ced128008d36a0d0d6b3df8ff8517c]
    Right Witness: [6143d38759845238cc949b927060bbefbd84ec11f486c3a621ecc66bae32b402]
    Height: 1
    Binary configuration: 1
    Right Seed:    [0000000000000000000000000000000000000000000000000000000000000000]
    Left Witness:  [9e7ce610f7cb7a9f1deb790863ac4a218927e6d4d5a991e861ed07f9c79f666c]
    Right Witness: [9510ad34137ccc06502dcb7c2700641b2f2b2446fbca8cbb7918d62f16a2e181]
    Height: 0
    Ed25519 Secret Key:       [53f1b3b2be9f632a2a87bc29cef1c73c0e7226068549c6b0708763bfc6bb9cde]
    Ed25519 Verification Key: [906714b5583cd2006c17719af3be4a0208c821dbc4a09a45eb5c16af55b21db8]
```
