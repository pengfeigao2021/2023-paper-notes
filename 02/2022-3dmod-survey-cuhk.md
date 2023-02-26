
# 2022, 3d mod survey, cuhk, Hongsheng Li

## Abstract
1. 3d obj, cam, lidar, multimodal
2. performance analysis

## Intro
1. understand driving env: obj det&tracking,lane det,semantic/instance segmentation.
2. comparison of different 3d det
3. recent
4. 3d det from range image
5. self semi weakly supervised det
6. 3d det in end to end driving
7. all sensory types 
8. ni most apps

## Background
1. cam: no 3d structure info
2. lidar: m beams
3. lidar raw: range r azi alpha, inclin phi
4. spherical coordinate system
5. BEV, point view, cylindrical view
6. indoor dataset: ScanNet,SuN RGB-D, most room 10x10x3m, indoor high time complexity, high density around objects
7. dataset: KITTI,, larger:diversity,future: e2e dataset
8. metric: AP3d APbev, ap3d: 3d iou. APbev bev iou
9. PKL: KL-div of future planning path, need pretrained motion planner. SDE: mininal distance to ego vihicle, need contruct boundaries

## Lidar 3d det
1. point based, grid-based, point-voxel based, range based.
2. prob: point sparse, irregular, range image dense, pixel is 3d info.

## Point based lidar det
1. directly from raw points
2. points sampled
3. sampling: FPS, segmnetaiton sampling, voxel based sampling
4. feature learning: SA, GNN, Transformer
5. feature learning: context collected from r ball
6. context point + feature - mlp - max pooling
7. limitation: number of context points, r too large: lost detail
8. lim: sampling take inference time. random sampling will lost low density region/obj, FPS is seq, cannot parallel.
9. FPS: seqly choose furtherest point

## grid based
1. point - grid
2. voxel, pillar, BEV feature map
3. 2d conv, 3d sparse
4. grid based repr and network
5. voxel: voxelnet
6. pilllar: pointNet encoding
7. multiview voxel: bev + perspective view, cylindrical and spherical, range view
8. multi scale voxel, reconfigurable voxel.
9. Pillars. 
10. bEV: dnese 2d, occupancy, height and density of points
11. grid based nn: 2d conv ,3d sparse nn
12. [most widely]3d sparse conv: sparse conv / submanifolde con
13. voxel repr 3d information
14. bev repr high efficient
15. pillar repr balance
16. chooose voxel size: smaller - memory comsumption

## Point voxel based