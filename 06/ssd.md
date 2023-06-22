# ssd: Single Shot MultiBox Detector
year: 2016
Wei Liu1
Dragomir Anguelov2
1UNC Chapel Hill 2Zoox Inc. 3<b>Google Inc.</b> 4University of Michigan, Ann-Arbor
$$\delta J(x, \delta x)  = \int^1_0 {[2x(t)+2] \delta x(t)} dt $$

##  Our approach, named SSD, discretizes the output space of bounding boxes into ------. At prediction time, the network generates scores for the presence of each object category in each default box and produces adjustments to the box to better match the object shape. 
 Our approach, named SSD, discretizes the output space of bounding boxes into <b style="color:green">a set of default boxes over different aspect ratios and scales per feature map location </b>. At prediction time, the network generates scores for the presence of each object category in each default box and produces adjustments to the box to better match the object shape. 

 ## Additionally, the network combines predictions from multiple ----- to naturally handle objects of various sizes. 
 Additionally, the network combines pre- dictions from <b>multiple feature maps with different resolutions</b> to naturally handle objects of various sizes. 

 ## This paper presents the first deep network based object detector that does not re- sample pixels or features for bounding box hypotheses and and is as accurate as ap- proaches that do. This results in a significant improvement in speed for high-accuracy detection (-- FPS with mAP -- on VOC2007 test, vs. Faster R-CNN -- FPS with mAP 73.2% or YOLO -- FPS with mAP 63.4%). The fundamental improvement in speed comes from eliminating ---- and the subsequent pixel or feature resampling stage. 
 This paper presents the first deep network based object detector that does not re- sample pixels or features for bounding box hypotheses and and is as accurate as ap- proaches that do. This results in a significant improvement in speed for high-accuracy detection (59 FPS with mAP 74.3% on VOC2007 test, vs. Faster R-CNN 7 FPS with mAP 73.2% or YOLO 45 FPS with mAP 63.4%). The fundamental improvement in speed comes from eliminating <b>bounding box proposals</b> and the subsequent pixel or fea- ture resampling stage. 


 ## SSD framework. (a) SSD only needs an input image and ground truth boxes for each object during training. In a convolutional fashion, we evaluate a small set (e.g. 4) of ____ of different ____ at each location in several feature maps with different ____ (e.g. 8 × 8 and 4 × 4 in (b) and (c)). For each default box, we predict both the ____and the ____ ((c1 , c2 , · · · , cp )). At training time, we first match these default boxes to the ground truth boxes. For example, we have matched two default boxes with the cat and one with the dog, which are treated as positives and the rest as negatives. The model loss is a ____ between localization loss (e.g. Smooth L1 [6]) and confidence loss (e.g. Softmax).

 Fig. 1: SSD framework. (a) SSD only needs an input image and ground truth boxes for each object during training. 
 In a convolutional fashion, we evaluate a small set (e.g. 4) of default boxes of different aspect ratios at each location in several feature maps with different scales (e.g. 8 × 8 and 4 × 4 in (b) and (c)). 
 For each default box, we predict both the shape offsets and the confidences for all object categories ((c1 , c2 , · · · , cp )). 
 At training time, we first match these default boxes to the ground truth boxes. For example, we have matched two default boxes with the cat and one with the dog, which are treated as positives and the rest as negatives. 
 The model loss is a weighted sum between localization loss (e.g. Smooth L1 [6]) and confidence loss (e.g. Softmax).

## SSD consists of base network and ssd head. the base network is __?
 The early network layers are based on a standard architecture used for high quality image classification (truncated before any classification layers)

## SSD consists of base network and ssd head. the ssd head is __?
a feed-forward convolutional network that produces a fixed-size collection of bounding boxes and scores for the presence of object class instances in those boxes, followed by a non-maximum suppression step to produce the final detections

## Multi-scale feature maps for detection We add convolutional feature layers to the end of the truncated base network. These layers decrease in size progressively and allow predictions of detections at _____. The convolutional model for predicting detections is different for each feature layer (cf Overfeat[4] and YOLO[5] that operate on a single scale feature map).

Multi-scale feature maps for detection We add convolutional feature layers to the end of the truncated base network. These layers decrease in size progressively and allow predictions of detections at multiple scales. The convolutional model for predicting detections is different for each feature layer (cf Overfeat[4] and YOLO[5] that operate on a single scale feature map).

## At each feature map cell, we predict the offsets relative to the default box shapes in the cell, as well as the per-class scores that indicate the presence of a class instance in each of those boxes. Specifically, for each box out of k at a given location, we compute c class scores and the 4 offsets relative to the original default box shape. This results in a total of _____ filters that are applied around each location in the feature map, yielding _____ outputs for a m × n feature map.

(c + 4)k 
(c + 4)kmn 
 

## Unlike MultiBox, we then match default boxes to any ground truth with _____. This simplifies the learning problem, allowing the network to predict high scores for multiple overlapping default boxes rather than requiring it to pick only the one with maximum overlap.

jaccard overlap higher than a threshold (0.5)

## Hard negative mining After the matching step, most of the default boxes are nega- tives, especially when the number of possible default boxes is large. This introduces a significant imbalance between the positive and negative training examples. Instead of using all the negative examples, we sort them using the ______. We found that this leads to faster optimization and a more stable training.

Hard negative mining After the matching step, most of the default boxes are nega- tives, especially when the number of possible default boxes is large. This introduces a significant imbalance between the positive and negative training examples. Instead of using all the negative examples, we sort them using the highest confidence loss for each default box and pick the top ones so that the ratio between the negatives and positives is at most 3:1. We found that this leads to faster optimization and a more stable training.
