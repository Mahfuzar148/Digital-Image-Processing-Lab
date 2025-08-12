
---


# 🖼️ Digital Image Processing – Image Thresholding  

## 📌 Overview  
This project demonstrates **Image Thresholding** — a technique in Digital Image Processing (DIP) used to separate objects from the background by converting a grayscale image into a binary or multi-level image based on intensity thresholds.  

---

## ⚙️ What is Image Thresholding?  
**Image Thresholding** is a method where pixel intensity values are compared to a threshold value:  
- If the pixel value is below the threshold → it becomes one value (e.g., 0 or black)  
- If the pixel value is equal to or above the threshold → it becomes another value (e.g., 255 or white)  
- With multiple thresholds, **multi-level thresholding** can be performed.  

It is widely used in:  
- Object detection  
- Document scanning  
- Image segmentation  

---

## 📋 Functions Used  

1. **Function 1:**  
   - `0–128 => 0`  
   - `else => 255`  

2. **Function 2:**  
   - `0–127 => original value`  
   - `127–190 => 127`  
   - `>190 => 255`  

3. **Function 3:**  
   - `0–100 => original value`  
   - `100–150 => 120`  
   - `150–180 => original value`  
   - `180–220 => 220`  
   - `>220 => 255`  

---

## 📌 Function Diagram  
![Function Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/image%20thresholding/images/function_img.png?raw=true)  

---

## 📥 Input Images  
| Image 1 | Image 2 | Image 3 |  
|---------|---------|---------|  
| ![Image 1](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/image%20thresholding/images/img1.png?raw=true) | ![Image 2](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/image%20thresholding/images/img2.png?raw=true) | ![Image 3](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/image%20thresholding/images/img3.png?raw=true) |  

---

## 📤 Output Image  
![Output Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/image%20thresholding/images/img_thresholding_output.png?raw=true)  

---

## 💻 Code  

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function 1
def function1(img):
    result = np.where(img <= 128, 0, 255).astype(np.uint8)
    return result

# Function 2
def function2(img):
    result = np.copy(img)
    result[(img >= 0) & (img <= 127)] = img[(img >= 0) & (img <= 127)]
    result[(img > 127) & (img <= 190)] = 127
    result[(img > 190)] = 255
    return result

# Function 3
def function3(img):
    result = np.copy(img)
    result[(img >= 0) & (img <= 100)] = img[(img >= 0) & (img <= 100)]
    result[(img > 100) & (img <= 150)] = 120
    result[(img > 150) & (img <= 180)] = img[(img > 150) & (img <= 180)]
    result[(img > 180) & (img <= 220)] = 220
    result[(img > 220)] = 255
    return result

# Read input images
img1 = cv2.imread('images/img1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/img2.png', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('images/img3.png', cv2.IMREAD_GRAYSCALE)

# Apply functions
out1 = function1(img1)
out2 = function2(img2)
out3 = function3(img3)

# Display results
titles = ['Input 1', 'Output 1', 'Input 2', 'Output 2', 'Input 3', 'Output 3']
images = [img1, out1, img2, out2, img3, out3]

plt.figure(figsize=(10, 8))
for i in range(6):
    plt.subplot(3, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

# Save final output image
output_combined = np.hstack([out1, out2, out3])
cv2.imwrite('images/img_thresholding_output.png', output_combined)
````

---

## ▶️ How to Run

```bash
pip install opencv-python matplotlib numpy
python thresholding.py
```

---


