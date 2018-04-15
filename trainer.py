import cv2
import sys
import os
import numpy as np
from PIL import Image


from util.constants.string_constants import users_data_folder, face_cascPath, trained_data_folder
from util.constants.quality_constants import capture_freq
from util.temp_id_gen import temp_id_gen
from lib.files import verify_folder
from lib.thanks import thanks


def get_user_folders_in_path(path):
    folders = []
    child_paths = [ os.path.join(path,obj) for obj in os.listdir(path) ]
    for child_path in child_paths:
        if (os.path.isdir(child_path)):
            name = os.path.split(child_path)[-1]
            if(name.split('_')[0]=='user'):
                name = name.split('_')[-1]
                folders.append([name,child_path])
    return folders


def get_files_in_path(path):
    files = []
    child_paths = [ os.path.join(path,obj) for obj in os.listdir(path) ]
    for child_path in child_paths:
        if(os.path.isfile(child_path)):
            if(child_path.split('.')[-1]=='jpg'):
                files.append(child_path)
    return files


def getImagesWithId():
    folders = get_user_folders_in_path(users_data_folder)
    IDs = []
    faces = []
    for folder in folders:
        user_name = folder[0]
        # needs to be implemented
        user_id = temp_id_gen(user_name)

        pic_paths = get_files_in_path(folder[1])
        for pic_path in pic_paths:
            faceImg = Image.open(pic_path).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            faces.append(faceNp)
            IDs.append(user_id)
            cv2.imshow("training",faceNp)
            cv2.waitKey(5)
    return IDs, faces


def recogniser():
    # recogniser = cv2.createLBPHFaceRecognizer()
    recogniser = cv2.face.LBPHFaceRecognizer_create()
    Ids, faces = getImagesWithId()

    verify_folder(trained_data_folder)
    recogniser.train(faces,np.array(Ids))
    trained_data_yml = trained_data_folder + '/trained_data.yml'
    recogniser.write(trained_data_yml)

    cv2.destroyAllWindows()
    thanks('Processing your information . . . ')


if(__name__=="__main__"):
    recogniser()
