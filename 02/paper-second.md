## 2018 second

### keywords

* sparse conv
* angle loss regression
* new data augmentation
* dataset kitti 3d

### network structure

* vfe layer
* sparse conv
* RPN

### vfe layer

* point cloud grouping
  * iterate fill in voxel(not random sample, implementation depends)
  * voxel (0.4, 0.2, 0.2m)
  * max point per voxel T = 35
* VFE
  * T points $\rightarrow$ fcn
  * fcn $\in$ {linear, bn, ReLU}
  * max pooling on T
  * concat point-feature and aggragated feature

