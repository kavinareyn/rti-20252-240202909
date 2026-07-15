# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Bagaimana performa Convolutional Neural Network (CNN) dalam mengklasifikasikan 10 kelas penyakit daun tomat menggunakan Tomato Leaf Disease Dataset, serta bagaimana Grad-CAM memvisualisasikan area citra yang digunakan model dalam melakukan prediksi?
Metrik Utama      : Accuracy, Precision, Recall, dan F1-Score

Tabel Hasil:
| Skenario       | Accuracy (mean ± std) | F1-Score (mean ± std) | n |
| -------------- | --------------------- | --------------------- | - |
| CNN (20 Epoch) | **91.65% ± 0.91%**    | **91.64% ± 0.92%**    | 4 |


Visualisasi yang Direncanakan:
| # | Jenis Grafik                              | Pesan Utama                                                                  | Metrik                      |
| - | ----------------------------------------- | ---------------------------------------------------------------------------- | --------------------------- |
| 1 | Grafik Accuracy dan Loss                  | Menunjukkan proses pembelajaran model selama training dan validasi           | Accuracy, Loss              |
| 2 | Confusion Matrix                          | Menunjukkan performa klasifikasi pada setiap kelas penyakit daun tomat       | Accuracy per kelas          |
| 3 | Bar Chart Precision, Recall, dan F1-Score | Membandingkan performa model pada masing-masing kelas                        | Precision, Recall, F1-Score |
| 4 | Visualisasi Grad-CAM                      | Menunjukkan area citra daun yang menjadi fokus model saat melakukan prediksi | Heatmap Grad-CAM            |


Bias Check:
  [v] Y-axis mulai dari 0 (atau dijustifikasi)
  [v] Error bar/CI ditampilkan
  [v] Semua data disertakan (tidak cherry-picked)
  [v] Tidak menggunakan 3D tanpa alasan
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario                                                 | Accuracy (mean ± std) | Waktu Eksekusi (mean ± std) |  n |
| -------------------------------------------------------- | --------------------: | --------------------------: | -: |
| CNN (Epoch = 20, Batch Size = 32, Learning Rate = 0.001) |    **91.65 ± 0.90 %** |    **119.84 ± 32.92 menit** |  4 |


**Checklist tabel:**
- [v] Self-contained (judul jelas, satuan ada, N tercantum)
- [v] Mean ± std (bukan single number)
- [v] Diurutkan berdasarkan metrik utama
- [v] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik                 | Pesan                                                                                 | Data yang Digunakan                               |
| - | ---------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 1 | Line Chart (Accuracy & Loss) | Menunjukkan proses pembelajaran model selama training dan validasi hingga konvergen   | Accuracy dan Loss setiap epoch                    |
| 2 | Confusion Matrix             | Menunjukkan kemampuan model mengklasifikasikan setiap kelas penyakit daun tomat       | Hasil prediksi dan label sebenarnya pada data uji |
| 3 | Bar Chart + Error Bar        | Menunjukkan performa rata-rata model beserta variasi hasil dari empat kali eksperimen | Mean Accuracy ± Standard Deviation (4 run)        |


---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan                        | Jawaban                                                                                                                                                          |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Apakah Y-axis menyesatkan?        | **Ya.** Perbedaan 0,4% akan terlihat jauh lebih besar daripada kondisi sebenarnya karena sumbu Y tidak dimulai dari 0.                                           |
| Apakah error bar ditampilkan?     | **Tidak.** Error bar perlu ditampilkan agar variasi hasil antar-run dapat diketahui.                                                                             |
| Apakah semua kondisi ditampilkan? | **Ya.** Kedua metode ditampilkan, tetapi visualisasi masih berpotensi menyesatkan karena skala sumbu Y.                                                          |
| Apa solusinya?                    | Gunakan sumbu Y yang dimulai dari 0 atau berikan alasan jika menggunakan rentang tertentu, serta tampilkan error bar (standar deviasi atau confidence interval). |


**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [v] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: ____

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel dan grafik memiliki fungsi yang saling melengkapi. Tabel menyajikan nilai numerik secara lengkap dan presisi sehingga memudahkan pembaca melihat hasil setiap metrik. Sementara itu, grafik memudahkan pembaca memahami pola, tren, dan perbandingan hasil secara visual. Oleh karena itu, penggunaan keduanya memberikan informasi yang lebih komprehensif dibandingkan hanya menggunakan salah satunya.
> Pada penelitian ini, visualisasi dirancang agar tidak menyesatkan dengan menggunakan skala sumbu yang sesuai, menampilkan seluruh data hasil eksperimen, serta menyertakan error bar ketika menyajikan nilai rata-rata dari beberapa kali run. Pendekatan ini membantu memastikan bahwa hasil penelitian disajikan secara objektif dan mudah dipahami.