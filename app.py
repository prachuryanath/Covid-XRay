import streamlit as st
from utils import image_classification
from PIL import Image
from tensorflow.keras.models import load_model
st.title("Covid 19 Prediction")

st.text("Upload a XRAY Image for Covid classification as Covid or Non Covid")

uploaded_file = st.file_uploader("Choose a XRAY Image ...", type=['jpg','jpeg','png'])

@st.cache(allow_output_mutation=True)
def load(model_path):
    # Load the model
    model = load_model(model_path)
    return model
    
model = load('model')

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded XRAY.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    data = image_classification(image)
    pred = model.predict(data)

    # st.write(label)
    print(pred)
    if pred < 0.5:
        pred_acc = (0.5 - pred[0][0])/0.005
        st.write("Prediction ACCURACY :",pred_acc)
        st.write("COVID Positive")
    else:
        pred_acc = (pred[0][0]-0.5)*2
        st.write("Prediction ACCURACY :",pred_acc)
        st.write("COVID Negative")
