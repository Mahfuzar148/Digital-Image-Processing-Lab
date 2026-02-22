import cv2
import matplotlib.pyplot as plt
import numpy as np

# ================= Load Image =================
img = cv2.imread('F:/7th semister/DIP LAB/image/bit_plane_slicing_input.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# ================= Extract Bit Planes =================
bit_planes_visual = []     # Only 0/255 for display
bit_planes_weighted = []   # Weighted for reconstruction

for i in range(8):
    bit = (img_gray >> i) & 1
    
    visual_plane = bit * 255
    weighted_plane = bit * (2**i)
    
    bit_planes_visual.append(visual_plane)
    bit_planes_weighted.append(weighted_plane)

# ================= Reconstruction =================
reconstructed = np.zeros_like(img_gray, dtype=np.uint8)

for i in range(8):
    reconstructed += bit_planes_weighted[i]

# ================= Combined Planes =================
combined_0123 = sum(bit_planes_weighted[0:4])
combined_4567 = sum(bit_planes_weighted[4:8])
combined_567  = sum(bit_planes_weighted[5:8])

# ================= Display =================
plt.figure(figsize=(18, 14))
plt.suptitle("Bit Plane Slicing with Proper Reconstruction", fontsize=18)

# Original
plt.subplot(4,4,1)
plt.imshow(img)
plt.title("Original RGB")
plt.axis('off')

# Grayscale
plt.subplot(4,4,2)
plt.imshow(img_gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

# Show All 8 Bit Planes
for i in range(8):
    plt.subplot(4,4,i+3)
    plt.imshow(bit_planes_visual[i], cmap='gray')
    plt.title(f"Bit Plane {i}")
    plt.axis('off')

# Combined Images
plt.subplot(4,4,11)
plt.imshow(combined_0123, cmap='gray')
plt.title("Combined 0-3")
plt.axis('off')

plt.subplot(4,4,12)
plt.imshow(combined_567, cmap='gray')
plt.title("Combined 5-7")
plt.axis('off')

plt.subplot(4,4,13)
plt.imshow(combined_4567, cmap='gray')
plt.title("Combined 4-7")
plt.axis('off')

# Reconstructed
plt.subplot(4,4,14)
plt.imshow(reconstructed, cmap='gray')
plt.title("Reconstructed Image")
plt.axis('off')

plt.tight_layout()
plt.show()