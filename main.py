import numpy as np
import cv2
import imutils
from imutils.video import VideoStream
import time
import datetime
from .face_detection import found_obj
from PIL import Image
from .post import post

classifier = cv2.CascadeClassifier('model/face_model.xml')
vs = VideoStream(src = 0).start()
time.sleep(2.0)
last_epoch = 0
update_interval = 30

while True:
    frame = vs.read()
    frame = imutils.resize(frame, width = 400)
    f_obj = found_obj(classifier, frame)
    date = datetime.datetime.now()
    template = date.strftime("%d-%m-%y-%H.%M.%S")
    
    if f_obj and (time.time()-last_epoch)> update_interval:
        last_epoch = time.time()
        time.sleep(1)
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),"RGB")
        img_dir = image.save("output/" + str(template)+".jpg")
        post(img_dir)

    
    cv2.imshow("Frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
vs.stop()