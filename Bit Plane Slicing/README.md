
---

# 📸 **Bit Plane Slicing in Digital Image Processing**

---

## 🗂️ **GitHub Folder & Project Topic**

* **Folder Name:** `Bit Plane Slicing`
* **Topic:** **Bit Plane Slicing Implementation and Analysis**

---

## 👨‍🎓 **Author Information**

* **Name:** Md. Mahfuzar Rahman
* **ID:** 2110976123
* **Session:** 2020–21
* **Department:** Computer Science and Engineering
* **University:** University of Rajshahi

---

## 📖 **Basic Theory of Bit-Plane Slicing**

**Bit-plane slicing** is an essential digital image processing technique used to visualize and analyze an image by separating its intensity values into individual bits. Each pixel in a grayscale image typically contains 8 bits (binary digits), with bit positions from `0` (least significant bit - LSB) to `7` (most significant bit - MSB).

### **Importance of Bit Planes:**

* **MSB (Higher bit-plane)**: Contains the most critical visual information and contributes significantly to image appearance.
* **LSB (Lower bit-plane)**: Usually contains less critical information, such as noise or subtle details.

---

## 🎯 **Purpose of Bit Plane Slicing**

* Understand how individual bits contribute to the overall image.
* Image compression and watermarking applications.
* Analyze robustness against noise or data hiding techniques.

---

## 🛠️ **Tools and Libraries**

* Python 🐍
* OpenCV (`cv2`)
* NumPy
* Matplotlib

To install necessary libraries:

```bash
pip install numpy matplotlib opencv-python
```

---

## 🧮 **Bit Plane Slicing - Working Concept**

**Step-by-step Explanation:**

1. **Convert Image to Grayscale**
   Convert the image to grayscale to simplify pixel intensity analysis.

   ```
   img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   ```

2. **Right Shift Operation**
   Use the right-shift (`>>`) operation to isolate each bit:

   ```
   bit_plane = (img_gray >> bit_number) & 1
   ```

   * Shifting places the desired bit in the least significant position.
   * Bitwise AND with `1` isolates the bit.

3. **Visualization**
   Multiply by `255` for visibility:

   ```
   bit_plane = bit_plane * 255
   ```

4. **Combine Selected Bit Planes**
   To reconstruct a partial image from specific bit-planes, multiply them by their original importance:

   ```
   combined_img_567 = ((img_gray >> 5) & 1) * 32 + 
                      ((img_gray >> 6) & 1) * 64 + 
                      ((img_gray >> 7) & 1) * 128
   ```

   * Here, `32`, `64`, and `128` represent the importance of bit positions `5`, `6`, and `7`.

---
## 📸 **Input and Output Images**



🖼️ Input Image 

 ![Input Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Bit%20Plane%20Slicing/bit_plane_slicing_input.png?raw=true)
 
🖼️ Output Image 

![Output Image](https://github.com/Mahfuzar148/Digital-Image-Processing-Lab/blob/main/Bit%20Plane%20Slicing/bit_plane_slicing_output.png?raw=true) 


---

## 💻 **Complete Python Implementation**

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load image and convert to RGB
img = cv2.imread('bit_plane_slicing_input.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Plot setup
plt.figure(figsize=(30, 20))
plt.suptitle('Bit Plane Slicing', fontsize=24)

# Original Image
plt.subplot(4, 4, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Bit-plane extraction
for i in range(8):
    bit_plane = ((img_gray >> i) & 1) * 255
    plt.subplot(4, 4, i + 2)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')

# Combine selected bit planes
combined_img_567 = ((img_gray >> 5) & 1)*32 + ((img_gray >> 6) & 1)*64 + ((img_gray >> 7) & 1)*128
combined_img_0123 = ((img_gray >> 0) & 1)*1 + ((img_gray >> 1) & 1)*2 + ((img_gray >> 2) & 1)*4 + ((img_gray >> 3) & 1)*8
combined_img_4567 = ((img_gray >> 4) & 1)*16 + ((img_gray >> 5) & 1)*32 + ((img_gray >> 6) & 1)*64 + ((img_gray >> 7) & 1)*128
combined_img_01 = ((img_gray >> 0) & 1)*1 + ((img_gray >> 1) & 1)*2
combined_img_23 = ((img_gray >> 2) & 1)*4 + ((img_gray >> 3) & 1)*8
combined_img_45 = ((img_gray >> 4) & 1)*16 + ((img_gray >> 5) & 1)*32
combined_img_67 = ((img_gray >> 6) & 1)*64 + ((img_gray >> 7) & 1)*128

# Display combined images
combined_imgs = [combined_img_567, combined_img_0123, combined_img_4567, combined_img_01, combined_img_23, combined_img_45, combined_img_67]
titles = ['Combined 5,6,7', 'Combined 0,1,2,3', 'Combined 4,5,6,7', 'Combined 0,1', 'Combined 2,3', 'Combined 4,5', 'Combined 6,7']

for i, (img_comb, title) in enumerate(zip(combined_imgs, titles), 10):
    plt.subplot(4, 4, i)
    plt.imshow(img_comb, cmap='gray')
    plt.title(title)
    plt.axis('off')

# Adjust layout & save output
plt.subplots_adjust(wspace=0.1, hspace=0.5)
plt.savefig('bit_plane_slicing_output.png', bbox_inches='tight')
plt.show()
```

---

## 🚩 **How to Perform Bit Slicing Operation (Summary)**

* **Load and preprocess** the image (convert to grayscale).
* Perform **bitwise right shift** (`>>`) by the plane number.
* Perform **bitwise AND** with `1` to isolate the desired bit.
* Multiply by `255` to visualize each bit-plane.
* Combine selected bit-planes using their respective significance to partially reconstruct the image.

---

## 📁 **Recommended Project Folder Structure**

```
Digital-Image-Processing-Lab/
└── Bit Plane Slicing/
    ├── bit_plane_slicing_input.png
    ├── bit_plane_slicing_output.png
    ├── bit_plane_slicing.py
    └── README.md
```

---

## 📗 **Conclusion & Application**

Through this project, you can visually comprehend how digital images store and represent data at a bit level. Bit-plane slicing is crucial for various image processing techniques such as compression, steganography, watermark embedding, and understanding digital image characteristics at a fundamental binary level.

---

