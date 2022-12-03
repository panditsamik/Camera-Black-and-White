import streamlit as st
from PIL import Image

with st.expander("Open your Camera :"):
    img = st.camera_input("Camera")

if img:
    cameraImg = Image.open(img)
    converted_Image = cameraImg.convert("L")
    st.image(converted_Image)

