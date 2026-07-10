# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

--- 

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Klasifikasi Penyakit Daun Tomat Menggunakan CNN dengan Explainable AI (Grad-CAM)
Database   : Google Scholar, IEEE Xplore, ScienceDirect
Query      : ("Tomato Leaf Disease" OR "Tomato Disease Detection")
AND ("Convolutional Neural Network" OR CNN)
AND ("Grad-CAM" OR "Explainable AI")
Tahun      : 2020–2025
Hasil awal : 50 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|   Saputra et al.    |  2023     |  CNN LeNet-5 Custom      |   2000 citra daun tomat   |  Akurasi 95%      |    Dataset hanya 4 kelas        |
|Wahid et al.|2021|Inception V4|Citra daun tomat|Akurasi 90%|Komputasi lebih tinggi|
|Putri et al.|2021|ANN Backpropagation| Data daun tomat| Akurasi 78%|Ekstraksi fitur manual|
|Rosiani et al.|2020|K-Means Segmentation|Citra daun jagung|Akurasi 90%|Fokus hanya segmentasi|
|Laily|2013|Artificial Neural Network|Daun tembakau| Akurasi 73%| Akurasi masih rendah|

Pola yang ditemukan:
  Metode dominan     : Convolutional Neural Network (CNN)
  Dataset umum       : Dataset citra daun tomat (PlantVillage)
  Limitasi berulang  : Jumlah kelas penyakit masih terbatas dan model belum menyediakan interpretasi hasil prediksi (black box).

GAP IDENTIFICATION

Gap 1: Data Gap
  Deskripsi    : Penelitian sebelumnya hanya mengklasifikasikan empat jenis penyakit daun tomat sehingga belum mencakup variasi penyakit yang lebih luas.
  Bukti        : Saputra et al. (2023) menggunakan empat kelas penyakit yaitu Healthy, Layu Fusarium, Tomato Crinivirus, dan Tomato Yellow Leaf Curl.
  Signifikansi : Memperluas jumlah kelas penyakit akan meningkatkan kemampuan model dalam mengenali variasi penyakit yang lebih beragam sehingga lebih relevan untuk penerapan di dunia nyata.

Gap 2: [Jenis: Method Gap]
  Deskripsi    : Penelitian sebelumnya belum menerapkan Explainable Artificial Intelligence (Grad-CAM) sehingga proses pengambilan keputusan model CNN masih sulit dijelaskan.
  Bukti        : Evaluasi penelitian hanya menggunakan metrik klasifikasi seperti confusion matrix dan akurasi tanpa visualisasi area citra yang menjadi dasar prediksi.
  Signifikansi : Penambahan Grad-CAM dapat meningkatkan transparansi model dengan memperlihatkan area daun yang menjadi dasar pengambilan keputusan sehingga hasil klasifikasi lebih mudah dipahami dan dipercaya.

Baseline Selection:
| Baseline                  | Relevansi     | Representatif                                                                        | Source                            |
| ------------------------- | ------------- | ------------------------------------------------------------------------------------ | --------------------------------- |
| **Saputra et al. (2023)** | Sangat Tinggi | Ya (Baseline utama karena topik, objek, dan metode paling mirip)                     | AVITEC, 2023                      |
| **Wahid et al. (2021)**   | Tinggi        | Ya (Pembanding arsitektur CNN menggunakan Inception V4)                              | KONIK, 2021                       |
| **Putri et al. (2021)**   | Sedang        | Ya (Pembanding metode ANN non-CNN)                                                   | MATHunesa, 2021                   |
| **Rosiani et al. (2020)** | Sedang        | Tidak (Objek berbeda, digunakan sebagai referensi metode segmentasi)                 | Jurnal Informatika Polinema, 2020 |
| **Laily (2013)**          | Rendah        | Tidak (Penelitian lama dan objek berbeda, sebagai referensi perkembangan metode ANN) | Simetris Journal, 2013            |


```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Klasifikasi Penyakit Daun Tomat Menggunakan CNN dengan Explainable AI Berbasis Grad-CAM
**Query pencarian:** ("Tomato Leaf Disease" OR "Tomato Disease Detection") AND ("Convolutional Neural Network" OR CNN)
**Database:** Google Scholar, IEEE Xplore, ScienceDirect

| # | Study          | Tahun | Method                    | Dataset               | Result      | Limitasi                                                   |
| - | -------------- | ----- | ------------------------- | --------------------- | ----------- | ---------------------------------------------------------- |
| 1 | Saputra et al. | 2023  | CNN LeNet-5 Custom        | 2000 citra daun tomat | Akurasi 95% | Dataset hanya 4 kelas, belum menggunakan Explainable AI    |
| 2 | Wahid et al.   | 2021  | CNN Inception V4          | Citra daun tomat      | Akurasi 90% | Komputasi lebih tinggi, belum menggunakan Explainable AI   |
| 3 | Putri et al.   | 2021  | ANN Backpropagation       | Data daun tomat       | Akurasi 78% | Memerlukan ekstraksi fitur manual                          |
| 4 | Rosiani et al. | 2020  | K-Means Segmentation      | Citra daun jagung     | Akurasi 90% | Fokus pada segmentasi, bukan klasifikasi penyakit tomat    |
| 5 | Laily          | 2013  | Artificial Neural Network | Daun tembakau         | Akurasi 73% | Akurasi masih rendah dan memerlukan ekstraksi fitur manual |



**Pola yang terlihat — Metode dominan:** CNN
**Limitasi yang berulang:** Jumlah kelas penyakit masih terbatas, model belum menggunakan Explainable AI sehingga hasil prediksi sulit diinterpretasikan (black box), serta pada metode lama masih memerlukan ekstraksi fitur manual.
---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| **Jenis Gap**       | **Ditemukan?**         | **Gap Statement**                                                                                                                                                                   |
| ------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Performance Gap** | [ ] Ya / **[✓] Tidak** | Sebagian besar penelitian telah mencapai akurasi yang cukup tinggi (90–95%), sehingga peningkatan akurasi bukan menjadi fokus utama penelitian ini.                                 |
| **Method Gap**      | **[✓] Ya** / [ ] Tidak | Penelitian sebelumnya belum menerapkan Explainable AI (Grad-CAM), sehingga model CNN masih bersifat *black box* dan belum mampu menjelaskan area citra yang menjadi dasar prediksi. |
| **Data Gap**        | **[✓] Ya** / [ ] Tidak | Sebagian penelitian hanya menggunakan jumlah kelas penyakit yang terbatas, sehingga kemampuan model dalam mengenali variasi penyakit daun tomat belum optimal.                      |
| **Context Gap**     | [ ] Ya / **[✓] Tidak** | Penelitian ini masih menggunakan dataset publik sehingga belum berfokus pada pengujian pada kondisi lapangan nyata.                                                                 |


**Gap utama yang dipilih:** Method Gap dan Data Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
>Method Gap penting karena hasil klasifikasi CNN masih sulit dipahami oleh pengguna. Dengan menambahkan Grad-CAM, model tidak hanya memberikan prediksi, tetapi juga menunjukkan area daun yang menjadi dasar pengambilan keputusan sehingga hasilnya lebih transparan dan dapat dipercaya.
>Data Gap penting karena penggunaan jumlah kelas penyakit yang lebih banyak memungkinkan model mengenali variasi penyakit daun tomat secara lebih lengkap. Hal ini meningkatkan cakupan klasifikasi dan membuat sistem lebih relevan untuk membantu identifikasi berbagai jenis penyakit daun tomat.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline               | Mengapa Relevan                                                     | Mengapa Representatif                                                     | Apakah SOTA?                                                 | Sumber               |
| - | ---------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------- |
| 1 | **CNN LeNet-5 Custom** | Sama-sama melakukan klasifikasi penyakit daun tomat menggunakan CNN | Menjadi penelitian acuan utama dan memiliki performa tinggi (akurasi 95%) | Tidak, tetapi masih menjadi baseline yang relevan            | Saputra et al., 2023 |
| 2 | **CNN Inception V4**   | Sama-sama menggunakan CNN untuk klasifikasi penyakit daun tomat     | Mewakili arsitektur CNN yang lebih kompleks sebagai pembanding            | Tidak, tetapi merupakan arsitektur CNN yang banyak digunakan | Wahid et al., 2021   |


**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [v] Tidak
> Justifikasi: Kedua baseline dipilih karena memiliki tujuan penelitian yang sama, yaitu klasifikasi penyakit daun tomat menggunakan CNN. Selain itu, kedua penelitian berasal dari literatur yang relevan dan memiliki performa yang baik sehingga layak dijadikan pembanding. Dengan demikian, perbandingan dilakukan terhadap metode yang representatif, bukan metode yang sengaja dipilih karena memiliki performa rendah.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Pernyataan "belum ada yang meneliti" merupakan klaim yang tidak cukup kuat karena belum didukung oleh bukti dari hasil studi literatur. Sebaliknya, research gap harus didasarkan pada analisis beberapa penelitian sebelumnya sehingga dapat menunjukkan keterbatasan yang masih ada, misalnya keterbatasan metode, data, performa, atau konteks penelitian. Untuk membuktikan bahwa suatu gap benar-benar ada, perlu dilakukan telaah literatur secara sistematis dan membandingkan hasil, metode, dataset, serta keterbatasan dari penelitian-penelitian terdahulu.


