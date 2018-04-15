import os

def verify_folder(folder):
    if not os.path.exists(folder):
        print('creating folder '+ folder)
        os.makedirs(folder)
    elif os.path.isfile(folder):
        print('there exists file of same name')

def verify_file(file_path):
    if not os.path.exists(file_path):
        print('creating file '+ file_path)
        file_ = open(file_path, 'w')
        file_.close()
    elif os.path.isdir(file_path):
        print('there exists folder of same name')

