# 2022, RangeDet, Tusimple

## abstract
1. near far obj size
2. pixel coords diff from 3d Coords output


## Methods
1. 3 component： 1. FPN learn range, 2meta-conv, 3. weighted-NMS
2. weighted NMS: prop in full resolution
3. weighetd NMS: filter out < 0.5, weighted average of all box IOU >0.5 with b0
   
## DAta aug
1. rotation and translation aug in range view
2. range view occluded removal

## Achirtechrue
1. 8 channel in: range, density ,xyz, elongation, azimuth, incliantion,
2. elongation: 距角
3. featuer downsample 16
4. [0,80] -> 3 layers [0, 15), [15, 30), [30, 80]
5. 2 fc 64 filters
6. IOU pred: varifocal loss
7. regression target: box 中心点yaw角作为local 坐标系x轴
