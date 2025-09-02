
'''
Problem Statement:
Write a Python script that loads a grayscale image and performs the following transformations:
1. Load the image.
2. Print the shape of the image.
3. Display the original image.
4. Create a negative of the image using the transformation:
    g(x, y) = max(f(x, y)) - f(x, y),
5. Display the negative image. 

'''

---

# **Theory Explanation**

### **১. গ্রেস্কেল ইমেজ**

* একটি **RGB ইমেজ** থাকে 3টি চ্যানেল নিয়ে: **Red, Green, Blue**।
* কিন্তু **Grayscale ইমেজ**-এ আসলে একটাই intensity channel থাকে (কালো-সাদা শেড)।
* তবুও কিছু লাইব্রেরি (যেমন matplotlib, OpenCV) গ্রেস্কেল ইমেজকে `(H, W, 3)` বা `(H, W, 4)` shape-এও load করতে পারে, যদিও real ডেটা একটাই চ্যানেলে থাকে।

👉 উদাহরণ:

* Pure Grayscale → shape = `(height, width)`
* PNG হিসেবে save করা → shape = `(height, width, 4)` (RGBA)

---

### **২. Image Negative Transformation**

**Mathematical definition:**

$$
g(x, y) = L - 1 - f(x, y)
$$

* এখানে:

  * $f(x, y)$ = Original pixel intensity at position (x, y)
  * $g(x, y)$ = Negative pixel intensity
  * $L$ = Total possible intensity levels (e.g., 256 for 8-bit image)
* অর্থাৎ, **উজ্জ্বল পিক্সেল গাঢ় হবে, আর গাঢ় পিক্সেল উজ্জ্বল হবে।**

👉 তোমার কোডে তুমি ব্যবহার করেছো:

```python
img_negative = img_2D.max() - img_2D
```

* এখানে `img_2D.max()` হচ্ছে image-এর সর্বোচ্চ intensity value।
* এইভাবে **bright → dark** আর **dark → bright** হয়ে যায়।

---

### **৩. কোডের ধাপে ধাপে কাজ**

#### (i) **Load Image**

```python
img_2D = plt.imread(img_path)
```

* ইমেজ মেমোরিতে load হয় একটি NumPy array হিসেবে।
* যদি ইমেজ 256x256 গ্রেস্কেল হয়, তবে shape হতে পারে `(256, 256)`।
* যদি PNG হয়, তবে shape `(256, 256, 4)` হতে পারে।

---

#### (ii) **Print Shape**

```python
print("Image shape using matplotlib:", img_2D.shape)
```

* এটা image-এর dimension সম্পর্কে জানায়।
* যেমন `(512, 512, 4)` মানে: height = 512, width = 512, channels = 4 (RGBA)।

---

#### (iii) **Display Original Image**

```python
plt.imshow(img_2D[:, :, 0], cmap='gray')
```

* `imshow` ব্যবহার করে ছবি display করা যায়।
* `cmap='gray'` দিলে ছবিটা গ্রেস্কেলে render হয়।
* `[:, :, 0]` মানে প্রথম channel দেখানো হচ্ছে।

  * দরকার কারণ কিছু PNG ফাইলে অপ্রয়োজনীয় extra channel (alpha/transparency) থাকে।

---

#### (iv) **Negative Transformation**

```python
img_negative = img_2D.max() - img_2D
```

* প্রতিটি pixel intensity `max - pixel_value` দ্বারা replace হয়।
* যেমন:

  * যদি max intensity = 255
  * আর pixel value = 200
  * তবে negative pixel = 255 - 200 = 55

👉 ফলে **কালো → সাদা**, **সাদা → কালো**, আর মাঝামাঝি শেড উল্টে যায়।

---

#### (v) **Display Negative Image**

```python
plt.imshow(img_negative[:, :, 0], cmap='gray')
```

* Negative image display হয়।

---

### **৪. Visualization**

* Original image → কালো জায়গা কালোই থাকে, সাদা জায়গা সাদাই থাকে।
* Negative image → কালো → সাদা, সাদা → কালো হয়ে যায়।
* উদাহরণস্বরূপ:

  * লেখা থাকলে → সাদা background + কালো লেখা।
  * Negative করলে → কালো background + সাদা লেখা।

---

### **৫. Practical Applications**

1. **Medical Imaging** – X-ray বা MRI তে contrast বাড়ানোর জন্য।
2. **Document Analysis** – কালো-সাদা লেখা আলাদা করতে।
3. **Forensic Image Processing** – লুকানো details বের করতে।

---

👉 সংক্ষেপে:

* তুমি একটি **গ্রেস্কেল ইমেজ লোড** করছো।
* তার **shape প্রিন্ট** করছো।
* **Original image show** করছো।
* **Negative transformation** apply করছো।
* এরপর **Negative image show** করছো।

---

# ✅ Python Code (with Explanation)

```python
import matplotlib.pyplot as plt
import numpy as np

def main():
    #================ Load the image ========================================
    img_path = "/home/mohon/4_1/cse4161/images/gray_4.png"
    img = plt.imread(img_path)

    #=============== Print the shape ============================
    print("Original image shape:", img.shape)

    #================ Handle grayscale or multi-channel =========
    # যদি image 2D হয় (H, W) → pure grayscale
    if img.ndim == 2:
        img_gray = img
    else:
        # যদি image 3D হয় (H, W, C) → RGB/RGBA
        # তখন আমরা শুধু প্রথম channel (Red বা Gray channel) নেবো
        img_gray = img[:, :, 0]

    print("Grayscale image shape:", img_gray.shape)

    #============== Display the original image ==================
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')

    #============== Perform negative transformation =============
    # formula: g(x,y) = max(f) - f(x,y)
    img_negative = img_gray.max() - img_gray

    #============== Display the negative image ==================
    plt.subplot(1, 2, 2)
    plt.imshow(img_negative, cmap='gray')
    plt.title('Negative Image')
    plt.axis('off')

    #============== Show both together ==========================
    plt.tight_layout()
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
```

---

# 📖 Explanation

### **1. Image Load**

```python
img = plt.imread(img_path)
```

* ইমেজটি numpy array আকারে লোড হবে।
* Example:

  * Shape `(512, 512)` → pure grayscale
  * Shape `(512, 512, 3)` → RGB
  * Shape `(512, 512, 4)` → RGBA (extra alpha channel)

---

### **2. Grayscale Conversion**

```python
if img.ndim == 2:
    img_gray = img
else:
    img_gray = img[:, :, 0]
```

* যদি ইতিমধ্যে 2D হয় → grayscale 그대로 ব্যবহার করা হবে।
* যদি 3D হয় → শুধু প্রথম channel (Red/Gray) ব্যবহার করা হবে।

---

### **3. Negative Transformation**

```python
img_negative = img_gray.max() - img_gray
```

* Pixel intensity উল্টানো হচ্ছে।
* উদাহরণ:

  * max intensity = 255
  * pixel value = 200
  * negative = 255 - 200 = 55

---

### **4. Display**

```python
plt.subplot(1, 2, 1)   # প্রথম subplot → original
plt.subplot(1, 2, 2)   # দ্বিতীয় subplot → negative
```

* দুইটা ছবি পাশাপাশি দেখানো হচ্ছে।

---

# 🎯 Output

1. **Left side** → Original grayscale image
2. **Right side** → Negative image (কালো ↔ সাদা উল্টানো)

---

