# Jadwal & Log Pelaksanaan Penelitian

Dokumen ini berisi kronologi pelaksanaan penelitian mulai dari tahap persiapan dataset, implementasi model Convolutional Neural Network (CNN), proses pelatihan (training), evaluasi model, hingga visualisasi hasil menggunakan Grad-CAM. Seluruh eksperimen dilakukan pada komputer lokal menggunakan framework TensorFlow dan bahasa pemrograman Python.

# Informasi Penelitian
| Keterangan             | Informasi                                                                      |
| ---------------------- | ------------------------------------------------------------------------------ |
| **Nama Peneliti**      | Kavina Reyna Riyadi                                                            |
| **NIM**                | 240202909                                                                      |
| **Program Studi**      | S1 Ilmu Komputer                                                                 |
| **Universitas**        | Universitas Putra Bangsa                                                       |
| **Judul Penelitian**   | Klasifikasi Penyakit Daun Tomat Menggunakan Convolutional Neural Network (CNN) |
| **Dataset**            | Tomato Leaf Disease Dataset (22.193 citra, 10 kelas)                           |
| **Platform**           | Visual Studio Code (Windows 11)                                                |
| **Framework**          | TensorFlow 2.21.0, Keras 3.15.0                                                |
| **Bahasa Pemrograman** | Python 3.11                                                                    |
| **Metode**             | Convolutional Neural Network (CNN)                                             |
| **Visualisasi**        | Grad-CAM                                                                       |
| **Status Penelitian**  | ⏳ Dalam Proses *(ubah menjadi ✅ Selesai setelah seluruh eksperimen selesai)*   |

## Log Pelaksanaan

| Tanggal         | Tahap                                         | Deskripsi Kegiatan                                                                                                                                                                                                                                      | Referensi                               |
| --------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| 01–03 Juli 2026 | **Tahap 1 — Studi Literatur**                 | Mempelajari konsep Convolutional Neural Network (CNN), klasifikasi citra, TensorFlow, serta beberapa penelitian terdahulu mengenai klasifikasi penyakit daun tomat menggunakan metode deep learning.                                                    | WS-01 s.d. WS-08                        |
| 04 Juli 2026    | **Tahap 2 — Persiapan Dataset & Environment** | Menyiapkan lingkungan pengembangan menggunakan Visual Studio Code, Python 3.11, TensorFlow 2.21, Keras 3.15, serta mengunduh dan menyusun struktur folder Tomato Leaf Disease Dataset yang terdiri dari 10 kelas.                                       | Dataset, requirements.txt               |
| 05 Juli 2026    | **Tahap 3 — Preprocessing Data**              | Melakukan pemuatan dataset menggunakan `image_dataset_from_directory`, mengubah ukuran citra menjadi 224×224 piksel, normalisasi data, serta membangun pipeline `tf.data` untuk proses training dan testing.                                            | `dataset_loader.py`, `preprocessing.py` |
| 06–08 Juli 2026 | **Tahap 4 — Implementasi Model CNN**          | Membangun arsitektur CNN sederhana yang terdiri atas tiga lapisan Convolution, MaxPooling, Flatten, Dense, Dropout, dan Softmax sebagai layer keluaran untuk klasifikasi 10 kelas penyakit daun tomat.                                                  | `cnn_model.py`                          |
| 09–12 Juli 2026 | **Tahap 5 — Training Model**                  | Melakukan proses pelatihan model menggunakan optimizer Adam, learning rate 0,001, batch size 32, dan jumlah epoch sesuai konfigurasi. Selama tahap ini dilakukan beberapa pengujian serta perbaikan pada proses penyimpanan model dan history training. | `train.py`, `main.py`                   |
| 12 Juli 2026    | **Tahap 6 — Evaluasi Model**                  | Menghitung metrik Accuracy, Precision, Recall, dan F1-Score, menghasilkan Classification Report, Confusion Matrix, serta menyimpan hasil evaluasi ke dalam file JSON dan TXT.                                                                           | `evaluate.py`                           |
| 12 Juli 2026    | **Tahap 7 — Visualisasi Hasil**               | Membuat grafik Accuracy dan Loss selama proses training, serta menghasilkan visualisasi Grad-CAM untuk menunjukkan area citra daun yang menjadi fokus model dalam proses klasifikasi.                                                                   | `plot_history.py`, `gradcam.py`         |
| 13 Juli 2026    | **Tahap 8 — Analisis Hasil**                  | Menganalisis performa model berdasarkan metrik evaluasi, grafik training, confusion matrix, dan hasil visualisasi Grad-CAM untuk mengetahui kemampuan model dalam membedakan setiap kelas penyakit daun tomat.                                          | Output Evaluasi                         |
| 13 Juli 2026    | **Tahap 9 — Penyusunan Laporan**              | Menyusun dokumentasi eksperimen, hasil implementasi, pembahasan, serta kesimpulan penelitian berdasarkan hasil pengujian yang telah diperoleh.                                                                                                          | Laporan Akhir                           |

## Informasi Eksperimen
| Parameter               | Nilai                           |
| ----------------------- | ------------------------------- |
| Image Size              | 224 × 224 piksel                |
| Batch Size              | 32                              |
| Optimizer               | Adam                            |
| Learning Rate           | 0.001                           |
| Loss Function           | Sparse Categorical Crossentropy |
| Activation Hidden Layer | ReLU                            |
| Activation Output Layer | Softmax                         |
| Epoch                   | 20                              |
| Jumlah Kelas            | 10                              |
| Seed                    | 42 *(jika memang digunakan)*    |


## Status Ringkas

- **Tahap 1–4**: Selesai (dataset final: matrix 400 run / 40 replikasi per kombinasi, 2026-06-15).
- **Tahap 5**: Konten naskah selesai dengan statistik n=40 (termasuk tinjauan pustaka & verifikasi CVE-2026-48524); menyisakan keputusan bahasa final dan pemindahan ke template jurnal tujuan (dilakukan oleh peneliti).

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Lengkapi matriks literatur dengan paper *related work* nyata ([02-literatur/matriks-literatur.md](../02-literatur/matriks-literatur.md)) — 18 referensi terverifikasi
- [x] Verifikasi CVE-2026-48524 terhadap basis data NVD/MITRE — terkonfirmasi via GHSA-fhv5-28vv-h8m8 (PyJWT, CVSS 3.7)
- [ ] Tetapkan bahasa final naskah (Indonesia/Inggris) sesuai jurnal tujuan
- [ ] Pindahkan konten [07-manuskrip/naskah-jurnal.md](../07-manuskrip/naskah-jurnal.md)/`.docx` ke template jurnal tujuan
- [ ] Finalisasi penempatan figure/tabel sesuai gaya jurnal
- [ ] Review akhir seluruh klaim numerik agar konsisten antar dokumen (lihat daftar pada [07-manuskrip/00-outline.md](../07-manuskrip/00-outline.md))

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
