# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5?

Variable → Component Mapping:
| Variabel                 | Tipe | Komponen Sistem      | Cara Manipulasi/Pengukuran                                        |
| ------------------------ | ---- | -------------------- | ----------------------------------------------------------------- |
| Jenis arsitektur CNN     | IV   | Model klasifikasi    | Mengganti model LeNet-5 dengan CNN Custom                         |
| Akurasi deteksi penyakit | DV   | Modul evaluasi model | Mengukur accuracy, precision, recall menggunakan confusion matrix |
| Dataset citra daun tomat | CV   | Dataset input        | Menggunakan dataset yang sama untuk semua model                   |


4 Prinsip Desain:
  [v] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [v] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [v] Measurement Integration — Pengukuran DV built-in
  [v] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : citra daun tomat
  Parameter      : Epoch, learning rate, batch size
  Output format  : Nilai accuracy, precision, recall, dan confusion matrix
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5?

| Variabel                 | Tipe | Komponen Sistem       | Cara Manipulasi / Pengukuran                                          |
| ------------------------ | ---- | --------------------- | --------------------------------------------------------------------- |
| Jenis arsitektur CNN     | IV   | Modul klasifikasi CNN | Mengganti model LeNet-5 dengan CNN Custom                             |
| Akurasi deteksi penyakit | DV   | Modul evaluasi model  | Mengukur accuracy, precision, dan recall menggunakan confusion matrix |
| Dataset citra daun tomat | CV   | Dataset input         | Menggunakan dataset yang sama pada semua model                        |


**Apakah semua variabel bisa di-map?** [v] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip         | Status | Bukti / Penjelasan                                                                         |
| --------------- | ------ | ------------------------------------------------------------------------------------------ |
| Traceability    | ✅      | Setiap variabel terhubung dengan komponen sistem seperti modul CNN, dataset, dan evaluasi  |
| Modularity      | ✅      | Model CNN dapat diganti antara LeNet-5 dan CNN Custom tanpa mengubah sistem utama          |
| Controllability | ✅      | Variabel kontrol seperti dataset dan parameter training dijaga tetap sama                  |
| Measurability   | ✅      | Performa sistem dapat diukur menggunakan accuracy, precision, recall, dan confusion matrix |


**Prinsip mana yang paling sulit dipenuhi?** Controllability
**Strategi untuk mengatasinya:**
>Menggunakan dataset, parameter, dan lingkungan pengujian yang sama agar hasil perbandingan model tetap adil dan konsisten.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A        | Komponen B            | Komponen C               | Hasil yang Diharapkan                                   |
| ------- | ----------------- | --------------------- | ------------------------ | ------------------------------------------------------- |
| Full    | ✅ CNN Custom      | ✅ Data preprocessing  | ✅ Hyperparameter tuning  | Akurasi terbaik sebagai baseline penuh                  |
| – A     | ❌ LeNet-5 standar | ✅                     | ✅                        | Akurasi menurun dibanding CNN Custom                    |
| – B     | ✅                 | ❌ Tanpa preprocessing | ✅                        | Model kurang stabil karena kualitas citra tidak seragam |
| – C     | ✅                 | ✅                     | ❌ Tanpa tuning parameter | Akurasi menurun karena parameter tidak optimal          |


**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (CNN Custom)
**Mengapa?**
> Karena arsitektur model CNN paling berpengaruh terhadap kemampuan sistem dalam mengenali pola penyakit pada citra daun tomat sehingga berdampak langsung pada peningkatan akurasi deteksi.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
Jika sistem langsung dibangun seperti produk yang monolitik dan penuh fitur, akan sulit mengetahui komponen mana yang sebenarnya mempengaruhi hasil eksperimen. Perubahan kecil pada satu bagian juga bisa memengaruhi bagian lain sehingga hasil penelitian menjadi kurang jelas dan sulit dievaluasi.

Arsitektur modular penting dalam riset karena setiap komponen dapat diuji, diganti, atau dihapus secara terpisah. Dengan begitu, peneliti lebih mudah melakukan eksperimen, ablation study, dan membuktikan pengaruh tiap komponen terhadap hasil penelitian.

