# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : Tomato Leaf Disease Dataset (Kaggle)
Jumlah data awal  : 22.193 citra (17.753 data training + 4.440 data testing)

| Masalah  | Jumlah Kasus | Penanganan         | Justifikasi                                                              |
| -------- | -----------: | ------------------ | ------------------------------------------------------------------------ |
| Missing  |            0 | Tidak ada tindakan | Seluruh citra berhasil dimuat tanpa data hilang.                         |
| Duplikat |            0 | Tidak ada tindakan | Dataset tidak mengandung citra duplikat yang digunakan dalam eksperimen. |
| Error    |            0 | Tidak ada tindakan | Seluruh file citra berhasil dibaca dan diproses.                         |


Transformation:
| Transformasi      | Variabel     | Detail                        | Alasan                                              |
| ----------------- | ------------ | ----------------------------- | --------------------------------------------------- |
| Resize Image      | Citra daun   | 224 × 224 piksel              | Menyeragamkan ukuran input CNN.                     |
| Convert to Tensor | Citra daun   | TensorFlow Tensor             | Agar dapat diproses oleh TensorFlow/Keras.          |
| Rescaling         | Nilai piksel | 0–255 → 0–1 (`image / 255.0`) | Mempercepat dan menstabilkan proses training model. |


Normalization:
  Metode    : Min-Max Normalization (Rescaling)
  Alasan    : Mengubah rentang nilai piksel dari 0–255 menjadi 0–1 sehingga proses optimasi model CNN menjadi lebih stabil dan konvergensi lebih cepat.
  Parameter : Dihitung dari setiap citra pada dataset training dan diterapkan secara konsisten pada data testing.

Leakage Check:
  [v] Parameter normalisasi dari training set saja
  [v] Tidak ada informasi test set dalam preprocessing
  [v] Cross-validation dilakukan setelah split

Jumlah data akhir : 22.193 citra
Script tersedia   : [v] Ya → path: src/data/check_dataset.py
src/data/dataset_loader.py
src/data/preprocessing.py | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah               | Jumlah Kasus | Penanganan         | Justifikasi                                                    |
| --------------------- | -----------: | ------------------ | -------------------------------------------------------------- |
| Missing value         |            0 | Tidak ada tindakan | Dataset citra tidak memiliki data yang hilang.                 |
| Duplikat              |            0 | Tidak ada tindakan | Tidak ditemukan citra duplikat yang digunakan pada eksperimen. |
| Error/Corrupted Image |            0 | Tidak ada tindakan | Seluruh citra berhasil dibaca saat pengecekan dataset.         |


**Jumlah data sebelum cleaning:** 22.193 citra
**Jumlah data setelah cleaning:** 22.193 citra
**Persentase data yang hilang/berubah:** 0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel           | Range Asli | Distribusi        | Outlier? | Metode Normalisasi | Alasan                                                                     |
| ------------------ | ---------- | ----------------- | -------- | ------------------ | -------------------------------------------------------------------------- |
| Nilai piksel citra | 0–255      | Intensitas piksel | Tidak    | Rescaling (÷255)   | Mengubah rentang piksel menjadi 0–1 agar proses training CNN lebih stabil. |
| Label kelas        | 0–9        | Kategorikal       | Tidak    | Tidak perlu        | Label digunakan sebagai target klasifikasi sehingga tidak dinormalisasi.   |


**Apakah normalisasi diperlukan?** [v] Ya / [ ] Tidak
**Justifikasi:**
> Normalisasi diperlukan pada nilai piksel citra karena CNN bekerja lebih baik ketika nilai input berada pada rentang yang kecil dan seragam. Pada penelitian ini digunakan metode rescaling dengan membagi setiap nilai piksel dengan 255 sehingga rentang berubah dari 0–255 menjadi 0–1. Label kelas tidak dinormalisasi karena merupakan data kategorikal yang digunakan sebagai target klasifikasi.

**Leakage check:**
- [v] Parameter dihitung dari training set saja
- [v] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset:
   Tomato Leaf Disease Dataset (Kaggle)

2. Data awal:
   22.193 records (17.753 training, 4.440 testing),
   10 kelas penyakit daun tomat

3. Cleaning:
   - Missing values : 0 kasus, metode: tidak ada tindakan
   - Duplikat       : 0 kasus, tindakan: tidak ada tindakan
   - Error          : 0 kasus, tindakan: tidak ada tindakan

4. Transformation:
   - Resize citra menjadi 224 × 224 piksel
   - Konversi gambar menjadi Tensor
   - Rescaling nilai piksel dari 0–255 menjadi 0–1

5. Normalisasi:
   Rescaling (nilai piksel /255),
   parameter diterapkan secara konsisten pada data training dan testing.

6. Data akhir:
   22.193 records,
   10 kelas

7. Leakage check:
   ☑ Lulus

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Normalisasi tidak selalu diperlukan untuk setiap jenis data. Pemilihan metode preprocessing harus disesuaikan dengan karakteristik data dan algoritma yang digunakan. Pada penelitian ini, normalisasi hanya diterapkan pada nilai piksel citra karena CNN memerlukan input dengan skala yang seragam, sedangkan label kelas tidak dinormalisasi. Jika preprocessing dilakukan secara berlebihan (over-preprocessing), terdapat risiko informasi penting pada data hilang, distribusi data berubah, atau bahkan terjadi data leakage yang dapat menyebabkan hasil evaluasi model menjadi bias dan tidak merepresentasikan performa sebenarnya.
