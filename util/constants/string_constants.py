# string constants used in files

data_folder         = 'data_set'

users_data_folder   = data_folder+'/users'
users_data_json     = users_data_folder+'/users_data.json'


trained_data_folder = data_folder+'/trained_data'
trained_data_yml    = trained_data_folder+'/trained_data.yml'


face_cascPath       = data_folder+'/haarcascades/haarcascade_frontalface_default.xml'

blank_img_path      = 'util/nothing.jpg'


main_help = """
options
-h  : show help
-c  : capture mode
-r  : recogniser
-t  : train data
-f  : simple face detector (by default argument)
"""
