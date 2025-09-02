

---

## 📝 **Problem Statement**

Write a Python script that:

* Loads an RGB image.
* Applies the transformation:

  $$
  g(x, y, c) = f(x, y, c) + \text{constant}
  $$

  where `constant = 100` and `f(x, y, c)` is the original image value at pixel location `(x, y)` for channel `c`.
* Displays both the original and the transformed image using `matplotlib`.

---

## ✅ **Python Code**

```python

import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    #===================== Load the image =========================
    img_path = "/home/mohon/4_1/cse4161/images/rgb_flower1.png"
    img_3D = cv2.imread(img_path)    
    img_rgb = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)
    constant = 50

    #===================== Apply transformation =========================  
    # constant-এর মতো shape এর array বানাতে হবে
    M = np.full(img_rgb.shape, constant, dtype=np.uint8)
    img_rgb_transformed = cv2.add(img_rgb, M)   # safe addition (saturation at 255)

    #===================== Display the images =========================
    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title('Original RGB Image') 

    plt.subplot(1, 2, 2)
    plt.imshow(img_rgb_transformed)
    plt.title('Transformed RGB Image')
    
    plt.tight_layout()
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()

```

---

## 📄 **Documentation / Explanation**

---

### 🔹 1. **Image Loading**

```python
img_3D = cv2.imread(img_path)
img_rgb = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)
```

* Loads the image in **BGR format** (OpenCV default).
* Converts it to **RGB format** so `matplotlib` can display it correctly.

---

### 🔹 2. **Pixel-wise Transformation**

```python
img_rgb_transformed = cv2.add(img_rgb, constant)
```

* Applies the transformation:

  $$
  g(x, y, c) = f(x, y, c) + 100
  $$
* `cv2.add()` performs **saturated addition**:

  * If `f(x, y, c) + 100 > 255`, result is **clipped to 255**.
* Ensures pixel values stay within the valid range `[0, 255]`.

---

### 🔹 3. **Display with `matplotlib`**

```python
plt.subplot(...)
plt.imshow(...)
plt.title(...)
plt.axis('off')
```

| Plot Panel | Content                           |
| ---------- | --------------------------------- |
| (1,1)      | Original RGB image                |
| (1,2)      | Brightened image (+100 to pixels) |

* `plt.axis('off')` removes axis ticks for a cleaner display.
* `plt.tight_layout()` adjusts spacing between subplots to avoid overlap.

---

### 🧠 Additional Notes

* This operation is often used in **brightness enhancement**.
* Works on **color images** (RGB) and can also be extended to **grayscale**.
* If you use `img + constant` instead of `cv2.add()`, it may cause **overflow** (wrap-around) — OpenCV avoids this.

---

## ✅ Summary

| Task                       | Done? |
| -------------------------- | ----- |
| Load and convert image     | ✅     |
| Add constant brightness    | ✅     |
| Use OpenCV safe arithmetic | ✅     |
| Visualize results          | ✅     |


