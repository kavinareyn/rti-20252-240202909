# 05-kode

Source code implementasi penelitian yang digunakan untuk membangun model Convolutional Neural Network (CNN), melakukan preprocessing dataset, proses pelatihan model, evaluasi performa, visualisasi hasil, serta prediksi penyakit daun tomat menggunakan model yang telah dilatih.

## Struktur yang direncanakan

```
tomato-disease-cnn/
│
├── dataset/
│   ├── train/                  # Dataset training (10 kelas)
│   └── test/                   # Dataset testing (10 kelas)
│
├── outputs/
│   ├── evaluation/             # Hasil evaluasi model
│   ├── figures/                # Accuracy, Loss, Confusion Matrix
│   ├── gradcam/                # Original, Heatmap, Overlay
│   ├── history/                # history.csv & history.pkl
│   └── models/                 # tomato_cnn.keras
│
├── src/
│   ├── data/
│   │   ├── check_dataset.py
│   │   ├── dataset_loader.py
│   │   └── preprocessing.py
│   │
│   ├── models/
│   │   ├── cnn_model.py
│   │   ├── train.py
│   │   └── test_model.py
│   │
│   ├── evaluation/
│   │   └── evaluate.py
│   │
│   ├── prediction/
│   │   └── predictor.py
│   │
│   ├── visualization/
│   │   ├── gradcam.py
│   │   └── plot_history.py
│   │
│   └── utils/
│       └── history.py
│
├── config.py                   # Konfigurasi penelitian
├── main.py                     # Training & evaluasi model
├── predict.py                  # Prediksi citra baru
├── run_gradcam.py              # Visualisasi Grad-CAM
├── README.md
└── requirements.txt
```

## Deskripsi Struktur
| Folder/File            | Fungsi                                                                                                            |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **dataset/**           | Menyimpan dataset training dan testing.                                                                           |
| **src/data/**          | Memuat proses pengecekan dataset, pemuatan dataset, dan preprocessing.                                            |
| **src/models/**        | Berisi implementasi arsitektur CNN serta proses training model.                                                   |
| **src/evaluation/**    | Menghitung Accuracy, Precision, Recall, F1-Score, dan Confusion Matrix.                                           |
| **src/prediction/**    | Melakukan prediksi penyakit daun tomat menggunakan model yang telah dilatih.                                      |
| **src/visualization/** | Membuat grafik training dan visualisasi Grad-CAM.                                                                 |
| **src/utils/**         | Fungsi pendukung seperti penyimpanan history training.                                                            |
| **outputs/**           | Menyimpan seluruh hasil eksperimen dan evaluasi.                                                                  |
| **config.py**          | Berisi konfigurasi parameter penelitian seperti path dataset, ukuran citra, batch size, learning rate, dan epoch. |
| **main.py**            | Program utama untuk menjalankan proses training hingga evaluasi model.                                            |
| **predict.py**         | Digunakan untuk menguji citra baru menggunakan model yang telah dilatih.                                          |
| **run_gradcam.py**     | Menampilkan visualisasi Grad-CAM pada hasil prediksi.                                                             |


## Acuan

- Implementasi Convolutional Neural Network (CNN) menggunakan TensorFlow 2.21 dan Keras 3.15.
- Dataset: Tomato Leaf Disease Dataset (Kaggle).
- Framework: Python 3.11.
- Library utama: TensorFlow, Keras, NumPy, Matplotlib, Scikit-learn, dan OpenCV.
