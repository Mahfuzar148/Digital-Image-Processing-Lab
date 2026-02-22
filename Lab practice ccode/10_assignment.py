import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read image in grayscale
img = cv2.imread("flower.png", 0)

# Convert to binary
#_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

rows, cols = img.shape
binary = np.zeros((rows, cols), dtype=np.uint8)

for i in range(rows):
    for j in range(cols):
        if img[i, j] > 127:
            binary[i, j] = 255
        else:
            binary[i, j] = 0 

# -----------------------------
# Structuring Elements (5x5)
# -----------------------------

rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))

diamond = np.array([[0,0,1,0,0],
                    [0,1,1,1,0],
                    [1,1,1,1,1],
                    [0,1,1,1,0],
                    [0,0,1,0,0]], dtype=np.uint8)

kernels = {
    "Rectangular": rect,
    "Elliptical": ellipse,
    "Cross": cross,
    "Diamond": diamond
}

# -----------------------------
# Built-in Operations
# -----------------------------

for name, kernel in kernels.items():
    
    erosion = cv2.erode(binary, kernel)
    dilation = cv2.dilate(binary, kernel)
    opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    tophat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, kernel)

    plt.figure(figsize=(10,8))
    plt.suptitle(name)

    plt.subplot(2,3,1); plt.imshow(erosion, cmap='gray'); plt.title("Erosion"); plt.axis("off")
    plt.subplot(2,3,2); plt.imshow(dilation, cmap='gray'); plt.title("Dilation"); plt.axis("off")
    plt.subplot(2,3,3); plt.imshow(opening, cmap='gray'); plt.title("Opening"); plt.axis("off")
    plt.subplot(2,3,4); plt.imshow(closing, cmap='gray'); plt.title("Closing"); plt.axis("off")
    plt.subplot(2,3,5); plt.imshow(tophat, cmap='gray'); plt.title("Top Hat"); plt.axis("off")
    plt.subplot(2,3,6); plt.imshow(blackhat, cmap='gray'); plt.title("Black Hat"); plt.axis("off")

    plt.tight_layout()
    plt.show()

# -----------------------------
# From Scratch (Manual Erosion & Dilation)
# -----------------------------

def erosion_manual(img, kernel):
    m, n = img.shape
    k = kernel.shape[0]
    pad = k // 2
    padded = np.pad(img, pad, mode='constant', constant_values=0)
    output = np.zeros_like(img)

    for i in range(m):
        for j in range(n):
            region = padded[i:i+k, j:j+k]
            if np.all(region[kernel==1] == 255):
                output[i,j] = 255
    return output

def dilation_manual(img, kernel):
    m, n = img.shape
    k = kernel.shape[0]
    pad = k // 2
    padded = np.pad(img, pad, mode='constant', constant_values=0)
    output = np.zeros_like(img)

    for i in range(m):
        for j in range(n):
            region = padded[i:i+k, j:j+k]
            if np.any(region[kernel==1] == 255):
                output[i,j] = 255
    return output

# Example Manual Run
manual_erosion = erosion_manual(binary,rect)
manual_dilation = dilation_manual(binary,rect)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.imshow(manual_erosion, cmap='gray')
plt.title("Manual Erosion")
plt.axis("off")
plt.subplot(1,2,2)
plt.imshow(manual_dilation, cmap='gray')
plt.title("Manual Dilation")
plt.axis("off")
plt.show()