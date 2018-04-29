from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import os
from keras import backend as K
import cv2
K.set_image_dim_ordering('th')
# load data
imput_data_dir = "C:/Users/jieyang/Desktop/1/"
save_data_dir_width = "C:/Users/jieyang/Desktop/2/"
save_data_dir_height = "C:/Users/jieyang/Desktop/3/"
if os.path.isdir(save_data_dir) == False:
    os.makedirs(save_data_dir)
max_width_shift = 2
max_height_shift = 3


# define data preparation
datagen_width_shift_range = ImageDataGenerator(width_shift_range = max_width_shift)
datagen_height_shift_range = ImageDataGenerator(height_shift_range = max_height_shift)


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
        
        datagen_width_shift_range.fit(im)
        count_time = 0
        for X_batch in datagen_width_shift_range.flow(im, batch_size=1, save_to_dir=save_data_dir_width, save_prefix = "widthshift_" + str(image_num_string) + "%%%", save_format='jpg'):
            count_time += 1
            if count_time > 0:
                break
        
        datagen_height_shift_range.fit(im)
        count_time = 0
        for X_batch in datagen_height_shift_range.flow(im, batch_size=1, save_to_dir=save_data_dir_height, save_prefix="heightshift_" + str(image_num_string) + "%%%", save_format='jpg'):
            count_time += 1
            if count_time > 0:
                break
