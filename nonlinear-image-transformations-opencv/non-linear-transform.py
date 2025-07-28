import cv2
import matplotlib.pyplot as plt
import numpy as np

# === Entry point of the program ===
def main():
    print("📢 Non-linear Function Image Processing Example")

# === STEP 1: Load the grayscale image ===
gray_scale_img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Check if the image loaded correctly
if gray_scale_img is None:
    print('❌ Image not loaded! Check the file path.')

# === STEP 2: Normalize image pixel values to [0, 1] range ===
img_norm = gray_scale_img / 255.0  # Converts 8-bit values to float values between 0 and 1

# === STEP 3: Apply Gamma Correction ===
gamma_values = [0.1, 0.3, 0.7, 1, 2, 3]  # Different gamma values to experiment with
c = 1.0  # Scaling constant
# Apply s = c * r^γ transformation for each gamma
gamma_imgs = [c * np.power(img_norm, g) for g in gamma_values]

# === STEP 4: Apply Logarithmic Transformation ===
# Formula: s = c * log2(1 + r)
log_img = c * np.log2(1 + img_norm)
# Normalize log output to [0, 1] for visualization
log_img = log_img / np.max(log_img)

# === STEP 5: Plot all the results ===
plt.figure(figsize=(18, 10))  # Create a large figure to hold all subplots

# Plot Original Grayscale Image
plt.subplot(2, 4, 1)
plt.imshow(gray_scale_img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Plot Gamma Corrected Images
for i, g_img in enumerate(gamma_imgs):
    # Scale back to 0–255 and convert to uint8 for display
    g_img_scaled = np.clip(g_img * 255, 0, 255).astype(np.uint8)
    plt.subplot(2, 4, i + 2)
    plt.imshow(g_img_scaled, cmap='gray')
    plt.title(f'Gamma = {gamma_values[i]}')
    plt.axis('off')

# Plot Log Transformed Image
plt.subplot(2, 4, 8)
log_scaled = np.clip(log_img * 255, 0, 255).astype(np.uint8)
plt.imshow(log_scaled, cmap='gray')
plt.title('Log Transform')
plt.axis('off')

# Automatically adjust subplot layout
plt.tight_layout()
plt.show()

# Call the main function when script is executed
if __name__ == "__main__":
    main()
