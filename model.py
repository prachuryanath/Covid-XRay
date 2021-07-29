import streamlit as st
from utils import image_classification
from PIL import Image

st.title("Covid 19 Prediction")

st.text("Upload a XRAY Image for Covid classification as Covid or Non Covid")

uploaded_file = st.file_uploader("Choose a XRAY Image ...", type=['jpg','jpeg','png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded XRAY.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = image_classification(image, 'model')
    if label == 0:
        st.write("COVID Positive")
    else:
        st.write("COVID Negative")
