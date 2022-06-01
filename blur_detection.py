import glob
import os
from skimage.metrics import structural_similarity as compare_ssim
import cv2
from yolo import YOLO
from tqdm import tqdm
import logging

def blur_delete(files):
    logging.info("Started blur deleting")
    
    for file in tqdm(files):
        image = cv2.imread(file)

        if len(image) == 0:
            logging.warning("While blur detection image length == 0!  " + file)
            continue

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lapl_var = cv2.Laplacian(gray, cv2.CV_64F).var()

        if lapl_var<500.0:
            os.remove(file)



