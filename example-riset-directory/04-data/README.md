# 04-data

Data pada tahap ini merupakan hasil dari proses preprocessing dan training model yang akan digunakan sebagai dasar pada tahap analisis hasil penelitian. Data yang dihasilkan berasal dari proses pelatihan dan evaluasi model Convolutional Neural Network (CNN) menggunakan Tomato Leaf Disease Dataset. Seluruh data disimpan dalam beberapa format file agar dapat digunakan kembali pada proses analisis, visualisasi, dan dokumentasi penelitian.

## Isi yang diharapkan

Tahap ini menghasilkan beberapa jenis data sebagai berikut.

1. History training dalam format CSV dan PKL yang berisi nilai accuracy, validation accuracy, loss, dan validation loss pada setiap epoch pelatihan.
2. Model CNN terlatih dalam format .keras yang digunakan untuk proses prediksi penyakit daun tomat.
3. Hasil evaluasi model yang meliputi Accuracy, Precision, Recall, F1-Score, Classification Report, dan Confusion Matrix.
4. Visualisasi hasil pelatihan berupa grafik Accuracy dan Loss selama proses training.
5. Visualisasi Grad-CAM yang terdiri atas citra asli (original image), heatmap, dan overlay sebagai interpretasi area citra yang menjadi perhatian model.
6. Metadata proses eksperimen yang mencakup jumlah epoch, learning rate, batch size, waktu eksekusi, jumlah kelas, ukuran citra, serta hasil empat kali run eksperimen untuk menguji konsistensi performa model.

## Stuktur prnyimpanan data
Data hasil eksperimen disimpan pada direktori sebagai berikut.
| Folder                | Isi Data                                                |
| --------------------- | ------------------------------------------------------- |
| `outputs/models/`     | Model CNN terlatih (`tomato_cnn.keras`)                 |
| `outputs/history/`    | History training (`history.csv`, `history.pkl`)         |
| `outputs/figures/`    | Grafik Accuracy, Loss, dan Confusion Matrix             |
| `outputs/gradcam/`    | Hasil visualisasi Grad-CAM (original, heatmap, overlay) |
| `outputs/evaluation/` | Hasil evaluasi model dan classification report          |

## Kegunaan Data

Data yang dihasilkan pada tahap ini digunakan sebagai masukan pada tahap analisis hasil penelitian. Nilai metrik evaluasi digunakan untuk mengukur performa model CNN dalam mengklasifikasikan penyakit daun tomat, sedangkan visualisasi Grad-CAM digunakan untuk menjelaskan bagian citra yang menjadi dasar pengambilan keputusan model. Seluruh data tersebut menjadi dasar dalam penyusunan pembahasan, penarikan kesimpulan, serta verifikasi bahwa model yang dibangun mampu menjawab tujuan penelitian.



