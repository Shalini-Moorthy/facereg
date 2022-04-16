import cv2
#ONE MORE FILE FOR FACE DETECTION ALONE THIS DOESN'T TRAIN OR COLLECT DATA

face_classifier=cv2.CascadeClassifier('C:/Python/Python392/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

def face_detector(img,size=0.5):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return img,[]
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+y),(0,255,255),2)
        roi = img[y:y+h,x:x+w]
        roi= cv2.resize(roi,(200,200))

    return img,roi

def recognize(ID):
    cap=cv2.VideoCapture(0)
    model=cv2.face.FisherFaceRecognizer_create()
    model.read('C:/Users/shalini/Desktop/sotproject/fishermodels/model'+str(ID)+'.yml')
    count=0
    minC=3500

    while count<10:
        ret,frame=cap.read()
        image,face=face_detector(frame)

        try:
            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

            result=model.predict(face)
            print(result[1])
            if result[1]<3500:
                confidence=result[1]
                if confidence<minC:
                    minC=confidence
                display_string=str(confidence)+'% confident it is user'
            cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)
            if confidence>80:
                cv2.putText(image, "Recognized", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow("Face Cropper",image)


            else:
                cv2.putText(image, "Not Recognized", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0,255), 2)
                cv2.imshow("Face Cropper", image)

        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow("Face Cropper", image)
            pass
        count+=1
        print(count)

        if cv2.waitKey(1)==13:
            break
    cap.release()
    cv2.destroyAllWindows()

    return minC
