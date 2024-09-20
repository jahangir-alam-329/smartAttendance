# import streamlit as st
# button=st.button("click me")
# if button==False:
#     picture = st.camera_input("Take a picture")

#     if picture:
#         p=st.image(picture)


# to start live_webcam on streamlit

# elif button==True:
import cv2
from cvzone.FaceDetectionModule import FaceDetector
import streamlit as st


st.title("web app using opencv cvzone and streamlit")
st.title("face dection")
run=st.checkbox("Run")
frame_window=st.image([])
detector=FaceDetector()
cap=cv2.VideoCapture(0)
while True:
    ret, img=cap.read()
    imgRGB=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    face, New_Image=detector.findFaces(img)
    q=frame_window.image(img)
        

# else:
#     st.success("click button")
