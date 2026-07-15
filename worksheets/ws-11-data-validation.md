# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [✓] Semua skenario tercakup
  [✓] Jumlah run sesuai rencana
  [✓] Tidak ada file output hilang
  Missing: 0 dari 4 data points

Format Consistency:
  [✓] Semua file format sama (CSV/JSON/PKL/PNG/KERAS/TXT)
  [✓] Header konsisten
  [✓] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [✓] Nilai dalam range masuk akal
  [✓] Tidak ada waktu negatif
  [✓] Metrik 0–100%, tidak di luar range
  Anomali ditemukan:
  - Perbedaan waktu eksekusi antar-run (98–168 menit), namun seluruh metrik evaluasi tetap konsisten sehingga tidak memengaruhi validitas hasil.

Cross-Validation:
  [✓] Run identik → hasil mendekati
  [✓] Trend konsisten dengan ekspektasi teori

Keputusan:
  [✓] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: -)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

|| Skenario                                 | Run Direncanakan | Run Tercatat | Missing | Alasan |
| ---------------------------------------- | :--------------: | :----------: | :-----: | ------ |
| CNN – Tomato Leaf Disease Classification |         4        |       4      |    0    | —      |


**Total expected:** 4 | **Total actual:** 4 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data yang hilang. Seluruh run berhasil dikumpulkan sesuai rencana sehingga data siap digunakan untuk analisis.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
| --- | -----------: |
| 1   |        91.08 |
| 2   |        91.55 |
| 3   |        91.01 |
| 4   |        92.95 |


**Deteksi outlier:**
- Q1 = 91.045 | Q3 = 92.25 | IQR = 1.205
- Batas bawah (Q1 - 1.5×IQR) = 89.238
- Batas atas (Q3 + 1.5×IQR) = 94.058
- Outlier terdeteksi: tidak ada

**Investigasi (untuk setiap outlier):**

| Outlier   | Nilai | Kemungkinan Penyebab                          | Keputusan                                               |
| --------- | ----: | --------------------------------------------- | ------------------------------------------------------- |
| Tidak ada |     — | Seluruh nilai accuracy berada dalam batas IQR | Seluruh data dipertahankan dan digunakan untuk analisis |


---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

1. Completeness: 100% data terkumpul.

2. Format: ☑ Konsisten / ☐ Ada inkonsistensi

3. Range check (anomali):

Tidak ditemukan nilai di luar rentang yang wajar. Seluruh metrik Accuracy, Precision, Recall, dan F1-Score berada pada rentang 0–100%, serta tidak ditemukan outlier berdasarkan metode IQR.

4. Logic check: ☑ Parameter sesuai plan / ☐ Ada ketidaksesuaian

Semua eksperimen menggunakan konfigurasi yang sama:

Model CNN
Epoch = 20
Batch Size = 32
Learning Rate = 0.001
Seed = 42
Kesimpulan

☑ Data siap analisis
☐ Perlu tindakan: —

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar adalah data yang berhasil dikumpulkan sesuai hasil pengukuran atau proses komputasi. Namun, data yang dipercaya adalah data yang telah melalui proses validasi sehingga terbukti lengkap, konsisten, logis, dan bebas dari kesalahan yang dapat memengaruhi hasil penelitian. Oleh karena itu, validasi formal tetap diperlukan meskipun data dikumpulkan secara otomatis, karena proses otomatis masih dapat menghasilkan kesalahan seperti data yang tidak lengkap, nilai yang tidak wajar, atau inkonsistensi akibat gangguan selama proses eksperimen. Validasi membantu memastikan bahwa data yang digunakan benar-benar layak untuk dianalisis dan dijadikan dasar dalam penarikan kesimpulan penelitian.
