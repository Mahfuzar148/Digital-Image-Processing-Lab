
---

# 🖥️ Full Python Code

```python
import cv2
import matplotlib.pyplot as plt

def main():
    #================= Load the images =====================================
    img1 = cv2.cvtColor(cv2.imread("path/to/image1.png"), cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(cv2.imread("path/to/image2.png"), cv2.COLOR_BGR2RGB)

    #================= Resize the second image to match the first ==========
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    #================= Add the images together ============================
    result = cv2.add(img1, img2)

    #================= Display the images =================================
    plt.figure(figsize=(12, 6)) 
    titles = ['Image 1', 'Image 2', 'Added Image']
    images = [img1, img2, result]

    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

---

# 📘 Theory Behind the Code

### 1. Image as a Matrix

* A **RGB image** is stored as a **3D NumPy array**:

  * Dimensions: `(height × width × 3)`
  * Each channel (R, G, B) has intensity values from **0 to 255**.

### 2. Image Addition

* When adding two images, we combine the pixel values from both images:

$$
g(x, y, c) = f_1(x, y, c) + f_2(x, y, c)
$$

* Here:

  * `f1(x,y,c)` → pixel value from image1 at `(x,y)` in channel `c`.
  * `f2(x,y,c)` → pixel value from image2.
  * `g(x,y,c)` → resulting pixel value.

* Example:

  * If pixel from `img1` = 100, and pixel from `img2` = 150,
  * Result = `250`.
  * If the sum exceeds 255, **OpenCV clips it to 255** (saturation).

### 3. Why Resize?

* For **pixel-wise addition**, both images must be the same size (same height, width, and channels).
* Otherwise, OpenCV will throw an error.
* That’s why `cv2.resize()` is used to match dimensions.

### 4. Visualization

* Matplotlib is used to **display images** in RGB format.
* Since OpenCV loads images in **BGR format**, we convert them to **RGB** using `cv2.cvtColor()` for correct display.

---

# 📜 Code Explanation (Line by Line)

```python
import cv2
import matplotlib.pyplot as plt
```

* Importing required libraries:

  * `cv2` for image processing.
  * `matplotlib.pyplot` for visualization.

---

```python
def main():
    #================= Load the images =====================================
    img1 = cv2.cvtColor(cv2.imread("path/to/image1.png"), cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(cv2.imread("path/to/image2.png"), cv2.COLOR_BGR2RGB)
```

* `cv2.imread()` loads the images (default format: **BGR**).
* `cv2.cvtColor(..., cv2.COLOR_BGR2RGB)` converts them to **RGB** for proper display.

---

```python
    #================= Resize the second image to match the first ==========
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
```

* `cv2.resize()` resizes `img2` to match dimensions of `img1`:

  * `(width, height)` = `(img1.shape[1], img1.shape[0])`.

---

```python
    #================= Add the images together ============================
    result = cv2.add(img1, img2)
```

* Adds corresponding pixel values from `img1` and `img2`.
* If result > 255 → clipped to 255.

---

```python
    #================= Display the images =================================
    plt.figure(figsize=(12, 6)) 
    titles = ['Image 1', 'Image 2', 'Added Image']
    images = [img1, img2, result]
```

* Creates a figure for display.
* Stores image titles and images in lists.

---

```python
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
```

* Loops through the three images.
* `plt.subplot(1, 3, i+1)` → arranges them in **1 row, 3 columns**.
* Displays each image with its title.

---

```python
    plt.tight_layout()
    plt.show()
```

* `tight_layout()` adjusts spacing.
* `plt.show()` displays all three images.

---

# 🎯 Summary

* **Theory**: Two RGB images are added pixel-by-pixel → results in a brighter combined image.
* **Code**:

  * Load both images.
  * Resize one to match the other.
  * Add them using `cv2.add()`.
  * Display original and result images with Matplotlib.

---

