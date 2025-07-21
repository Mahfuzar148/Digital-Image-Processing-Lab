

## 🏷️ **Topic: Image Arithmetic Operations (Add, Subtract, Multiply, Divide) with OpenCV and Matplotlib**

---

### ✅ **Full Python Code**

```python
import cv2
import matplotlib.pyplot as plt

# Step 1: Load two images
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')

# Step 2: Resize second image to match the size of the first (if needed)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Step 3: Perform image arithmetic operations
added = cv2.add(img1, img2)             # Addition
subtracted = cv2.subtract(img1, img2)   # Subtraction
multiplied = cv2.multiply(img1, img2)   # Multiplication
divided = cv2.divide(img1, img2)        # Division

# Step 4: Convert all BGR images to RGB for correct display with matplotlib
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
added_rgb = cv2.cvtColor(added, cv2.COLOR_BGR2RGB)
subtracted_rgb = cv2.cvtColor(subtracted, cv2.COLOR_BGR2RGB)
multiplied_rgb = cv2.cvtColor(multiplied, cv2.COLOR_BGR2RGB)
divided_rgb = cv2.cvtColor(divided, cv2.COLOR_BGR2RGB)

# Step 5: Plot all images
plt.figure(figsize=(12, 8))

# Original Images
plt.subplot(2, 3, 1)
plt.imshow(img1_rgb)
plt.title('Image 1')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(img2_rgb)
plt.title('Image 2')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(divided_rgb)
plt.title('Divided Image')
plt.axis('off')

# Arithmetic Results
plt.subplot(2, 3, 4)
plt.imshow(added_rgb)
plt.title('Added Image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(subtracted_rgb)
plt.title('Subtracted Image')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(multiplied_rgb)
plt.title('Multiplied Image')
plt.axis('off')

# Layout adjustment
plt.tight_layout()
plt.show()
```

---

## 📄 **Documentation / Explanation**

---

### 🔹 **Step 1: Load Two Images**

```python
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
```

* Loads two images from disk using OpenCV.
* `cv2.imread()` loads images in **BGR format by default**.
* Ensure that both images exist in the same directory or provide full path.

---

### 🔹 **Step 2: Resize `img2` to Match `img1`**

```python
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
```

* Ensures both images are of the **same width and height** so arithmetic operations are valid.
* `img1.shape[1]` = width, `img1.shape[0]` = height.

---

### 🔹 **Step 3: Arithmetic Operations**

```python
cv2.add(img1, img2)
cv2.subtract(img1, img2)
cv2.multiply(img1, img2)
cv2.divide(img1, img2)
```

* Performs **element-wise (pixel by pixel)** operations.
* Pixel values are **clipped** to valid range (0–255).
* `cv2.divide()` handles division safely by avoiding divide-by-zero errors internally.

---

### 🔹 **Step 4: Convert BGR to RGB**

```python
cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

* Converts each BGR image to RGB format so `matplotlib` displays them correctly.
* If skipped, colors will look distorted (e.g., red appears blue).

---

### 🔹 **Step 5: Plotting with Matplotlib**

```python
plt.subplot(2, 3, position)
plt.imshow(image)
plt.title('Label')
plt.axis('off')
```

* Displays all images in a **2-row, 3-column grid**.
* `.axis('off')` hides axis ticks for a cleaner look.
* `.tight_layout()` ensures labels/titles don’t overlap.

---

## ✅ **Image Grid Layout**

| Row | Column 1    | Column 2   | Column 3      |
| --- | ----------- | ---------- | ------------- |
| 1   | Image 1     | Image 2    | Divided Image |
| 2   | Added Image | Subtracted | Multiplied    |

---

## ⚠️ Additional Notes

* If `img2` contains black (pixel value 0), **division may produce high values or artifacts**.
* For better control, you can normalize results or clip manually using NumPy.
* You can add save functionality like:

  ```python
  cv2.imwrite('added.png', added)
  ```

---

