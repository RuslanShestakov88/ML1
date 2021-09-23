import os
import matplotlib as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

target = []
images = []
flat_data = []

DATADIR = 'images/'
CATEGORIES = ['traffic cone',]

for category in CATEGORIES:
    class_num = CATEGORIES.index(category)
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = imread(os.path.join(path, img))
        #print(img_array)
        #print(img_array.shape)
        #img_resized = resize(img_array(150,150,3))
        #flat_data.append(img_resized.flatten())
        flat_data.append(img_array.flatten())
        images.append(img_array)
        target.append(class_num)

flat_data = np.array(flat_data)
target = np.array(target)
images = np.array(images)

print(flat_data[0])

a = np.array([[1,2,3,4,5],
              [4,5,6,7,8]])
a.ndim
print(a.flatten())