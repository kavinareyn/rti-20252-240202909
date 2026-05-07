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

Research Question : Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5?
Hypothesis        : H₁ : CNN Custom memberikan peningkatan akurasi yang signifikan dibanding LeNet-5.
Tipe Eksperimen   : [v] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi   | Deskripsi                         | IV Value   | CV Settings                                           |
| --------- | --------------------------------- | ---------- | ----------------------------------------------------- |
| Control   | Menggunakan model LeNet-5 standar | LeNet-5    | Dataset, preprocessing, dan parameter lingkungan sama |
| Treatment | Menggunakan model CNN Custom      | CNN Custom | Dataset, preprocessing, dan parameter lingkungan sama |


Fairness Checklist:
  [v] Dataset identik untuk semua kondisi
  [v] Preprocessing setara
  [v] Tuning effort setara
  [v] Environment identik
  [v] Metrik evaluasi sama

| Threat Type | Ancaman Spesifik                             | Mitigasi                                              |
| ----------- | -------------------------------------------- | ----------------------------------------------------- |
| Internal    | Overfitting pada dataset terbatas            | Menggunakan validasi dan data uji terpisah            |
| External    | Model belum tentu bekerja pada kondisi nyata | Menambah variasi dataset dari lingkungan berbeda      |
| Construct   | Accuracy saja belum cukup mewakili performa  | Menambahkan precision, recall, dan F1-score           |
| Conclusion  | Perbedaan hasil bisa dipengaruhi parameter   | Menggunakan parameter yang konsisten pada semua model |


Statistical Plan:
  Uji statistik   : Paired t-test
  Justifikasi      : Untuk membandingkan performa dua model pada dataset yang sama
  Alpha            : 0,05
  Effect size min  : 0,2
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5?
**Tipe eksperimen:** [v] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi   | Deskripsi                                  | IV Value   | CV Settings                                                    |
| --------- | ------------------------------------------ | ---------- | -------------------------------------------------------------- |
| Control   | Model baseline menggunakan LeNet-5 standar | LeNet-5    | Dataset citra daun tomat, preprocessing sama, split data 80:20 |
| Treatment | Model menggunakan CNN Custom               | CNN Custom | Dataset citra daun tomat, preprocessing sama, split data 80:20 |


---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria             | Status | Detail                                                          |
| -------------------- | ------ | --------------------------------------------------------------- |
| Dataset identik      | ✅      | Sama-sama menggunakan dataset citra daun tomat yang sama        |
| Preprocessing setara | ✅      | Kedua model menggunakan preprocessing citra yang sama           |
| Tuning effort setara | ✅      | Parameter training disesuaikan secara seimbang pada kedua model |
| Environment identik  | ✅      | Pengujian dilakukan pada perangkat dan lingkungan yang sama     |
| Metrik evaluasi sama | ✅      | Menggunakan accuracy, precision, recall, dan confusion matrix   |


**Ada yang tidak fair?** [ ] Ya / [v] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik                                                | Mitigasi                                                                   |
| ----------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Internal    | Overfitting pada dataset training                               | Menggunakan data uji terpisah dan validasi model                           |
| External    | Model mungkin tidak bekerja baik pada kondisi nyata di lapangan | Menambah variasi dataset dari berbagai kondisi pencahayaan dan lingkungan  |
| Construct   | Accuracy saja belum cukup menggambarkan performa model          | Menambahkan precision, recall, dan F1-score                                |
| Conclusion  | Hasil eksperimen bisa dipengaruhi pemilihan parameter tertentu  | Menggunakan parameter yang konsisten dan dokumentasi eksperimen yang jelas |


**Ancaman mana yang paling sulit dimitigasi?** External validity
**Mengapa?**
> Karena kondisi nyata di lapangan sangat beragam, sedangkan dataset penelitian biasanya masih terbatas dan tidak selalu mewakili semua kondisi tanaman tomat sebenarnya.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah semua baseline diuji dengan dataset, preprocessing, dan kondisi eksperimen yang sama?
2. Apakah baseline yang digunakan benar-benar relevan dan representatif, bukan metode lama yang sengaja dipilih agar mudah dikalahkan?
3. Apakah peningkatan hasilnya signifikan secara statistik dan dievaluasi dengan metrik yang jelas?

