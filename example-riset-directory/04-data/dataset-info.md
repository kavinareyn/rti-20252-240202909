## Informasi Dataset

Dataset yang digunakan pada penelitian ini adalah Tomato Leaf Disease Dataset yang diperoleh dari platform Kaggle. Dataset tersebut berisi citra daun tomat yang telah diberi label berdasarkan kondisi daun, baik daun sehat maupun berbagai jenis penyakit. Dataset ini dipilih karena memiliki jumlah data yang cukup besar, kualitas citra yang seragam, serta mencakup berbagai kelas penyakit yang umum menyerang tanaman tomat sehingga sesuai untuk proses pelatihan model Convolutional Neural Network (CNN).

## Informasi Dataset
| Keterangan          | Informasi                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Nama Dataset        | Tomato Leaf Disease Dataset                                                                                                     |
| Sumber Dataset      | Kaggle ([https://www.kaggle.com/datasets/luisolazo/tomato-diseases](https://www.kaggle.com/datasets/luisolazo/tomato-diseases)) |
| Jenis Data          | Citra digital daun tomat (.jpg)                                                                                                 |
| Ukuran Citra        | 256 × 256 piksel                                                                                                                |
| Jumlah Kelas        | 10 kelas                                                                                                                        |
| Total Data Training | 17.753 citra                                                                                                                    |
| Total Data Testing  | 4.440 citra                                                                                                                     |
| Total Keseluruhan   | 22.193 citra                                                                                                                    |

## Distribusi Dataset
| Kelas                   | Data Training | Data Testing |
| ----------------------- | ------------: | -----------: |
| Bacterial Spot          |         1.679 |          444 |
| Early Blight            |         2.177 |          444 |
| Healthy                 |         1.883 |          444 |
| Late Blight             |         2.093 |          444 |
| Leaf Mold               |         1.460 |          444 |
| Mosaic Virus            |         1.197 |          444 |
| Septoria Leaf Spot      |         1.327 |          444 |
| Target Spot             |         1.110 |          444 |
| Two-Spotted Spider Mite |         1.232 |          444 |
| Yellow Leaf Curl Virus  |         3.595 |          444 |
| **Total**               |    **17.753** |    **4.440** |

## Karakteristik Dataset
Dataset terdiri atas citra daun tomat dengan kondisi sehat maupun terinfeksi penyakit. Seluruh citra telah dikelompokkan ke dalam masing-masing kelas sehingga dapat langsung digunakan untuk proses klasifikasi. Sebelum digunakan pada tahap pelatihan model, seluruh citra melalui proses preprocessing berupa perubahan ukuran citra menjadi 224 × 224 piksel dan normalisasi nilai piksel ke rentang 0–1 agar sesuai dengan kebutuhan input model CNN.

## Tujuan Penggunaan Dataset
Dataset digunakan sebagai sumber data utama untuk melatih, menguji, dan mengevaluasi model CNN dalam mengklasifikasikan penyakit daun tomat. Selain menghasilkan prediksi kelas penyakit, model juga dianalisis menggunakan metode Grad-CAM untuk memvisualisasikan area citra yang menjadi perhatian model saat melakukan klasifikasi.

## Referensi Dataset
> Luis Olazo. Tomato Diseases Dataset. Kaggle. https://www.kaggle.com/datasets/luisolazo/tomato-diseases