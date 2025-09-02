
1. **Full working code (already correct, just structured in function style)**
2. **Theory explanation (what actually happens in addition, subtraction, multiplication, division of images)**
3. **Code explanation line by line**

---

# ✅ Full Code

```python
import cv2
import matplotlib.pyplot as plt

def main():
    #================ Load the images ================================================================
    img1 = cv2.cvtColor(cv2.imread("/home/mohon/4_1/cse4161/images/rgb_flower.png"), cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(cv2.imread("/home/mohon/4_1/cse4161/images/rgb_flower1.png"), cv2.COLOR_BGR2RGB)

    #================ Resize the second image to match the first image dimensions ====================
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    #cv.resize(img_source, (new_width, new_height))

    #================ Perform arithmetic operations on the images ==================================
    added      = cv2.add(img1, img2)         # Saturation arithmetic
    subtracted = cv2.subtract(img1, img2)    # No negative values (clipped at 0)
    multiplied = cv2.multiply(img1, img2)    # Scaled product
    divided    = cv2.divide(img1, img2)      # Pixel-wise division

    #================ Display the original and resulting images ====================================
    titles = ['Image 1', 'Image 2', 'Addition', 'Subtraction', 'Multiplication', 'Division']
    images = [img1, img2, added, subtracted, multiplied, divided]

    plt.figure(figsize=(12, 8))
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
```

---

# 📘 Theory Explanation

### 1. Image as a Matrix

* An image is a **NumPy array**:

  * Shape: `(height, width, channels)`
  * Each pixel = `[R, G, B]` intensity (0–255).

### 2. Arithmetic Operations

#### ➤ **Addition (`cv2.add`)**

$$
g(x, y, c) = f_1(x, y, c) + f_2(x, y, c)
$$

* Pixel values are added channel-wise.
* If result > 255 → clipped to 255 (saturation).
* Produces a brighter/combined image.

#### ➤ **Subtraction (`cv2.subtract`)**

$$
g(x, y, c) = f_1(x, y, c) - f_2(x, y, c)
$$

* If result < 0 → clipped to 0.
* Highlights the **differences** between two images.

#### ➤ **Multiplication (`cv2.multiply`)**

$$
g(x, y, c) = f_1(x, y, c) \times f_2(x, y, c)
$$

* Each pixel multiplied by the corresponding pixel.
* Values are scaled down to 0–255 range internally.
* Useful for masking or blending effects.

#### ➤ **Division (`cv2.divide`)**

$$
g(x, y, c) = \frac{f_1(x, y, c)}{f_2(x, y, c)}
$$

* Division is pixel-wise.
* If denominator is 0 → safely handled (avoids crash).
* Produces normalized contrast-like effects.

---

# 📜 Code Explanation

```python
img1 = cv2.cvtColor(cv2.imread("..."), cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread("..."), cv2.COLOR_BGR2RGB)
```

* Loads the two RGB images (OpenCV loads as BGR by default → converted to RGB for matplotlib).

---

```python
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
```

* Ensures both images are the same size (required for pixel-wise arithmetic).
* Remember: `cv2.resize(img, (width, height))`.

---

```python
added      = cv2.add(img1, img2)
subtracted = cv2.subtract(img1, img2)
multiplied = cv2.multiply(img1, img2)
divided    = cv2.divide(img1, img2)
```

* Performs the 4 arithmetic operations pixel by pixel.

---

```python
plt.subplot(2, 3, i+1)
plt.imshow(images[i])
plt.title(titles[i])
```

* Displays all **original + processed images** in a 2×3 grid.

---

# 🎯 Summary

* **Addition** → brighter, merged effect.
* **Subtraction** → shows differences (useful in motion detection, change detection).
* **Multiplication** → pixel scaling, blending.
* **Division** → normalization, contrast adjustment.

---

