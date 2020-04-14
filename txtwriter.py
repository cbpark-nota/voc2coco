import os
import sys

path = "Path/of/VOCdevkit/VOC2012/Annotations"
file_list = os.listdir(path)
file_list_xml = [file for file in file_list if file.endswith(".xml")]

f = open('xmllist.txt', "a")
for i in range(len(file_list_xml)):
    f.write(file_list_xml[i] + "\n")
