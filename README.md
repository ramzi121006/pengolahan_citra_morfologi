# pengolahan_citra_morfologi

# 📸 MORFOLOGI CITRA DIGITAL

## 👩‍🎓 Identitas Mahasiswa

| Keterangan | Isi |
|---|---|
| 👤 Nama | Nadhia Shafira |
| 🆔 NIM | 312410498 |
| 🏫 Kelas | I241E |
| 📚 Mata Kuliah | Pengolahan Citra |
| 👨‍🏫 Dosen Pengampu | Dr. Muhamad Fatchan, S.Kom., M.Kom. |

---

# 📖 Deskripsi Praktikum

Praktikum ini membahas tentang **Morfologi Citra Digital** menggunakan bahasa pemrograman Python dan library OpenCV.  

Morfologi citra merupakan teknik pengolahan citra yang digunakan untuk melakukan manipulasi bentuk objek pada gambar, terutama pada citra biner.

Pada praktikum ini dilakukan beberapa operasi morfologi, yaitu:

- ✅ Erosi
- ✅ Dilasi
- ✅ Opening
- ✅ Closing

Tujuan praktikum ini adalah memahami bagaimana proses morfologi bekerja dalam memperbaiki, membersihkan, dan memanipulasi objek pada citra digital.

---

# 🎯 Tujuan Praktikum

Adapun tujuan dari praktikum ini yaitu:

- Memahami konsep dasar morfologi citra.
- Memahami penggunaan OpenCV dalam pengolahan citra digital.
- Mengetahui fungsi operasi erosi dan dilasi.
- Mengetahui fungsi operasi opening dan closing.
- Menghasilkan citra hasil proses morfologi.

---

# 🛠️ Tools dan Library

Praktikum ini menggunakan beberapa tools dan library berikut:

| Tools / Library | Fungsi |
|---|---|
| Python | Bahasa pemrograman utama |
| OpenCV | Pengolahan citra digital |
| NumPy | Operasi array dan matriks |
| Matplotlib | Menampilkan gambar |
| VS Code | Text editor / IDE |

---

# 📂 Struktur Folder Project

```bash
Morfologi_Citra
│
├── images
│   └── sample.jpg
│
├── hasil
│   ├── citra_biner.jpg
│   ├── erosi.jpg
│   ├── dilasi.jpg
│   ├── opening.jpg
│   └── closing.jpg
│
├── morfologi.py
└── README.md
```

---

# 📥 Instalasi Library

Sebelum menjalankan program, install library terlebih dahulu menggunakan perintah berikut:

```bash
pip install opencv-python
pip install matplotlib
pip install numpy
```

---

# ▶️ Cara Menjalankan Program

Buka terminal kemudian jalankan perintah:

```bash
python morfologi.py
```

---

# 🧠 Source Code Program

## 📌 Import Library

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt
```

### 📖 Penjelasan

- `cv2` digunakan untuk pengolahan citra digital menggunakan OpenCV.
- `numpy` digunakan untuk operasi matriks dan array.
- `matplotlib` digunakan untuk menampilkan gambar hasil proses.

---

# 📌 Membaca Gambar

```python
image = cv2.imread('images/sample.jpg')
```

### 📖 Penjelasan

Kode di atas digunakan untuk membaca gambar dari folder `images`.

Jika gambar gagal dibaca maka program akan menampilkan pesan error.

---

# 📌 Konversi RGB

```python
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

### 📖 Penjelasan

OpenCV membaca gambar dalam format BGR.  
Oleh karena itu gambar perlu diubah ke RGB agar warna tampil normal saat ditampilkan menggunakan matplotlib.

---

# 📌 Konversi Grayscale

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

### 📖 Penjelasan

Kode di atas digunakan untuk mengubah gambar menjadi grayscale atau abu-abu.

Konversi grayscale dilakukan karena operasi morfologi lebih efektif digunakan pada citra grayscale atau biner.

---

# 📌 Thresholding

```python
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
```

### 📖 Penjelasan

Thresholding digunakan untuk mengubah citra grayscale menjadi citra biner.

Nilai pixel:
- Di atas 127 → putih
- Di bawah 127 → hitam

---

# 📌 Kernel Morfologi

```python
kernel = np.ones((5,5), np.uint8)
```

### 📖 Penjelasan

Kernel merupakan matriks kecil yang digunakan dalam proses operasi morfologi.

Ukuran kernel yang digunakan yaitu `5x5`.

Semakin besar ukuran kernel, maka efek morfologi akan semakin besar.

---

# 📌 Operasi Erosi

```python
erosi = cv2.erode(binary, kernel, iterations=1)
```

### 📖 Penjelasan

Erosi digunakan untuk mengecilkan objek putih pada citra biner.

Fungsi erosi:
- Mengurangi noise kecil
- Mengikis objek
- Mengecilkan area putih

---

# 📸 Hasil Erosi

👉 Letakkan gambar hasil erosi di bawah ini:

```md
![Hasil Erosi](hasil/erosi.jpg)
```

![Hasil Erosi](hasil/erosi.jpg)

---

# 📌 Operasi Dilasi

```python
dilasi = cv2.dilate(binary, kernel, iterations=1)
```

### 📖 Penjelasan

Dilasi digunakan untuk memperbesar objek putih pada citra.

Fungsi dilasi:
- Mempertebal objek
- Memperbesar area putih
- Menutup celah kecil

---

# 📸 Hasil Dilasi

👉 Letakkan gambar hasil dilasi di bawah ini:

```md
![Hasil Dilasi](hasil/dilasi.jpg)
```

![Hasil Dilasi](hasil/dilasi.jpg)

---

# 📌 Operasi Opening

```python
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
```

### 📖 Penjelasan

Opening merupakan gabungan dari:
- Erosi
- Dilasi

Opening digunakan untuk:
- Menghilangkan noise kecil
- Membersihkan citra
- Mempertahankan bentuk objek utama

---

# 📸 Hasil Opening

👉 Letakkan gambar hasil opening di bawah ini:

```md
![Hasil Opening](hasil/opening.jpg)
```

![Hasil Opening](hasil/opening.jpg)

---

# 📌 Operasi Closing

```python
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
```

### 📖 Penjelasan

Closing merupakan gabungan dari:
- Dilasi
- Erosi

Closing digunakan untuk:
- Menutup lubang kecil
- Menyambungkan objek yang terputus
- Memperhalus bentuk objek

---

# 📸 Hasil Closing

👉 Letakkan gambar hasil closing di bawah ini:

```md
![Hasil Closing](hasil/closing.jpg)
```

![Hasil Closing](hasil/closing.jpg)

---

# 💾 Menyimpan Hasil Gambar

```python
cv2.imwrite('hasil/erosi.jpg', erosi)
cv2.imwrite('hasil/dilasi.jpg', dilasi)
cv2.imwrite('hasil/opening.jpg', opening)
cv2.imwrite('hasil/closing.jpg', closing)
```

### 📖 Penjelasan

Kode di atas digunakan untuk menyimpan hasil proses morfologi secara otomatis ke folder `hasil`.

---

# 📊 Analisis Hasil

Berdasarkan hasil percobaan yang telah dilakukan, diperoleh beberapa hasil sebagai berikut:

- Operasi erosi berhasil mengecilkan objek putih pada citra.
- Operasi dilasi berhasil memperbesar objek putih.
- Opening mampu menghilangkan noise kecil pada citra.
- Closing mampu menutup celah kecil pada objek.

Teknik morfologi sangat berguna dalam proses preprocessing citra sebelum dilakukan segmentasi atau analisis lanjutan.

---

# ✅ Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa operasi morfologi citra dapat digunakan untuk memanipulasi bentuk objek pada gambar digital.

Operasi erosi dan dilasi memiliki fungsi dasar untuk mengecilkan dan memperbesar objek, sedangkan opening dan closing digunakan untuk memperbaiki kualitas citra dengan menghilangkan noise dan menutup celah kecil.

Dengan menggunakan Python dan OpenCV, proses morfologi citra dapat dilakukan dengan mudah dan efektif.

---

# 📚 Referensi

- Gonzalez, R. C., & Woods, R. E. *Digital Image Processing*.
- Dokumentasi OpenCV Morphology.
- Modul Praktikum Pengolahan Citra Digital.

---

# ✨ Hasil Akhir Praktikum

Praktikum morfologi citra berhasil dijalankan dengan baik menggunakan Python dan OpenCV.

Semua operasi morfologi berhasil diterapkan dan menghasilkan output citra sesuai teori.
