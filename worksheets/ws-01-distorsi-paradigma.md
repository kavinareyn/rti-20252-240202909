# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Kavina Reyna Riyadi
Tanggal          :7 Mei 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: 95% dibandingkan metode apa? data apa yang digunakan untuk pengujian dan bagaimana cara pengujiannya?
   - Data yang dibutuhkan untuk verifikasi: data set yang digunakan, metode pengujian, perbandingan dengan metode sebelumnya.

2. Posisi paradigma:
   - Pendekatan: [v] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
   - Alasan: Karena penelitian berfokus pada pengukuran objektif, pengujian performa metode, serta penggunaan data kuantitatif untuk membuktikan peningkatan akurasi.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Bahwa akurasi tinggi otomatis berarti metode lebih baik dan dapat digunakan di semua kondisi
   - Sumber bias potensial: dataset yang terlalu kecil, pemilihan data yang menguntungkan metode tertentu
   - Langkah mitigasi: memilih dataset yang lebih beragam, membandingkan dengan metode lain.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Hasil eksperimen, jumlah data, nilai evaluasi model, dan hasil pengujian yang sebenarnya
   - Batasan yang diakui sejak awal: dataset yang terbatas, hasil belum tentu berlaku untuk semua kasus, performa dapat berubah pada data dunia nyata.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Deteksi Penyakit Tomat Melalui Citra Daun menggunakan Metode Convolutional Neural Network
> Penulis (Tahun): Roni Halim Saputra, Rito Cipta Sigitta Hariyono*, Fathulloh (2023)
> Sumber/Link DOI: Aviation Electronics, Information Technology, Telecommunications, Electricals, Controls (AVITEC) 43 Vol. 5, No. 1, February 2023, pp. 43~51, p-ISSN 2685-2381, e-ISSN 2715-2626 http://dx.doi.org/10.28989/avitec.v5i1.1404

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan 2000 citra daun tomat dari 4 kelas penyakit dan daun sehat. | Data hanya berasal dari kondisi tertentu, pencahayaan tertentu, atau jenis daun tertentu sehingga tidak mewakili kondisi nyata. |
| Data → Processing |Melakukan resize citra dari 2448×3264 menjadi 64×64 dan 32×32 piksel, serta membagi data train:test = 80:20.|Informasi detail daun bisa hilang saat resize, dan pembagian data mungkin tidak benar-benar acak sehingga model terlalu cocok dengan data tertentu. |
| Processing → Analysis |Melatih model CNN LeNet-5 dan Custom Model dengan pengaturan parameter tertentu (epoch, learning rate, batch size). |Parameter dipilih secara subjektif sehingga hasil akurasi bisa dipengaruhi trial-and-error atau overfitting. |
| Analysis → Inference |Menghitung akurasi menggunakan confusion matrix dan menyimpulkan model Custom lebih baik dengan akurasi 95%. |Fokus hanya pada akurasi tanpa membahas precision, recall, atau performa di data dunia nyata. |
| Inference → Knowledge | Menyimpulkan CNN efektif untuk deteksi penyakit daun tomat dan berpotensi dikembangkan ke web/mobile.|Generalisasi berlebihan bahwa model pasti efektif di semua kondisi pertanian padahal data terbatas pada 4 kelas penyakit.|

**Distorsi paling besar di tahap:** Processing → Analysis

**Dua distorsi spesifik yang teridentifikasi:**
1. Pemilihan parameter CNN yang subjektif dapat menyebabkan overfitting dan hasil akurasi terlalu optimis.
2. Dataset terbatas hanya pada 4 jenis kelas penyakit sehingga model belum tentu bekerja baik pada kondisi nyata yang lebih beragam.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Laporkan hasil analisis dengan dan tanpa outlier, serta jelaskan alasan penghapusan data tersebut. |
| Transparansi | Peneliti harus menjelaskan bagaimana outlier ditemukan, metode identifikasi yang digunakan, dan dampaknya terhadap hasil penelitian.|
| Peer review |Reviewer perlu memeriksa apakah penghapusan outlier dilakukan berdasarkan metode statistik yang valid atau hanya untuk membuat hasil menjadi signifikan. |

**Keputusan akhir dan justifikasi:**
> Data outlier tidak boleh dihapus hanya untuk memperoleh hasil yang signifikan. Jika outlier memang terbukti berasal dari kesalahan pengukuran, kesalahan input, atau kondisi yang tidak relevan dengan penelitian, penghapusan dapat dilakukan dengan penjelasan yang jelas. Peneliti tetap harus melaporkan kedua hasil analisis agar penelitian tetap objektif, transparan, dan dapat dipercaya.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** ________________________________________

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 — menggunakan pengujian akurasi dan data kuantitatif | 1 — tidak berfokus pada makna sosial atau pengalaman pengguna |5 — membangun model/artefak CNN untuk menyelesaikan masalah deteksi penyakit |
| Jenis data yang dikumpulkan | Dataset citra daun, akurasi, confusion matrix, hasil training | Wawancara atau observasi pengguna tidak menjadi fokus utama | Hasil performa model, perbandingan arsitektur LeNet-5 dan Custom |
| Limitasi paradigma | Sulit menjelaskan kondisi nyata di lapangan secara mendalam|Tidak cocok untuk evaluasi performa teknis model AI |Fokus pada artefak sehingga aspek sosial dan pengguna bisa kurang diperhatikan |

**Paradigma yang dipilih:** Design Science
**Alasan:** Penelitian berfokus pada perancangan dan pengembangan artefak teknologi berupa model CNN untuk mendeteksi penyakit daun tomat, kemudian mengevaluasi performanya melalui pengujian akurasi dan confusion matrix.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum membaca materi ini, saya cenderung langsung percaya pada klaim “95% akurat”. Setelah memahami rantai distorsi, saya jadi lebih kritis dan akan bertanya: data apa yang digunakan, bagaimana proses pengujiannya, apakah ada bias atau overfitting, dan apakah hasilnya benar-benar bisa diterapkan di kondisi nyata.

