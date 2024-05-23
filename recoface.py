# recoface.py temporary filename = regognize face lol
import cv2
import numpy as np
import os

# size parameter
size = 4

# Please customize the file path according to your system configuration 
haar_file = 'C:\\Lendelcosep\\Codedumps\\repos\\CSC126_FINALS_GROUPTEMP\\haarcascade_frontalface_default.xml'
datasets = 'C:\\Lendelcosep\\Codedumps\\repos\\CSC126_FINALS_GROUPTEMP\\datasets'

# LBPH face recognizer
print('Recognizing Face. Please be in sufficient lighting...')

# lists hold images, labels, and a dictionary to hold names
(images, labels, names, id) = ([], [], {}, 0)

# Fixed size for images
(width, height) = (130, 100)

# loop through dataset directory and load images and labels
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)
            label = id
            # Read image in grayscale
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Warning: Skipping image {path}, unable to read.")
                continue
            # Resize the image
            img = cv2.resize(img, (width, height))
            images.append(img)
            labels.append(label)
        id += 1

# Convert lists
images = np.array(images)
labels = np.array(labels)

# Train the LBPH face recognizer
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

#Use trained recognizer on video stream
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    # capture and check frame
    ret, im = webcam.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    # convert to grayscale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # draw shape extract region and resize face region
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        
        # Try to recognize the face
        prediction, confidence = model.predict(face_resize)
        
        # draw shape with text for result
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if confidence < 500:
            cv2.putText(im, f'{names[prediction]} - {confidence:.0f}', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
        else:
            cv2.putText(im, 'not recognized', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
    # display
    cv2.imshow('OpenCV', im)
    
    key = cv2.waitKey(10)
    if key == 27:  # Press 'ESC' to exit
        break

webcam.release()
cv2.destroyAllWindows()