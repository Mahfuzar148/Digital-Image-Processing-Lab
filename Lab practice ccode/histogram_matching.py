import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    # Load images
    src_path = "source.png"
    ref_path = "reference.png"

    src_img = cv2.imread(src_path, 0)
    ref_img = cv2.imread(ref_path, 0)

    # Histogram
    src_hist = histogram(src_img)
    ref_hist = histogram(ref_img)

    # PDF
    src_pdf = pdf_f(src_hist)
    ref_pdf = pdf_f(ref_hist)

    # CDF
    src_cdf = cdf_f(src_pdf)
    ref_cdf = cdf_f(ref_pdf)

    # Mapping
    mapping = match_histogram(src_cdf, ref_cdf)

    # Apply mapping
    matched_img = img_conv(src_img, mapping)
    matched_hist = histogram(matched_img)

    # Display
    display(src_img, ref_img, matched_img,
            src_hist, ref_hist, matched_hist,
            src_cdf, ref_cdf)

# ================= Histogram Matching =================
def match_histogram(src_cdf, ref_cdf):
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        diff = np.abs(ref_cdf - src_cdf[i])
        mapping[i] = np.argmin(diff)
    return mapping

# ================= Apply Mapping =================
def img_conv(img, mapping):
    return mapping[img]

# ================= Histogram =================
def histogram(img):
    h, w = img.shape
    hist = np.zeros(256, dtype=int)
    for i in range(h):
        for j in range(w):
            hist[img[i,j]] += 1
    return hist

# ================= PDF & CDF =================
def pdf_f(hist):
    return hist / hist.sum()

def cdf_f(pdf):
    return np.cumsum(pdf)

# ================= Display =================
def display(src, ref, matched,
            src_hist, ref_hist, matched_hist,
            src_cdf, ref_cdf):

    plt.figure(figsize=(15,12))

    # Images
    plt.subplot(3,3,1)
    plt.title("Source Image")
    plt.imshow(src, cmap='gray')
    plt.axis('off')

    plt.subplot(3,3,2)
    plt.title("Reference Image")
    plt.imshow(ref, cmap='gray')
    plt.axis('off')

    plt.subplot(3,3,3)
    plt.title("Matched Image")
    plt.imshow(matched, cmap='gray')
    plt.axis('off')

    # Histograms
    plt.subplot(3,3,4)
    plt.title("Source Histogram")
    plt.bar(range(256), src_hist, color='blue')

    plt.subplot(3,3,5)
    plt.title("Reference Histogram")
    plt.bar(range(256), ref_hist, color='green')

    plt.subplot(3,3,6)
    plt.title("Matched Histogram")
    plt.bar(range(256), matched_hist, color='red')

    # CDF
    plt.subplot(3,3,7)
    plt.title("Source CDF")
    plt.plot(src_cdf)

    plt.subplot(3,3,8)
    plt.title("Reference CDF")
    plt.plot(ref_cdf)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    
