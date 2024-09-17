import streamlit as st
from PIL import Image
import os


import cv2
import numpy as np
import face_recognition as face_rec
import os
import pyttsx3 as textSpeach
from datetime import datetime






st.set_page_config(
    page_title="GLA portal",
    page_icon="#"
)

s=st.header("SMART ATTENDANCE SYSTEM")
img=Image.open("homepage2.png")
st.image(img,width=1000,caption="___________")

img2=Image.open("homepage3.jpg")
st.image(img2,width=1000,caption="____________")
st.sidebar.success("select page above.")

button=st.button("takeAttendance")
if button==True:
    engine = textSpeach.init()

    def resize(img, size) :
        width = int(img.shape[1]*size)
        height = int(img.shape[0] * size)
        dimension = (width, height)
        return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)

    path = 'student_images' # folder whare the image of student saved
    studentImg = []
    studentName = []
    myList = os.listdir(path) # by the help of OS module we can retrive all the image from file
    for cl in myList :  # hare myList is like list which contain all the image of folder
        curimg = cv2.imread(f'{path}/{cl}') # by the help of f{} string and imread() function we extract all image one by one
        # hare path='student_images' i.e, image folder c1 it the image at that index
        studentImg.append(curimg) # hare we append image
        studentName.append(os.path.splitext(cl)[0]) # hare we append studentname which is in c1.

    # we incode the image which is present in studentImg
    def findEncoding(images) :
        imgEncodings = []
        for img in images :
            img = resize(img, 0.50)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodeimg = face_rec.face_encodings(img)[0]
            imgEncodings.append(encodeimg)
        return imgEncodings

    # to update csv
    def MarkAttendence(name):
        with open('attendence.csv', 'r+') as f:
            myDatalist =  f.readlines()
            nameList = []
            for line in myDatalist :
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:
                now = datetime.now()
                datestr = now.strftime("%m/%d/%y")
                timestr = now.strftime('%H:%M')
                f.writelines(f'\n{name}, {timestr}, {datestr}') # we use comma to seprate name and time in csv file
                statment = str('welcome to class' + name)
                engine.say(statment)
                engine.runAndWait()


    # to update csv
    def MarkAttendence2(name):
        j=str(name + '.csv')
        with open(j, 'r+') as f:
            myDatalist =  f.readlines()
            nameList = []
            for line in myDatalist :
                entry = line.split(',')
                nameList.append(entry[0])

            if name not in nameList:
                now = datetime.now()
                datestr = now.strftime("%m/%d/%y")
                timestr = now.strftime('%H:%M')
                f.writelines(f'\n{name}, {timestr}, {datestr}') # we use comma to seprate name and time in csv file
                statment = str('welcome to class' + name)
                engine.say(statment)
                engine.runAndWait()




    # call the findEncoding function to incode images and hare we pass list of image i.e, studentImg
    EncodeList = findEncoding(studentImg)


    # by using cv2 module we capture and record video and photo at run time
    vid = cv2.VideoCapture(0)
    while True :  # hare we run infinite loop
        success, frame = vid.read()  # hare by using read() function of cv2 we read frame
        Smaller_frames = cv2.resize(frame, (0,0), None, 0.25, 0.25) # by the help of resize() we fix the size of image to get appropriate frame

        facesInFrame = face_rec.face_locations(Smaller_frames)
        encodeFacesInFrame = face_rec.face_encodings(Smaller_frames, facesInFrame)

        for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame) :
            matches = face_rec.compare_faces(EncodeList, encodeFace)
            facedis = face_rec.face_distance(EncodeList, encodeFace)
            print(facedis)
            matchIndex = np.argmin(facedis)

            if matches[matchIndex] :
                name = studentName[matchIndex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                cv2.rectangle(frame, (x1, y2-25), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                MarkAttendence(name)
                MarkAttendence2(name)

        cv2.imshow('video',frame)
        cv2.waitKey(1)
