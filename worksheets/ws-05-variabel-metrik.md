# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5?

| Variabel                 | Tipe | Konsep                                            | Metrik                      | Skala   | Satuan       | Cara Mengukur                                  | Justifikasi                                      |
| ------------------------ | ---- | ------------------------------------------------- | --------------------------- | ------- | ------------ | ---------------------------------------------- | ------------------------------------------------ |
| Jenis arsitektur CNN     | IV   | Perbedaan model CNN yang digunakan                | Jenis model                 | Nominal | -            | Membandingkan CNN Custom dan LeNet-5           | Untuk melihat pengaruh model terhadap performa   |
| Akurasi deteksi          | DV   | Kemampuan model mengenali penyakit daun tomat     | Accuracy, precision, recall | Rasio   | Persen (%)   | Menggunakan confusion matrix                   | Mengukur performa model klasifikasi              |
| Dataset citra daun tomat | CV   | Data yang digunakan untuk pelatihan dan pengujian | Jumlah dan kelas data       | Rasio   | Jumlah citra | Menggunakan dataset yang sama pada semua model | Agar perbandingan hasil lebih adil dan konsisten |


Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [v] Setiap langkah terdokumentasi
  [v] Tidak ada "lompatan logis"
  [v] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah penggunaan CNN Custom dapat meningkatkan akurasi deteksi penyakit daun tomat dibandingkan LeNet-5?

| Variabel                 | Tipe | Konsep Abstrak                     | Metrik Konkret                  | Skala (NOIR) | Satuan       |
| ------------------------ | ---- | ---------------------------------- | ------------------------------- | ------------ | ------------ |
| Jenis arsitektur CNN     | IV   | Pendekatan klasifikasi citra       | CNN Custom vs LeNet-5           | Nominal      | —            |
| Akurasi deteksi penyakit | DV   | Kemampuan model mengenali penyakit | Accuracy, precision, recall     | Rasio        | %            |
| Dataset citra daun tomat | CV   | Data pelatihan dan pengujian model | Jumlah citra dan kelas penyakit | Rasio        | Jumlah citra |


**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [v] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria       | Skor (1–5) | Justifikasi                                                                                                      |
| -------------- | ---------- | ---------------------------------------------------------------------------------------------------------------- |
| Representative | 5          | Accuracy, precision, dan recall cukup mewakili performa model klasifikasi penyakit daun tomat                    |
| Sensitive      | 4          | Metrik dapat menunjukkan perubahan performa model, tetapi accuracy bisa kurang sensitif pada data tidak seimbang |
| Feasible       | 5          | Mudah dihitung menggunakan confusion matrix dan umum digunakan pada CNN                                          |


**Apakah perlu secondary metric?** [v] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? F1-Score, karena dapat menyeimbangkan precision dan recall terutama jika jumlah data tiap kelas tidak seimbang.

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika accuracy sudah sangat tinggi, misalnya 98–99%, peningkatan kecil performa model menjadi sulit terlihat hanya dari accuracy saja.
---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi            | Pertanyaan                                 | Jawaban                                                  | Strategi Mitigasi                                            |
| ------------------ | ------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------ |
| Completeness       | Apakah semua data point terkumpul?         | Tidak semua citra mungkin lengkap atau berkualitas baik  | Melakukan pengecekan dataset dan menghapus data rusak        |
| Consistency        | Apakah ada kontradiksi internal?           | Bisa terjadi perbedaan label antar data citra            | Validasi ulang label dataset sebelum training                |
| Validity           | Apakah benar-benar mengukur yang dimaksud? | Ya, karena metrik mengukur performa klasifikasi penyakit | Menggunakan confusion matrix dan evaluasi beberapa metrik    |
| Representativeness | Apakah sampel mewakili populasi target?    | Belum sepenuhnya, karena dataset masih terbatas          | Menambah variasi citra dan jenis penyakit dari kondisi nyata |


---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik setelah melihat hasil data disebut p-hacking karena metrik dipilih agar hasil terlihat bagus atau signifikan. Ini membuat penelitian menjadi tidak objektif.

Sedangkan eksplorasi data yang sah dilakukan untuk memahami data, bukan untuk mencari hasil yang paling menguntungkan.
