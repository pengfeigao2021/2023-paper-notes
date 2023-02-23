# 1. 2019, Point Voxel
用voxel 操作近似 找每个点邻域内的点的操作。
## 1.1. Abstract

1. MIT
2. song han
3. PVCNN
4. voxel: memory grow cubically
5. point: 80% structuring sparse data
6. PVCNN: repr in point, conv in voxel
7. object det - better than Frustrum PointNet 2.4% mAP.

## 1.2. Introduction
1. 3D-Unet 10GB memory 64x64x64
2. reduce random memory access: reduce bank conflicts
3. off-chip DRAM access
4. consider hardware
5. repr as point cloud

## 1.3. Related
1. hardware-efficient dl
2. voxel based 3d 
3. ponit based 3d
4. special purpose 3d

## 1.4. motivation
1. yk = sum(K(xk,xi)*F(xi))
2. neighbor of xk
3. resolution 64 -> GPU 12GB?? large
4. point based: irregular mem access
5. point based: dynamic kernal(conv distance is not fixed e.g conv3 0,1,-1)

## 1.5. Point Voxel Conv
1. Normalization: pc gravity center
2. Norm: div max|pk|2 , move to [0,1]
3. Voxelization: avg feature in voxel (uvw)
4. PVConv: 2 branch: low resolution voxel high res point branch
5. stack 3D vol conv
6. relu + bn
7. assign point in voxel same feature -> trilinear interpolation -> point feature
8. point -> MLP -> point feature
9. feature fusion?

## 1.6. Advantage
1. Efficiency: better data locality regularity: O(N) point access
2. compare: PointNet++ O(kN) k=32/64
3. compare PointCNN k=16
4. Effective keeping points in high res
