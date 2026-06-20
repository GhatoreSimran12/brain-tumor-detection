import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import gdown

MODEL_PATH = "best_efficientnet_model.h5"

# Google Drive File ID
FILE_ID = "1VkryeeHXk6DmKTCDdtDV7vJPMeH4o4OF"

@st.cache_resource
def load_model():

    if not os.path.exists(MODEL_PATH):

        url = f"https://drive.google.com/uc?id={FILE_ID}"

        with st.spinner("Downloading model... Please wait."):
            gdown.download(url, MODEL_PATH, quiet=False)

    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

st.title("Brain Tumor Detection System")

uploaded_file = st.file_uploader(
    "Upload MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded MRI",
        use_container_width=True
    )

    img = image.resize((224,224))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    if st.button("Detect Tumor"):

        prediction = model.predict(img)

        score = float(prediction[0][0])

        if score > 0.5:
            st.error("Tumor Detected")
        else:
            st.success("No Tumor Detected")