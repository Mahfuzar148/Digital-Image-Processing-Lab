

---

## 🏷️ **Topic: Image Processing and Visualization using OpenCV and Matplotlib**

---

### ✅ **Full Python Code:**

```python
import cv2
import matplotlib.pyplot as plt

# Load the image in BGR format (default OpenCV behavior)
img1 = cv2.imread('img1.png')

# Convert original image to RGB for correct color display in matplotlib
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# Convert BGR to Grayscale
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur with an odd kernel size
blurImg = cv2.GaussianBlur(grayImg, (51, 51), 0)

# Plotting
plt.figure(figsize=(10, 5))  # Set figure size in inches

# 1. Original image (in RGB format)
plt.subplot(2, 2, 1)
plt.imshow(img1_rgb)
plt.title('Original Image')
plt.axis('off')

# 2. Grayscale image
plt.subplot(2, 2, 2)
plt.imshow(grayImg, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

# 3. Blurred grayscale image
plt.subplot(2, 2, 3)
plt.imshow(blurImg, cmap='gray')
plt.title('Blurred Image')
plt.axis('off')

# Adjust layout to prevent overlapping titles
plt.tight_layout()

# Display all plots
plt.show()
```

---

### 📄 **Documentation / Explanation**

#### 📌 **1. Importing Libraries**

```python
import cv2
import matplotlib.pyplot as plt
```

* `cv2`: OpenCV library for image reading, color conversion, and blurring.
* `matplotlib.pyplot`: Used for plotting and displaying images inline.

---

#### 📌 **2. Loading the Image**

```python
img1 = cv2.imread('img1.png')
```

* Reads the image in **BGR format** (OpenCV default).
* Make sure `'img1.png'` is in the same folder as your script or provide a full path.

---

#### 📌 **3. BGR to RGB Conversion**

```python
img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
```

* Converts the BGR image to **RGB** for accurate display in `matplotlib`.
* If skipped, colors will appear incorrectly (e.g., blue instead of red).

---

#### 📌 **4. Grayscale Conversion**

```python
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
```

* Converts the image to **grayscale** — only one channel, pixel intensity from 0 (black) to 255 (white).

---

#### 📌 **5. Applying Gaussian Blur**

```python
blurImg = cv2.GaussianBlur(grayImg, (51, 51), 0)
```

* Blurs the grayscale image using a **Gaussian kernel**.
* `(51, 51)` is the kernel size — must be **odd**.
* Larger values → stronger blur.

---

#### 📌 **6. Plotting the Images**

```python
plt.figure(figsize=(10, 5))
```

* Creates a new figure for plotting.
* `figsize` sets the display size in inches (10×5 inches).

---

#### 📌 **7. Display Each Image in a Grid**

```python
plt.subplot(2, 2, 1)
...
plt.subplot(2, 2, 2)
...
plt.subplot(2, 2, 3)
```

* Arranges images in a **2×2 grid**.
* Positions images in **1st, 2nd, and 3rd spots**.

#### 🖼️ `imshow()` + `axis('off')`

```python
plt.imshow(image, cmap='gray') 
plt.axis('off')
```

* `imshow()` displays an image.
* `cmap='gray'` shows grayscale images correctly.
* `axis('off')` removes axes and ticks for a cleaner view.

---

#### 📌 **8. Layout Adjustment**

```python
plt.tight_layout()
```

* Automatically adjusts subplot spacing to **avoid overlapping** of titles and images.

---

#### 📌 **9. Final Display**

```python
plt.show()
```

* Renders the full figure with all subplots displayed.

---

### ✅ **Summary of Output**

| Image Panel       | Description             |
| ----------------- | ----------------------- |
| Top-left (1,1)    | Original RGB image      |
| Top-right (1,2)   | Grayscale version       |
| Bottom-left (2,1) | Blurred grayscale image |

---


