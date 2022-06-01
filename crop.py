import glob
import os
from skimage.metrics import structural_similarity as compare_ssim
import cv2
from tqdm import tqdm

from yolo import YOLO

from frames import *
import logging



def detect_crop(files, save_to, fn_c):
    yolo = YOLO("models/cross-hands.cfg", "models/cross-hands.weights", ["hand"])

    yolo.size = int(416)
    yolo.confidence = float(0.8)

    conf_sum = 0
    detection_count = 0
    saved = False
    j = 0
    k = 0
    logging.info("Started cropping")
    for file in tqdm(files):
        mat = cv2.imread(file)
        #vidObj = cv2.VideoCapture(file)

        #success, mat = vidObj.read()
        

        width, height, inference_time, results = yolo.inference(mat)

        output = []
        i = 0

        for detection in results:
                    
            id, name, confidence, x, y, w, h = detection

            conf_sum += confidence
            detection_count += 1

            crop_img = mat[y-10:y+h+10, x-10:x+w+10]
            
            if len(crop_img) == 0:
                logging.warning("While cropping image length == 0!  " + file)
                continue
            
            cv2.imwrite(save_to+"/"+str(k)+"_"+str(i)+'_'+str(fn_c)+'cropped.jpg', crop_img)
            i+=1
        k+=1

    
    for file in files:
        os.remove(file)
    logging.info("Cleared the frames directory")
        
