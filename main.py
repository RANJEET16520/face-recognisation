from sys import exit,argv

from srbColour import Colour
from constants/string_constants import main_help
from lib.face import face_detector
















if(__name__=='__main__'):
    if(len(argv)<2):
        face_detector()
    elif(argv[1]=='-h'):
        print(main_help)
    elif(argv[1]=='-c'):
        print('capturing data')
    elif(argv[1]=='-r'):
        print('running recogniser')
    elif(argv[1]=='-t'):
        print('training please wait ')
    elif(argv[1]=='-f'):
        print('Detecting faces in picture')


