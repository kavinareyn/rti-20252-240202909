# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Bagaimana performa model Convolutional Neural Network (CNN) dalam mengklasifikasikan berbagai jenis penyakit daun tomat menggunakan dataset Tomato Diseases serta bagaimana Grad-CAM memvisualisasikan area yang menjadi dasar prediksi model?
Hypothesis        : H₁ : Model CNN yang dikembangkan mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat dengan performa yang baik serta memberikan interpretasi visual hasil prediksi menggunakan Grad-CAM.
Tipe Eksperimen   : [v] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi       | Deskripsi                                                                                                                | IV Value                        | CV Settings                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------- | ---------------------------------------------------------------------- |
| **Control**   | Penelitian baseline (Saputra et al., 2023) menggunakan CNN untuk klasifikasi 4 kelas penyakit daun tomat tanpa Grad-CAM. | CNN (4 kelas, tanpa Grad-CAM)   | Metrik evaluasi dan prosedur klasifikasi dibuat setara.                |
| **Treatment** | Model usulan menggunakan CNN untuk klasifikasi 10 kelas penyakit daun tomat dengan Grad-CAM.                             | CNN (10 kelas, dengan Grad-CAM) | Dataset Tomato Diseases, preprocessing, dan metrik evaluasi yang sama. |



Fairness Checklist:
  [v] Dataset identik untuk semua kondisi
  [v] Preprocessing setara
  [v] Tuning effort setara
  [v] Environment identik
  [v] Metrik evaluasi sama

| Threat Type    | Ancaman Spesifik                                                         | Mitigasi                                                                                                |
| -------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Internal**   | Parameter pelatihan dapat memengaruhi hasil klasifikasi.                 | Menggunakan parameter pelatihan yang konsisten pada seluruh eksperimen.                                 |
| **External**   | Hasil mungkin berbeda jika menggunakan dataset lain atau citra lapangan. | Menjelaskan bahwa penelitian menggunakan dataset Tomato Diseases sebagai ruang lingkup penelitian.      |
| **Construct**  | Metrik evaluasi belum sepenuhnya menggambarkan interpretabilitas model.  | Menggunakan Accuracy, Precision, Recall, F1-score, Confusion Matrix, serta visualisasi Grad-CAM.        |
| **Conclusion** | Kesimpulan dapat dipengaruhi oleh jumlah data atau distribusi kelas.     | Menggunakan pembagian data latih dan data uji secara konsisten serta melaporkan seluruh hasil evaluasi. |



Statistical Plan:
  Uji statistik   : Analisis deskriptif menggunakan Accuracy, Precision, Recall, F1-score, dan Confusion Matrix.
  Justifikasi      : UTujuan penelitian adalah mengevaluasi performa model CNN dan interpretasi hasil menggunakan Grad-CAM, sehingga analisis deskriptif sudah memadai untuk membandingkan hasil dengan penelitian baseline.
  Alpha            : 0,05
  Effect size min  : Tidak ditetapkan, karena penelitian ini berfokus pada evaluasi performa model, bukan pengujian signifikansi statistik.
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana performa model Convolutional Neural Network (CNN) dalam mengklasifikasikan berbagai jenis penyakit daun tomat menggunakan dataset Tomato Diseases serta bagaimana Grad-CAM memvisualisasikan area yang menjadi dasar prediksi model?
**Tipe eksperimen:** [v] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi       | Deskripsi                                                                                                     | IV Value                        | CV Settings                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------------- |
| **Control**   | Penelitian baseline (Saputra et al., 2023) menggunakan CNN untuk klasifikasi 4 kelas penyakit tanpa Grad-CAM. | CNN (4 kelas, tanpa Grad-CAM)   | Dataset Tomato Diseases, preprocessing yang sama, ukuran citra 224×224, metrik evaluasi sama. |
| **Treatment** | Model usulan menggunakan CNN untuk klasifikasi 10 kelas penyakit dengan Grad-CAM.                             | CNN (10 kelas, dengan Grad-CAM) | Dataset Tomato Diseases, preprocessing yang sama, ukuran citra 224×224, metrik evaluasi sama. |



---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria             | Status | Detail                                                                            |
| -------------------- | ------ | --------------------------------------------------------------------------------- |
| Dataset identik      | ✅      | Kedua kondisi menggunakan dataset Tomato Diseases.                                |
| Preprocessing setara | ✅      | Seluruh citra diproses dengan langkah preprocessing yang sama.                    |
| Tuning effort setara | ✅      | Parameter pelatihan ditetapkan secara konsisten pada kedua kondisi.               |
| Environment identik  | ✅      | Eksperimen dijalankan pada perangkat dan lingkungan perangkat lunak yang sama.    |
| Metrik evaluasi sama | ✅      | Evaluasi menggunakan Accuracy, Precision, Recall, F1-score, dan Confusion Matrix. |



**Ada yang tidak fair?** [ ] Ya / [v] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| **Threat Type** | **Ancaman Spesifik**                                                                                                               | **Mitigasi**                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Internal**    | Pembagian data latih dan data uji yang tidak tepat dapat menyebabkan hasil evaluasi menjadi bias.                                  | Menggunakan pembagian data train dan test yang konsisten serta memastikan tidak ada data yang tumpang tindih. |
| **External**    | Model mungkin memiliki performa berbeda jika diuji menggunakan citra daun tomat dari kondisi lapangan yang berbeda dengan dataset. | Menjelaskan bahwa penelitian hanya menggunakan dataset Tomato Diseases sebagai ruang lingkup penelitian.      |
| **Construct**   | Metrik evaluasi belum sepenuhnya menggambarkan interpretabilitas model.                                                            | Menggunakan Accuracy, Precision, Recall, F1-score, Confusion Matrix, serta visualisasi Grad-CAM.              |
| **Conclusion**  | Kesimpulan dapat dipengaruhi oleh jumlah data atau distribusi kelas yang tidak seimbang.                                           | Melaporkan seluruh hasil evaluasi dan menggunakan pembagian data yang proporsional pada setiap kelas.         |



**Ancaman mana yang paling sulit dimitigasi?** External Threat
**Mengapa?**
> Karena penelitian menggunakan dataset publik sehingga belum dapat menjamin bahwa model akan memiliki performa yang sama pada citra daun tomat yang diambil langsung di lapangan dengan kondisi pencahayaan, sudut pengambilan gambar, atau kualitas kamera yang berbeda.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah semua metode dibandingkan menggunakan dataset dan metrik evaluasi yang sama?
2. Apakah eksperimen dilakukan dengan kondisi yang adil, seperti preprocessing, parameter pelatihan, dan lingkungan pengujian yang sama?
3. Apakah peningkatan hasil didukung oleh analisis atau bukti yang jelas sehingga klaim dapat dipercaya dan direproduksi?

