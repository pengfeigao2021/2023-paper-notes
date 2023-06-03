# 2019, cornernet
1. detect obj as paired keypoints
2. cornerpooling
3. anchor box: 1. needs more than 40k/100k retinaNet, imbalance pos/neg cases.
4. anchor box: 2 choose hyperparam for anchor boxes, aspect ratio, etc. heuristics.
5. top-left and bottom right corner: seperate head?
6. corner pooling: max pooling right and below, 2 feature maps
7. center: depends on 4 sides of box
8. corners: depends on 2 sides of box
9. anchors: O(W * H * W * H) possible combinations
10. corners: O(W * H ) combinations.
11. backbone: hourglass network