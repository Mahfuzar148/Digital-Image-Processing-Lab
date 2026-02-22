import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.exposure import match_histograms

src_img = cv2.imread("source.png", 0)
ref_img = cv2.imread("flower.png", 0)

if src_img is None or ref_img is None:
    print("Image not found!")
    exit()

matched_img = match_histograms(src_img, ref_img, channel_axis=None)
matched_img = np.uint8(matched_img)

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(src_img, cmap='gray')
plt.title("Source")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(ref_img, cmap='gray')
plt.title("Reference")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(matched_img, cmap='gray')
plt.title("Matched (Built-in)")
plt.axis('off')

plt.tight_layout()
plt.show()