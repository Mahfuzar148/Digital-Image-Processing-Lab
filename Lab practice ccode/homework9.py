import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure

# ==============================
# Contrast Modification Helpers
# ==============================

def make_low_contrast(img):
    x = img.astype(np.float32) / 255.0
    y = np.clip(x * 0.4 + 0.3, 0, 1)
    return (y * 255).astype(np.uint8)

def make_high_contrast(img):
    x = img.astype(np.float32) / 255.0
    y = np.clip(np.power(x, 0.5), 0, 1)
    return (y * 255).astype(np.uint8)

# ==============================
# Histogram Function
# ==============================

def histogram(img):
    hist = np.zeros(256, dtype=int)
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            hist[img[i,j]] += 1
    return hist

# ==============================
# PDF & CDF
# ==============================

def pdf(hist):
    return hist / hist.sum()

def cdf(pdf):
    return np.cumsum(pdf)

# ==============================
# Built-in Matching (scikit-image)
# ==============================

def builtin_matching(source, reference):
    matched = exposure.match_histograms(source, reference, channel_axis=None)
    return np.clip(matched, 0, 255).astype(np.uint8)

# ==============================
# Custom Method 1 (CDF Difference)
# ==============================

def custom_cdf_matching(source, reference):
    src_hist = histogram(source)
    ref_hist = histogram(reference)

    src_cdf = cdf(pdf(src_hist))
    ref_cdf = cdf(pdf(ref_hist))

    mapping = np.zeros(256, dtype=np.uint8)

    for i in range(256):
        diff = np.abs(ref_cdf - src_cdf[i])
        mapping[i] = np.argmin(diff)

    return mapping[source]

# ==============================
# Custom Method 2 (Interpolation)
# ==============================

def custom_hist_spec(source, reference):
    src_hist, bins = np.histogram(source.flatten(), 256, [0,256], density=True)
    ref_hist, _    = np.histogram(reference.flatten(), 256, [0,256], density=True)

    src_cdf = np.cumsum(src_hist)
    ref_cdf = np.cumsum(ref_hist)

    mapping = np.interp(src_cdf, ref_cdf, np.arange(256))

    src_bin = np.digitize(source.flatten(), bins) - 1
    src_bin = np.clip(src_bin, 0, 255)

    matched = mapping[src_bin].reshape(source.shape)

    return np.clip(matched, 0, 255).astype(np.uint8)

# ==============================
# Display Function
# ==============================

def display_results(source, reference, b_img, c1_img, c2_img, title_suffix):

    plt.figure(figsize=(14,8))

    plt.subplot(2,3,1)
    plt.title("Source " + title_suffix)
    plt.imshow(source, cmap='gray')
    plt.axis('off')

    plt.subplot(2,3,2)
    plt.title("Reference " + title_suffix)
    plt.imshow(reference, cmap='gray')
    plt.axis('off')

    plt.subplot(2,3,3)
    plt.title("Built-in")
    plt.imshow(b_img, cmap='gray')
    plt.axis('off')

    plt.subplot(2,3,4)
    plt.title("Custom CDF")
    plt.imshow(c1_img, cmap='gray')
    plt.axis('off')

    plt.subplot(2,3,5)
    plt.title("Custom Hist Spec")
    plt.imshow(c2_img, cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# ==============================
# Main Experiment
# ==============================

def main():

    source = cv2.imread("source.png", 0)
    reference = cv2.imread("reference.png", 0)

    # ---------- Normal ----------
    b = builtin_matching(source, reference)
    c1 = custom_cdf_matching(source, reference)
    c2 = custom_hist_spec(source, reference)

    display_results(source, reference, b, c1, c2, "(Normal)")

    # ---------- Low Contrast Source ----------
    low_src = make_low_contrast(source)
    b = builtin_matching(low_src, reference)
    c1 = custom_cdf_matching(low_src, reference)
    c2 = custom_hist_spec(low_src, reference)

    display_results(low_src, reference, b, c1, c2, "(Low Source)")

    # ---------- High Contrast Source ----------
    high_src = make_high_contrast(source)
    b = builtin_matching(high_src, reference)
    c1 = custom_cdf_matching(high_src, reference)
    c2 = custom_hist_spec(high_src, reference)

    display_results(high_src, reference, b, c1, c2, "(High Source)")

    # ---------- Low Contrast Reference ----------
    low_ref = make_low_contrast(reference)
    b = builtin_matching(source, low_ref)
    c1 = custom_cdf_matching(source, low_ref)
    c2 = custom_hist_spec(source, low_ref)

    display_results(source, low_ref, b, c1, c2, "(Low Reference)")

    # ---------- High Contrast Reference ----------
    high_ref = make_high_contrast(reference)
    b = builtin_matching(source, high_ref)
    c1 = custom_cdf_matching(source, high_ref)
    c2 = custom_hist_spec(source, high_ref)

    display_results(source, high_ref, b, c1, c2, "(High Reference)")

if __name__ == "__main__":
    main()