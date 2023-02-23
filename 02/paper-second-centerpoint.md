## 2018 second

keywords

* sparse conv
* angle loss regression
* new data augmentation
* dataset kitti 3d

network structure

* vfe layer
* sparse conv
* RPN

vfe layer

* point cloud grouping
  * iterate fill in voxel(not random sample, implementation depends)
  * voxel (0.4, 0.2, 0.2m)
  * max point per voxel T = 35
* VFE
  * T points $\rightarrow$ fcn
  * fcn $\in$ {linear, bn, ReLU}
  * max pooling on T
  * concat point-feature and aggragated feature


## 2021 center point
abstract

1. key point detector
2. reg size pos angle
3. velocity
4. nearest matching

dataset

1. nuscenes
2. waymo


structure

1. Backbone output dense feature 
2. center heatmap head : focal loss . 2. Gaussian: increase positive supervision  
2. Sigma = f(w,l) gaussian 
3. Reg head ：
  * height above ground=center z 
  * （sin,cos)
4. Velocity head 
5. Tracking 

pre

1. centernet 2d
2. Reg size map
3. Offset：quantization error 

3d detection 

1. Box in bev 
2. Backbone voxel net and point pillar 
3. 
