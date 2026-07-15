# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Klasifikasi Penyakit Daun Tomat Menggunakan Convolutional Neural Network (CNN) dengan Visualisasi Grad-CAM
Target  : [v] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
[v] Abstract
    Memuat latar belakang, tujuan penelitian, metode CNN,
    dataset Tomato Leaf Disease, hasil utama (Accuracy ±91–93%),
    dan kontribusi berupa visualisasi Grad-CAM.

[v] Introduction
    Menjelaskan pentingnya identifikasi penyakit daun tomat,
    research gap, research question, dan kontribusi penelitian.

[v] Related Work
    Membahas penelitian terdahulu mengenai klasifikasi penyakit tanaman
    menggunakan CNN serta penggunaan Grad-CAM sebagai metode interpretasi.

[v] Method
    Menjelaskan dataset, preprocessing,
    arsitektur CNN, proses training,
    evaluasi menggunakan Accuracy, Precision,
    Recall, F1-Score, Confusion Matrix,
    serta visualisasi Grad-CAM.

[v] Results
    Menyajikan hasil eksperimen,
    tabel metrik evaluasi,
    grafik accuracy dan loss,
    confusion matrix,
    classification report,
    serta visualisasi Grad-CAM.

[v] Discussion
    Menginterpretasikan hasil,
    menghubungkan dengan research question,
    membandingkan dengan penelitian terdahulu,
    serta membahas keterbatasan penelitian.

[v] Conclusion
    Menjawab research question,
    menyampaikan kontribusi penelitian,
    dan memberikan saran penelitian selanjutnya.

Consistency Matrix:
  [v] Research Question konsisten pada
    Introduction, Method, Results,
    Discussion, dan Conclusion

[v] Variabel pada Method
    sesuai dengan hasil pada Results

[v] Klaim pada Discussion
    didukung oleh data hasil penelitian

[v] Limitasi penelitian dijelaskan
    pada Discussion dan dijadikan
    dasar Future Work

Writing Quality:
  [v] Clarity — mudah dipahami tanpa re-read
  [v] Precision — tidak ada istilah ambigu
  [v] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section          | Konten Utama (2–3 kalimat)                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Target Kata |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------: |
| **Abstract**     | Penelitian ini bertujuan mengembangkan model **Convolutional Neural Network (CNN)** untuk mengklasifikasikan 10 kelas penyakit daun tomat menggunakan **Tomato Leaf Disease Dataset**. Model dievaluasi menggunakan Accuracy, Precision, Recall, F1-Score, Confusion Matrix, serta dijelaskan menggunakan **Grad-CAM**. Hasil empat kali eksperimen menunjukkan rata-rata accuracy sebesar **91,65%**, sehingga model dinilai mampu melakukan klasifikasi secara akurat dan interpretabel. |     200–250 |
| **Introduction** | Menjelaskan pentingnya deteksi dini penyakit daun tomat dalam meningkatkan produktivitas pertanian. Dibahas keterbatasan identifikasi manual dan potensi CNN sebagai solusi otomatis, kemudian dipaparkan research gap mengenai kurangnya interpretabilitas model pada penelitian sebelumnya. Bagian ini diakhiri dengan Research Question, tujuan penelitian, dan kontribusi berupa penerapan Grad-CAM.                                                                                   |     500–700 |
| **Related Work** | Mengulas penelitian terdahulu mengenai klasifikasi penyakit tanaman menggunakan CNN maupun deep learning lainnya, termasuk penggunaan Grad-CAM untuk interpretasi model. Dibahas persamaan, perbedaan, serta posisi penelitian ini dibanding penelitian sebelumnya sehingga terlihat kontribusi yang diberikan.                                                                                                                                                                            |    700–1000 |
| **Method**       | Menjelaskan desain penelitian, dataset Tomato Leaf Disease, proses preprocessing (resize 224×224, rescaling 0–1), arsitektur CNN, proses training selama 20 epoch, konfigurasi eksperimen, evaluasi menggunakan Accuracy, Precision, Recall, F1-Score, Confusion Matrix, serta visualisasi Grad-CAM. Bagian ini juga menjelaskan empat kali eksperimen (repeatability) dengan parameter yang sama.                                                                                         |    800–1200 |
| **Results**      | Menyajikan hasil empat kali eksperimen berupa tabel metrik evaluasi, rata-rata accuracy **91,65%**, grafik accuracy dan loss, confusion matrix, classification report, serta visualisasi Grad-CAM. Bagian ini juga menyajikan analisis statistik deskriptif dari hasil eksperimen.                                                                                                                                                                                                         |     500–800 |
| **Discussion**   | Menginterpretasikan hasil penelitian dengan menghubungkannya pada Research Question. Dibahas alasan model mampu mencapai accuracy di atas 91%, analisis confusion matrix dan Grad-CAM, perbandingan dengan penelitian terdahulu, serta keterbatasan penelitian seperti penggunaan dataset tunggal dan arsitektur CNN sederhana.                                                                                                                                                            |     600–900 |
| **Conclusion**   | Menyimpulkan bahwa CNN mampu mengklasifikasikan penyakit daun tomat dengan performa yang baik dan Grad-CAM membantu meningkatkan interpretabilitas model. Disampaikan pula kontribusi penelitian, keterbatasan, serta saran pengembangan seperti penggunaan arsitektur CNN yang lebih modern dan pengujian pada dataset lapangan yang lebih beragam.                                                                                                                                       |     200–400 |


---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|                                                          | Intro | Method | Result | Discussion | Conclusion |
| -------------------------------------------------------- | :---: | :----: | :----: | :--------: | :--------: |
| **RQ1**                                                  |   ✓   |    ✓   |    ✓   |      ✓     |      ✓     |
| **RQ2**                                                  |   –   |    –   |    –   |      –     |      –     |
| **Metrik utama (Accuracy, Precision, Recall, F1-Score)** |   ~   |    ✓   |    ✓   |      ✓     |      ✓     |
| **Variabel IV (Model CNN & Grad-CAM)**                   |   ✓   |    ✓   |    ✓   |      ✓     |      ✓     |
| **Variabel DV (Hasil klasifikasi penyakit daun tomat)**  |   ✓   |    ✓   |    ✓   |      ✓     |      ✓     |
| **Klaim/Kontribusi penelitian**                          |   ✓   |    ✓   |    ✓   |      ✓     |      ✓     |


**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Metrik evaluasi (Accuracy, Precision, Recall, dan F1-Score) belum dijelaskan secara rinci pada bagian Introduction karena bagian tersebut hanya memaparkan tujuan penelitian dan research question. Penjelasan lengkap mengenai metrik baru disampaikan pada bagian Method.

**Tindakan perbaikan:**
> Menambahkan satu kalimat pada akhir Introduction yang menyatakan bahwa performa model akan dievaluasi menggunakan Accuracy, Precision, Recall, F1-Score, Confusion Matrix, dan visualisasi Grad-CAM. Dengan demikian, terdapat kesinambungan yang lebih jelas antara tujuan penelitian, metode evaluasi, hasil, pembahasan, dan kesimpulan.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Penelitian ini menggunakan metode Convolutional Neural Network (CNN) untuk mengklasifikasikan penyakit daun tomat. Dataset yang digunakan adalah Tomato Leaf Disease Dataset yang terdiri dari 10 kelas. Model kemudian dilatih selama 20 epoch dan dilakukan evaluasi menggunakan accuracy, precision, recall, dan F1-score. Selain itu digunakan Grad-CAM untuk melihat bagian citra yang menjadi perhatian model. Hasil penelitian menunjukkan bahwa model memiliki performa yang baik.

| Kriteria        | Evaluasi                                                                        | Perbaikan                                                                                       |
| --------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Clarity**     | Kalimat terakhir "model memiliki performa yang baik" masih terlalu umum.        | Sebutkan metrik secara spesifik, misalnya "model memperoleh rata-rata accuracy sebesar 91,65%". |
| **Precision**   | Belum menyebutkan hasil utama secara kuantitatif dan kontribusi Grad-CAM.       | Tambahkan nilai accuracy, jumlah eksperimen, dan fungsi Grad-CAM.                               |
| **Conciseness** | Kalimat ke-3 dan ke-4 dapat digabung agar lebih ringkas tanpa mengurangi makna. | Gabungkan informasi evaluasi dan Grad-CAM dalam satu kalimat.                                   |


**Paragraf setelah perbaikan:**
> Penelitian ini menggunakan Convolutional Neural Network (CNN) untuk mengklasifikasikan 10 kelas penyakit daun tomat menggunakan Tomato Leaf Disease Dataset. Model dilatih selama 20 epoch dan dievaluasi menggunakan Accuracy, Precision, Recall, dan F1-Score, sedangkan Grad-CAM digunakan untuk memvisualisasikan area citra yang menjadi dasar prediksi model. Berdasarkan empat kali eksperimen, model memperoleh rata-rata accuracy sebesar 91,65%, sehingga menunjukkan bahwa CNN mampu melakukan klasifikasi penyakit daun tomat dengan performa yang baik sekaligus memberikan interpretasi visual terhadap hasil prediksi.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis tentang riset berarti hanya mendeskripsikan apa yang dilakukan dalam penelitian, misalnya menjelaskan metode, dataset, atau tahapan eksperimen. Sebaliknya, menulis sebagai argumen riset berarti setiap bagian tulisan disusun untuk meyakinkan pembaca bahwa metode yang dipilih tepat, hasil yang diperoleh valid, dan kesimpulan yang diambil didukung oleh data. Dengan demikian, setiap klaim harus disertai bukti berupa hasil eksperimen, metrik evaluasi, maupun pembahasan yang relevan.

> Urutan penulisan Method → Discussion → Introduction membantu meningkatkan kualitas tulisan karena peneliti terlebih dahulu memahami secara jelas apa yang benar-benar dilakukan dan hasil apa yang diperoleh sebelum menyusun latar belakang dan rumusan masalah. Dengan pendekatan ini, bagian Introduction dapat difokuskan pada masalah yang memang berhasil dijawab oleh penelitian, sedangkan Discussion dapat menghubungkan hasil eksperimen dengan research question secara lebih logis dan konsisten. Akibatnya, keseluruhan tulisan menjadi lebih runtut, fokus, dan didukung oleh bukti yang diperoleh selama penelitian.
