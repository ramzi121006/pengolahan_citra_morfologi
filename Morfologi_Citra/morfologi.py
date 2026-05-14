# ============================================================
# PENGOLAHAN CITRA DIGITAL — MORFOLOGI CITRA
# ============================================================

# Import library
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. MEMBACA GAMBAR
# ============================================================

# Membaca gambar dari folder images
image = cv2.imread('images/sample.jpg')

# Mengecek apakah gambar berhasil dibaca
if image is None:
    print("Gambar tidak ditemukan!")
    exit()

# ============================================================
# 2. KONVERSI KE RGB
# ============================================================

# OpenCV membaca gambar dalam format BGR
# Maka perlu diubah ke RGB agar warna tampil normal
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ============================================================
# 3. KONVERSI KE GRAYSCALE
# ============================================================

# Mengubah gambar menjadi grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ============================================================
# 4. MENAMPILKAN GAMBAR
# ============================================================

plt.figure(figsize=(10,5))

# Gambar asli
plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title('Gambar Asli')
plt.axis('off')

# Gambar grayscale
plt.subplot(1,2,2)
plt.imshow(gray, cmap='gray')
plt.title('Grayscale')
plt.axis('off')

plt.show()
# ============================================================
# 5. THRESHOLDING
# ============================================================

# Mengubah grayscale menjadi citra biner
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# ============================================================
# 6. MEMBUAT KERNEL
# ============================================================

# Kernel digunakan untuk operasi morfologi
kernel = np.ones((5,5), np.uint8)

# ============================================================
# 7. OPERASI EROSI
# ============================================================

# Melakukan erosi pada citra
erosi = cv2.erode(binary, kernel, iterations=1)

# ============================================================
# 8. MENAMPILKAN HASIL EROSI
# ============================================================

plt.figure(figsize=(15,5))

# Gambar biner
plt.subplot(1,2,1)
plt.imshow(binary, cmap='gray')
plt.title('Citra Biner')
plt.axis('off')

# Hasil erosi
plt.subplot(1,2,2)
plt.imshow(erosi, cmap='gray')
plt.title('Hasil Erosi')
plt.axis('off')

plt.show()
# ============================================================
# 9. OPERASI DILASI
# ============================================================

# Melakukan dilasi pada citra
dilasi = cv2.dilate(binary, kernel, iterations=1)

# ============================================================
# 10. MENAMPILKAN HASIL DILASI
# ============================================================

plt.figure(figsize=(15,5))

# Citra biner
plt.subplot(1,2,1)
plt.imshow(binary, cmap='gray')
plt.title('Citra Biner')
plt.axis('off')

# Hasil dilasi
plt.subplot(1,2,2)
plt.imshow(dilasi, cmap='gray')
plt.title('Hasil Dilasi')
plt.axis('off')

plt.show()
# ============================================================
# 11. OPERASI OPENING
# ============================================================

# Opening = Erosi + Dilasi
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# ============================================================
# 12. MENAMPILKAN HASIL OPENING
# ============================================================

plt.figure(figsize=(15,5))

# Citra biner
plt.subplot(1,2,1)
plt.imshow(binary, cmap='gray')
plt.title('Citra Biner')
plt.axis('off')

# Hasil opening
plt.subplot(1,2,2)
plt.imshow(opening, cmap='gray')
plt.title('Hasil Opening')
plt.axis('off')

plt.show()
# ============================================================
# 13. OPERASI CLOSING
# ============================================================

# Closing = Dilasi + Erosi
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# ============================================================
# 14. MENAMPILKAN HASIL CLOSING
# ============================================================

plt.figure(figsize=(15,5))

# Citra biner
plt.subplot(1,2,1)
plt.imshow(binary, cmap='gray')
plt.title('Citra Biner')
plt.axis('off')

# Hasil closing
plt.subplot(1,2,2)
plt.imshow(closing, cmap='gray')
plt.title('Hasil Closing')
plt.axis('off')

plt.show()
# ============================================================
# 15. MENYIMPAN HASIL GAMBAR
# ============================================================

# Menyimpan hasil operasi morfologi
cv2.imwrite('hasil/citra_biner.jpg', binary)
cv2.imwrite('hasil/erosi.jpg', erosi)
cv2.imwrite('hasil/dilasi.jpg', dilasi)
cv2.imwrite('hasil/opening.jpg', opening)
cv2.imwrite('hasil/closing.jpg', closing)

print("Semua hasil berhasil disimpan di folder hasil/")