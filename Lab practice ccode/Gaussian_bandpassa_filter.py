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

# Gaussian LPF masks
gauss_lp1 = np.exp(-(D**2) / (2*(D1**2)))
gauss_lp2 = np.exp(-(D**2) / (2*(D2**2)))

# Band Pass
gauss_bp = gauss_lp2 - gauss_lp1

# Apply filter
filtered = fshift * gauss_bp
result = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered)))

# Show
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(result, cmap='gray')
plt.title("Gaussian Band Pass")
plt.axis('off')

plt.show()