
---


# 🎨 Color Conversion and Intensity Visualization in Python (OpenCV + Matplotlib)

This project demonstrates **color manipulation** and **channel intensity visualization** using `OpenCV`, `NumPy`, and `Matplotlib`. It's ideal for learning how RGB channels contribute to digital image creation and how color intensities affect image appearance.

---

## 📘 Basics: How Color Works in Images

In RGB (Red-Green-Blue) color space:

- Every pixel is represented by three values: **Red**, **Green**, and **Blue**.
- Each value ranges from `0` (no intensity) to `255` (full intensity).
- By adjusting individual channels, we can create different **tints**, **solid colors**, and **custom colors**.

| R   | G   | B   | Color Result       |
| --- | --- | --- | ------------------ |
| 0   | 0   | 0   | Black              |
|255  |255  |255  | White              |
|255  | 0   | 0   | Red                |
| 0   |255  | 0   | Green              |
| 0   | 0   |255  | Blue               |
|255  |255  | 0   | Yellow (Red+Green) |
| 0   |255  |255  | Cyan (Green+Blue)  |
|255  | 0   |255  | Magenta (Red+Blue) |

---

## 🔧 How to Convert an Image to a Solid Color

These transformations are performed using NumPy array operations:

### 🏳️ White Image
```python
white_img = np.ones_like(img) * 255
````

### 🏴 Black Image

```python
black_img = np.zeros_like(img)
```

### 🟥 Red Image

```python
red_img = np.copy(white_img)
red_img[:, :, 1] = 0  # Remove green
red_img[:, :, 2] = 0  # Remove blue
```

### 🟩 Green Image

```python
green_img = np.copy(white_img)
green_img[:, :, 0] = 0  # Remove red
green_img[:, :, 2] = 0  # Remove blue
```

### 🟦 Blue Image

```python
blue_img = np.zeros_like(img)
blue_img[:, :, 2] = 255  # Only blue channel
```

### 🌈 Custom Color Example (Yellow)

```python
yellow_img = np.zeros_like(img)
yellow_img[:, :, 0] = 255  # Red
yellow_img[:, :, 1] = 255  # Green
yellow_img[:, :, 2] = 0    # Blue
```

---

## 🧾 Input and Output

### 🔗 Input Image

[![Input Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Color%20Conversion%20Of%20Image/input_img.png?raw=true)](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Color%20Conversion%20Of%20Image/input_img.png)

### 📤 Output Visualization

[![Output Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Color%20Conversion%20Of%20Image/output_img.png?raw=true)](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Color%20Conversion%20Of%20Image/output_img.png)

---

## 🧑‍💻 Full Code Breakdown

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load and convert image
img = cv2.imread('F:/7th semister/DIP LAB/image/scenery1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create solid color images
white_img = np.ones_like(img) * 255
black_img = np.zeros_like(img)

red_img = np.copy(white_img)
red_img[:, :, 1] = 0
red_img[:, :, 2] = 0

green_img = np.copy(white_img)
green_img[:, :, 0] = 0
green_img[:, :, 2] = 0

blue_img = np.copy(black_img)
blue_img[:, :, 2] = 255

intensity_values = [20, 50, 80, 120, 160, 180, 200, 220, 230, 255]

# Plotting
plt.figure(figsize=(30, 25))
plt.subplot(5, 10, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

plt.subplot(5, 10, 2)
plt.imshow(black_img)
plt.title('Black Image')
plt.axis('off')

plt.subplot(5, 10, 3)
plt.imshow(white_img)
plt.title('White Image')
plt.axis('off')

# Red Tints
for i, intensity in enumerate(intensity_values):
    red_img[:, :, 0] = intensity
    plt.subplot(5, 10, 4 + i)
    plt.imshow(red_img)
    plt.title(f'Red {intensity}')
    plt.axis('off')

# Green Tints
for i, intensity in enumerate(intensity_values):
    green_img[:, :, 1] = intensity
    plt.subplot(5, 10, 14 + i)
    plt.imshow(green_img)
    plt.title(f'Green {intensity}')
    plt.axis('off')

# Blue Tints
for i, intensity in enumerate(intensity_values):
    blue_img[:, :, 2] = intensity
    plt.subplot(5, 10, 24 + i)
    plt.imshow(blue_img)
    plt.title(f'Blue {intensity}')
    plt.axis('off')

plt.tight_layout()
# Optional: Save output
# plt.savefig('color_conversion.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 🖼️ Output Layout

Your output will show a **5x10 grid**, where:

* The first three images show the original, black, and white versions.
* Next 10 show **red** tints at varying intensities.
* Next 10 show **green** tints.
* Last 10 show **blue** tints.

---

## 💡 Learning Outcomes

* Understand the RGB color space.
* Learn to manipulate image channels using NumPy.
* Visualize color intensity and tinting effects.
* Construct solid and tinted images for visualization and teaching.

---

## 📦 Requirements

Install necessary packages with:

```bash
pip install opencv-python matplotlib numpy
```

---

## 📁 Project Structure

```
Color-Conversion/
├── input_img.png
├── output_img.png
├── color_conversion.py
└── README.md
```

---

## 🧪 Educational Use

This is a great starting point for:

* Digital Image Processing (DIP) lab assignments
* Teaching RGB theory
* Color-based filtering or segmentation
* Visual experiments and presentations

---



