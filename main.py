import os
import matplotlib as plt
import numpy as np
from skimage.io import imread
from skimage.transform import resize

target = []
image = []
flat_data = []

DATADIR = 'images/'
CATEGORIES = ['traffic cone',]

for category in CATEGORIES:
    class_num = CATEGORIES.index(category)
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = imread(os.path.join(path, img))
        print(img_array)

