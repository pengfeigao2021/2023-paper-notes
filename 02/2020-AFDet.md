

# 1. 2020, [AFDet](../../2022-paper-notes/3d-detection/singleframe/2020-AFDet.pdf)

## 1.1. abstract
1. embed system
2. not anchor, nms free, one stage
3. dataset KITTI, Waymo

## 1.2. intro
1. encoder: pointpillar
2. CNN backbone
3. 5 head: obj center - max pooling

## 1.3. Method
1. 5 head: center, offset, z, 3d size, orientation
2. center heatmap gt(only in bbox):
$$M_{xyc}= \Biggl\{
   \begin{array}{l}
   1\ d = 0;  \\
   0\ d = 1;  \\
   \frac{1}{d}, else
   \end{array}
$$
3. focal loss for center
怎么理解log项?
$$
L_{heat} = \Biggl\{ 
   \begin{array}{l}
   (1 - \hat{M})^\alpha log(\hat{M}),\ if M=1 \\
   (1 - M)^\beta(\hat{M})^\alpha log(1 - \hat{M})
   \end{array}
$$

4. reg offset: can move several pixels: how many? 
square: side length 2r+1
[可能涨点r=2]
5. reg offset: L1 loss
6. reg z: L1 loss: 
$$ L=\frac{1}{N}\sum|\hat{z} - z_{gt}| $$
7. reg size: L1 loss
8. orientation: 2 bins, 2*4 scalars
9. orientation: 
$$ [-\frac{7\pi}{6},\frac{\pi}{6}] $$
$$ [-\frac{\pi}{6},\frac{7\pi}{6}] $$
10. orientation: sin/cos value reg to bin center $\gamma_i$
11. orientation: cls: softmax, reg: L1 loss
12. orientation: 没懂 softmax(a,b) 是什么函数？
13. orientation: u 是 indicator

## LOSS
1. back propagation: only center (predicted center/ gt center?)
2. infer: max pooling + AND
3. object as points
4. weight: offset 1.0, orientation 1.0, size 0.3, z 1.5

## Network 
1. do not downsample
2. FLOPS: 
3. Range [(0,70.4), (-40,40), (-3,1)]
4. Data aug: uniform rotation 9deg, gaussian translation 0.25m, uniform global rotation 40deg

# 2. Related
1. Jiquan Ngiam, Benjamin Caine, Wei Han, Brandon Yang, Yuning Chai, Pei Sun, Yin Zhou, Xi Yi, Ouais Al- sharif, Patrick Nguyen, et al. Starnet: Targeted compu- tation for object detection in point clouds. arXiv preprint arXiv:1908.11069, 2019. 1, 8
2. CharlesRQi,WeiLiu,ChenxiaWu,HaoSu,andLeonidasJ Guibas. Frustum pointnets for 3d object detection from rgb-d data. In CVPR, 2018. 1, 2
3. Shaoshuai Shi, Xiaogang Wang, and Hongsheng Li. Pointr- cnn: 3d object proposal generation and detection from point cloud. In CVPR, 2019. 1, 2
4. Zhixin Wang and Kui Jia. Frustum convnet: Sliding frustums to aggregate local point-wise features for amodal 3d object detection. In IROS, 2019. 1
5. ZetongYang,YananSun,ShuLiu,XiaoyongShen,andJiaya Jia. Std: Sparse-to-dense 3d object detector for point cloud. In ICCV, 2019. 1, 2