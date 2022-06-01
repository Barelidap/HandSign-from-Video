import cv2
import glob
import logging

def split_by_frames(from_path, to_path):
  i = 0
  files = sorted(glob.glob("%s/*.mp4" % from_path))
  logging.info("Started spliting by frames")

  for file in files:
    vidcap = cv2.VideoCapture(file)
    success,image = vidcap.read()

    count = 0
    while success:

      cv2.imwrite(to_path+"/"+str(i)+"vid_"+str(count)+"frame"+".jpg", image)     # save frame as JPEG file      
      success,image = vidcap.read()
      count += 1
    i+=1
