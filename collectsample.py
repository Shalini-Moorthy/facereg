from flask import Flask,render_template,request
import cv2
import numpy as np
import os
face_classifier=cv2.CascadeClassifier('C:/Python/Python392/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def face_extractor(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return  None
    for(x,y,w,h) in faces:
        cropped_face=img[y:y+h,x:x+w]
    return cropped_face
def collect(ID)   :
    cap =  cv2.VideoCapture(0)
    count=0
    dir = "UserID" + str(ID)
    par_directory = "C:/Users/shalini/Desktop/sotproject/faces/"
    path = os.path.join(par_directory, dir)
    os.mkdir(path)
    while True:
        ret, frame=cap.read()
        if face_extractor(frame) is not None:
            count+=1
            face=cv2.resize(face_extractor(frame),(200,200))
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

            file_name_path='C:/Users/shalini/Desktop/sotproject/faces/UserID'+str(ID)+'/count'+str(count)+'.jpg'
            print(file_name_path)
            cv2.imwrite(file_name_path,face)
            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('face cropper',face)
        else:
            print('face not found')
            pass
        if cv2.waitKey(1)==13 or count==10:
            break
    cap.release()
    cv2.destroyAllWindows()
    print('collecting samples completed')
    return render_template("MessageSampleCollected.html")