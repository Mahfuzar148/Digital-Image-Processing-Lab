# 🖼️ Python Image Channel Visualization and Negative Image Generation

This Python program loads a color image using `matplotlib`, removes the alpha channel if present, and displays different views of the image, including its red, green, blue channels and a negative image.

---

## ✅ Full Python Code

```python
import matplotlib.pyplot as plt


def main():
    # Load an image
    img_path = 'F:/6TH SEMISTER/Python Code/OIF.jpeg'
    img_4D = plt.imread(img_path)
    print(img_4D.shape)

    # Convert 4D image into a 3D image
    img_3D = img_4D[:, :, :3]
    print(img_3D.shape)

    # Print some values of images
    print(img_3D[:5, :5, :2])
    print(img_3D.max(), img_3D.min())

    # Prepare negative of loaded image
    negative_img = img_3D.max() - img_3D

    # Display loaded 3D image
    plt.figure(figsize=(20, 20))
    plt.subplot(2, 3, 1)
    plt.title('Original Image')
    plt.imshow(img_3D)

    plt.subplot(2, 3, 2)
    plt.imshow(img_3D[:, :, 0], cmap='Reds')
    plt.title('Red Channel')

    plt.subplot(2, 3, 3)
    plt.imshow(img_3D[:, :, 1], cmap='Greens')
    plt.title('Green Channel')

    plt.subplot(2, 3, 4)
    plt.imshow(img_3D[:, :, 2], cmap='Blues')
    plt.title('Blue Channel')

    plt.subplot(2, 3, 5)
    plt.imshow(negative_img)
    plt.title('Negative Image')

    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
```

---

## 📘 Step-by-Step Documentation

### 🔹 Step 1: Load the Image

```python
img_4D = plt.imread(img_path)
```

* Loads the image as a NumPy array.
* If the image has an alpha channel (RGBA), the shape will be (height, width, 4).
* Example output:

  ```python
  (220, 330, 3)
  ```

---

### 🔹 Step 2: Remove Alpha Channel (If Exists)

```python
img_3D = img_4D[:, :, :3]
```

* This retains only the RGB channels.
* Output shape:

  ```python
  (220, 330, 3)
  ```

---

### 🔹 Step 3: Print Sample Pixel Values

```python
print(img_3D[:5, :5, :2])
```

* Prints the top-left 5x5 pixel values of **Red** and **Green** channels.
* Output (example):

```python
[[[67 52]
  [67 54] ... ]]
```

```python
print(img_3D.max(), img_3D.min())
```

* Finds maximum and minimum pixel intensity values.
* Output (for 8-bit image):

  ```python
  255 0
  ```

---

### 🔹 Step 4: Create Negative Image

```python
negative_img = img_3D.max() - img_3D
```

* Inverts pixel intensity values for RGB:

  ```
  negative_pixel = 255 - original_pixel
  ```

---

### 🔹 Step 5: Display Subplots

```python
plt.subplot(...)
plt.imshow(...)
```

* Creates 6 subplots:

| Subplot | What it shows      |
| ------- | ------------------ |
| (2,3,1) | Original RGB Image |
| (2,3,2) | Red Channel        |
| (2,3,3) | Green Channel      |
| (2,3,4) | Blue Channel       |
| (2,3,5) | Negative Image     |

---

## 🎯 Summary Output:

* Image Shape: `(220, 330, 3)`
* Top-left pixel values for R & G printed
* Max/Min values: `255 / 0`
* Negative image generated
* Subplots display original and individual channels visually

---

✅ This script is excellent for learning basic image manipulation, channel separation, and visualization with `matplotlib`.

