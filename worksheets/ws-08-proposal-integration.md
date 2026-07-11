# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [v] Problem → Gap: masalah terdokumentasi di literatur
  [v] Gap → RQ: RQ dirumuskan untuk menjawab Data Gap dan Method Gap.
  [v] RQ → Hypothesis: hipotesis memprediksi hasil penerapan CNN dan Grad-CAM.
  [v] Hypothesis → Metric: hipotesis diuji menggunakan Accuracy, Precision, Recall, F1-score, dan Confusion Matrix.
  [v] Metric → System: sistem menghasilkan prediksi yang dapat diukur dengan metrik evaluasi dan divisualisasikan menggunakan Grad-CAM.
  [v] System → Experiment: desain eksperimen menggunakan sistem CNN dengan dataset Tomato Diseases.

Koneksi Horizontal (Konsistensi):
  [v] Istilah sama di semua bagian
  [v] Variabel di RQ = variabel di hipotesis = metrik di desain
  [v] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [v] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [v] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [v] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [v] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [v] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |    3  |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |   3   |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |   3   |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |    2  |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| **Komponen**          | **Sumber** | **Isi (1–2 kalimat)**                                                                                                                                                                                                                          |
| --------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem Statement** | WS-02      | Klasifikasi penyakit daun tomat menggunakan CNN telah menunjukkan performa yang baik, namun penelitian sebelumnya masih terbatas pada jumlah kelas penyakit dan belum memberikan penjelasan mengenai dasar pengambilan keputusan model.        |
| **Gap**               | WS-03      | Penelitian sebelumnya umumnya hanya menggunakan empat kelas penyakit dan belum mengintegrasikan Explainable AI melalui Grad-CAM untuk memvisualisasikan area yang menjadi dasar prediksi model.                                                |
| **RQ**                | WS-04      | Bagaimana performa model Convolutional Neural Network (CNN) dalam mengklasifikasikan berbagai jenis penyakit daun tomat menggunakan dataset Tomato Diseases serta bagaimana Grad-CAM memvisualisasikan area yang menjadi dasar prediksi model? |
| **Hipotesis**         | WS-04      | **H₁:** Model CNN mampu mengklasifikasikan berbagai jenis penyakit daun tomat dengan performa yang baik serta Grad-CAM dapat memvisualisasikan area yang menjadi dasar prediksi model.                                                         |
| **Variabel & Metrik** | WS-05      | **IV:** Model CNN. **DV:** Performa klasifikasi yang diukur menggunakan Accuracy, Precision, Recall, F1-score, dan Confusion Matrix. **CV:** Dataset Tomato Diseases.                                                                          |
| **Sistem**            | WS-06      | Sistem terdiri atas preprocessing citra, klasifikasi menggunakan CNN, evaluasi performa model, serta visualisasi hasil prediksi menggunakan Grad-CAM.                                                                                          |
| **Desain Eksperimen** | WS-07      | Penelitian menggunakan eksperimen comparison terhadap penelitian baseline dengan kondisi evaluasi yang setara menggunakan dataset Tomato Diseases, preprocessing yang sama, dan metrik evaluasi yang konsisten.                                |


---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi                 | Status | Bukti                                                                                                                                                                            |
| ----------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Problem → Gap**       | ✅      | Masalah pada penelitian sebelumnya menunjukkan cakupan penyakit masih terbatas dan belum menerapkan Explainable AI, sehingga muncul Data Gap dan Method Gap.                     |
| **Gap → RQ**            | ✅      | RQ secara langsung menanyakan performa CNN pada berbagai jenis penyakit daun tomat serta visualisasi prediksi menggunakan Grad-CAM untuk menjawab kedua gap tersebut.            |
| **RQ → Hypothesis**     | ✅      | Hipotesis memprediksi bahwa CNN mampu mengklasifikasikan berbagai jenis penyakit daun tomat dengan baik serta Grad-CAM dapat memvisualisasikan area yang menjadi dasar prediksi. |
| **Hypothesis → Metric** | ✅      | Hipotesis diuji menggunakan Accuracy, Precision, Recall, F1-score, Confusion Matrix, serta visualisasi Grad-CAM.                                                                 |
| **Metric → System**     | ✅      | Sistem menghasilkan prediksi yang dievaluasi menggunakan metrik klasifikasi dan divisualisasikan menggunakan Grad-CAM.                                                           |
| **System → Experiment** | ✅      | Desain eksperimen menggunakan sistem CNN dengan dataset Tomato Diseases dan parameter yang konsisten selama proses pelatihan dan pengujian.                                      |


**Koneksi mana yang paling lemah?** Hypothesis -> Metric
**Bagaimana cara memperkuatnya?**
> Menambahkan target performa yang lebih spesifik (misalnya target Accuracy atau F1-score) jika hasil eksperimen sudah diperoleh, sehingga hubungan antara hipotesis dan metrik menjadi lebih terukur.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [v] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria        | Skor (1–3) | Justifikasi                                                                                                                                                                    |
| --------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Koherensi**   | **3**      | Alur penelitian konsisten mulai dari problem, research gap, RQ, hipotesis, variabel, sistem, hingga desain eksperimen.                                                         |
| **Specificity** | **3**      | Variabel penelitian, dataset, metode CNN, metrik evaluasi (Accuracy, Precision, Recall, F1-score, Confusion Matrix), dan penggunaan Grad-CAM telah didefinisikan dengan jelas. |
| **Feasibility** | **3**      | Penelitian realistis untuk dilaksanakan menggunakan dataset publik dari Kaggle dan perangkat yang tersedia, dengan ruang lingkup yang sesuai.                                  |
| **Rigor**       | **2**      | Proposal menggunakan baseline yang relevan, namun belum melibatkan lebih dari satu baseline atau metode state-of-the-art sehingga masih dapat diperkuat.                       |


**Skor total:** 11 / 12

**Apakah proposal siap untuk fase eksekusi?** [v] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Merumuskan Research Question (RQ) berdasarkan research gap yang telah diidentifikasi.
**Bagian tersulit:** Mengidentifikasi research gap yang valid dan menyusun desain eksperimen agar konsisten dengan RQ, variabel, serta metode penelitian
**Yang akan dilakukan berbeda:**
> Melakukan studi literatur dan menentukan dataset sejak awal agar penyusunan research gap, RQ, dan metodologi menjadi lebih konsisten serta mengurangi revisi pada tahap selanjutnya.

