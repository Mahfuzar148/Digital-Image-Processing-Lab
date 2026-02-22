import cv2
import matplotlib.pyplot as plt
import numpy as np

# ======================
# Read input image in Grayscale
# ======================
img_gray = cv2.imread("flower_img.png", cv2.IMREAD_GRAYSCALE)

if img_gray is None:
    print("Image not found!")
    exit()

# ======================
# 1. Smoothing / Average Filter
# ======================
kernel_avg = np.ones((3,3), np.float32) / 9
smooth = cv2.filter2D(img_gray, cv2.CV_64F, kernel_avg)

# ======================
# 2. Sobel Filters
# ======================
sobel_x_kernel = np.array([[-1,0,1],
                           [-2,0,2],
                           [-1,0,1]], dtype=np.float32)

sobel_y_kernel = np.array([[-1,-2,-1],
                           [ 0, 0, 0],
                           [ 1, 2, 1]], dtype=np.float32)

sobel_x = cv2.filter2D(img_gray, cv2.CV_64F, sobel_x_kernel)
sobel_y = cv2.filter2D(img_gray, cv2.CV_64F, sobel_y_kernel)

# ======================
# 3. Prewitt Filters
# ======================
prewitt_x_kernel = np.array([[-1,0,1],
                             [-1,0,1],
                             [-1,0,1]], dtype=np.float32)

prewitt_y_kernel = np.array([[-1,-1,-1],
                             [ 0, 0, 0],
                             [ 1, 1, 1]], dtype=np.float32)

prewitt_x = cv2.filter2D(img_gray, cv2.CV_64F, prewitt_x_kernel)
prewitt_y = cv2.filter2D(img_gray, cv2.CV_64F, prewitt_y_kernel)

# ======================
# 4. Laplacian Filter
# ======================
laplacian_kernel = np.array([[0,-1,0],
                             [-1,4,-1],
                             [0,-1,0]], dtype=np.float32)

laplacian = cv2.filter2D(img_gray, cv2.CV_64F, laplacian_kernel)

# ======================
# Convert to absolute and normalize for display
# ======================
def normalize(img):
    img = np.abs(img)
    img = (img / np.max(img)) * 255
    return img.astype(np.uint8)

smooth = normalize(smooth)
sobel_x = normalize(sobel_x)
sobel_y = normalize(sobel_y)
prewitt_x = normalize(prewitt_x)
prewitt_y = normalize(prewitt_y)
laplacian = normalize(laplacian)

# ======================
# Plotting results
# ======================
titles = ["Original", "Smoothing",
          "Sobel X", "Sobel Y",
          "Prewitt X", "Prewitt Y",
          "Laplacian"]

images = [img_gray, smooth,
          sobel_x, sobel_y,
          prewitt_x, prewitt_y,
          laplacian]

plt.figure(figsize=(14, 8))

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()