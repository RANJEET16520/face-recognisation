import cv2
import sys

from constants.string_constants import face_cascPath

def face_detector():
    cascPath = default_cascPath
    faceCascade = cv2.CascadeClassifier(face_cascPath)
    video_capture = cv2.VideoCapture(0)
    blank_img = cv2.imread(blank_img_path,0)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if(__name__=="__main__"):
    face_detector()
