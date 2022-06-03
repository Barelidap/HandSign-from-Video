# HandSign-from-Video

It is required to create 'frames' and 'cropped_imgs' folders in the same directory. 

Then for run:  For Linux - cd models && sh ./download-models.sh  For Windows - cd models && powershell .\download-models.ps1

Test_videos is a folder that simulates the real dataset.  
Models folder contains a Yolo model that is used for hand detection.  

blur_detection.py - deletes blur images.  
crop.py - uses Yolo model to detect a hand and crop its area (Yolo.size = 416, Yolo confidence threshold = 0.8, Crop padding =  10 pixels).  
debug.py - used only for debugging purposes.  
file.py - traverses though given root folder and saves paths to all the videos.  
frames.py - splits videos into frames and saves them in a given folder.  
source_2.py - the main source code that brings together all the algorithm.  

When you run the source_2.py, you will see a two progress bars. The first one is the main one that shows the progress of the program. The second one shows the progress of current file.  

![image](https://user-images.githubusercontent.com/31180324/171438506-7555a7b1-354a-44bc-9d23-e119a8608b42.png)  

Also, the log.txt file will be created in the same directory.  
