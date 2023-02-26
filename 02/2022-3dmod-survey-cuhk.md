
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
1. 1-stage: voxel - head point -head
2. 2-stage: voxel - box - key point - ROI grid pooling - box refine
3. 1-stage: featuers bridge - backbone
4. 2-stage: PVRCNN - improve 2nd: RefinerNet, VectorPool, point wise attention scale aware pooling ROI grid attention channel wise Transformer, point density aware refinement module.
5. p&c: time cost in point voxel fusion. effientyly aggregate point. increase infer time

## Range based 3d det
1. dense image 2d 
2. pixel - distance info - not RGB
3. sutable view for det
4. conv, range dilated conv, meta/graph kernel conv, tranform BEV, transform point view
5. 2d: LaserNet, DLA-Net, U-Net, RPN,FPN
6. Range ops: pixels may be far away each other. dilated conv, graph op, meta kernel conv.
7. views: cylindrical view, range view, bev, pv
8. [latter experiment, improve close range yaw?]range view: vulnerable to occlusion and scale variaation. practical: det in BEV, feature in range view.

## Learning objective
1. anchor: 3d fix size
2. anchor loss: VoxelNet
3. anchor loss: binary cross entropy
4. BCE: $L=-[qlog(p)+(1-q)*log(1-p)]$ q=1,0, p = $\hat{p}$
5. Focal loss: $L=-\alpha(1-p)^\gamma log(p)$ $\alpha=0.25$ $\gamma=2$
6. anchor gt: $\Delta x = \frac{x^g-x^a}{d^a}$
7. gt: $\Delta l = log(\frac{l^g}{l^a})$
8. reg smoothL1 loss
9. anchor heading: radian smooth l1, gt: $\theta^g - \theta^a$
10. anchor heading: bin head $L=L_{dir}+smoothL1(\theta - \Delta \theta')$
11. anchor heading: sin/cos
12. IOU loss: $L_{IOU}=1-IOU$
13. Corner loss: $L=\sum||c^g - c||$ 8 corners
14. bad: large number of anchors: 7w for KITTI

## anchor free
1. select of positive and negative samples
2. grid based, point based, range based, set to set assignment
3. grid: PIXOR
4. grid: cetner point, smoothL1 loss reg
5. point: raw point segment + centerness score
6. range-based: range pixel inside box  = positive
7. set-to-set: DETR - 2d det - hungarian matching
8. chanllenge: select bad positive samples?
   
## 3d auxiliary task
