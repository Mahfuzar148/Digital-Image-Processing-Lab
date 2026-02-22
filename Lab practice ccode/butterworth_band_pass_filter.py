import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image
img = cv2.imread("input.png", 0)

# FFT
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow, ccol = rows//2, cols//2

# Distance matrix
x = np.arange(rows)
y = np.arange(cols)
X, Y = np.meshgrid(x, y, indexing='ij')
D = np.sqrt((X-crow)**2 + (Y-ccol)**2)

# Parameters
D1 = 20   # lower cutoff
D2 = 60   # upper cutoff
n = 2

# Butterworth LPF masks
butter_lp1 = 1 / (1 + (D/D1)**(2*n))
butter_lp2 = 1 / (1 + (D/D2)**(2*n))

# Band Pass
butter_bp = butter_lp2 - butter_lp1

# Apply filter
filtered = fshift * butter_bp
result = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered)))

# Show
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(result, cmap='gray')
plt.title("Butterworth Band Pass")
plt.axis('off')

plt.show()