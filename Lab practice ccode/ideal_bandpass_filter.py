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

# Band pass range
D1 = 20   # lower cutoff
D2 = 60   # upper cutoff

# Ideal Band Pass mask
mask = np.logical_and(D > D1, D <= D2).astype(float)

# Apply filter
filtered = fshift * mask
result = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered)))

# Show
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(result, cmap='gray')
plt.title("Ideal Band Pass")
plt.axis('off')

plt.show()