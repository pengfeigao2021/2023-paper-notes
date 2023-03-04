# 2017, PointNet++, Guibas, Stanford

## Abstract
1. POintnet no local structure - finegrained pattern
2. hierarchical nn
3. nested partition
4. metric space distance
5. set learning


## Introduction
1. Point Net: each point feature -> aggregate
2. hierarchical
3. partition points
4. neighbor feature -> group feature
5. 1) partition 2) local feature
6. overlap partition
7. FPS - centeriods
8. neighbor scale = multiple
   

## Method
PointNet
1. continuous set
2. f: point set -> vector
3. $\gamma(MAX(h(x)))$
4. $\gamma$ = MLP
4. h = MLP


Hierarchical
1. point net = max pooling
2. larger and larger region
3. set abstraction
4. each level: set - new set
5. 3 layers: sampling, grouping, pointNet
6. sampling: points - centroids
7. grouping: find neighbor
8. point net: mini pointnet on local
9. distance: metric (pos + feature)
10. grouping: d metric distance neighbor

non-uniform sampling
1. adaptive point net
2. combine different scale
3. MSG MRG
4. multiscale feature extraction
5. MSG: scale - concat pointnet feature
6. MRG: resolution: solve large local neighbor issue
7. MRG: set abstraction on Li-1 concat point net on raw points

propagation
1. set abstration
2. pointset subsampled
3. point segmentation: propagate subsampled - original feature
4. hierarchical propagation
5. inverse disatnce weighted avearage
6. interpolate
7. unit point net
8. distance based interpolate
9. $f = \frac{\sum w f}{\sum w}$
10. $w = \frac{1}{d^p}$