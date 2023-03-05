# 1. 2017, voxelnet, apple Inc, Tuzel

pointnet & voxelnet 标志3d det进入深度学习时代。

## 1.1. Abstract
1. unify 3d feature extraction and detection
2. equally spaced 3d voxel
3. VFE
4. RPN

## 1.2. Introduction
1. handcrafted feature bad
2. pointnet train ~1k points


## 1.3. Achitecture
1. feature learning - conv - rpn
2. voxel point num different - sample T
3. typical 100k = 10w points
4. stacked VFE
5. VFE-1: centroid - feature: [xyzr, x-vx,y-vy,z-vz] - fc - MaxPool - f'
6. fcn - linear - BN - ReLU
7. each point concat [f, f']
8. stack vfe - fc - max pool
9. sparse tensor
    

### 1.3.1. conv 
1. 3d conv: k,s,p

### 1.3.2. RPN
1. e2e trainable
2. input: conv emb
3. conv-1 block downsample by half + s=1 conv
4. upsample output of block and concat(FPN)
5. score map + regression map

## 1.4. loss funciton

1. anchors
2. 7 regression targets
3. xyz$\Delta x = \frac{x^g - x^a}{d^a}$
4. lhw $\Delta l = log(\frac{l^g}{l^a})$
5. $\theta = \theta^g - \theta^a$
6. binary cross entropy loss
7. smoothL1 loss
   
## implement GPU
1. K * T *7, K non-empty voxel, T num point, 7 point raw feature
2. foreach point - hash find voxel

## network detail
1. car: [-3, 1] [-40, 40] [0, 70.4]
2. vd = 0.4 vh=0.2 vw = 0.2
3. 10 * 400 * 352
4. T = 35
5. VFE-1 (7, 32)
6. VFE-2 (32, 128)
7. final FCN - R128
8. final VFE: 128 * 10 * 400 * 352
9. conv3d (128, 64, 3)
10. conv3d (64, 64, 3)
11. conv3d (64,64, 3)
12. output 64 * 2 * 400 * 352
13. reshape: 128 * 400 * 352 CHW
14. car - 1 anchor size
15. la = 3.9 wa = 1.6 ha = 1.56, 0, 90deg
16. IOU th 0.6 match
17. negative: IOU <0.45
18. alpha = 1.5, beta = 1.0 in pos loss and neg anchor loss

### ped and cyc 
1. [-3, 1] [-20, 20] [0, 48]
2. 10 * 200 * 240
3. T = 45
4. ped: la = 0.8 wa = 0.6 h = 1.73
5. cyc: la=1.76, wa=0.6, ha=1.73
6. IOU > 0.5 IOU < 0.35 other dontcare
7. lr0.001 B=16

## Data Aug
1. aug on the fly
2. rotate and tranlate bbox
3. collision detect
4. global scaling and rotation
