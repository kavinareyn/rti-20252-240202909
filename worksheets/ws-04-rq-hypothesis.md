# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Dataset penyakit daun tomat yang digunakan pada penelitian sebelumnya masih terbatas sehingga performa model kurang stabil pada kondisi nyata.

Research Question:
  Tipe         : [ ] Comparison  [v] Improvement  [ ] Exploratory
  Formulasi    : Apakah penggunaan model CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5 standar?
  Variabel IV  : Jenis arsitektur CNN
  Variabel DV  : Akurasi deteksi penyakit daun tomat
  Metrik       : Accuracy, precision, recall
  Dataset      : Dataset citra daun tomat
  Baseline     : LeNet-5 CNN

Quality Check RQ:
  [v] Variabel spesifik
  [v] Metrik jelas
  [v] Baseline ada
  [v] Konteks disebutkan
  [v] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Pengaruh penggunaan CNN Custom terhadap peningkatan akurasi deteksi penyakit daun tomat
  Jenis kontribusi        : [v] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Keterbatasan performa model pada dataset penyakit daun tomat

Hypothesis Pair:
  H₀ : CNN Custom tidak memberikan peningkatan akurasi yang signifikan dibanding LeNet-5 standar
  H₁ : CNN Custom memberikan peningkatan akurasi yang signifikan dibanding LeNet-5 standar
  Threshold              : Akurasi ≥ 95%
  Justifikasi threshold  : Berdasarkan hasil penelitian sebelumnya, akurasi model terbaik berada di sekitar 90–95% sehingga threshold tersebut realistis untuk dijadikan target peningkatan performa.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Dataset penyakit daun tomat masih terbatas sehingga performa model kurang stabil pada kondisi nyata.
**RQ versi pertama (tulis bebas):**
> Bagaimana meningkatkan akurasi deteksi penyakit daun tomat menggunakan CNN?

**Evaluasi RQ:**

| Komponen        | Ada? | Isi                          |
| --------------- | ---- | ---------------------------- |
| Metode spesifik | Ya   | CNN Custom dibanding LeNet-5 |
| Metrik terukur  | Ya   | Accuracy, precision, recall  |
| Baseline        | Ya   | LeNet-5 CNN                  |
| Dataset/konteks | Ya   | Dataset citra daun tomat     |


**Tipe RQ:** [v] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan metode LeNet-5 pada dataset citra daun tomat?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen              | Isi                                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| H₀                    | Tidak ada peningkatan akurasi yang signifikan antara CNN Custom dan LeNet-5 pada deteksi penyakit daun tomat                                      |
| H₁                    | CNN Custom memberikan peningkatan akurasi yang signifikan dibanding LeNet-5 pada deteksi penyakit daun tomat                                      |
| Metrik                | Accuracy, precision, recall                                                                                                                       |
| Threshold             | Akurasi ≥ 95%                                                                                                                                     |
| Justifikasi threshold | Berdasarkan penelitian sebelumnya, model terbaik mencapai akurasi sekitar 90–95% sehingga threshold tersebut realistis sebagai target peningkatan |


**Apakah hipotesis ini falsifiable?** [v] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan melakukan eksperimen dan membandingkan hasil kedua model. Jika CNN Custom tidak menghasilkan akurasi yang lebih baik atau tidak mencapai threshold yang ditentukan, maka hipotesis H₁ ditolak.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap           | Isi                                                                                                       |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| RQ              | Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5? |
| Variable (IV)   | Jenis arsitektur CNN (CNN Custom dan LeNet-5)                                                             |
| Variable (DV)   | Akurasi deteksi penyakit daun tomat                                                                       |
| Metric          | Accuracy, precision, recall                                                                               |
| Data source     | Dataset citra daun tomat                                                                                  |
| Analysis method | Perbandingan hasil confusion matrix dan evaluasi performa model CNN                                       |


**Apakah rantai lengkap?** [v] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Deteksi Penyakit Tomat Melalui Citra Daun menggunakan Metode Convolutional Neural Network
**RQ yang diekstrak:** Apakah metode CNN dapat meningkatkan akurasi deteksi penyakit daun tomat berdasarkan citra digital?
**Komponen yang hilang:** Baseline pembanding dan konteks dataset belum dijelaskan secara spesifik pada RQ.
