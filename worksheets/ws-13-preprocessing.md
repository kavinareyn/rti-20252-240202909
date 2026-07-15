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

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| *Contoh: Missing di kolom "label"* | *12 dari 500 (2.4%)* | *Listwise deletion* | *< 5%, distribusi random (MCAR)* |
| | | | |
| | | | |
| | | | |

**Jumlah data sebelum cleaning:** ____
**Jumlah data setelah cleaning:** ____
**Persentase data yang hilang/berubah:** ____%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| *Contoh: response_time* | *0.1 – 45.2s* | *Right-skewed* | *Ya (45.2s)* | *Robust scaling* | *Ada outlier, perlu robust* || *Contoh: accuracy_score* | *0.72 – 0.95* | *Normal, narrow* | *Tidak* | *Tidak perlu* | *Sudah dalam [0,1], metode berbasis distance tidak digunakan* || | | | | | |
| | | | | | |

**Apakah normalisasi diperlukan?** [ ] Ya / [ ] Tidak
**Justifikasi:**
> ___________________________________________________

**Leakage check:**
- [ ] Parameter dihitung dari training set saja
- [ ] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: ____________________
2. Data awal: ____ records, ____ features
3. Cleaning:
   - Missing values: ____ kasus, metode: ____
   - Duplikat: ____ kasus, tindakan: ____
   - Error: ____ kasus, tindakan: ____
4. Transformation: ____________________
5. Normalisasi: ____ (metode), parameter dari ____
6. Data akhir: ____ records, ____ features
7. Leakage check: [ ] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> ___________________________________________________
> ___________________________________________________
