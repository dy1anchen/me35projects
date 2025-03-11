#import libraries 
from picamera2 import Picamera2 
import cv2 as cv 
from libcamera import controls
import time

picam2 = Picamera2()

#configure the picamera
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous}) #sets auto focus mode

picam2.start() #must start the camera before taking any images
time.sleep(1)

name = input("enter file name: ")

input("type 'start' to beign photo capture: ")

#take range photos
for i in range(500):
    img_name = name + str(i) + '.jpg'
    picam2.capture_file(img_name) #take image 
    print(str(i + 1))
    time.sleep(0.1)

picam2.stop() #stop the picam 