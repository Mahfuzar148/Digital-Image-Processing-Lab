# ================= Import Libraries =================
import cv2
import matplotlib.pyplot as plt
import numpy as np


# ================= Manual Histogram =================
def histogram(img):
    hist = np.zeros(256, dtype=int)
    h, w = img.shape

    for i in range(h):
        for j in range(w):
            hist[img[i, j]] += 1

    return hist


# ================= Manual Equalization =================
def manual_equalization(img):

    # Histogram
    hist = histogram(img)

    # PDF
    pdf = hist / hist.sum()

    # CDF
    cdf = np.cumsum(pdf)

    # Mapping
    new_level = np.round(cdf * 255).astype(np.uint8)

    # Apply mapping
    new_img = new_level[img]

    return new_img, hist


# ================= Main =================
def main():

    img = cv2.imread("flower.png", 0)

    if img is None:
        print("Image not found!")
        return

    # Manual Equalization
    manual_img, hist_original = manual_equalization(img)

    # Built-in Equalization
    builtin_img = cv2.equalizeHist(img)

    # Histograms
    hist_manual = histogram(manual_img)
    hist_builtin = histogram(builtin_img)

    # ================= Display =================
    plt.figure(figsize=(12,8))

    # Original
    plt.subplot(3,2,1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis('off')

    # Manual
    plt.subplot(3,2,2)
    plt.imshow(manual_img, cmap='gray')
    plt.title("Manual Equalization")
    plt.axis('off')

    # Built-in
    plt.subplot(3,2,3)
    plt.imshow(builtin_img, cmap='gray')
    plt.title("Built-in Equalization")
    plt.axis('off')

    # Original Histogram
    plt.subplot(3,2,4)
    plt.bar(range(256), hist_original)
    plt.title("Original Histogram")

    # Manual Histogram
    plt.subplot(3,2,5)
    plt.bar(range(256), hist_manual)
    plt.title("Manual Histogram")

    # Built-in Histogram
    plt.subplot(3,2,6)
    plt.bar(range(256), hist_builtin)
    plt.title("Built-in Histogram")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()