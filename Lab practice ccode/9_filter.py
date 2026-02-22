import cv2
import matplotlib.pyplot as plt
import numpy as np

# ===============================
# 1️⃣ Load Image (Grayscale)
# ===============================
img = cv2.imread("input.png", 0)

if img is None:
    print("Image not found!")
    exit()

# ===============================
# 2️⃣ Apply FFT
# ===============================
f = np.fft.fft2(img)              # Fourier Transform
fshift = np.fft.fftshift(f)       # Shift low freq to center

rows, cols = img.shape
crow, ccol = rows//2, cols//2     # Center row & column

# ===============================
# 3️⃣ Create Distance Matrix
# ===============================
x = np.arange(rows)
y = np.arange(cols)
X, Y = np.meshgrid(x, y, indexing='ij')

# Distance from center
D = np.sqrt((X-crow)**2 + (Y-ccol)**2)

# Cutoff values
D0 = 30
D1 = 20
D2 = 60
n = 2   # Butterworth order

# ===============================
# 4️⃣ IDEAL FILTERS
# ===============================

ideal_lpf = (D <= D0).astype(float)                    # Low Pass
ideal_hpf = (D > D0).astype(float)                     # High Pass
ideal_bpf = np.logical_and(D > D1, D <= D2).astype(float)  # Band Pass

# ===============================
# 5️⃣ BUTTERWORTH FILTERS
# ===============================

butter_lpf = 1 / (1 + (D/D0)**(2*n))
butter_hpf = 1 - butter_lpf
butter_bpf = (1 / (1 + (D/D2)**(2*n))) - (1 / (1 + (D/D1)**(2*n)))

# ===============================
# 6️⃣ GAUSSIAN FILTERS
# ===============================

gauss_lpf = np.exp(-(D**2) / (2*(D0**2)))
gauss_hpf = 1 - gauss_lpf
gauss_bpf = np.exp(-(D**2)/(2*(D2**2))) - np.exp(-(D**2)/(2*(D1**2)))

# ===============================
# 7️⃣ Apply All Filters
# ===============================
def apply_filter(mask):
    filtered = fshift * mask
    img_back = np.fft.ifft2(np.fft.ifftshift(filtered))
    return np.abs(img_back)

results = [
    apply_filter(ideal_lpf),
    apply_filter(ideal_hpf),
    apply_filter(ideal_bpf),
    apply_filter(butter_lpf),
    apply_filter(butter_hpf),
    apply_filter(butter_bpf),
    apply_filter(gauss_lpf),
    apply_filter(gauss_hpf),
    apply_filter(gauss_bpf),
]

titles = [
    "Ideal LPF", "Ideal HPF", "Ideal BPF",
    "Butterworth LPF", "Butterworth HPF", "Butterworth BPF",
    "Gaussian LPF", "Gaussian HPF", "Gaussian BPF"
]

# ===============================
# 8️⃣ Display Results
# ===============================
plt.figure(figsize=(15,12))

plt.subplot(4,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

for i in range(9):
    plt.subplot(4,3,i+2)
    plt.imshow(results[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()