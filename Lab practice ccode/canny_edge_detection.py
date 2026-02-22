import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread('image.png')

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Step 3: Apply Gaussian Blur (Noise Reduction)
# blur = cv2.GaussianBlur(gray, (5,5), 1.4)

# # Step 4: Apply Canny Edge Detection
# edges = cv2.Canny(blur, 100, 200)

blur = cv2.GaussianBlur(gray, (5,5), 1.4)

# ---- 5️⃣ Canny edge detection ----
edges = cv2.Canny(blur, 50, 150)


# Step 5: Display the results using matplotlib
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Canny Edge Detection")
plt.imshow(edges, cmap='gray')
plt.axis("off")

plt.show()