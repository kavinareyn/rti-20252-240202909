# 01-proposal

# Proposal Penelitian

## Judul

Implementasi Convolutional Neural Network (CNN) untuk Klasifikasi Penyakit Daun Tomat Menggunakan Visualisasi Grad-CAM

---

# Latar Belakang

Tanaman tomat merupakan salah satu komoditas hortikultura yang memiliki nilai ekonomi tinggi di Indonesia. Namun, produktivitas tanaman tomat sering mengalami penurunan akibat serangan berbagai jenis penyakit pada daun. Identifikasi penyakit umumnya masih dilakukan secara manual oleh petani atau tenaga ahli, sehingga membutuhkan waktu dan berpotensi menimbulkan kesalahan diagnosis.

Perkembangan teknologi Artificial Intelligence, khususnya Deep Learning, memberikan solusi dalam proses klasifikasi citra. Salah satu metode yang paling banyak digunakan adalah Convolutional Neural Network (CNN), karena mampu mempelajari karakteristik visual dari suatu objek secara otomatis tanpa memerlukan ekstraksi fitur manual.

Pada penelitian ini akan dikembangkan model CNN untuk mengklasifikasikan penyakit daun tomat berdasarkan citra digital. Selain menghasilkan prediksi kelas penyakit, penelitian ini juga memanfaatkan metode Grad-CAM (Gradient-weighted Class Activation Mapping) untuk menampilkan area citra yang menjadi dasar pengambilan keputusan model sehingga hasil prediksi menjadi lebih mudah dipahami.

Dataset yang digunakan berasal dari Kaggle Tomato Diseases Dataset yang terdiri dari 10 kelas penyakit dan kondisi daun sehat.

---

# Rumusan Masalah

1. Bagaimana membangun model CNN untuk mengklasifikasikan penyakit daun tomat?
2. Seberapa baik performa model CNN dalam mengidentifikasi penyakit daun tomat?
3. Bagaimana Grad-CAM dapat membantu menjelaskan hasil prediksi model CNN?

---

# Tujuan Penelitian

1. Membangun model klasifikasi penyakit daun tomat menggunakan CNN.
2. Mengukur performa model menggunakan Accuracy, Precision, Recall, dan F1-Score.
3. Mengimplementasikan Grad-CAM untuk memberikan visualisasi bagian citra yang menjadi perhatian model.
4. Mengevaluasi kemampuan model dalam mengklasifikasikan 10 kelas penyakit daun tomat.

---

# Manfaat Penelitian

## Bagi Petani

Membantu proses identifikasi penyakit daun tomat secara lebih cepat sehingga penanganan dapat dilakukan lebih dini.

## Bagi Peneliti

Menjadi referensi implementasi CNN dan Grad-CAM pada bidang klasifikasi citra pertanian.

## Bagi Dunia Akademik

Menambah referensi penelitian mengenai penerapan Deep Learning pada bidang pertanian.

---

# Urgensi Penelitian

Serangan penyakit pada tanaman tomat dapat menyebabkan penurunan hasil panen dan kerugian ekonomi. Identifikasi yang cepat sangat diperlukan agar tindakan pengendalian dapat segera dilakukan.

Penggunaan CNN memungkinkan proses identifikasi dilakukan secara otomatis dengan tingkat akurasi yang tinggi. Selain itu, penggunaan Grad-CAM meningkatkan interpretabilitas model sehingga pengguna dapat mengetahui alasan model memberikan suatu prediksi. Hal ini penting untuk meningkatkan kepercayaan pengguna terhadap sistem berbasis Artificial Intelligence.

---

# Dataset

- Nama Dataset : Tomato Diseases Dataset
- Sumber : Kaggle
- Jumlah Kelas : 10 kelas
- Jenis Data : Citra daun tomat

---

# Metode Penelitian

1. Pengumpulan Dataset
2. Preprocessing citra
   - Resize
   - Normalisasi
3. Pembagian data Training dan Testing
4. Pembangunan model CNN
5. Training model
6. Evaluasi model
7. Visualisasi Grad-CAM
8. Analisis hasil

---

# Evaluasi

Performa model akan diukur menggunakan:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# Luaran Penelitian

Penelitian ini menghasilkan:

- Model CNN untuk klasifikasi penyakit daun tomat.
- Visualisasi Grad-CAM sebagai penjelasan hasil prediksi.
- Evaluasi performa model menggunakan beberapa metrik pengujian.

---

# Referensi Singkat

1. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
2. LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep Learning. *Nature*, 521(7553), 436–444.
3. Selvaraju, R. R., et al. (2017). Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization. ICCV.
4. Kaggle. Tomato Diseases Dataset.


## Berkas

- [proposal-penelitian.md](proposal-penelitian.md) — draf proposal (rekonstruksi retrospektif berdasarkan hasil Tahap 1-4)

## Acuan

Ringkasan topik & roadmap penelitian: [../09-docs/rencana-penelitian.md](../09-docs/rencana-penelitian.md)
