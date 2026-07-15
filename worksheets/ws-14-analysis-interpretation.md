# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
  | Skenario         |      Mean |      Std |    Median |       Min |       Max |     n |
| ---------------- | --------: | -------: | --------: | --------: | --------: | ----: |
| CNN (Accuracy %) | **91.65** | **0.90** | **91.32** | **91.01** | **92.95** | **4** |


2. Uji Hipotesis:
   Uji yang digunakan  : Tidak dilakukan uji hipotesis inferensial.
   Justifikasi          : Penelitian ini bertujuan mengevaluasi performa satu model CNN pada klasifikasi penyakit daun tomat, bukan membandingkan dua atau lebih metode. Oleh karena itu, analisis difokuskan pada statistik deskriptif dan evaluasi metrik performa (Accuracy, Precision, Recall, dan F1-Score).
   Hasil: p = -, effect size (d/r/η²) = -
   CI 95%               : -

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak
   > Tidak dilakukan pengujian hipotesis inferensial karena penelitian tidak membandingkan dua kelompok atau lebih. Evaluasi dilakukan menggunakan metrik performa model.

4. Interpretasi:
   Hubungan ke RQ       : Hasil penelitian menunjukkan bahwa model CNN mampu mengklasifikasikan 10 kelas penyakit daun tomat dengan baik. Berdasarkan empat kali eksperimen, model memperoleh rata-rata accuracy sebesar 91,65%, sehingga dapat disimpulkan bahwa CNN memiliki performa yang baik dalam melakukan klasifikasi pada Tomato Leaf Disease Dataset. Selain itu, visualisasi Grad-CAM menunjukkan area citra yang menjadi perhatian model ketika menghasilkan prediksi, sehingga membantu menjelaskan proses pengambilan keputusan model.

   Practical significance: Akurasi di atas 90% menunjukkan bahwa model memiliki potensi untuk membantu proses identifikasi penyakit daun tomat secara otomatis. Dengan bantuan visualisasi Grad-CAM, pengguna juga dapat memahami bagian daun yang menjadi dasar prediksi model sehingga meningkatkan interpretabilitas sistem.

   Perbandingan literatur: Hasil penelitian ini sejalan dengan berbagai penelitian sebelumnya yang menunjukkan bahwa Convolutional Neural Network (CNN) efektif digunakan untuk klasifikasi penyakit tanaman berdasarkan citra daun. Perbedaan nilai akurasi dapat dipengaruhi oleh perbedaan dataset, arsitektur CNN, jumlah epoch, teknik preprocessing, serta konfigurasi pelatihan yang digunakan.

5. Limitation:
   | Jenis      | Ancaman                                         | Dampak                                                    | Mitigasi                                                                              |
| ---------- | ----------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Dataset    | Dataset hanya berasal dari satu sumber (Kaggle) | Generalisasi model pada data lapangan mungkin terbatas    | Menggunakan dataset yang lebih beragam pada penelitian selanjutnya                    |
| Model      | Menggunakan CNN sederhana                       | Performa mungkin lebih rendah dibanding arsitektur modern | Membandingkan dengan ResNet, EfficientNet, atau MobileNet pada penelitian selanjutnya |
| Lingkungan | Training dilakukan menggunakan CPU              | Waktu pelatihan relatif lama                              | Menggunakan GPU pada penelitian berikutnya                                            |


6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial :
Tidak terdapat kegagalan signifikan selama eksperimen. Variasi kecil antar-run disebabkan oleh proses pelatihan yang bersifat stokastik.

Boundary condition :
Model dievaluasi pada Tomato Leaf Disease Dataset dengan 10 kelas. Performa pada citra dari lingkungan nyata dengan kondisi pencahayaan, sudut pengambilan gambar, atau kualitas kamera yang berbeda belum dievaluasi.

Insight :
Model CNN menunjukkan performa yang stabil pada empat kali eksperimen dengan rata-rata accuracy 91,65%. Variasi antar-run relatif kecil sehingga menunjukkan repeatability yang baik.
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan                                     | Jawaban                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Berapa grup yang dibandingkan?**             | **1 grup (Model CNN)**                                                                                                                                                                                                                                                                                                                       |
| **Apakah data berpasangan (paired)?**          | **Tidak**                                                                                                                                                                                                                                                                                                                                    |
| **Apakah distribusi normal? (uji normalitas)** | **Tidak diuji, karena tidak dilakukan analisis inferensial atau perbandingan antargrup.**                                                                                                                                                                                                                                                    |
| **Uji yang dipilih:**                          | **Tidak dilakukan uji statistik inferensial.**                                                                                                                                                                                                                                                                                               |
| **Justifikasi:**                               | **Penelitian ini bertujuan mengevaluasi performa satu model CNN dalam mengklasifikasikan penyakit daun tomat. Analisis dilakukan menggunakan statistik deskriptif (mean, standar deviasi) serta metrik evaluasi Accuracy, Precision, Recall, dan F1-Score dari empat kali eksperimen, sehingga tidak diperlukan uji hipotesis inferensial.** |


**Effect size yang akan dilaporkan:** [ ] Cohen's d / [ ] Eta-squared / [v] Lainnya: Tidak dilaporkan (tidak dilakukan uji inferensial).

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Aspek                      | Interpretasi                                                                                                                                                                                                                  |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Signifikansi statistik** | **Nilai p = 0,045 lebih kecil dari α = 0,05, sehingga perbedaan performa antara Model A dan Model B signifikan secara statistik.**                                                                                            |
| **Effect size**            | **Cohen's d = 0,74 menunjukkan effect size sedang hingga besar (medium-to-large effect), sehingga perbedaan kedua model memiliki pengaruh yang cukup berarti.**                                                               |
| **Practical significance** | **Selain signifikan secara statistik, peningkatan accuracy dari 87,8% menjadi 89,2% dapat memberikan peningkatan performa yang bermanfaat pada aplikasi nyata, terutama jika kesalahan klasifikasi memiliki dampak penting.** |
| **Hubungan ke RQ**         | **Hasil menunjukkan bahwa Model A memberikan performa yang lebih baik dibandingkan Model B sehingga lebih sesuai untuk menjawab research question mengenai metode dengan akurasi yang lebih tinggi.**                         |
| **Perbandingan literatur** | **Hasil ini sejalan dengan penelitian sebelumnya yang menunjukkan bahwa metode dengan karakteristik serupa mampu meningkatkan akurasi klasifikasi dibandingkan pendekatan dasar (baseline).**                                 |


---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan                            | Jawaban                                                                                                                                                                                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Apakah ini "gagal"?**               | **Tidak. Hipotesis yang tidak didukung tetap merupakan hasil penelitian yang valid dan memberikan informasi mengenai batasan metode yang diuji.**                                                                                            |
| **Kemungkinan penyebab?**             | **Metode baru menambah kompleksitas komputasi tetapi tidak memberikan peningkatan performa yang signifikan dibandingkan baseline. Selain itu, konfigurasi parameter atau karakteristik dataset mungkin belum sesuai untuk metode tersebut.** |
| **Boundary condition?**               | **Metode baru kemungkinan lebih efektif pada dataset yang lebih besar atau dengan karakteristik data yang berbeda. Pada dataset saat ini, baseline sudah memberikan performa yang baik sehingga peningkatan menjadi sulit dicapai.**         |
| **Insight yang bisa diambil?**        | **Peningkatan kompleksitas algoritma tidak selalu menghasilkan peningkatan performa. Pemilihan metode harus mempertimbangkan keseimbangan antara akurasi, kompleksitas, dan waktu komputasi.**                                               |
| **Apakah layak dilaporkan? Mengapa?** | **Ya. Hasil negatif tetap penting karena membantu menjelaskan batasan metode, mencegah penelitian lain mengulangi pendekatan yang sama tanpa alasan, serta memberikan arahan untuk penelitian selanjutnya.**                                 |


**Limitation terkait:**
| Jenis         | Ancaman                            | Dampak                                                                                   |
| ------------- | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| Statistical   | Jumlah run eksperimen terbatas     | Variasi hasil mungkin belum sepenuhnya menggambarkan seluruh kemungkinan performa model. |
| Dataset       | Dataset berasal dari satu sumber   | Generalisasi model terhadap data dari lingkungan nyata belum dapat dipastikan.           |
| Computational | Training dilakukan menggunakan CPU | Waktu pelatihan relatif lama sehingga membatasi jumlah eksperimen yang dapat dilakukan.  |


---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Dalam penelitian, failure tidak selalu berarti kegagalan. Hasil yang tidak sesuai dengan hipotesis tetap merupakan kontribusi ilmiah karena menunjukkan batasan suatu metode dan memberikan informasi yang dapat digunakan sebagai dasar penelitian berikutnya. Melalui failure analysis, peneliti dapat memahami penyebab hasil yang kurang optimal, mengidentifikasi kondisi ketika suatu metode bekerja dengan baik atau kurang efektif, serta memberikan rekomendasi untuk pengembangan di masa mendatang. Dengan demikian, hasil negatif tetap memiliki nilai ilmiah dan membantu meningkatkan kualitas penelitian selanjutnya.
