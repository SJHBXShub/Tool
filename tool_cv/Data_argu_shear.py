from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import os
from keras import backend as K
import cv2
K.set_image_dim_ordering('th')
# load data
imput_data_dir = "C:/Users/jieyang/Desktop/1/"
save_data_dir_shear = "C:/Users/jieyang/Desktop/3/"
if os.path.isdir(save_data_dir) == False:
    os.makedirs(save_data_dir)

max_shear_range = 5

# define data preparation
datagen_shear_range = ImageDataGenerator(shear_range = max_shear_range)

for root, sub_folder, file_list in os.walk(imput_data_dir):
    for file_path in file_list:
        print("!!!!!!!!!!!!!", file_path)
        image_name = os.path.join(root,file_path)
        image_num_string = file_path.split('.')[0]
        im = cv2.imread(image_name,1)#/255.#read the gray image
        shape = im.shape
        im = im.transpose(2,0,1)
        im = im.reshape(1, shape[2], shape[0], shape[1])
        im = im.astype('float32')
        
        datagen_rotation.fit(im)
        count_time = 0
        for X_batch in datagen_shear_range.flow(im, batch_size=1, save_to_dir=save_data_dir_rotation, save_prefix = "shear0" + "_" + str(image_num_string) + "%%%", save_format='jpg'):
            count_time += 1
            if count_time > 0:
                break
        for X_batch in datagen_shear_range.flow(im, batch_size=1, save_to_dir=save_data_dir_rotation, save_prefix = "shear1" + "_" + str(image_num_string) + "%%%", save_format='jpg'):
            count_time += 1
            if count_time > 0:
                break

for root, sub_folder, file_list in os.walk(save_data_dir_rotation):
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
                    new_filename = filename.split("%%%")[0]
                    i = 5
                    Newdir=os.path.join(root, new_filename+filetype);
                    i = 6
                    os.rename(Olddir,Newdir);
                except:
                    print("wrong!!!",i)