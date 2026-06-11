# Aplikasi Deteksi Kendaraan Area Perkotaan 🚦

Aplikasi ini menggunakan model **YOLOv12** untuk mendeteksi berbagai jenis kendaraan di area perkotaan, seperti:
- Mobil (Car)
- Motor (Motorcycle)
- Truk (Truck)
- Bus (Bus)

Proyek ini disusun oleh:
- Hanna Aulya
- Zahid Rizky Fakhri
- Ananda Aryaguna Margaputra

## Struktur Proyek

- `TugasKelompokACV.ipynb`: Jupyter notebook yang berisi proses pengunduhan dataset dari Roboflow, pelatihan model YOLOv12.
- `app.py`: Source code aplikasi web berbasis **Streamlit** untuk antarmuka pengguna deteksi kendaraan.
- `yolo12s.pt`: Model dasar YOLOv12s yang diunduh untuk pelatihan model.
- `runs/`: Direktori yang menyimpan hasil pelatihan model dan *weights* terbaik (`best.pt`).

## Persyaratan (Requirements)

Untuk menjalankan proyek ini secara lokal, pastikan Anda telah menginstal beberapa library berikut:
- `streamlit`
- `ultralytics`
- `Pillow` (PIL)
- `numpy`
- `roboflow` (hanya diperlukan untuk mengunduh dataset dari notebook)

Anda dapat menginstal dependensi dengan menjalankan:
```bash
pip install streamlit ultralytics pillow numpy roboflow
```

## Cara Menjalankan Aplikasi

1. Pastikan Anda memiliki model yang telah dilatih (atau jalankan terlebih dahulu notebook `TugasKelompokACV.ipynb` untuk melatih model Anda sendiri). Secara default, aplikasi mencari model yang disimpan di sub-direktori `runs/detect/train/weights/best.pt` secara relatif terhadap lokasi `app.py`.
2. Buka terminal dan arahkan ke direktori proyek.
3. Jalankan aplikasi menggunakan perintah Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Buka tautan lokal yang diberikan (biasanya `http://localhost:8501`) di browser web Anda.
5. Unggah gambar jalanan (`.jpg`, `.jpeg`, atau `.png`) dan klik tombol **Deteksi Kendaraan** untuk melihat hasil deteksinya.

## Dataset
Dataset yang digunakan dalam proyek ini diunduh dari Roboflow (workspace: `zahidrf`, project: `kelompok-applied-computer-vision`).

## Teknologi yang Digunakan
- **Python**
- **Ultralytics YOLO**: Framework untuk mendeteksi objek.
- **Streamlit**: Framework untuk membangun antarmuka web secara interaktif.

---
*Proyek ini merupakan Tugas Kelompok untuk mata kuliah Applied Computer Vision.*
