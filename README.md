# voc2coco
Make COCO annotation format .json file from Pascal VOC annotation xml file


# How to use
1. Use txtwriter.py to make xmllist.txt
xmllist.txt contain xml file names like this

2007_000027.xml\n
2007_000032.xml\n
2007_000033.xml\n
2007_000039.xml\n
2007_000042.xml\n
2007_000061.xml\n
2007_000063.xml\n
2007_000068.xml\n
2007_000121.xml\n


2. Use voc2coco.py to make .json file
Example command: python voc2coco.py xmllist.txt path/of/VOCdevkit/VOC2012/Annotations output.json
