import numpy as np
import cv2

def found_obj (classifier, frame):
    found_objects = False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    objects = classifier.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
        )
    
    if len(objects) > 0:
        found_objects = True
        
    return found_objects