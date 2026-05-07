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

Topik      : Deteksi penyakit daun tomat menggunakan CNN
Database   : Google Scholar
Query      : “tomato leaf disease detection CNN”
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
  Dataset umum       : Citra digital daun tanaman
  Limitasi berulang  : Dataset terbatas dan risiko overfitting

GAP IDENTIFICATION

Gap 1: [Jenis: performance]
  Deskripsi    : Akurasi model masih belum stabil pada kondisi data nyata yang beragam
  Bukti        : Sebagian besar penelitian hanya menggunakan dataset terbatas dan kondisi citra terkontrol
  Signifikansi : Model perlu lebih robust agar dapat digunakan langsung oleh petani di lapangan

Gap 2: [Jenis: Data]
  Deskripsi    : Jumlah kelas penyakit yang digunakan masih sedikit
  Bukti        : Banyak penelitian hanya memakai 3–4 jenis penyakit daun
  Signifikansi : Penambahan variasi penyakit dapat meningkatkan kemampuan generalisasi model

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| LeNet-5 CNN         | Tinggi    | Ya            | Saputra et al., 2023 |
| Inception V4        | Tinggi    | Ya            | Wahid et al., 2021   |
| ANN Backpropagation | Sedang    | Cukup         | Putri et al., 2021   |

```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Deteksi penyakit daun tomat menggunakan CNN
**Query pencarian:** ("tomato leaf disease" OR "leaf disease detection") AND ("CNN" OR "deep learning") NOT ("medical")
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Saputra et al. | 2023  | CNN LeNet-5 Custom        | 2000 citra daun tomat | Acc 95% | Dataset hanya 4 kelas  |
| 2 | Wahid et al.   | 2021  | Inception V4              | Citra daun tomat      | Acc 90% | Komputasi tinggi       |
| 3 | Putri et al.   | 2021  | ANN Backpropagation       | Data daun tomat       | Acc 78% | Ekstraksi fitur manual |
| 4 | Rosiani et al. | 2020  | K-Means + CNN             | Citra daun jagung     | Acc 90% | Fokus segmentasi       |
| 5 | Laily          | 2013  | Artificial Neural Network | Daun tembakau         | Acc 73% | Akurasi rendah         |


**Pola yang terlihat — Metode dominan:** CNN
**Limitasi yang berulang:** Dataset terbatas, jumlah kelas sedikit, dan risiko overfitting.
---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [V] Ya / [ ] Tidak | Akurasi model masih menurun pada dataset yang terbatas dan kondisi citra yang beragam |
| Method Gap | [V] Ya / [ ] Tidak |Sebagian penelitian masih menggunakan metode ANN yang memerlukan ekstraksi fitur manual |
| Data Gap | [v] Ya / [ ] Tidak | Banyak penelitian hanya menggunakan sedikit kelas penyakit dan jumlah data terbatas|
| Context Gap | [v] Ya / [ ] Tidak |Model umumnya diuji pada kondisi laboratorium, belum banyak diterapkan pada kondisi nyata di lapangan |

**Gap utama yang dipilih:** Data Gap
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
>Karena dataset yang terbatas dapat membuat model kurang mampu mengenali variasi penyakit pada kondisi nyata. Akibatnya, performa sistem bisa menurun saat digunakan langsung oleh petani di lapangan sehingga hasil deteksi menjadi kurang akurat dan kurang dapat diandalkan.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline     | Mengapa Relevan                                               | Mengapa Representatif                                          | Apakah SOTA?                       | Sumber               |
| - | ------------ | ------------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------- | -------------------- |
| 1 | LeNet-5 CNN  | Digunakan untuk deteksi penyakit daun tomat berbasis citra    | Banyak dipakai pada penelitian klasifikasi citra sederhana     | Bukan, tetapi masih umum digunakan | Saputra et al., 2023 |
| 2 | Inception V4 | Memiliki task yang sama yaitu klasifikasi penyakit daun tomat | Digunakan pada penelitian deep learning dengan performa tinggi | Ya, termasuk arsitektur modern     | Wahid et al., 2021   |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [v] Tidak
> Justifikasi: Baseline dipilih dari metode yang memang digunakan pada penelitian serupa dan memiliki relevansi langsung dengan tugas klasifikasi penyakit daun tomat, sehingga perbandingan dilakukan secara adil dan realistis.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> “Belum ada yang meneliti ini” hanya berupa asumsi tanpa bukti dari literatur. Sedangkan research gap yang valid harus didukung hasil analisis beberapa penelitian, misalnya adanya keterbatasan metode, data, performa, atau konteks yang belum teratasi.

Cara membuktikannya adalah dengan melakukan studi literatur, membandingkan hasil penelitian sebelumnya, lalu menunjukkan pola kekurangan atau masalah yang masih muncul secara konsisten.

