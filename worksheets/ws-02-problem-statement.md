# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---
 
## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Pertanian / Artificial Intelligence
  Konteks  : Deteksi penyakit daun tomat menggunakan CNN

System Context
  Input       : Citra digital daun tomat dari dataset PlantVillage.
  Process     : Preprocessing citra, pelatihan model CNN, klasifikasi penyakit daun tomat, evaluasi model, dan visualisasi hasil menggunakan Grad-CAM.
  Output      : Prediksi jenis penyakit daun tomat, nilai evaluasi model (Accuracy, Precision, Recall, F1-score, Confusion Matrix), serta visualisasi heatmap Grad-CAM.
  Outcome     : Sistem mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat dan memberikan interpretasi visual terhadap hasil prediksi model.
  Constraints : Dataset terbatas pada citra daun tomat, implementasi menggunakan satu arsitektur CNN, dan evaluasi dilakukan pada dataset PlantVillage.
  Stakeholders: Petani, penyuluh pertanian, peneliti, dan akademisi.

Fenomena → Problem
  Fenomena yang diamati             : Model CNN telah mampu mengklasifikasikan penyakit daun tomat, namun penelitian sebelumnya hanya mencakup empat jenis penyakit dan belum memberikan penjelasan terhadap proses pengambilan keputusan model.
  Gejala (symptom) yang terukur     : Jumlah kelas penyakit terbatas, hasil klasifikasi hanya berupa label, dan tidak tersedia visualisasi area citra yang menjadi dasar prediksi.
  Masalah yang didiagnosis          : Kemampuan klasifikasi penyakit daun tomat masih terbatas dan model bersifat black box sehingga hasil prediksi sulit diinterpretasikan.
  Masalah riset (researchable)      : Bagaimana mengembangkan model CNN yang mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat serta memberikan interpretasi visual terhadap hasil prediksi menggunakan Grad-CAM?
  Variabel yang terukur             : 
  - Variabel bebas: Arsitektur CNN, jumlah kelas penyakit, penerapan Grad-CAM.
  - Variabel terikat: Accuracy, Precision, Recall, F1-score, Confusion Matrix, dan visualisasi Grad-CAM.

Problem Quality Check
  [v] Clarity — Apakah satu orang membaca akan paham?
  [v] Measurability — Apakah ada metrik kuantitatif?
  [v] Relevance — Apakah penting untuk domain?
  [v] Testability — Apakah bisa gagal?
  [v] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
Penelitian sebelumnya telah menerapkan Convolutional Neural Network (CNN) untuk mengklasifikasikan penyakit daun tomat dengan tingkat akurasi yang baik, namun cakupan klasifikasi masih terbatas pada empat jenis penyakit dan hasil prediksi yang diberikan belum dapat dijelaskan karena model masih bersifat black box. Keterbatasan tersebut menyebabkan sistem belum mampu mengenali variasi penyakit daun tomat yang lebih luas serta belum memberikan informasi mengenai area citra yang menjadi dasar pengambilan keputusan model. Oleh karena itu, diperlukan pengembangan model CNN yang mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat dengan menambahkan metode Explainable Artificial Intelligence berbasis Grad-CAM sehingga hasil klasifikasi tidak hanya memiliki performa yang baik, tetapi juga dapat diinterpretasikan melalui visualisasi area citra yang berkontribusi terhadap prediksi model.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Klasifikasi Penyakit Daun Tomat Menggunakan Convolutional Neural Network (CNN) dengan Explainable AI Berbasis Grad-CAM

| Tahap | Hasil |
|-------|-------|
| Reality | Identifikasi penyakit daun tomat menggunakan CNN telah banyak dilakukan, namun sebagian besar penelitian hanya mengenali beberapa jenis penyakit dan hanya menghasilkan prediksi tanpa penjelasan.|
| Observed Issue (Symptom) | Model hanya mengklasifikasikan 4 jenis penyakit dan hasil prediksi tidak menunjukkan area daun yang menjadi dasar pengambilan keputusan. |
| Diagnosed Problem (Root Cause) |Cakupan dataset penyakit yang digunakan masih terbatas dan belum diterapkannya metode Explainable AI sehingga model bersifat black box. |
| Researchable Problem |Bagaimana mengembangkan model CNN yang mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat serta memberikan interpretasi visual terhadap hasil prediksi menggunakan Grad-CAM? |
| Measurable Variable |Accuracy, Precision, Recall, F1-score, Confusion Matrix, jumlah kelas penyakit yang diklasifikasikan, dan visualisasi Grad-CAM.|

**Apakah terjebak solution-first thinking?** [ ] Ya / [v] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|st 
| Input | Citra digital daun tomat dari dataset PlantVillage yang terdiri atas beberapa kelas penyakit dan daun sehat. |
| Process | Melakukan preprocessing citra, pelatihan model CNN, klasifikasi penyakit daun tomat, evaluasi model, dan visualisasi hasil prediksi menggunakan Grad-CAM. |
|Output| Prediksi jenis penyakit daun tomat, nilai Accuracy, Precision, Recall, F1-score, Confusion Matrix, serta heatmap Grad-CAM. |
| Outcome |Sistem mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat dan memberikan interpretasi visual terhadap hasil prediksi sehingga meningkatkan transparansi model. |
| Constraints |Dataset terbatas pada citra daun tomat, implementasi menggunakan satu arsitektur CNN, spesifikasi perangkat keras terbatas, dan evaluasi dilakukan menggunakan dataset PlantVillage. |
| Stakeholders |Petani, penyuluh pertanian, peneliti, akademisi, dan pengembang sistem pertanian cerdas. |

**Komponen mana yang paling relevan dengan masalah riset?** Process, karena fokus penelitian adalah mengembangkan proses klasifikasi menggunakan CNN serta menambahkan Grad-CAM untuk meningkatkan interpretabilitas hasil prediksi.

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| **Kriteria**      | **Skor (1–5)** | **Justifikasi**                                                                                                                                                    |
| ----------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Clarity**       | **5**          | Permasalahan telah dijelaskan secara spesifik, yaitu keterbatasan jumlah kelas penyakit dan belum adanya interpretasi hasil klasifikasi.                           |
| **Measurability** | **5**          | Keberhasilan penelitian dapat diukur menggunakan Accuracy, Precision, Recall, F1-score, Confusion Matrix, serta visualisasi Grad-CAM.                              |
| **Relevance**     | **5**          | Penelitian relevan dengan bidang Artificial Intelligence, Computer Vision, dan pertanian karena mendukung identifikasi penyakit daun tomat.                        |
| **Testability**   | **5**          | Hipotesis dapat diuji melalui implementasi CNN, pengujian pada dataset PlantVillage, dan evaluasi menggunakan metrik klasifikasi serta hasil visualisasi Grad-CAM. |
| **Impact**        | **5**          | Penelitian memberikan kontribusi dengan memperluas cakupan klasifikasi penyakit dan meningkatkan interpretabilitas model melalui Explainable AI.                   |


**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
> Penelitian sebelumnya telah menerapkan Convolutional Neural Network (CNN) untuk mengklasifikasikan penyakit daun tomat dengan hasil yang baik, namun masih memiliki keterbatasan karena hanya mampu mengenali empat jenis penyakit dan belum menyediakan penjelasan mengenai proses pengambilan keputusan model. Keterbatasan tersebut menyebabkan cakupan klasifikasi penyakit belum optimal dan hasil prediksi masih bersifat black box, sehingga sulit dipahami serta diverifikasi oleh pengguna. Oleh karena itu, penelitian ini bertujuan mengembangkan model CNN yang mampu mengklasifikasikan lebih banyak jenis penyakit daun tomat dengan memanfaatkan dataset multikelas serta menerapkan Explainable Artificial Intelligence berbasis Grad-CAM untuk memvisualisasikan area citra yang menjadi dasar prediksi model. Pendekatan ini diharapkan dapat meningkatkan kemampuan klasifikasi sekaligus menghasilkan model yang lebih transparan dan mudah diinterpretasikan.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding biasanya berupa bug atau error yang membuat program tidak berjalan dengan benar. Penyelesaiannya dilakukan dengan mencari penyebab error lalu memperbaiki kode. Sementara itu, masalah riset adalah pertanyaan atau permasalahan yang belum memiliki solusi pasti. Penyelesaiannya dilakukan melalui studi literatur, eksperimen, dan analisis untuk menghasilkan pengetahuan atau metode baru. Jadi, masalah coding berfokus pada memperbaiki program, sedangkan masalah riset berfokus pada mencari dan mengembangkan solusi baru.
