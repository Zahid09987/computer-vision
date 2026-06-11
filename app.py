import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

# Konfigurasi Halaman Web
st.set_page_config(page_title="Deteksi Kendaraan YOLOv12", page_icon="🚗")

st.title("Aplikasi Deteksi Kendaraan Area Perkotaan 🚦")
st.write("**Disusun oleh:** Hanna Aulya, Zahid Rizky Fakhri, Ananda Aryaguna Margaputra")
st.write("Unggah gambar jalanan untuk mendeteksi Mobil, Motor, Truk, dan Bus.")

@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'runs', 'detect', 'train', 'weights', 'best.pt')
    return YOLO(model_path)

model = load_model()

uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar Asli', use_container_width=True)

    if st.button('Deteksi Kendaraan'):
        with st.spinner('Sedang memproses gambar menggunakan YOLOv12...'):
            results = model.predict(image, conf=0.5)
            res_plotted = results[0].plot()
            res_image = Image.fromarray(res_plotted[..., ::-1])

            st.success('Deteksi Selesai!')
            st.image(res_image, caption='Hasil Deteksi', use_container_width=True)

            boxes = results[0].boxes
            st.write(f"Total kendaraan terdeteksi: **{len(boxes)}** objek")
