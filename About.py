import streamlit as st
from PIL import Image
import os
st.set_page_config(
    page_title="GLA portal",
    page_icon="#"
)

s=st.header("SMART ATTENDANCE SYSTEM")
img=Image.open("homepage2.png")
st.image(img,width=1000,caption="about")

img2=Image.open("homepage3.jpg")
st.image(img2,width=1000,caption="about2")
st.sidebar.success("select page above.")


@st.cache_resource
def load_image(image_file):
    img=Image.open(image_file)
    return img
name=st.text_input("enter your name")
button=st.button("upload image")
#if button==True:
st.subheader("upload image")
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

