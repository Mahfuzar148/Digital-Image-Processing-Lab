
---

# 📘 Theory Behind the Transformation

### 1. Image as a 3D Matrix

* A digital **RGB image** can be thought of as a 3D matrix:

  * Dimensions: `(height × width × 3)`
  * 3 channels correspond to **Red (R)**, **Green (G)**, and **Blue (B)** intensities.
  * Each pixel value is usually in the range `[0, 255]`.

### 2. Transformation Function

The given transformation is:

$$
g(x, y, c) = f(x, y, c) + \text{constant}
$$

* `f(x, y, c)` → original pixel intensity at position `(x, y)` and channel `c`.
* `constant = 10 (or 50 in your code)` → the amount we want to brighten the image by.
* `g(x, y, c)` → new pixel intensity after transformation.

### 3. Effect of Adding Constant

* Adding a positive constant **brightens the image** (all pixel values increase).
* If values exceed **255**, they get **saturated (clipped to 255)**, so the image doesn’t overflow.
* In OpenCV, `cv2.add()` automatically handles this **saturation arithmetic** (instead of wrapping around like NumPy addition).

---

# 📜 Code Explanation (Step by Step)

```python
import matplotlib.pyplot as plt
import cv2
```

* **matplotlib.pyplot** → used to display images.
* **cv2 (OpenCV)** → used for image processing.

---

```python
def main():
    #===================== Load the image =========================
    img_path = "/home/mohon/4_1/cse4161/images/rgb_flower1.png"
    img_3D = cv2.imread(img_path)    
    img_rgb = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)
    constant = 50
```

* `cv2.imread(img_path)` → loads the image (default format: **BGR**).
* `cv2.cvtColor(..., cv2.COLOR_BGR2RGB)` → converts BGR to **RGB** (so colors display correctly in matplotlib).
* `constant = 50` → defines how much to brighten the image.

---

```python
    #===================== Apply transformation =========================  
    img_rgb_transformed = cv2.add(img_rgb, constant)
```

* `cv2.add(img_rgb, constant)` → adds `50` to each pixel value in each channel.
* Handles **saturation at 255**, ensuring valid pixel values.

---

```python
    #===================== Display the images =========================
    plt.figure(figsize=(10, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(img_rgb)
    plt.title('Original RGB Image') 

    plt.subplot(2, 2, 2)
    plt.imshow(img_rgb_transformed)
    plt.title('Transformed RGB Image')
    
    plt.tight_layout()
    plt.show()
    plt.close()
```

* Creates a **2×2 subplot** (only 2 slots used).
* Shows:

  * **Original Image** (before transformation).
  * **Transformed Image** (brightened).
* `plt.tight_layout()` → adjusts spacing between subplots.
* `plt.show()` → displays the window with images.
* `plt.close()` → closes the figure after displaying.

---

# 🎯 Summary

* **Theory**: The operation adds a constant brightness to all pixels → brighter image.
* **Code**:

  * Loads RGB image.
  * Converts from BGR to RGB.
  * Uses `cv2.add()` for pixel-wise brightness increase.
  * Displays original vs. transformed images.

---

