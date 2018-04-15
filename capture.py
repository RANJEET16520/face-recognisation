import cv2
import sys
import os

from util.constants.string_constants import data_folder, face_cascPath, users_data_folder
from util.constants.quality_constants import capture_freq, pics_per_user, max_pics_per_user
from lib.files import verify_folder
from lib.thanks import thanks


def gen_pic_path(user_folder, user_name, user_pic_id):
    return user_folder+"/user_id_"+user_name+"_"+str(user_pic_id)+".jpg"


def get_faceCascader():
    if(len(sys.argv)>1):
        cascPath = sys.argv[1]
    else:
        cascPath = face_cascPath

    faceCascade = cv2.CascadeClassifier(cascPath)
    return faceCascade


def get_faces(faceCascade,gray_image):
    faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    return faces


def save_face_image(face,gray_image,pic_path):
    x,y,w,h = face
    image = gray_image[y:y+h,x:x+w]
    cv2.imwrite(pic_path,image)


def main_loop(user_name):
    camera = cv2.VideoCapture(0)
    user_folder = users_data_folder + "/user_" +user_name

    # need to be started from last index
    user_pic_id = 0
    start_pic_id = user_pic_id # we began from here
    frame_with_face = 0
    faceCascade = get_faceCascader()

    while True:
        ret, frame = camera.read()
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = get_faces(faceCascade,gray_image)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if(len(faces)==1):
            frame_with_face += 1
            if(frame_with_face > capture_freq):
                pic_path = gen_pic_path(user_folder, user_name, user_pic_id)
                user_pic_id += 1
                save_face_image(faces[0],gray_image,pic_path)
                frame_with_face = 0

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if(user_pic_id > pics_per_user+start_pic_id):
            break

        if(user_pic_id > max_pics_per_user):
            print('limit of max pic per user reached ')
            # to be implemented
            break

    camera.release()


def capture():
    user_name = raw_input("Enter your user_name : ")
    user_folder = users_data_folder + "/user_" +user_name
    verify_folder(user_folder)

    main_loop(user_name)

    cv2.destroyAllWindows()
    thanks("Processing your information . . . ")


if(__name__=="__main__"):
    capture()
