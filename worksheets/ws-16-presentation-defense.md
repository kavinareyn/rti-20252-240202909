# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 12 (10 konten + title + closing)
Time per slide : ±2 menit
Total time     : ±20 menit

Slide Outline:
| #  | Pesan Utama                                            | Visual                                      | Waktu     |
| -- | ------------------------------------------------------ | ------------------------------------------- | --------- |
| 1  | Judul Penelitian & Identitas                           | Cover                                       | 30 detik  |
| 2  | Latar Belakang Permasalahan                            | Ilustrasi penyakit daun tomat               | 2 menit   |
| 3  | Research Gap, Research Question, dan Tujuan Penelitian | Diagram Research Gap                        | 2 menit   |
| 4  | Dataset & Preprocessing                                | Diagram alur preprocessing                  | 2 menit   |
| 5  | Arsitektur CNN                                         | Diagram arsitektur CNN                      | 2 menit   |
| 6  | Proses Training & Parameter                            | Flowchart training                          | 2 menit   |
| 7  | Hasil Evaluasi Model                                   | Tabel Accuracy, Precision, Recall, F1-Score | 2 menit   |
| 8  | Confusion Matrix & Repeatability                       | Confusion Matrix dan tabel 4 run            | 2 menit   |
| 9  | Visualisasi Grad-CAM                                   | Contoh Original, Heatmap, Overlay           | 2 menit   |
| 10 | Pembahasan & Keterbatasan                              | Ringkasan poin utama                        | 2 menit   |
| 11 | Kesimpulan & Future Work                               | Poin-poin kesimpulan                        | 1,5 menit |
| 12 | Terima Kasih & Sesi Tanya Jawab                        | Closing                                     | 30 detik  |


Anticipatory Defense Matrix:
| Kategori           | Pertanyaan Potensial                                       | Jawaban (CER)                                                                                                                                                                                                                                                                                                                              |
| ------------------ | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Problem**        | Mengapa memilih klasifikasi penyakit daun tomat?           | **Claim:** Deteksi dini penyakit daun tomat penting untuk meningkatkan produktivitas pertanian. **Evidence:** Identifikasi manual memerlukan waktu dan bergantung pada keahlian petani. **Reasoning:** CNN dapat membantu proses identifikasi secara otomatis dan lebih cepat.                                                             |
| **Gap**            | Apa perbedaan penelitian ini dengan penelitian sebelumnya? | **Claim:** Penelitian ini tidak hanya melakukan klasifikasi menggunakan CNN tetapi juga menerapkan Grad-CAM. **Evidence:** Grad-CAM menghasilkan visualisasi area citra yang menjadi perhatian model. **Reasoning:** Hal ini meningkatkan interpretabilitas hasil prediksi.                                                                |
| **Method**         | Mengapa menggunakan CNN?                                   | **Claim:** CNN efektif untuk klasifikasi citra. **Evidence:** CNN mampu mengekstraksi fitur spasial secara otomatis tanpa rekayasa fitur manual. **Reasoning:** Karakteristik ini sesuai dengan klasifikasi penyakit daun tomat berdasarkan citra.                                                                                         |
| **Method**         | Mengapa hanya menggunakan CNN sederhana?                   | **Claim:** CNN dipilih karena sesuai dengan tujuan penelitian dan mudah diimplementasikan. **Evidence:** Model memperoleh rata-rata accuracy sekitar 91,65%. **Reasoning:** Performa tersebut menunjukkan model sudah mampu mengklasifikasikan penyakit daun tomat dengan baik.                                                            |
| **Results**        | Mengapa accuracy tiap run berbeda?                         | **Claim:** Variasi kecil antar-run merupakan hal yang wajar. **Evidence:** Accuracy berada pada rentang 91,01%–92,95% dengan konfigurasi yang sama. **Reasoning:** Perbedaan berasal dari proses pelatihan yang bersifat stokastik dan kondisi komputasi.                                                                                  |
| **Results**        | Mengapa melakukan empat kali run?                          | **Claim:** Untuk menguji repeatability model. **Evidence:** Empat eksperimen menghasilkan metrik yang konsisten. **Reasoning:** Hal ini meningkatkan kepercayaan terhadap hasil penelitian.                                                                                                                                                |
| **Generalization** | Apakah model dapat digunakan pada foto dari kamera HP?     | **Claim:** Model berpotensi digunakan. **Evidence:** Model telah berhasil mengklasifikasikan citra pada dataset dengan akurasi tinggi. **Reasoning:** Namun, diperlukan pengujian lebih lanjut menggunakan citra lapangan karena kondisi pencahayaan, sudut pengambilan gambar, dan kualitas kamera dapat berbeda dari dataset penelitian. |

Latihan:
  Latihan 1 : ____________
Catatan :
- Durasi presentasi
- Bagian yang masih terlalu panjang
- Pertanyaan yang belum bisa dijawab

Latihan 2 : ____________
Catatan :
- Perbaikan alur presentasi
- Memperjelas hasil eksperimen
- Memperjelas kontribusi Grad-CAM

Latihan 3 : ____________
Catatan :
- Simulasi presentasi penuh
- Target durasi 20 menit
- Persiapan sesi tanya jawab
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama                                                           | Visual yang Digunakan                                                  |   Waktu   |
| - | --------------------------------------------------------------------- | ---------------------------------------------------------------------- | :-------: |
| 1 | **Judul penelitian, identitas, dan tujuan penelitian**                | Cover + ilustrasi daun tomat                                           |  1 menit  |
| 2 | **Latar belakang masalah dan pentingnya deteksi penyakit daun tomat** | Gambar daun tomat sehat dan berpenyakit + diagram masalah              |  2 menit  |
| 3 | **Research Gap, Research Question, dan tujuan penelitian**            | Tabel penelitian terdahulu dan research gap                            | 1,5 menit |
| 4 | **Dataset dan preprocessing**                                         | Diagram alur preprocessing (dataset → resize → rescaling → train/test) |  2 menit  |
| 5 | **Arsitektur CNN dan proses training**                                | Diagram arsitektur CNN + flowchart training                            |  2 menit  |
| 6 | **Hasil evaluasi model**                                              | Tabel Accuracy, Precision, Recall, F1-Score dan grafik Accuracy/Loss   |  2 menit  |
| 7 | **Confusion Matrix dan hasil repeatability (4 run)**                  | Confusion Matrix + tabel hasil 4 run                                   |  2 menit  |
| 8 | **Visualisasi Grad-CAM dan interpretasi hasil**                       | Original Image, Heatmap, Overlay                                       | 1,5 menit |
| 9 | **Kesimpulan, kontribusi penelitian, keterbatasan, dan saran**        | Poin-poin kesimpulan                                                   |  1 menit  |


**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| #     | Kategori           | Pertanyaan                                                                                | Claim                                                                                                 | Evidence                                                                                                                                                                                          | Reasoning                                                                                                                                                                                         |
| ----- | ------------------ | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | **Problem**        | Mengapa memilih klasifikasi penyakit daun tomat?                                          | Deteksi dini penyakit daun tomat penting untuk membantu meningkatkan produktivitas pertanian.         | Identifikasi secara manual memerlukan waktu, bergantung pada keahlian petani, dan berpotensi menimbulkan kesalahan.                                                                               | Dengan memanfaatkan CNN, proses identifikasi dapat dilakukan secara otomatis, lebih cepat, dan lebih konsisten.                                                                                   |
| **2** | **Method**         | Mengapa menggunakan CNN, bukan EfficientNet atau ResNet?                                  | CNN dipilih karena sesuai dengan tujuan penelitian dan mampu mempelajari fitur citra secara otomatis. | Model CNN yang dibangun memperoleh rata-rata accuracy **91,65%** pada empat kali eksperimen menggunakan Tomato Leaf Disease Dataset.                                                              | Hasil tersebut menunjukkan bahwa arsitektur CNN sederhana sudah mampu memberikan performa yang baik, sehingga sesuai dengan ruang lingkup penelitian.                                             |
| **3** | **Method**         | Mengapa menggunakan Grad-CAM?                                                             | Grad-CAM digunakan untuk meningkatkan interpretabilitas model.                                        | Grad-CAM menghasilkan visualisasi berupa heatmap yang menunjukkan area daun yang menjadi perhatian model saat melakukan prediksi.                                                                 | Dengan demikian, pengguna tidak hanya mengetahui hasil klasifikasi, tetapi juga memahami alasan model menghasilkan prediksi tersebut sehingga meningkatkan kepercayaan terhadap sistem.           |
| **4** | **Results**        | Mengapa melakukan empat kali run?                                                         | Empat kali eksperimen dilakukan untuk menguji konsistensi (repeatability) model.                      | Hasil empat run menghasilkan accuracy yang relatif konsisten, yaitu sekitar **91–93%** dengan rata-rata **91,65%**.                                                                               | Pengulangan eksperimen menunjukkan bahwa performa model stabil dan tidak bergantung pada satu kali proses training saja.                                                                          |
| **5** | **Generalization** | Apakah model dapat digunakan pada foto daun tomat yang diambil menggunakan kamera ponsel? | Model memiliki potensi untuk digunakan pada citra dari kamera ponsel.                                 | Model telah berhasil mengklasifikasikan citra pada Tomato Leaf Disease Dataset dengan accuracy rata-rata **91,65%**, serta dapat melakukan prediksi terhadap citra baru melalui fitur prediction. | Namun, diperlukan pengujian lebih lanjut menggunakan citra lapangan dengan variasi pencahayaan, sudut pengambilan gambar, dan kualitas kamera agar kemampuan generalisasi model dapat dipastikan. |


---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| #     | Pertanyaan                                                                                | Jawaban Saya                                                                                                                                                                                                                                                                                                                                             | Evaluasi                       |
| ----- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **1** | Mengapa memilih metode CNN dan tidak menggunakan EfficientNet atau ResNet?                | Penelitian ini bertujuan mengevaluasi kemampuan CNN dalam mengklasifikasikan penyakit daun tomat. CNN dipilih karena mampu mengekstraksi fitur citra secara otomatis dan memberikan rata-rata accuracy sebesar **91,65%** pada empat kali eksperimen. Penggunaan arsitektur yang lebih kompleks menjadi peluang penelitian selanjutnya.                  | ☑ Direct ☑ Data-based ☑ Honest |
| **2** | Mengapa menggunakan Grad-CAM? Apa manfaatnya?                                             | Grad-CAM digunakan untuk memvisualisasikan area citra yang menjadi perhatian model saat melakukan prediksi. Dengan demikian, hasil klasifikasi tidak hanya berupa label penyakit, tetapi juga disertai penjelasan visual sehingga meningkatkan interpretabilitas model.                                                                                  | ☑ Direct ☑ Data-based ☑ Honest |
| **3** | Apakah model dapat digunakan pada foto daun tomat yang diambil menggunakan kamera ponsel? | Model berpotensi digunakan karena mampu melakukan prediksi terhadap citra baru. Namun, penelitian ini hanya menggunakan Tomato Leaf Disease Dataset sehingga diperlukan pengujian lebih lanjut pada citra lapangan dengan variasi pencahayaan, sudut pengambilan gambar, dan kualitas kamera yang berbeda. Hal tersebut menjadi keterbatasan penelitian. | ☑ Direct ☑ Data-based ☑ Honest |


**Pertanyaan yang paling sulit dijawab:**
> Bagaimana performa model jika diterapkan pada kondisi nyata menggunakan foto dari kamera ponsel?

**Apa yang perlu disiapkan lebih baik:**
> Melakukan pengujian tambahan menggunakan citra daun tomat yang diambil langsung di lapangan agar kemampuan generalisasi model dapat dibuktikan secara lebih kuat.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Bagian yang paling mengubah cara berpikir saya adalah penyusunan research question dan perancangan eksperimen. Saya menyadari bahwa penelitian bukan hanya tentang membangun model yang menghasilkan akurasi tinggi, tetapi juga tentang memastikan setiap langkah penelitian dirancang secara sistematis, terdokumentasi, dapat direplikasi, dan mampu menjawab research question yang telah ditetapkan.

**Yang akan selalu diterapkan:**
> Pada penelitian berikutnya, saya akan selalu memulai dengan menyusun research question yang jelas, merancang eksperimen yang terstruktur, melakukan beberapa kali pengujian untuk memastikan konsistensi hasil, serta mendokumentasikan seluruh proses mulai dari preprocessing hingga evaluasi agar penelitian mudah direplikasi dan hasilnya dapat dipertanggungjawabkan secara ilmiah.
