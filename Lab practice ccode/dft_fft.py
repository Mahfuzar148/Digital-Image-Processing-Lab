import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1️⃣ Image read (grayscale)
img = cv2.imread("input.png", 0)

# =========================
# 🔵 DFT (OpenCV Built-in)
# =========================
img_float = np.float32(img)
dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_dft = cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])
magnitude_dft = 20 * np.log(magnitude_dft + 1)

# =========================
# 🟢 FFT (NumPy Built-in)
# =========================
fft = np.fft.fft2(img)
fft_shift = np.fft.fftshift(fft)

magnitude_fft = 20 * np.log(np.abs(fft_shift) + 1)

# =========================
# Show All Results
# =========================
plt.figure(figsize=(10,6))

plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(magnitude_dft, cmap='gray')
plt.title("DFT (OpenCV)")
plt.axis("off")

plt.subplot(2,2,3)
plt.imshow(magnitude_fft, cmap='gray')
plt.title("FFT (NumPy)")
plt.axis("off")

plt.tight_layout()
plt.show()