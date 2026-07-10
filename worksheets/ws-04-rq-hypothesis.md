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

Gap Statement  : Penelitian sebelumnya hanya mengklasifikasikan empat jenis penyakit daun tomat dan belum menerapkan Explainable AI sehingga hasil prediksi model CNN masih sulit diinterpretasikan.

Research Question:
  Tipe         : [ ] Comparison  [v] Improvement  [ ] Exploratory
  Formulasi    : Bagaimana penerapan Convolutional Neural Network (CNN) dengan Grad-CAM dapat meningkatkan kemampuan klasifikasi multikelas penyakit daun tomat sekaligus memberikan interpretasi visual terhadap hasil prediksi?
  Variabel IV  : Jenis arsitektur CNN, Penerapan Grad-CAM, Jumlah kelas penyakit
  Variabel DV  : Accuracy, Precision, Recall, F1-score, Confusion Matrix, dan interpretasi visual hasil prediksi (Grad-CAM).
  Metrik       : Accuracy, Precision, Recall, F1-score, Confusion Matrix, dan visualisasi Grad-CAM.
  Dataset      : PlantVillage Tomato Leaf Disease Dataset.
  Baseline     : LeNet-5 CNN Custom, Inception V4

Quality Check RQ:
  [v] Variabel spesifik
  [v] Metrik jelas
  [v] Baseline ada
  [v] Konteks disebutkan
  [v] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Model CNN yang dikembangkan mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat serta memberikan interpretasi visual terhadap hasil prediksi menggunakan Grad-CAM.
  Jenis kontribusi        : [v] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          :Method Gap dan Data Gap.

Hypothesis Pair:
  H₀ : Penerapan Grad-CAM dan penambahan jumlah kelas penyakit tidak memberikan peningkatan kemampuan klasifikasi maupun interpretasi hasil prediksi dibandingkan penelitian sebelumnya.
  H₁ : Penerapan Grad-CAM dan penambahan jumlah kelas penyakit mampu menghasilkan model CNN yang dapat mengklasifikasikan lebih banyak jenis penyakit daun tomat serta memberikan interpretasi visual terhadap hasil prediksi.
  Threshold              : Akurasi ≥ 95%
  Justifikasi threshold  : Nilai 95% dipilih karena merupakan akurasi terbaik yang dicapai oleh penelitian acuan menggunakan CNN LeNet-5 Custom (Saputra et al., 2023). Threshold ini digunakan sebagai acuan untuk mengevaluasi apakah model yang dikembangkan mampu mempertahankan performa klasifikasi sambil memberikan kontribusi tambahan berupa interpretasi visual melalui Grad-CAM.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Penelitian sebelumnya hanya mengklasifikasikan empat jenis penyakit daun tomat dan belum menerapkan Explainable AI (Grad-CAM), sehingga hasil prediksi model masih sulit diinterpretasikan.
**RQ versi pertama (tulis bebas):**
> Bagaimana penerapan Convolutional Neural Network (CNN) dengan Grad-CAM dapat mengklasifikasikan lebih banyak jenis penyakit daun tomat serta memberikan interpretasi visual terhadap hasil prediksi?

**Evaluasi RQ:**

| Komponen        | Ada?   | Isi                                                                             |
| --------------- | ------ | ------------------------------------------------------------------------------- |
| Metode spesifik | **Ya** | CNN dengan Grad-CAM                                                             |
| Metrik terukur  | **Ya** | Accuracy, Precision, Recall, F1-score, Confusion Matrix                         |
| Baseline        | **Ya** | CNN LeNet-5 Custom (Saputra et al., 2023) dan Inception V4 (Wahid et al., 2021) |
| Dataset/konteks | **Ya** | Dataset PlantVillage (penyakit daun tomat)                                      |



**Tipe RQ:** [ ] Comparison / [v] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Bagaimana performa model Convolutional Neural Network (CNN) yang dipadukan dengan Grad-CAM dalam mengklasifikasikan berbagai jenis penyakit daun tomat pada dataset PlantVillage berdasarkan metrik Accuracy, Precision, Recall, F1-score, dan Confusion Matrix dibandingkan dengan penelitian sebelumnya?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| **Komponen**              | **Isi**                                                                                                                                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **H₀**                    | Model CNN dengan Grad-CAM **tidak mampu** mencapai performa klasifikasi yang setara atau lebih baik dibandingkan baseline pada klasifikasi multikelas penyakit daun tomat.                                                 |
| **H₁**                    | Model CNN dengan Grad-CAM **mampu** mencapai performa klasifikasi yang setara atau lebih baik dibandingkan baseline pada klasifikasi multikelas penyakit daun tomat serta memberikan interpretasi visual melalui Grad-CAM. |
| **Metrik**                | Accuracy, Precision, Recall, F1-score, dan Confusion Matrix.                                                                                                                                                               |
| **Threshold**             | Accuracy ≥ **95%**.                                                                                                                                                                                                        |
| **Justifikasi threshold** | Nilai 95% digunakan sebagai acuan karena merupakan akurasi terbaik yang dicapai oleh penelitian baseline (Saputra et al., 2023).                                                                                           |



**Apakah hipotesis ini falsifiable?** [v] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Hipotesis ditolak apabila model CNN yang dikembangkan menghasilkan akurasi kurang dari 95% atau performanya lebih rendah dibandingkan baseline berdasarkan metrik Accuracy, Precision, Recall, dan F1-score.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| **Tahap**           | **Isi**                                                                                                                                                                                                                                                                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RQ**              | Bagaimana performa model Convolutional Neural Network (CNN) dalam mengklasifikasikan berbagai jenis penyakit daun tomat pada dataset PlantVillage berdasarkan metrik Accuracy, Precision, Recall, F1-score, dan Confusion Matrix, serta bagaimana Grad-CAM dapat memvisualisasikan area yang menjadi dasar prediksi model? |
| **Variable (IV)**   | Arsitektur CNN dan jumlah kelas penyakit daun tomat.                                                                                                                                                                                                                                                                       |
| **Variable (DV)**   | Performa klasifikasi model yang diukur menggunakan Accuracy, Precision, Recall, F1-score, dan Confusion Matrix.                                                                                                                                                                                                            |
| **Metric**          | Accuracy, Precision, Recall, F1-score, dan Confusion Matrix.                                                                                                                                                                                                                                                               |
| **Data source**     | PlantVillage Tomato Leaf Disease Dataset.                                                                                                                                                                                                                                                                                  |
| **Analysis method** | Melatih model CNN menggunakan dataset PlantVillage, mengevaluasi performa model menggunakan Accuracy, Precision, Recall, F1-score, dan Confusion Matrix, kemudian menerapkan Grad-CAM untuk memvisualisasikan area citra yang menjadi dasar prediksi serta membandingkan hasilnya dengan penelitian baseline.              |

  


**Apakah rantai lengkap?** [v] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Deteksi Penyakit Tomat Melalui Citra Daun menggunakan Metode Convolutional Neural Network
**RQ yang diekstrak:** Bagaimana penerapan Convolutional Neural Network (CNN) dapat mengklasifikasikan penyakit daun tomat berdasarkan citra digital?
**Komponen yang hilang:** Metrik evaluasi, baseline pembanding, dan konteks dataset tidak disebutkan secara eksplisit pada rumusan RQ.
