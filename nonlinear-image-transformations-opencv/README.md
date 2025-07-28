
---



# 🌀 Non-Linear Image Transformations with OpenCV (Gamma & Log)

This project demonstrates how to apply **non-linear intensity transformations** — namely **Gamma Correction** and **Logarithmic Transformation** — on grayscale images using Python, OpenCV, NumPy, and Matplotlib.

---

## 🖼️ Input Image

> The image used in this example is a grayscale image of size 512×512.

![Input Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/nonlinear-image-transformations-opencv/image.png?raw=true)

---

## 🎯 Objective

- ✅ Apply **Gamma Correction** to adjust brightness/darkness non-linearly.
- ✅ Apply **Logarithmic Transformation** to enhance dark regions.
- ✅ Visualize all outputs in a subplot layout for comparison.

---

## ⚙️ Python File

**Filename:** `nonlinear_transform.py`

---

## 📜 Code Explanation (Step-by-step)

### 📌 Step 1: Load Image

```python
gray_scale_img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
````

* Loads image in grayscale mode.
* Returns a NumPy 2D array with pixel values from 0–255.

---

### 📌 Step 2: Normalize Image

```python
img_norm = gray_scale_img / 255.0
```

* Normalizes pixel values to range `[0, 1]`.
* Required for applying gamma/log formulas safely.

---

### 📌 Step 3: Gamma Correction

```python
gamma_values = [0.1, 0.3, 0.7, 1, 2, 3]
gamma_imgs = [c * np.power(img_norm, g) for g in gamma_values]
```

- Applies log transformation:

  $$
  s = c \cdot \log_2(1 + r)
  $$

* γ < 1: brightens image
* γ > 1: darkens image
* γ = 1: no change

---



````markdown
## 📌 Step 4: Logarithmic Transform

```python
log_img = c * np.log2(1 + img_norm)
log_img = log_img / np.max(log_img)
````

* Applies log transformation:

  $$
  s = c \cdot \log_2(1 + r)
  $$

* Enhances dark pixel values.

* Normalized again to ensure proper 0–1 output range.



---

### 📌 Step 5: Display Images

```python
plt.subplot(...)
plt.imshow(...)
```

* Displays 8 images:

  * Original
  * 6 gamma results
  * 1 log result
* `np.clip(...).astype(np.uint8)` is used to convert image back to 0–255 grayscale format.

---

### 🖼️ Output Visualization

Here is the final output after applying multiple gamma values and a log transformation:

![Output Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/nonlinear-image-transformations-opencv/output_unnown_function_applied_on_the_img.png?raw=true)

---

## ▶️ How to Run

```bash
python nonlinear_transform.py
```

> 📁 Ensure `image.png` is in the same directory.

---

## 📦 Dependencies

Install required libraries using:

```bash
pip install opencv-python numpy matplotlib
```

---

## 🧠 Learning Outcome

* Understand **non-linear intensity mapping** in images.
* Learn to manipulate pixel values using math functions.
* See how transformations affect brightness, contrast, and visibility.
* Practice Python image processing & visualization skills.

---

## 📁 Folder Structure

```
nonlinear-image-transformations-opencv/
│
├── image.png                             # Input image
├── nonlinear_transform.py                # Python code
├── output_unnown_function_applied_on_the_img.png  # Output visualization
└── README.md                             # Project documentation
```




---


```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# === Entry point of the program ===
def main():
    print("📢 Non-linear Function Image Processing Example")

# === STEP 1: Load the grayscale image ===
gray_scale_img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Check if the image loaded correctly
if gray_scale_img is None:
    print('❌ Image not loaded! Check the file path.')

# === STEP 2: Normalize image pixel values to [0, 1] range ===
img_norm = gray_scale_img / 255.0  # Converts 8-bit values to float values between 0 and 1

# === STEP 3: Apply Gamma Correction ===
gamma_values = [0.1, 0.3, 0.7, 1, 2, 3]  # Different gamma values to experiment with
c = 1.0  # Scaling constant
# Apply s = c * r^γ transformation for each gamma
gamma_imgs = [c * np.power(img_norm, g) for g in gamma_values]

# === STEP 4: Apply Logarithmic Transformation ===
# Formula: s = c * log2(1 + r)
log_img = c * np.log2(1 + img_norm)
# Normalize log output to [0, 1] for visualization
log_img = log_img / np.max(log_img)

# === STEP 5: Plot all the results ===
plt.figure(figsize=(18, 10))  # Create a large figure to hold all subplots

# Plot Original Grayscale Image
plt.subplot(2, 4, 1)
plt.imshow(gray_scale_img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Plot Gamma Corrected Images
for i, g_img in enumerate(gamma_imgs):
    # Scale back to 0–255 and convert to uint8 for display
    g_img_scaled = np.clip(g_img * 255, 0, 255).astype(np.uint8)
    plt.subplot(2, 4, i + 2)
    plt.imshow(g_img_scaled, cmap='gray')
    plt.title(f'Gamma = {gamma_values[i]}')
    plt.axis('off')

# Plot Log Transformed Image
plt.subplot(2, 4, 8)
log_scaled = np.clip(log_img * 255, 0, 255).astype(np.uint8)
plt.imshow(log_scaled, cmap='gray')
plt.title('Log Transform')
plt.axis('off')

# Automatically adjust subplot layout
plt.tight_layout()
plt.show()

# Call the main function when script is executed
if __name__ == "__main__":
    main()
```

---

## ✅ Highlights of What This Code Does:

| Feature                      | Description                                                    |
| ---------------------------- | -------------------------------------------------------------- |
| **Image Loading**            | Reads a grayscale image using OpenCV                           |
| **Normalization**            | Converts 0–255 pixel values to float values between 0–1        |
| **Gamma Correction**         | Applies power-law transformation to change brightness contrast |
| **Log Transformation**       | Enhances dark pixel regions and compresses brighter ones       |
| **Matplotlib Visualization** | Shows all results side by side in a 2×4 layout                 |

---


---

## 👤 Author

**[Mahfuzar148](https://github.com/Mahfuzar148)**
Digital Image Processing Lab Repository

---



