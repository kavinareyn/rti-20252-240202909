# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : Intel® Core™ i7-12650H (12th Gen, 10 Cores / 16 Threads, 2.30 GHz)
  RAM     : 8 GB DDR4
  GPU     : NVIDIA GeForce RTX 2050 Laptop GPU (4 GB VRAM)
  Storage : SSD

Software:
  OS        : Windows 11 Home Single Language 23H2 (64-bit)
  Runtime   : Python 3.11
  Framework : TensorFlow 2.21.0

Dependencies:
| Library       | Version  | Sumber | Hash/Checksum |
| ------------- | -------- | ------ | ------------- |
| TensorFlow    | 2.21.0   | PyPI   | -             |
| Keras         | 3.15.0   | PyPI   | -             |
| NumPy         | 2.4.6    | PyPI   | -             |
| OpenCV-Python | 5.0.0.93 | PyPI   | -             |
| Matplotlib    | 3.11.0   | PyPI   | -             |
| Pandas        | 3.0.3    | PyPI   | -             |
| Scikit-learn  | 1.9.0    | PyPI   | -             |
| Pillow        | 12.3.0   | PyPI   | -             |



Konfigurasi:
  Config file     : config.py
  Random seed     : 42
  Hyperparameters : 
  - Image size : 224 × 224
  - Batch size : 32
  - Epoch : 20
  - Learning rate : 0.001
  - Optimizer : Adam
   - Loss Function : Sparse Categorical Crossentropy
   -Activation Function : ReLU (hidden layer) dan Softmax (output layer)
Reproducibility Check:
  [v] Dependency terdokumentasi (requirements.txt)
  [v] Seed ditetapkan di semua level (Python, NumPy, framework)
  [v] Config di version control
  [v] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen        | Spesifikasi                                                      |
| --------------- | ---------------------------------------------------------------- |
| **CPU**         | Intel® Core™ i7-12650H (12th Gen, 10 Core, 16 Threads, 2.30 GHz) |
| **RAM**         | 8 GB DDR4                                                        |
| **GPU**         | NVIDIA GeForce RTX 2050 Laptop GPU 4 GB                          |
| **OS**          | Windows 11 Home Single Language 23H2 (64-bit)                    |
| **Runtime**     | Python 3.11                                                      |
| **Framework**   | TensorFlow                                                       |
| **Random Seed** | 42                                                               |


**Dependencies (minimal 5):**

| Library       | Version  | Alasan Dibutuhkan                                                                                                 |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| TensorFlow    | 2.21.0   | Framework utama untuk membangun dan melatih model CNN                                                             |
| Keras         | 3.15.0   | API untuk membangun arsitektur CNN                                                                                |
| NumPy         | 2.4.6    | Operasi numerik dan manipulasi array                                                                              |
| Matplotlib    | 3.11.0   | Visualisasi grafik akurasi dan loss                                                                               |
| Scikit-learn  | 1.9.0    | Evaluasi model (confusion matrix, precision, recall, F1-score)                                                    |
| OpenCV-Python | 5.0.0.93 | Pengolahan citra dan implementasi Grad-CAM  |


---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama        | Hasil Sama? |
| --- | ---- | ------------------- | ----------- |
| 1   | 42   | Validation Accuracy | —           |
| 2   | 42   | Validation Accuracy | ☑ Ya*       |
| 3   | 42   | Validation Accuracy | ☑ Ya*       |


**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability:
> - **Thermal throttling** — CPU/GPU overheating pada run berturut-turut → clock speed turun → waktu eksekusi berubah
> - **Background process** — antivirus scan, update OS, atau cloud sync aktif saat run berlangsung
> - **Cache dari run sebelumnya** — hasil tersimpan di memori/disk sehingga run berikutnya tidak menjalankan komputasi penuh
> - **Random state tidak dikontrol di semua level** — Python seed di-set, tapi NumPy/PyTorch/TensorFlow punya seed independen

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [v] Random seed di-set di semua level
- [v] Tidak ada background process yang mengganggu
- [ ] Cache dibersihkan antar-run
- [ ] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen:
Tomato Leaf Disease Classification using Convolutional Neural Network (CNN) and Grad-CAM

## 1. Environment

- CPU          : Intel Core i7-12650H
- RAM          : 8 GB DDR4
- GPU          : NVIDIA GeForce RTX 2050 Laptop GPU (TensorFlow berjalan menggunakan CPU pada Windows)
- OS           : Windows 11 64-bit
- Runtime      : Python 3.11
- Framework    : TensorFlow 2.21.0
- Random Seed  : 42

---

## 2. Installation

1. Clone repository.
2. Buat virtual environment.

```bash
python -m venv .venv
```

3. Aktifkan virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

4. Install dependency.

```bash
pip install -r requirements.txt
```

---

## 3. Data

Dataset yang digunakan adalah **Tomato Diseases Dataset** yang diperoleh melalui Kaggle.

Sumber:
https://www.kaggle.com/datasets/luisolazo/tomato-diseases

Format data berupa citra RGB (.jpg) berukuran **256 × 256 piksel** yang terdiri atas **10 kelas** penyakit daun tomat.

Struktur dataset:

```text
dataset/
    train/
    test/
```

---

## 4. Execution

Jalankan eksperimen menggunakan:

```bash
python main.py
```

Program akan melakukan:

1. Memuat dataset
2. Melakukan preprocessing
3. Membangun model CNN
4. Melatih model
5. Menyimpan model
6. Menyimpan history training
7. Membuat grafik accuracy dan loss

---

## 5. Configuration

Seluruh konfigurasi eksperimen disimpan pada file:

```text
config.py
```

Parameter utama:

- Image Size : 224 × 224
- Batch Size : 32
- Learning Rate : 0.001
- Optimizer : Adam
- Epoch : 20 (pengujian awal menggunakan 3 epoch)
- Number of Classes : 10

---

## 6. Expected Output

Setelah eksperimen selesai, sistem menghasilkan:

```text
outputs/

├── models/
│   └── tomato_cnn.keras
│
├── history/
│   └── history.pkl
│
└── figures/
    ├── accuracy.png
    └── loss.png
```

Output tersebut digunakan sebagai hasil pelatihan model dan dokumentasi proses eksperimen.

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?
> Ya, sebagian besar dapat direproduksi, karena struktur proyek, dataset, dependency, konfigurasi eksperimen, serta langkah menjalankan program telah didokumentasikan melalui README.md, requirements.txt, dan config.py.
> Saat ini pengaturan random seed belum diterapkan pada seluruh komponen (Python, NumPy, dan TensorFlow), sehingga hasil pelatihan masih dapat sedikit berbeda pada setiap proses training. Selain itu, dokumentasi evaluasi model dan implementasi Grad-CAM masih dalam tahap pengembangan.

**Level saat ini:** [ ] Repeatability / [ ] Reproducibility / [v] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Dokumentasi pengaturan random seed secara menyeluruh, langkah evaluasi model (Accuracy, Precision, Recall, F1-score, dan Confusion Matrix), serta prosedur dan hasil visualisasi Grad-CAM belum tersedia karena masih dalam tahap pengembangan.
