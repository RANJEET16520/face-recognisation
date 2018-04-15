import cv2,os
import numpy as np
from PIL import Image
import pickle

from util.temp_id_gen import temp_name_gen
from util.constants.string_constants import trained_data_folder, face_cascPath
from lib.thanks import thanks

recognizer = cv2.face.LBPHFaceRecognizer_create()
trained_data_yml = trained_data_folder+'/trained_data.yml'
recognizer.read(trained_data_yml)
faceCascade = cv2.CascadeClassifier(face_cascPath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for(x,y,w,h) in faces:
        nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)

        roll = str(nbr_predicted)
        nbr_predicted = temp_name_gen(roll)

        cv2.putText(im,str(nbr_predicted),(x,y+h), font, 1,(255,255,255))

    cv2.imshow('im',im)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

thanks()
