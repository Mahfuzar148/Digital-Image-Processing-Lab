
---

## ✅ Full Code

```python
"""
Problem Statement:
Given an image, this script loads the image, converts it from 4D (RGBA) to 3D (RGB),
prints some pixel values, and displays the image using matplotlib.
"""

import matplotlib.pyplot as plt


def main():
    #=================   Load the image ======================
    img_path = '/home/mohon/4_1/cse4161/images/rgb.png'
    img_4D = plt.imread(img_path)
    print("Original image shape (with alpha channel):", img_4D.shape)

    #================= Convert to 3D from 4D ======================
    img_3D = img_4D[:, :, :3]   # keep only R,G,B channels, drop Alpha
    print("Converted image shape (RGB only):", img_3D.shape)

    #================= Print some values of images ======================
    print("\nFirst 5x5 pixels of RED channel:")
    print(img_3D[:5, :5, 0])  # Red channel values

    print("\nFirst 5x5 pixels of GREEN channel:")
    print(img_3D[:5, :5, 1])  # Green channel values

    print("\nFirst 5x5 pixels of BLUE channel:")
    print(img_3D[:5, :5, 2])  # Blue channel values

    print("\nMaximum pixel value:", img_3D.max())
    print("Minimum pixel value:", img_3D.min())

    #================= Display the image ======================
    plt.imshow(img_3D)
    plt.title("RGB Image (without Alpha Channel)")
    plt.axis("off")  # hide axes for better visualization
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
```

---

## 📝 Explanation

### 1. Import

```python
import matplotlib.pyplot as plt
```

* `matplotlib.pyplot` is used for image reading, displaying, and visualization.

---

### 2. Load Image

```python
img_path = '/home/mohon/4_1/cse4161/images/rgb.png'
img_4D = plt.imread(img_path)
print(img_4D.shape)
```

* Loads the PNG image into a NumPy array.
* PNG usually has **4 channels (RGBA)** → Red, Green, Blue, Alpha (transparency).
* Shape will look like `(height, width, 4)`.

---

### 3. Convert to 3D (Drop Alpha)

```python
img_3D = img_4D[:, :, :3]
print(img_3D.shape)
```

* Keeps only the **RGB channels** and removes the alpha channel.
* Shape becomes `(height, width, 3)`.

---

### 4. Print Pixel Values

```python
print(img_3D[:5, :5, 0])  # Red
print(img_3D[:5, :5, 1])  # Green
print(img_3D[:5, :5, 2])  # Blue
```

* Prints the **first 5×5 pixel values** of each color channel separately.

```python
print(img_3D.max(), img_3D.min())
```

* Prints the maximum and minimum intensity values of the image.
* If the image is normalized → values between **0.0 and 1.0**.
* If not normalized → values between **0 and 255**.

---

### 5. Display Image

```python
plt.imshow(img_3D)
plt.title("RGB Image (without Alpha Channel)")
plt.axis("off")
plt.show()
plt.close()
```

* Shows the image with only RGB channels.
* Removes axes for a cleaner view.
* Closes the figure after showing.

---

👉 In short:

* Load **RGBA image** → Convert to **RGB** → Print pixel values → Display the image.

---


