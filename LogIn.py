import streamlit as st
import pandas as pd
import time
from PIL import Image
import os
import csv

students=[]
passwords=[]
u_roll=[]
g=0
data_set=pd.read_csv('information.csv')
l=len(data_set)
for ii in range(0,l):
  for jj in range(0,1):
    u_roll.append(data_set.iloc[ii][g])
    g=g+1
    students.append(data_set.iloc[ii][g])
    g=g+1
    passwords.append(str(data_set.iloc[ii][g]))
    g=0














w=0
p=0
j=0
#students=["jahangir","naman","poonam","muskan","meet arora","khayati"]
#passwords=["0329","0330","0331","0332","0333","0334"]
#u_roll=[220001,220002,220003,220004,220005,220006]
Teachers=["Navin aggarwal"]
T_password=["1234"]


length=len(students)
t_length=len(Teachers)

#info={
#    "jahangir":"0329","naman":"0330","poonam":"0331","muskan":"0332",
#         "meet arora":"0333","khayati":"0334","jahangir":"0335"
#     }


st.title("attendance system")
st.title("")
status=st.radio('Please Choose a Option ',('Student LogIn','Teacher LogIn'))




###########################################################################################################



if status == 'Student LogIn':
    name=st.text_input("Enter your Name")
    roll=st.text_input("Enter your University roll")
    code=st.text_input("Enter your Password",type='password')
    #year=st.selectbox("enter yor BCA year",(1,2,3))
    button=st.button("LogIn")
    p=0


    if button==True:
        roll_no=roll # roll in string
        roll=int(roll)
        for i in range(0,length):
            if students[i]==name and passwords[i]==code and u_roll[i]==roll:
                p=p+1
                with st.spinner('wait a second'):
                    time.sleep(2)
                data=pd.read_csv(name +".csv")
                st.success("You sucsessfully LogIN "+ name)
                st.info("Name: "+ name)
                st.info("University Roll: "+roll_no)
                st.dataframe(data)
                st.balloons()
                break
        if p==0:
            st.error("The University roll and password not match") 


##############################################################################################################



#elif status == 'Register Student (only by teacher)':
    #t_name=st.text_input("enter your name")
    #t_code=st.text_input("enter your password",type='password')
    #login=st.button("LogIn")
    #if login==True:
        #for i in range(0,t_length):
           # if Teachers[i]==t_name and T_password[i]==t_code:
              #  p=p+1
               # j=j+i
                #st.success("you sucsessfully LogIn "+ t_name)
                #st.subheader("Enter the details of Student")
               # with st.spinner('wait a second'):
                   # time.sleep(5)
                    #st.success("you sucsessfully LogIn "+ t_name)
                    #st.subheader("Enter the details of Student")
                    # with k andar
                    
           # if p==0:
              #  st.error("The Name and password not match") 

    #if Teachers[j]==t_name and T_password[j]==t_code:
       # st.success("you sucsessfully LogIn "+ t_name)
        #st.subheader("Enter the details of Student")
        #name=st.text_input("Enter name of student")
        #code=st.text_input("Enter password",type='password')
       # roll=u_roll[length-1]+1
        #r=str(roll)
       # st.info("university roll:"+ r)


       # @st.cache_resource
       # def load_image(image_file):
           # img=Image.open(image_file)
          #  return img
                        #name=st.text_input("enter your name")
                        #if button==True:
       # image_file=st.file_uploader("upload an image",type=['png','jpeg','jpg'])
       # if image_file is not None:
         #   z=image_file.name
         #   z=name+".jpeg"

        #    file_details={"fileName":z,"FileType":image_file.type}
         #   st.write(file_details)
                            #st.write(type(image_file))
         #   img=load_image(image_file)
        #    st.image(img)#,height=250,width=250)



                        # saving file
        #    with open(os.path.join("student_images",z),"wb") as f:
        #        f.write(image_file.getbuffer())
        #    st.success("file saved")
       # submit=st.button("submit")
       # st.success("you sucsessfully")
      #  if submit==True:
       #         with open('information.csv','a',newline='')as f:
        #             data=csv.writer(f)
         #            data.writerow([roll,name,code])
        #        st.success("you sucsessfully")
                    


##########################################################################################


elif status == 'Teacher LogIn':
    t_name=st.text_input("Enter your Name")
    t_code=st.text_input("Enter your Password",type='password')
    login=st.button("LogIn")
    if login==True:
        for i in range(0,t_length):
            if Teachers[i]==t_name and T_password[i]==t_code:
                p=p+1
                j=j+i
                    #st.success("you sucsessfully LogIn "+ t_name)
                    #st.subheader("Enter the details of Student")
                with st.spinner('wait a second'):
                    time.sleep(3)
                    #st.success("You sucsessfully LogIn "+ t_name)
                        #st.success("you sucsessfully LogIn "+ t_name)
                        #st.subheader("Enter the details of Student")
                        # with k andar
                    #attendance=st.selectbox('Please Choose a Option ',('Take Attendance','Stop Attendance'))
                        
        if p==0:
            st.error("The Name and Password not match") 
                #else:
                    #attendance=st.checkbox('Please Choose a Option ',('Take Attendance','Stop Attendance'))
   

    if Teachers[j]==t_name and T_password[j]==t_code:
        st.success("You sucsessfully LogIn "+ t_name)
        attendance=st.selectbox('',('Select Option For Attendance','Take Attendance','Check Attandance'))
        if attendance=="Take Attendance":

            import cv2
            import numpy as np
            import face_recognition as face_rec
            import os
            import pyttsx3 as textSpeach
            from datetime import  datetime,date

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




                        # to update csv
            def MarkAttendence2(name):
                #j=str(name + '.csv')
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




        if attendance=="Check Attandance":
            data=pd.read_csv("attendence.csv")
            st.dataframe(data)

                



                    
    
            



        
            
            

















    #key=[k for k,v in info.items() if v==code][]
    #if info[name]==code and name==key:
       # data=pd.read_csv(name +".csv")
        #st.dataframe(data)
    #elif info[name]!=code:
        #st.title("enter correct password")
