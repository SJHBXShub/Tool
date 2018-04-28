# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:50:06 2018

@author: jieyang
"""
import os
import time
import re
num_string = {}

pic_dir = r'/home/sjhbxs/code/ICDAR_TASK2/train_data/train'
filelist=os.listdir(pic_dir)#该文件夹下所有的文件（包括文件夹）
for files in filelist:#遍历所有文件
    contant_line = str(files)
    num = contant_line.split('_')[0]
    string_line = contant_line.split('_')[1]
    if len(string_line) == 0:
        print("zero: ",num)
    if len(string_line)>35:
        print("max: ",num)
