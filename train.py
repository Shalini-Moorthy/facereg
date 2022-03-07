import cv2
import numpy as np
from os import listdir
from os.path import isfile , join

def trainfun(ID):
    data_path='C:/Users/shalini/Desktop/sotproject/faces/UserID'+str(ID)+'/'

    onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]
    training_data,labels=[],[]
    for i , files in enumerate(onlyfiles):
        image_path=data_path+onlyfiles[i]
        images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
        training_data.append(np.asarray(images,dtype=np.uint8))
        labels.append(i)
    labels=np.asarray(labels,dtype=np.int32)
    model=cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(training_data),np.asarray(labels))
    model.save('C:/Users/shalini/Desktop/sotproject/models/model'+str(ID)+'.yml')
    print("Model Training Complete")
