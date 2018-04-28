import cv2
import PIL.Image as img  
import os  
path_old = "/home/sjhbxs/code/ICDAR_TASK2_new3/test_data/train_words/"  

filelist = os.listdir(path_old)  
total_num = len(filelist) 
total_changed = 0 
for files in filelist:  
    im = img.open(path_old + files) 
    width, high = im.size
    
    if width > high:
        total_changed = total_changed + 1
        print("changing",total_changed)
        img_cv = cv2.imread(files)
        ng = im.transpose(img.ROTATE_90)  # 上下对换。  
        ng.save(path_old + files)  

