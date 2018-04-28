# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:50:06 2018

@author: jieyang
"""
import os
import time
import re
num_string = {}
f = open(r'/home/sjhbxs/coco/data/cropped_data/val_words_gt.txt',"r")  
line = f.readline()  
while line:  
    contant_line = str(line)
    if ',' in contant_line:
        num = contant_line.split(',')[0]
        string_line = contant_line.split(',')[1]
    else:
        line = f.readline()  
        continue
    if string_line[0] == '|':
        string_line = contant_line.split('|')[1]
    string_line = re.sub('[\r\n\t]', '', string_line)
    num_string[num] = str(string_line)
    #print(num,": ",num_string[num],":---len",len(num_string[num]))
    line = f.readline()  
f.close()
'''
print("!!!!!!!!!!!!!!!!!!!!!read line OK")
pic_dir = r"/home/sjhbxs/coco/data/cropped_data/format_val_data/"
i = 0;
filelist=os.listdir(pic_dir)
for files in filelist: 
     try:
         Olddir=os.path.join(pic_dir,files);
         if os.path.isdir(Olddir):
             continue;
         filename=os.path.splitext(files)[0];
         filetype=os.path.splitext(files)[1];
         new_filename = filename + '_' + re.sub('[\r\n\t]', '', num_string[str(filename)]) + '_'
         Newdir=os.path.join(pic_dir,new_filename+filetype);
         os.rename(Olddir,Newdir);
     except:
        i = i + 1
        print("!!!!!!",files,"---",i)
'''
print("!!!!!!!!!!!!!!!!!!!!!!!!OK")
