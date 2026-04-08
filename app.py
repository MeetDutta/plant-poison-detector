import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load model
model = load_model('model/plant_model.h5')

IMG_SIZE = (224, 224)

# Page config
st.set_page_config(page_title="Plant Poison Detector", page_icon="🌿")

st.title("🌿 Plant Poison Detector")
st.write("Upload an image to check if the plant is poisonous or not.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = img.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.error(f"⚠️ Poisonous ({prediction*100:.2f}% confidence)")
    else:
        st.success(f"✅ Non-Poisonous ({(1-prediction)*100:.2f}% confidence)")
