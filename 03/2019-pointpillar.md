# 2019, pointpillar, APTIV


## Abstract
1. pillar: column representation
2. detection at 62Hz. - 105Hz

## Introduction
1. point pillar - 2d conv nNN -> SSD
2. (DPN) D: 9-dim perpoint? P max pillars, N: max points per pillar
3. simple version: use fc + max pooling -> (CP) feature
4. D: (xyz, xcyczc, r, xp, yp) xp: to pillar center
5. focal loss + smooth L1