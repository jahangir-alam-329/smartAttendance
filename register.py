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
p=0
j=0
data_set=pd.read_csv('information.csv')
l=len(data_set)
for i in range(0,l):
  for j in range(0,1):
    u_roll.append(data_set.iloc[i][g])
    g=g+1
    students.append(data_set.iloc[i][g])
    g=g+1
    passwords.append(str(data_set.iloc[i][g]))
    g=0
length=len(students)
Teachers=["Navin aggarwal"]
T_password=["1234"]
t_length=len(Teachers)
st.title("attendance system")
st.title("")

#status=st.radio('Choose option to Register Student',('Register Student (only by teacher)','login'))

#if status == 'Register Student (only by teacher)':
st.info("Only Teacher Register a Student")
t_name=st.text_input("enter your name")
t_code=st.text_input("enter your password",type='password')
login=st.button("LogIn")
if login==True:
    for i in range(0,t_length):
        if Teachers[i]==t_name and T_password[i]==t_code:
            p=p+1
            j=j+i
                #st.success("you sucsessfully LogIn "+ t_name)
                #st.subheader("Enter the details of Student")
            with st.spinner('wait a second'):
                time.sleep(5)
                    #st.success("you sucsessfully LogIn "+ t_name)
                    #st.subheader("Enter the details of Student")
                    # with k andar
                    
        if p==0:
            st.error("The Name and password not match") 

if Teachers[j]==t_name and T_password[j]==t_code:
    st.success("you sucsessfully LogIn "+ t_name)
    st.subheader("Enter the details of Student")
    name=st.text_input("Enter name of student")
    code=st.text_input("Enter password",type='password')
    roll=u_roll[length-1]+1
    r=str(roll)
    st.info("university roll:"+ r)


    @st.cache_resource
    def load_image(image_file):
        img=Image.open(image_file)
        return img
                        #name=st.text_input("enter your name")
                        #if button==True:
    image_file=st.file_uploader("upload an image",type=['png','jpeg','jpg'])
    if image_file is not None:
        z=image_file.name
        z=name+".jpeg"

        file_details={"fileName":z,"FileType":image_file.type}
        st.write(file_details)
                            #st.write(type(image_file))
        img=load_image(image_file)
        st.image(img)#,height=250,width=250)



                        # saving file
        with open(os.path.join("student_images",z),"wb") as f:
            f.write(image_file.getbuffer())
        
        st.success("file saved")
    submit=st.button("submit")
    if submit==True:
            with open('information.csv','a',newline='')as f:
                    data=csv.writer(f)
                    data.writerow([roll,name,code])
            d=pd.DataFrame(columns=["name"," time"," date"])
            d.to_csv(name+".csv",index=False)
            st.success("you sucsessfully")

    