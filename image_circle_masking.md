
---

## 📝 **Problem Statement**

Write a Python program that:

* Loads an RGB image
* Applies a **circular mask** to it by setting pixels inside a circle to black
* Displays the modified image using `matplotlib`

---

## ✅ **Python Code**

```python
import matplotlib.pyplot as plt
import cv2
import numpy as np

def main():
    # Load the image
    img_3D = cv2.imread("F:/6TH SEMISTER/Python Code/img1.png")

    # Create a circular mask on the image
    center = (img_3D.shape[1] // 2, img_3D.shape[0] // 2)  # (x, y) center of image
    radius = 100  # radius of the circle
    color = (0, 0, 0)  # black
    thickness = -1  # fill the circle

    # Draw filled circle directly on the image (in-place)
    cv2.circle(img_3D, center, radius, color, thickness)

    # Convert to RGB for matplotlib
    img_rgb = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)

    # Show image
    plt.imshow(img_rgb)
    plt.title('Image with Circular Mask')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
```

---

## 📄 **Documentation / Explanation**

---

### 🔹 1. **Importing Libraries**

```python
import matplotlib.pyplot as plt
import cv2
import numpy as np
```

* `cv2` → OpenCV library for image reading and drawing
* `matplotlib.pyplot` → for displaying images
* `numpy` → used for general-purpose array operations (though not needed directly here, it's commonly included)

---

### 🔹 2. **Reading the Image**

```python
img_3D = cv2.imread("F:/6TH SEMISTER/Python Code/img1.png")
```

* Reads the image from the specified path using OpenCV
* Returns a 3D NumPy array in **BGR format**

---

### 🔹 3. **Defining the Circular Mask**

```python
center = (img_3D.shape[1] // 2, img_3D.shape[0] // 2)
radius = 100
color = (0, 0, 0)
thickness = -1
```

| Parameter        | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| `center`         | Coordinates of the circle center (image midpoint)    |
| `radius`         | Radius of the circle (in pixels)                     |
| `color`          | Color `(0, 0, 0)` = black (in BGR)                   |
| `thickness = -1` | Fills the circle instead of drawing just the outline |

---

### 🔹 4. **Applying the Mask**

```python
cv2.circle(img_3D, center, radius, color, thickness)
```

* Draws a **filled black circle** directly on the image (modifies `img_3D` in-place)
* All pixels inside the circle are set to black

---

### 🔹 5. **Converting to RGB**

```python
img_rgb = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)
```

* Converts the image to **RGB format** for correct color display using `matplotlib`

---

### 🔹 6. **Displaying the Result**

```python
plt.imshow(img_rgb)
plt.title('Image with Circular Mask')
plt.axis('off')
plt.show()
```

* Displays the final image without axes or grid lines
* `imshow()` renders the image
* `axis('off')` hides the X and Y axes for a cleaner view

---

## ✅ **Output Description**

* The image is displayed with a **black circular region** at the center
* The rest of the image remains unchanged

---

## 🧠 Additional Notes:

* You can change the `center`, `radius`, or `color` to experiment with different masking effects
* To **mask only a specific channel** (like red or green), use:

  ```python
  cv2.circle(img_3D[:, :, 2], center, radius, 0, thickness)  # mask red channel only
  ```

---


