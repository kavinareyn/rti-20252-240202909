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
  Input       : Citra daun tomat
  Process     : Pengolahan citra dan klasifikasi menggunakan CNN
  Output      : Jenis penyakit daun tomat
  Outcome     : Membantu identifikasi penyakit lebih cepat dan akurat
  Constraints : Dataset terbatas, variasi pencahayaan dan kualitas citra
  Stakeholders: Petani, peneliti, pengembang sistem pertanian

Fenomena → Problem
  Fenomena yang diamati             : Petani kesulitan membedakan penyakit daun tomat karena gejalanya mirip
  Gejala (symptom) yang terukur     : Tingginya kesalahan identifikasi penyakit secara manual
  Masalah yang didiagnosis          : Proses identifikasi penyakit masih lambat dan kurang akurat
  Masalah riset (researchable)      : Bagaimana meningkatkan akurasi deteksi penyakit daun tomat menggunakan CNN?
  Variabel yang terukur             : Akurasi, precision, recall, waktu proses

Problem Quality Check
  [v] Clarity — Apakah satu orang membaca akan paham?
  [v] Measurability — Apakah ada metrik kuantitatif?
  [v] Relevance — Apakah penting untuk domain?
  [v] Testability — Apakah bisa gagal?
  [v] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
Identifikasi penyakit daun tomat secara manual masih sulit dilakukan karena beberapa penyakit memiliki gejala yang mirip, sehingga dapat menyebabkan kesalahan diagnosis dan menurunkan kualitas hasil panen. Penelitian ini bertujuan mengembangkan metode Convolutional Neural Network (CNN) untuk mendeteksi jenis penyakit daun tomat berdasarkan citra digital dengan tingkat akurasi yang lebih tinggi dan proses identifikasi yang lebih cepat dibandingkan metode manual.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** ________________________________________

| Tahap | Hasil |
|-------|-------|
| Reality | Petani sering kesulitan mengenali penyakit pada daun tanaman secara cepat dan tepat|
| Observed Issue (Symptom) | Tingginya kesalahan identifikasi penyakit daun secara manual |
| Diagnosed Problem (Root Cause) |Gejala penyakit memiliki kemiripan dan identifikasi masih bergantung pada pengamatan manusia |
| Researchable Problem |Bagaimana meningkatkan akurasi deteksi penyakit daun tanaman menggunakan metode CNN? |
| Measurable Variable |Akurasi, precision, recall, dan waktu deteksi|

**Apakah terjebak solution-first thinking?** [ ] Ya / [v] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|st 
| Input | Citra daun tanaman tomat |
| Process | Pengolahan citra dan klasifikasi penyakit menggunakan CNN|
| Output |Hasil deteksi jenis penyakit daun tomat |
| Outcome |Membantu petani melakukan identifikasi penyakit lebih cepat dan akurat |
| Constraints |Dataset terbatas, kualitas citra berbeda-beda, dan kebutuhan komputasi |
| Stakeholders |Petani, peneliti, dan pengembang sistem AI pertanian |

**Komponen mana yang paling relevan dengan masalah riset?** Process (proses klasifikasi menggunakan CNN)

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 4 | Masalah sudah jelas, tetapi spesifikasi dataset dan jenis penyakit masih bisa diperjelas|
| Measurability |5 | Menggunakan metrik terukur seperti akurasi, precision, dan recall|
| Relevance |5 |Topik penting dalam bidang pertanian dan AI |
| Testability |4 | Model dapat diuji, tetapi hasil bisa dipengaruhi keterbatasan dataset|
| Impact |5 |Berpotensi membantu identifikasi penyakit tanaman lebih cepat dan efisien |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Identifikasi penyakit daun tomat secara manual masih sulit dilakukan karena beberapa penyakit memiliki gejala yang mirip sehingga sering menyebabkan kesalahan diagnosis. Penelitian ini bertujuan mengembangkan metode Convolutional Neural Network (CNN) untuk mendeteksi penyakit daun tomat berdasarkan citra digital dengan tingkat akurasi yang tinggi agar proses identifikasi penyakit menjadi lebih cepat, tepat, dan membantu petani dalam menjaga kualitas hasil panen.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah dalam coding seperti bug atau error biasanya lebih mudah dikenali karena terlihat langsung dari program yang tidak berjalan sesuai harapan. Penyebabnya cenderung jelas dan solusi dapat dicari dengan memperbaiki bagian kode, logika program, atau konfigurasi yang bermasalah. Fokus utamanya adalah membuat sistem kembali berjalan dengan benar.

Sedangkan masalah riset memiliki sifat yang lebih kompleks karena penyebab utamanya belum tentu diketahui dan belum memiliki solusi pasti. Dalam riset, masalah harus dipahami terlebih dahulu melalui pengamatan, pengumpulan data, dan analisis sebelum menentukan solusi yang tepat. Oleh karena itu, coding lebih berfokus pada memperbaiki kesalahan yang sudah diketahui, sedangkan riset berfokus pada menemukan pemahaman dan solusi baru berdasarkan proses ilmiah.
