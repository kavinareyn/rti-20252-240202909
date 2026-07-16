# 06-output

Tahap ini berisi seluruh hasil yang dihasilkan dari proses implementasi model Convolutional Neural Network (CNN) untuk klasifikasi penyakit daun tomat. Output diperoleh dari proses training, evaluasi model, prediksi citra, dan visualisasi Grad-CAM.

Hasil dihasilkan oleh:

main.py
predict.py
run_gradcam.py

menggunakan dataset Tomato Leaf Disease Dataset.

## outputs/
evaluations/

| File                        | Isi                                                                 |
| --------------------------- | ------------------------------------------------------------------- |
| `classification_report.txt` | Laporan Precision, Recall, F1-Score setiap kelas penyakit.          |
| `evaluation_result.txt`     | Accuracy, Precision, Recall, dan F1-Score model secara keseluruhan. |

figures/

| File                   | Isi                                                                          |
| ---------------------- | ---------------------------------------------------------------------------- |
| `accuracy.png`         | Grafik perkembangan accuracy training dan validation pada setiap epoch.      |
| `loss.png`             | Grafik perkembangan loss training dan validation selama proses training.     |
| `confusion_matrix.png` | Visualisasi Confusion Matrix hasil klasifikasi 10 kelas penyakit daun tomat. |

history/
| File          | Isi                                                                                  |
| ------------- | ------------------------------------------------------------------------------------ |
| `history.csv` | Riwayat nilai accuracy, validation accuracy, loss, dan validation loss setiap epoch. |
| `history.pkl` | History training dalam format Pickle untuk kebutuhan visualisasi ulang.              |

models/

| File               | Isi                                                                               |
| ------------------ | --------------------------------------------------------------------------------- |
| `tomato_cnn.keras` | Model CNN terbaik hasil proses training yang digunakan untuk prediksi citra baru. |

gradcam/
| File             | Isi                                                     |
| ---------------- | ------------------------------------------------------- |
| `*_original.png` | Citra asli sebelum diproses.                            |
| `*_heatmap.png`  | Heatmap Grad-CAM yang menunjukkan area perhatian model. |
| `*_overlay.png`  | Overlay antara citra asli dan heatmap Grad-CAM.         |

## Ringkasan Output Penelitian
| Jenis Output          | Keterangan                       |
| --------------------- | -------------------------------- |
| Model CNN             | Model hasil training (`.keras`)  |
| History Training      | CSV dan PKL                      |
| Accuracy Graph        | PNG                              |
| Loss Graph            | PNG                              |
| Confusion Matrix      | PNG                              |
| Classification Report | TXT                              |
| Evaluation Result     | TXT                              |
| Grad-CAM Heatmap      | PNG                              |
| Prediksi Citra Baru   | Label kelas dan confidence score |


## Contoh hasil evaluasi
| Metrik    | Nilai      |
| --------- | ---------- |
| Accuracy  | **92,95%** |
| Precision | **93,16%** |
| Recall    | **92,95%** |
| F1-Score  | **92,97%** |

## visualisasi output
Tahap ini menghasilkan beberapa visualisasi yang digunakan untuk mengevaluasi performa model CNN dan menginterpretasikan hasil klasifikasi penyakit daun tomat. Visualisasi dibuat secara otomatis selama proses training, evaluasi, dan interpretasi model.
| File                    | Visualisasi                  | Keterangan                                                                                                                                                                          |
| ----------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `accuracy.png`          | **Grafik Accuracy Training** | Menampilkan perkembangan nilai *training accuracy* dan *validation accuracy* pada setiap epoch. Grafik digunakan untuk melihat peningkatan kemampuan model selama proses pelatihan. |
| `loss.png`              | **Grafik Loss Training**     | Menampilkan perubahan nilai *training loss* dan *validation loss* pada setiap epoch untuk mengevaluasi proses konvergensi model.                                                    |
| `confusion_matrix.png`  | **Confusion Matrix**         | Menunjukkan jumlah prediksi benar dan salah pada setiap kelas penyakit daun tomat sehingga memudahkan analisis performa model.                                                      |
| `img_h_17_original.png` | **Original Image**           | Menampilkan citra daun tomat asli yang digunakan sebagai input proses prediksi.                                                                                                     |
| `img_h_17_heatmap.png`  | **Grad-CAM Heatmap**         | Menampilkan area citra yang memiliki kontribusi terbesar terhadap keputusan model dalam melakukan klasifikasi.                                                                      |
| `img_h_17_overlay.png`  | **Grad-CAM Overlay**         | Menggabungkan citra asli dengan heatmap sehingga area penting yang diperhatikan model dapat terlihat lebih jelas.                                                                   |
