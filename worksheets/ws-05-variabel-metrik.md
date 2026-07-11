# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Bagaimana performa model Convolutional Neural Network (CNN) dalam mengklasifikasikan berbagai jenis penyakit daun tomat menggunakan dataset Tomato Diseases serta bagaimana Grad-CAM memvisualisasikan area yang menjadi dasar prediksi model?

| Variabel             | Tipe | Konsep                                                       | Metrik                                                  | Skala   | Satuan | Cara Mengukur                                                      | Justifikasi                                                       |
| -------------------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------- | ------- | ------ | ------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Model CNN            | IV   | Model klasifikasi penyakit daun tomat berbasis CNN           | Arsitektur CNN yang digunakan                           | Nominal | -      | Mengimplementasikan satu model CNN untuk proses klasifikasi        | Model CNN merupakan metode utama yang digunakan dalam penelitian. |
| Performa klasifikasi | DV   | Kemampuan model dalam mengklasifikasikan penyakit daun tomat | Accuracy, Precision, Recall, F1-score, Confusion Matrix | Rasio   | %      | Menguji model menggunakan data uji dan menghitung metrik evaluasi  | Digunakan untuk mengetahui tingkat keberhasilan model.            |
| Dataset Tomato Diseases | CV   | Dataset yang digunakan selama pelatihan dan pengujian        | Dataset tetap                                           | Nominal | -      | Menggunakan dataset Tomato Diseases yang sama pada seluruh eksperimen | Menjaga konsistensi hasil penelitian.                             |




Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [v] Setiap langkah terdokumentasi
  [v] Tidak ada "lompatan logis"
  [v] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Bagaimana performa model Convolutional Neural Network (CNN) dalam mengklasifikasikan berbagai jenis penyakit daun tomat menggunakan dataset Tomato Diseases serta bagaimana Grad-CAM memvisualisasikan area yang menjadi dasar prediksi model?

| Variabel             | Tipe | Konsep Abstrak                                         | Metrik Konkret                                          | Skala (NOIR) | Satuan |
| -------------------- | ---- | ------------------------------------------------------ | ------------------------------------------------------- | ------------ | ------ |
| Model CNN            | IV   | Metode klasifikasi penyakit daun tomat                 | Implementasi CNN (MobileNetV2)                          | Nominal      | —      |
| Performa klasifikasi | DV   | Kemampuan model mengklasifikasikan penyakit daun tomat | Accuracy, Precision, Recall, F1-score, Confusion Matrix | Rasio        | %      |
| Dataset Tomato Diseases | CV   | Dataset yang digunakan selama eksperimen               | Dataset Tomato Diseases  (10 kelas penyakit daun tomat)     | Nominal      | —      |



**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [v] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| **Kriteria**       | **Skor (1–5)** | **Justifikasi**                                                                                                                               |
| ------------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Representative** | **5**          | Accuracy, Precision, Recall, dan F1-score merupakan metrik standar yang mampu merepresentasikan performa model klasifikasi secara menyeluruh. |
| **Sensitive**      | **5**          | Metrik tersebut sensitif terhadap perubahan hasil prediksi sehingga dapat menunjukkan peningkatan atau penurunan performa model.              |
| **Feasible**       | **5**          | Seluruh metrik dapat dihitung secara otomatis menggunakan library seperti Scikit-learn sehingga mudah diterapkan pada penelitian.             |



**Apakah perlu secondary metric?** [v] Ya / [ ] Tidak
> Confusion Matrix, karena dapat menunjukkan jumlah prediksi yang benar dan salah pada setiap kelas penyakit. Hal ini membantu menganalisis kelas mana yang masih sering mengalami kesalahan klasifikasi.
**Contoh kasus ceiling effect untuk metrik ini:**
> Jika nilai Accuracy sudah sangat tinggi (misalnya di atas 99%), maka peningkatan performa model akan sulit terlihat hanya dari accuracy. Oleh karena itu, Precision, Recall, F1-score, dan Confusion Matrix tetap diperlukan untuk memberikan evaluasi yang lebih rinci terhadap performa model pada setiap kelas penyakit.
---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| **Dimensi**            | **Pertanyaan**                             | **Jawaban**                                                                                                             | **Strategi Mitigasi**                                                                                                 |
| ---------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Completeness**       | Apakah semua data point terkumpul?         | Ya, seluruh citra daun tomat yang digunakan berasal dari dataset Tomato Diseases  yang telah memiliki label kelas penyakit. | Memastikan seluruh data berhasil dimuat dan tidak ada file yang rusak atau hilang sebelum proses pelatihan.           |
| **Consistency**        | Apakah ada kontradiksi internal?           | Tidak, seluruh data menggunakan format citra dan label yang konsisten.                                                  | Melakukan preprocessing yang sama pada seluruh citra dan menggunakan pembagian dataset yang konsisten.                |
| **Validity**           | Apakah benar-benar mengukur yang dimaksud? | Ya, metrik Accuracy, Precision, Recall, dan F1-score digunakan untuk mengukur performa klasifikasi model CNN.           | Menggunakan metrik evaluasi standar dan dataset yang telah diberi label dengan benar.                                 |
| **Representativeness** | Apakah sampel mewakili populasi target?    | Ya, dataset Diseases mencakup beberapa jenis penyakit daun tomat sehingga cukup mewakili objek penelitian.          | Menggunakan seluruh kelas penyakit yang tersedia pada dataset dan membagi data menjadi data latih, validasi, dan uji. |


---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat hasil data dapat dianggap sebagai p-hacking karena peneliti berpotensi memilih metrik yang menghasilkan nilai terbaik sehingga kesimpulan menjadi bias. Sebaliknya, eksplorasi data yang sah dilakukan untuk memahami karakteristik data tanpa mengubah tujuan atau metrik penelitian. Oleh karena itu, metrik evaluasi sebaiknya ditentukan sebelum eksperimen dilakukan agar hasil penelitian lebih objektif dan dapat dipercaya.