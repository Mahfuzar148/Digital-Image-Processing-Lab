
---

This project demonstrates how to generate different shades (33%, 66%, 100%) of primary and secondary colors starting from a black image. The code uses an original image for shape reference and applies shading on black pixels using NumPy and Matplotlib.

---

## 📌 Topic Title:
**Color Shades Generation from an Input Image**

---

## 👨‍💻 Author
- **Name:** Md. Mahfuzar Rahman  
- **ID:** 2110976123  
- **Session:** 2020–21  
- **Department:** Computer Science and Engineering  
- **University:** University of Rajshahi

---

## 📖 Basic Theory

Digital images are made up of tiny elements called **pixels**, and each pixel is represented by a combination of **Red**, **Green**, and **Blue (RGB)** values. These values usually range from 0 to 255.

In this experiment, we explore how color images are created and how **changing intensity** affects how we perceive colors:

- **Primary Colors:** Red, Green, and Blue  
- **Secondary Colors:** Cyan (G+B), Magenta (R+B), Yellow (R+G)  
- **White:** All RGB components are at full intensity (255,255,255)  
- **Black:** All components are zero (0,0,0)

By multiplying the color values by different shading factors (like 0.33, 0.66, 1.0), we simulate lighter or dimmer versions of each color. This helps visualize how colors are formed and adjusted in digital image processing.

---

## 📷 Input and Output

| Type       | Image |
|------------|-------|
| 🔽 Input Image | ![Input Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Color%20Conversion%20of%20image1/input_img.png) |
| 🔼 Output Image | ![Output Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Color%20Conversion%20of%20image1/color_shade.png) |

---

## 📄 Problem Statement

Write a Python program that displays 3 shades (light, medium, and full) of the following colors using the structure of a reference image:
- White
- Red
- Green
- Blue
- Cyan
- Magenta
- Yellow

Each shade should be displayed starting from a black base image and progressively increasing in intensity.

---

## 🧪 Tools Used

- Python 🐍
- OpenCV (cv2)
- NumPy
- Matplotlib

---

## 💻 Code Implementation

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img = cv2.imread('F:/7th semister/DIP LAB/image/scenery1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the image to RGB

# Create black and white images
black_img = np.zeros_like(img)

shade = [0.33, 0.66, 1.0]  # Define shades for white images

colors ={
    'white':[255, 255, 255],
    'red':[255, 0, 0],
    'green':[0, 255, 0],
    'blue':[0, 0, 255],
    'cyan':[0, 255, 255],
    'magenta':[255, 0, 255],
    'yellow':[255, 255, 0]
}

index = 1  # Start index for subplot
plt.figure(figsize=(30, 32))

for color_name, color_value in colors.items():
    for i, s in enumerate(shade):
        colored_img = np.copy(black_img)
        shaded_rgb = np.array(color_value) * s  # Apply shade to the color
        colored_img[:,:,] = shaded_rgb
        
        plt.subplot(len(colors), len(shade), index)
        plt.imshow(colored_img)
        plt.title(f'{color_name.capitalize()} Image {s}', fontsize=10)
        plt.axis('off')
        index += 1

plt.savefig('color_shade.png', bbox_inches='tight')  # Save the figure
plt.subplots_adjust(hspace=0.6, wspace=0.1)  # Adjust subplots to fit
plt.show()
````

---

## ✅ Output Details

* **Total shades generated:** 3 for each of 7 colors → 21 images
* **Arrangement:** Organized in a grid using `plt.subplot()`
* **Saved Output:** `color_shade.png` saved with `bbox_inches='tight'`

---

## 📦 Folder Structure

```
Digital-Image-Processing-Lab/
└── Color Conversion of image1/
    ├── input_img.png
    ├── color_shade.png
    ├── shade_color_generation.py
    └── README.md
```

---

## 🏁 Conclusion

This program visually demonstrates how color intensities change with different shading levels. It's a simple yet effective project for understanding pixel manipulation in RGB space using Python and OpenCV.

```

---


