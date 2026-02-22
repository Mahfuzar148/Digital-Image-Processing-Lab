import cv2
import matplotlib.pyplot as plt
import numpy as np

# ===============================
# 1️⃣ Load Image
# ===============================
img = cv2.imread("input.png", 0)

if img is None:
    print("Image not found!")
    exit()

# ===============================
# 2️⃣ Built-in CLAHE
# ===============================
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_img = clahe.apply(img)

# ===============================
# 3️⃣ Manual Adaptive HE
# ===============================
rows, cols = img.shape
block_size = 64
manual_img = np.zeros_like(img)

for i in range(0, rows, block_size):
    for j in range(0, cols, block_size):

        block = img[i:i+block_size, j:j+block_size]

        # Histogram
        hist = np.zeros(256)
        for pixel in block.flatten():
            hist[pixel] += 1

        # PDF & CDF
        pdf = hist / hist.sum()
        cdf = np.cumsum(pdf)

        # Mapping
        new_levels = np.round(cdf * 255).astype(np.uint8)

        # Apply mapping
        equalized_block = new_levels[block]

        manual_img[i:i+block_size, j:j+block_size] = equalized_block

# ===============================
# 4️⃣ Display Results
# ===============================
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(clahe_img, cmap='gray')
plt.title("Built-in CLAHE")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(manual_img, cmap='gray')
plt.title("Manual AHE")
plt.axis('off')

plt.tight_layout()
plt.show()