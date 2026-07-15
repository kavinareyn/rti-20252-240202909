# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario     | Seed | Parameter                    | Status    | Waktu       | Output File        |
| ----: | ------------ | ---- | ---------------------------- | --------- | ----------- | ------------------ |
|     1 | Training CNN | 42   | Epoch=20, Batch=32, LR=0.001 | ✅ Selesai | 167m 56.59s | `tomato_cnn.keras` |
|     2 | Training CNN | 42   | Epoch=20, Batch=32, LR=0.001 | ✅ Selesai | 98m 37.11s  | `tomato_cnn.keras` |
|     3 | Training CNN | 42   | Epoch=20, Batch=32, LR=0.001 | ✅ Selesai | 114m 18.09s | `tomato_cnn.keras` |
|     4 | Training CNN | 42   | Epoch=20, Batch=32, LR=0.001 | ✅ Selesai | 98m 29.28s  | `tomato_cnn.keras` |


Jumlah runs per skenario : 4
Total runs               : 4

Run ID    : RUN-001
Timestamp : (Isi tanggal dan waktu saat Run 1 dilakukan)
Skenario  : Training CNN 20 Epoch
Input     :
- Dataset : Tomato Leaf Disease Dataset
- Jumlah kelas : 10
- Image Size : 224×224
- Batch Size : 32
- Learning Rate : 0.001
- Epoch : 20
- Seed : 42

Output     :
Accuracy  : 91.08%
Precision : 91.32%
Recall    : 91.08%
F1-Score  : 91.06%
Execution Time : 167 menit 56.59 detik

Anomali   :
Warning TensorFlow terkait Prefetch Autotuner, namun proses training selesai dengan baik.

Catatan   :
Model berhasil disimpan.
History training berhasil disimpan.
Confusion Matrix berhasil dibuat.
Grafik Accuracy dan Loss berhasil dibuat.

Run ID    : RUN-002
Timestamp : (Isi tanggal dan waktu saat Run 2 dilakukan)
Skenario  : Training CNN 20 Epoch
Input     :
- Dataset : Tomato Leaf Disease Dataset
- Jumlah kelas : 10
- Image Size : 224×224
- Batch Size : 32
- Learning Rate : 0.001
- Epoch : 20
- Seed : 42

Output     :
Accuracy  : 91.55%
Precision : 92.01%
Recall    : 91.55%
F1-Score  : 91.59%
Execution Time : 98 menit 37.11 detik

Anomali   :
Tidak ada.

Catatan   :
Seluruh proses training dan evaluasi berhasil dijalankan.

Run ID    : RUN-003
Timestamp : (Isi tanggal dan waktu saat Run 3 dilakukan)
Skenario  : Training CNN 20 Epoch
Input     :
- Dataset : Tomato Leaf Disease Dataset
- Jumlah kelas : 10
- Image Size : 224×224
- Batch Size : 32
- Learning Rate : 0.001
- Epoch : 20
- Seed : 42

Output     :
Accuracy  : 91.01%
Precision : 91.18%
Recall    : 91.01%
F1-Score  : 90.94%
Execution Time : 114 menit 18.09 detik

Anomali   :
Tidak ada.

Catatan   :
Model berhasil disimpan dan seluruh output evaluasi berhasil dibuat.

Run ID    : RUN-004
Timestamp : (Isi tanggal dan waktu saat Run 4 dilakukan)
Skenario  : Training CNN 20 Epoch
Input     :
- Dataset : Tomato Leaf Disease Dataset
- Jumlah kelas : 10
- Image Size : 224×224
- Batch Size : 32
- Learning Rate : 0.001
- Epoch : 20
- Seed : 42

Output     :
Accuracy  : 92.95%
Precision : 93.16%
Recall    : 92.95%
F1-Score  : 92.97%
Execution Time : 98 menit 29.28 detik

Anomali   :
Tidak ada.

Catatan   :
Merupakan hasil terbaik dari empat kali eksperimen.
Seluruh artefak penelitian (model, history, confusion matrix, grafik, dan Grad-CAM) berhasil dihasilkan.
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario                          | Seed | Parameter Kunci              |    Status   |
| :---: | --------------------------------- | :--: | ---------------------------- | :---------: |
|   1   | CNN – Tomato Leaf Disease Dataset |  42  | lr=0.001, epoch=20, batch=32 | ✅ Completed |
|   2   | CNN – Tomato Leaf Disease Dataset |  42  | lr=0.001, epoch=20, batch=32 | ✅ Completed |
|   3   | CNN – Tomato Leaf Disease Dataset |  42  | lr=0.001, epoch=20, batch=32 | ✅ Completed |
|   4   | CNN – Tomato Leaf Disease Dataset |  42  | lr=0.001, epoch=20, batch=32 | ✅ Completed |



**Total skenario:** 1
**Run per skenario:** 4
**Total run keseluruhan:** 4

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field         | Nilai                                                                           |
| ------------- | ------------------------------------------------------------------------------- |
| **Run ID**    | RUN-001, RUN-002, RUN-003, RUN-004                                              |
| **Timestamp** | 12-07-2026 13:50, 14-07-2026 00:50, 14-07-2026 05:19, 15-07-2026 16:29          |


**Konfigurasi:**
| Field             | Nilai                                                                    |
| ----------------- | ------------------------------------------------------------------------ |
| **Seed**          | 42                                                                       |
| **Code Version**  | Final CNN Implementation (atau commit Git terakhir jika menggunakan Git) |
| **Dataset**       | Tomato Leaf Disease Dataset                                              |
| **Model**         | Convolutional Neural Network (CNN)                                       |
| **Image Size**    | 224 × 224                                                                |
| **Batch Size**    | 32                                                                       |
| **Learning Rate** | 0.001                                                                    |
| **Epoch**         | 20                                                                       |
| **Optimizer**     | Adam                                                                     |
| **Loss Function** | Sparse Categorical Crossentropy                                          |


**Hasil:**
| Metrik                 | Tipe Data | Range Valid      |
| ---------------------- | --------- | ---------------- |
| Accuracy               | float     | 0.0 – 1.0        |
| Precision              | float     | 0.0 – 1.0        |
| Recall                 | float     | 0.0 – 1.0        |
| F1-Score               | float     | 0.0 – 1.0        |
| Execution Time (menit) | float     | > 0              |
| Training Status        | string    | Success / Failed |


**Format output:** [v] CSV / [v] JSON / [ ] Database / [v] Lainnya: PKL (.pkl), PNG (.png), KERAS (.keras), TXT (.txt)
---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali                 | Contoh                                                                                              | Tindakan                                                                                                                                            |
| ----------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Run gagal (crash)             | Error saat proses training atau penyimpanan model (`ValueError: I/O operation on closed file`)      | Dokumentasikan error, periksa kode dan konfigurasi, perbaiki penyebabnya, lalu jalankan ulang eksperimen dengan parameter yang sama.                |
| Hasil ekstrem                 | Accuracy jauh lebih rendah atau lebih tinggi dibanding run lainnya (misalnya < 85% atau > 95%)      | Periksa kembali dataset, seed, parameter training, dan log proses. Jika ditemukan penyebab teknis, lakukan re-run dan catat hasilnya.               |
| Waktu eksekusi anomali        | Waktu training jauh lebih lama (misalnya Run 1 ±168 menit, sedangkan run lain sekitar 98–114 menit) | Periksa kondisi komputer (beban CPU, RAM, proses latar belakang), dokumentasikan perbedaan waktu, tetapi gunakan hasil jika metrik tetap konsisten. |
| Inkonsistensi dengan run lain | Nilai Accuracy, Precision, Recall, atau F1-Score berbeda jauh dibanding run lain                    | Bandingkan konfigurasi eksperimen, pastikan dataset dan parameter identik, kemudian lakukan analisis atau pengulangan eksperimen bila diperlukan.   |


**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Pada awalnya, hasil eksperimen hanya diperoleh dari satu kali proses training sehingga belum dapat menunjukkan konsistensi performa model. Selain itu, selama pengembangan sempat ditemukan beberapa kendala seperti error saat penyimpanan model (I/O operation on closed file) dan perbedaan waktu eksekusi antar-run yang perlu dianalisis sebelum hasil digunakan sebagai hasil akhir penelitian.
**Yang akan dilakukan berbeda:**
> Pada penelitian ini dilakukan empat kali eksperimen (multiple run) dengan konfigurasi yang sama untuk menguji repeatability model. Setiap hasil dicatat, dibandingkan menggunakan metrik Accuracy, Precision, Recall, dan F1-Score, serta didokumentasikan bersama waktu eksekusi dan kemungkinan anomali. Pendekatan ini meningkatkan kepercayaan terhadap hasil penelitian karena menunjukkan bahwa model memberikan performa yang konsisten pada beberapa kali pengujian.
