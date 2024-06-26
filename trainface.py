# trainface.py temporary file name 
import cv2
import sys
import numpy as np
import os

# Note:
# Please customize the file path according to your system configuration

# create folder and uses the name passed by trying.py
def create_subdata_folder(sub_data_name):
    # define and combine directories
    datasets_dir = 'C:\\Lendelcosep\\Codedumps\\repos\\CSC126_FINALS_GROUPTEMP\\datasets'
    sub_data_path = os.path.join(datasets_dir, sub_data_name)
    # check if subfolder exist
    if not os.path.isdir(sub_data_path):
        os.makedirs(sub_data_path)
    return sub_data_path

# runs the training part
def train_face(sub_data_name):
    sub_data_path = create_subdata_folder(sub_data_name)
    path = sub_data_path

    # load classifier and set resizing dimensions
    haar_file = 'C:\\Lendelcosep\\Codedumps\\repos\\CSC126_FINALS_GROUPTEMP\\haarcascade_frontalface_default.xml'
    (width, height) = (130, 100)

    # create classifier object
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)

    count = 1
    # image limit 
    while count < 30:
        (_, im) = webcam.read()
        # convert to grayscale
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            # draw around face
            cv2.rectangle(im, (x,y), (x + w, y + h), (255, 0, 0), 2)
            # extract region of interest
            face = gray[y:y + h, x:x + w]
            # resize then save image
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite('%s/%s.png' % (path, count), face_resize)
        count += 1


        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # check number of command line args
    if len(sys.argv) != 2:
        print("Usage: python train_face.py <sub_data_name>")
        sys.exit(1)

    # extract name from command line then call function
    sub_data_name = sys.argv[1]
    train_face(sub_data_name)
