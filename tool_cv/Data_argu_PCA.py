import numpy as np  
import os  
from PIL import Image, ImageOps  
import argparse  
import random  
from scipy import misc 
img_path = "C:/Users/jieyang/Desktop/1"
save_img_path = "C:/Users/jieyang/Desktop/2"
generate_times = 5
def PCA_Jittering(path,cur_time):  
    img_list = os.listdir(path)  
    img_num = len(img_list)  
      
    for i in range(img_num):  
        img_path = os.path.join(path, img_list[i])  
        img = Image.open(img_path)  
          
        img = np.asanyarray(img, dtype = 'float32')  
          
        img = img / 255.0  
        img_size = int(img.size / 3)  
        img1 = img.reshape(img_size, 3)  
        img1 = np.transpose(img1)  
        img_cov = np.cov([img1[0], img1[1], img1[2]])  
        lamda, p = np.linalg.eig(img_cov)  
          
        p = np.transpose(p)  
          
        alpha1 = random.normalvariate(0,3)  
        alpha2 = random.normalvariate(0,3)  
        alpha3 = random.normalvariate(0,3)  
          
        v = np.transpose((alpha1*lamda[0], alpha2*lamda[1], alpha3*lamda[2]))      
        add_num = np.dot(p,v)  
          
        img2 = np.array([img[:,:,0]+add_num[0], img[:,:,1]+add_num[1], img[:,:,2]+add_num[2]])  
          
        img2 = np.swapaxes(img2,0,2)  
        img2 = np.swapaxes(img2,0,1)  
        save_name = "PAC Jittering" + str(cur_time) + "_" + img_list[i]
        '''
        if os.path.isdir(save_img_path + "/" + str(cur_time) +"/") == False:
            os.makedirs(save_img_path + "/" + str(cur_time) +"/")
        '''
        save_path = os.path.join(save_img_path, save_name)  
        misc.imsave(save_path,img2)  

if __name__ == '__main__':
    for i in range(generate_times):
        print("curr", i)
        PCA_Jittering(img_path, cur_time = i)