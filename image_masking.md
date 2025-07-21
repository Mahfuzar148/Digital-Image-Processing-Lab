
---

## 📝 **Problem Statement**

> Write a Python program to perform **image masking** on a 3D image (RGB).
> That is: set a **specific region** of the image (a square area) to **zero (black)**.

---

## ✅ **Code Summary**

```python
import matplotlib.pyplot as plt
import cv2

def main():
    img_3D = cv2.imread("F:/6TH SEMISTER/Python Code/img2.png")

    masking_area = 1000
    img_3D[:masking_area, :masking_area] = 0    

    img_3D = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)
    plt.imshow(img_3D)
    plt.title('Modified Image')
    plt.show()

if __name__ == "__main__":
    main()
```

---

## 📄 **Line-by-Line Explanation**

---

### 🔹 1. **Importing Required Libraries**

```python
import matplotlib.pyplot as plt
import cv2
```

* `cv2`: For image reading and processing.
* `matplotlib.pyplot`: For displaying the image.

---

### 🔹 2. **Reading the Image**

```python
img_3D = cv2.imread("/home/mohon/4_1/cse4161/images/rgb_flower.png")
```

* Reads the image using OpenCV in **BGR format**.
* Resulting shape: `(height, width, 3)` → a **3D array** (RGB image).

---

### 🔹 3. **Masking a Region**

```python
masking_area = 1000
img_3D[:masking_area, :masking_area] = 0
```

This does:

* Selects a **square region** starting from the top-left corner:

  $$
  \text{Rows: } 0 \text{ to } 999,\quad \text{Columns: } 0 \text{ to } 999
  $$
* Sets **all 3 channels (R, G, B)** to 0 in that region.
* Result: a **black square mask** applied to the top-left portion of the image.

> ⚠️ If the image is smaller than 1000×1000, this may mask beyond the actual size, so resizing/safety check may be needed.

---

### 🔹 4. **Convert BGR to RGB for Display**

```python
img_3D = cv2.cvtColor(img_3D, cv2.COLOR_BGR2RGB)
```

* OpenCV uses BGR format, but `matplotlib` expects RGB.
* This ensures correct color display when plotting.

---

### 🔹 5. **Displaying the Result**

```python
plt.imshow(img_3D)
plt.title('Modified Image')
plt.show()
```

* Shows the masked image with a **black square** in the corner.
* No axes or grid shown by default.

---

## ✅ **Visual Summary**

| Operation        | Effect                                    |
| ---------------- | ----------------------------------------- |
| Load image       | Reads color image in BGR                  |
| Masking          | Sets top-left `1000×1000` pixels to black |
| Color conversion | BGR → RGB for display                     |
| Display          | Shows modified image using `matplotlib`   |

---

## 🧠 Notes:

* You can change the shape of the masked area like:

  ```python
  img_3D[200:400, 300:500] = 0  # Rectangular region
  ```

---


