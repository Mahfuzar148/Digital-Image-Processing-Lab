

---

## 📝 **Question:**

### 📌 **Problem Statement:**

Write a Python program that:

1. Loads a 4D image using `matplotlib`
2. Converts the image to 3D by removing the alpha (transparency) channel
3. Prints specific pixel values from red, green, and blue channels
4. Prints the minimum and maximum pixel values
5. Displays the image using `matplotlib`

---

## ✅ **Python Code:**

```python
''' 
Problem Statement: 
Given an image, this script loads the image, converts it from 4D to 3D, prints some pixel values,
and displays the image using matplotlib.
'''

import matplotlib.pyplot as plt

def main():
    #=================   Load the image ======================
    img_path = '/home/4_1/cse4161/images/rgb.png'
    img_4D = plt.imread(img_path)
    print(img_4D.shape)

    #================= Convert to 3D from 4D ======================
    img_3D = img_4D[:, :, :3]
    print(img_3D.shape)

    #================= Print some values of images ======================
    print(img_3D[:5, :5, 0])  # Print first 5x5 pixels of the red channel
    print(img_3D[:5, :5, 1])  # Print first 5x5 pixels of the green channel
    print(img_3D[:5, :5, 2])  # Print first 5x5 pixels of the blue channel
    print(img_3D.max(), img_3D.min())  # Print max and min values of the image

    #================= display the image ======================
    plt.imshow(img_3D)
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()
```

---

## 📄 **Documentation / Explanation**

---

### 🔹 **1. Load the Image**

```python
img_path = '/home/4_1/cse4161/images/rgb.png'
img_4D = plt.imread(img_path)
print(img_4D.shape)
```

* Uses `matplotlib.pyplot.imread()` to load the image.
* The loaded image is likely in **4D (RGBA)** format: 4th channel = Alpha (transparency).
* `img_4D.shape` prints the dimensions, e.g., `(height, width, 4)`.

---

### 🔹 **2. Convert from 4D to 3D**

```python
img_3D = img_4D[:, :, :3]
print(img_3D.shape)
```

* Removes the **alpha channel** by slicing only the first 3 channels (RGB).
* Now `img_3D` has shape: `(height, width, 3)` — standard RGB image.

---

### 🔹 **3. Print Some Pixel Values**

```python
print(img_3D[:5, :5, 0])  # Red channel
print(img_3D[:5, :5, 1])  # Green channel
print(img_3D[:5, :5, 2])  # Blue channel
print(img_3D.max(), img_3D.min())
```

* Prints **first 5×5 pixels** of each color channel (R, G, B) separately.
* Helpful for analyzing pixel intensity.
* `img_3D.max()` and `img_3D.min()` show the range of values (often in 0.0–1.0 for floats).

---

### 🔹 **4. Display the Image**

```python
plt.imshow(img_3D)
plt.show()
plt.close()
```

* Displays the RGB image using `matplotlib`.
* `plt.close()` is good practice to close the figure after display.

---

## ✅ **Output Summary**

| Section           | Output Example                      |
| ----------------- | ----------------------------------- |
| Image Shape (4D)  | `(256, 256, 4)`                     |
| Image Shape (3D)  | `(256, 256, 3)`                     |
| Pixel Values      | 5×5 matrix of float/int values      |
| Max/Min Intensity | e.g., `1.0 0.0`                     |
| Image Display     | Shows RGB image without alpha layer |

---
