from fileinput import filename
import glob
import os
from skimage.metrics import structural_similarity as compare_ssim
import cv2
from yolo import YOLO
from tqdm import tqdm

from blur_detection import *
from frames import *
from crop import *
from files import *
#from debug import *
import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format = "%(asctime)s %(message)s")

all_vid_paths = get_all_videos('test_videos')

filename_counts = {}

i = 0
for folder in tqdm(all_vid_paths):
    new_folder = folder
    c_name = []

    for p in reversed(new_folder):
        if p == '\\': break

        c_name.append(p)
    str_name = ''.join(c_name)
    path = str_name[::-1]
    if not os.path.exists('cropped_imgs/'+str(path)):
        logging.info("created a new directory " + path)
        os.mkdir('cropped_imgs/'+str(path))

    if path in filename_counts:
        filename_counts[path] = filename_counts[path] + 1
        print(path+" in " + str(filename_counts[path]))
    else:
        filename_counts[path] = 0

    i+=1

fff = list(filename_counts.values())
vvv = list(filename_counts.keys())

print(fff)
print(vvv)

