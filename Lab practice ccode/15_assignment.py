import cv2
import matplotlib.pyplot as plt
import numpy as np

# =============================
# 1️⃣ Load Input Image
# =============================
img = cv2.imread("input.png", 0)

if img is None:
    print("Image not found!")
    exit()

img = cv2.resize(img, (256,256))

# =============================
# 2️⃣ Create Contrast Versions
# =============================
low_contrast = cv2.convertScaleAbs(img, alpha=0.5, beta=30)
normal_contrast = img
high_contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=-50)

images = {
    "Low Contrast": low_contrast,
    "Normal Contrast": normal_contrast,
    "High Contrast": high_contrast
}

# =============================
# 3️⃣ FFT Function
# =============================
def fft_image(image):
    f = np.fft.fft2(image)
    return np.fft.fftshift(f)

def ifft_image(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    return np.abs(img_back)

# =============================
# 4️⃣ Distance Matrix
# =============================
def distance_matrix(shape):
    rows, cols = shape
    crow, ccol = rows//2, cols//2
    u = np.arange(rows)
    v = np.arange(cols)
    U, V = np.meshgrid(u, v, indexing='ij')
    D = np.sqrt((U-crow)**2 + (V-ccol)**2)
    return D

# =============================
# 5️⃣ Filter Functions
# =============================
def ideal_lpf(D, D0):
    return (D <= D0).astype(float)

def butter_lpf(D, D0, n):
    return 1 / (1 + (D/D0)**(2*n))

def gaussian_lpf(D, D0):
    return np.exp(-(D**2)/(2*(D0**2)))

# HPF = 1 - LPF
# BPF = LPF(D2) - LPF(D1)

D0_low = 20
D0_high = 60

# =============================
# 6️⃣ Apply Filters
# =============================
for title, image in images.items():

    fshift = fft_image(image)
    D = distance_matrix(image.shape)

    # Ideal
    ideal_lp = ideal_lpf(D, D0_low)
    ideal_hp = 1 - ideal_lp
    ideal_bp = ideal_lpf(D, D0_high) - ideal_lpf(D, D0_low)

    # Butterworth (n=2)
    butter_lp = butter_lpf(D, D0_low, 2)
    butter_hp = 1 - butter_lp
    butter_bp = butter_lpf(D, D0_high, 2) - butter_lpf(D, D0_low, 2)

    # Gaussian
    gauss_lp = gaussian_lpf(D, D0_low)
    gauss_hp = 1 - gauss_lp
    gauss_bp = gaussian_lpf(D, D0_high) - gaussian_lpf(D, D0_low)

    # Apply filters
    results = [
        ifft_image(fshift * ideal_lp),
        ifft_image(fshift * ideal_hp),
        ifft_image(fshift * ideal_bp),
        ifft_image(fshift * butter_lp),
        ifft_image(fshift * butter_hp),
        ifft_image(fshift * butter_bp),
        ifft_image(fshift * gauss_lp),
        ifft_image(fshift * gauss_hp),
        ifft_image(fshift * gauss_bp),
    ]

    titles = [
        "Ideal LPF", "Ideal HPF", "Ideal BPF",
        "Butter LPF", "Butter HPF", "Butter BPF",
        "Gaussian LPF", "Gaussian HPF", "Gaussian BPF"
    ]

    plt.figure(figsize=(15,12))
    plt.suptitle(title)

    plt.subplot(4,3,1)
    plt.imshow(image, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    for i in range(9):
        plt.subplot(4,3,i+2)
        plt.imshow(results[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# =============================
# 7️⃣ Butterworth Different n
# =============================
plt.figure(figsize=(10,4))
plt.suptitle("Butterworth LPF - Different n")

D = distance_matrix(normal_contrast.shape)
fshift = fft_image(normal_contrast)

for i, n in enumerate([1,2,5]):
    mask = butter_lpf(D, D0_low, n)
    result = ifft_image(fshift * mask)

    plt.subplot(1,3,i+1)
    plt.imshow(result, cmap='gray')
    plt.title(f"n = {n}")
    plt.axis('off')

plt.tight_layout()
plt.show()