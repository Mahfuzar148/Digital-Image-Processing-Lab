

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

---

## 📌 **Problem Statement**

Write a Python program that:

1. Loads an image with an alpha (transparency) channel (4D),
2. Converts it to a standard RGB image (3D),
3. Extracts and displays the individual red, green, and blue channel values from the top-left 5×5 region,
4. Visualizes the original and extracted image data using `matplotlib`.

---

## ✅ **Full Python Code**

```python
import cv2
import matplotlib.pyplot as plt

def main():
   # Load the image
   img_4d = plt.imread('img1.png')
   print(img_4d.shape)
   
   img_3d = img_4d[:,:,:3]
   print(img_3d.shape)
   
   print(img_3d.max(), img_3d.min())
   
   red_img = img_3d[:5,:5,0]
   green_img = img_3d[:5,:5,1]
   blue_img = img_3d[:5,:5,2]
   
   plt.figure(figsize=(16,10))
   
   plt.subplot(3,2,1)
   plt.imshow(img_4d)
   plt.title('4D Image')
   plt.axis('off')
   
   plt.subplot(3,2,2)
   plt.imshow(img_3d)
   plt.title('3D Image')
   plt.axis('off')
   
   plt.subplot(3,2,3)
   plt.imshow(red_img, cmap='Reds')
   plt.title('Red Channel')
   plt.axis('off')
   
   plt.subplot(3,2,4)
   plt.imshow(green_img, cmap='Greens')
   plt.title('Green Channel')
   plt.axis('off')
   
   plt.subplot(3,2,5)
   plt.imshow(blue_img, cmap='Blues')
   plt.title('Blue Channel')
   plt.axis('off')
   
   plt.tight_layout()
   plt.show()

if __name__ =="__main__":
    main()
```

---

## 📄 **Documentation / Explanation**

---

### 🔹 1. **Image Loading**

```python
img_4d = plt.imread('img1.png')
```

* Loads an RGBA image (4 channels: Red, Green, Blue, Alpha).
* Image shape will be: `(height, width, 4)`.

---

### 🔹 2. **Conversion from 4D to 3D**

```python
img_3d = img_4d[:, :, :3]
```

* Removes the alpha (transparency) channel.
* Converts it to a 3D RGB image: `(height, width, 3)`.

---

### 🔹 3. **Print Image Details**

```python
print(img_4d.shape)
print(img_3d.shape)
print(img_3d.max(), img_3d.min())
```

* Displays shapes before and after conversion.
* Prints max/min pixel values — typically in range `0.0` to `1.0` for floating-point images.

---

### 🔹 4. **Extract Color Channels**

```python
red_img = img_3d[:5, :5, 0]
green_img = img_3d[:5, :5, 1]
blue_img = img_3d[:5, :5, 2]
```

* Extracts the top-left **5×5 pixel** block from each channel.
* These matrices represent **pixel intensities** for red, green, and blue colors.

---

### 🔹 5. **Image Display Using `matplotlib`**

```python
plt.subplot(...)
plt.imshow(..., cmap='Reds' / 'Greens' / 'Blues')
```

| Subplot Position | Image Content       | Colormap |
| ---------------- | ------------------- | -------- |
| (3,2,1)          | Original 4D image   | RGBA     |
| (3,2,2)          | Converted 3D image  | RGB      |
| (3,2,3)          | Red channel (5x5)   | `Reds`   |
| (3,2,4)          | Green channel (5x5) | `Greens` |
| (3,2,5)          | Blue channel (5x5)  | `Blues`  |

* `axis('off')`: removes axes for clean visualization.
* `tight_layout()`: avoids overlapping titles or plots.

---

### ✅ Summary of Output

* **Displays original image with alpha (if present)**
* **Displays RGB version of the image**
* **Shows red, green, blue components of top-left 5×5 block visually**

---

