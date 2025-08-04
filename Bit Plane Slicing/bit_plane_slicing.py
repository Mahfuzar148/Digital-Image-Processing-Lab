import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image and convert to RGB
img = cv2.imread('F:/7th semister/DIP LAB/image/bit_plane_slicing_input.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale for bit-plane slicing
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Create figure to display all images
plt.figure(figsize=(30, 20))
plt.suptitle('Bit Plane Slicing', fontsize=24)

# Display original image
plt.subplot(4, 4, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Extract and display each bit plane
for i in range(8):
    # Perform bitwise shift and extract the bit plane
    bit_plane = (img_gray >> i) & 1
    bit_plane = bit_plane * 255  # Scale to 255 for visualization

    # Display bit-plane
    plt.subplot(4, 4, i + 2)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')

# Combining bit planes 5, 6, and 7
combined_img_567 = ((img_gray >> 5) & 1) * 32 + ((img_gray >> 6) & 1) * 64 + ((img_gray >> 7) & 1) * 128
combined_img_01 = ((img_gray >> 0) & 1) * 1 + ((img_gray >> 1) & 1) * 2
combined_img_23 = ((img_gray >> 2) & 1) * 4 + ((img_gray >> 3) & 1) * 8
combined_img_45 = ((img_gray >> 4) & 1) * 16 + ((img_gray >> 5) & 1) * 32
combined_img_0123 = ((img_gray >> 0) & 1) * 1 + ((img_gray >> 1) & 1) * 2 + ((img_gray >> 2) & 1) * 4 + ((img_gray >> 3) & 1) * 8
combined_img_67 = ((img_gray >> 6) & 1) * 64 + ((img_gray >> 7) & 1) * 128
combined_img_4567 = ((img_gray >> 4) & 1) * 16 + ((img_gray >> 5) & 1) * 32 + ((img_gray >> 6) & 1) * 64 + ((img_gray >> 7) & 1) * 128

# Display combined bit plane images
plt.subplot(4, 4, 10)
plt.imshow(combined_img_567, cmap='gray')
plt.title('Combined Bit Planes 5, 6, 7')
plt.axis('off')

plt.subplot(4, 4, 11)
plt.imshow(combined_img_0123, cmap='gray')
plt.title('Combined Bit Planes 0, 1, 2, 3')
plt.axis('off')

plt.subplot(4, 4, 12)
plt.imshow(combined_img_4567, cmap='gray')
plt.title('Combined Bit Planes 4, 5, 6, 7')
plt.axis('off')

plt.subplot(4, 4, 13)
plt.imshow(combined_img_01, cmap='gray')
plt.title('Combined Bit Planes 0, 1')
plt.axis('off')

plt.subplot(4, 4, 14)
plt.imshow(combined_img_23, cmap='gray')
plt.title('Combined Bit Planes 2, 3')
plt.axis('off')

plt.subplot(4, 4, 15)
plt.imshow(combined_img_45, cmap='gray')
plt.title('Combined Bit Planes 4, 5')
plt.axis('off')

plt.subplot(4, 4, 16)
plt.imshow(combined_img_67, cmap='gray')
plt.title('Combined Bit Planes 6, 7')
plt.axis('off')

# Adjust layout and display
plt.subplots_adjust(wspace=0.1, hspace=0.5)
plt.show()

