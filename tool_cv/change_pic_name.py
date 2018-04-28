import os,sys
import numpy as np
import cv2,time
import re
data_dir = '/home/sjhbxs/code/ICDAR_TASK2_new1/train_data/out'
i = 0
for root, sub_folder, file_list in os.walk(data_dir):
            for file_path in file_list:
                try:
                    Olddir=os.path.join(root,file_path);
                    i = 1
                    if os.path.isdir(Olddir):
                        continue;
                    i = 2
                    filename=os.path.splitext(file_path)[0];
                    i = 3
                    filetype=os.path.splitext(file_path)[1];
                    i = 4
                    new_filename = '111_' + re.sub('[\r\n\t]', '',filename)
                    i = 5
                    Newdir=os.path.join(root, new_filename+filetype);
                    i = 6
                    os.rename(Olddir,Newdir);
                except:
                    print("wrong!!!",i)
                
