
---

### **মূল ধারণা (Basic Concept)**

প্রতিটি গ্রেস্কেল ছবি (image) গঠিত হয় ৮-বিট পিক্সেল দিয়ে, যেখানে একটি পিক্সেলের মান ০ থেকে ২৫৫ এর মধ্যে হতে পারে। প্রতিটি পিক্সেলের মান বাইনারি (দ্বিমিক) আকারে ৮টি বিট দিয়ে লেখা হয়।

**Bit-Plane Slicing** বলতে বোঝায়, ৮টি বিটকে আলাদা করে দেখার প্রক্রিয়া, যেখানে প্রতিটি বিট আলাদা একটি "plane" তৈরি করে। এর মাধ্যমে প্রতিটি বিটের প্রভাব আলাদা করে বুঝতে পারা যায়।

---

### **Bit-Plane Slicing এর কাঠামো**

প্রতিটি পিক্সেল ৮টি বিট নিয়ে গঠিত, অর্থাৎ ৮টি আলাদা plane থাকে। এই ৮টি plane:

| Plane | বিট | মান (MSB → LSB)                        |
| ----- | --- | -------------------------------------- |
| 7     | 1   | সবচেয়ে গুরুত্বপূর্ণ (structure)        |
| 6     | 0   |                                        |
| 5     | 0   |                                        |
| 4     | 1   |                                        |
| 3     | 0   |                                        |
| 2     | 1   |                                        |
| 1     | 1   |                                        |
| 0     | 0   | সবচেয়ে কম গুরুত্বপূর্ণ (noise/texture) |

এখানে, Plane 7-6 মূল কাঠামো এবং বর্ডার/এজের জন্য গুরুত্বপূর্ণ, এবং Plane 0-1 সাধারণত noise বা texture হিসাবে কাজ করে।

---

### **Bit-Plane এর গুরুত্ব**

| Bit Plane | গুরুত্ব   | চরিত্র                            |
| --------- | --------- | --------------------------------- |
| Plane 7–6 | খুবই উচ্চ | ছবি গঠন, বর্ডার, প্রধান অঙ্গ      |
| Plane 5–4 | মাঝারি    | কিছু texture এবং structure        |
| Plane 3–2 | কম        | কিছু subtle texture বা brightness |
| Plane 1–0 | খুবই কম   | noise বা texture/jitter           |

---

### **চিত্র উদাহরণ:**

ধরুন, একটি ২x২ ইমেজ:

```
[[200, 185],
 [120, 10]]
```

এখানে প্রতিটি মানের বাইনারি রূপ:

| মান | বাইনারি  |
| --- | -------- |
| 200 | 11001000 |
| 185 | 10111001 |
| 120 | 01111000 |
| 10  | 00001010 |

**Bit Plane 7 (MSB):**

```
[[1, 1],
 [0, 0]]
```

**Bit Plane 0 (LSB):**

```
[[0, 1],
 [0, 0]]
```

---

### **Python কোড উদাহরণ**

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load grayscale image
img = cv2.imread('image_path', 0)

plt.figure(figsize=(12, 8))
for i in range(8):
    bit_plane = np.bitwise_and(img, 1 << i)
    bit_plane = np.where(bit_plane > 0, 255, 0).astype(np.uint8)

    plt.subplot(2, 4, i+1)
    plt.imshow(bit_plane, cmap='gray')
    plt.title(f'Bit Plane {i}')
    plt.axis('off')

plt.tight_layout()
plt.show()
```

এই কোডটি গ্রেস্কেল ছবির ৮টি বিট প্লেন আলাদাভাবে প্রদর্শন করবে।

---

### **Bit-Plane Slicing এর ব্যবহার**

| ব্যবহার ক্ষেত্র                | বর্ণনা                                          |
| ------------------------------ | ----------------------------------------------- |
| **Image Compression**          | শুধু উচ্চ বিটগুলো রেখে ছবির সাইজ কমানো যায়      |
| **Watermarking/Steganography** | Plane 0–1 তে গোপন বার্তা রাখা যায়               |
| **Edge Detection**             | Plane 7 এবং 6 ব্যবহার করে edges স্পষ্ট দেখা যায় |
| **Noise Reduction**            | নিচের planes বাদ দিলে নয়েজ কমে যায়              |



✅ সারাংশ (Summary)
 প্রতিটি পিক্সেল ৮টি bit নিয়ে গঠিত।

 bit-plane slicing একটি ছবি ভেঙে ৮টি লেয়ার তৈরি করে।

 এতে করে image এর structural এবং texture তথ্য আলাদা করা যায়।

 বিভিন্ন বিট-plane আলাদা আলাদা কাজের জন্য ব্যবহার করা যায়।
---

### **উপসংহার**

Bit-Plane Slicing একটি গুরুত্বপূর্ণ টেকনিক যা প্রতিটি পিক্সেলের বাইনারি বিটকে আলাদা করে দেখে এবং এর মাধ্যমে বিভিন্ন structural ও low-level তথ্য বিশ্লেষণ করা যায়। এটি ইমেজ কমপ্রেশন, স্টেগানোগ্রাফি, noise রিডাকশন ইত্যাদি কাজে ব্যবহার করা যায়।

---

---

## 🎯 আমরা যা শিখবো:

### 1. Bit-Plane Slicing (Grayscale Image)

* ➕ ছবিকে plane 0 থেকে 7 পর্যন্ত কেটে দেখা
* ➕ কোন প্লেনে কি থাকে তা বিশ্লেষণ

### 2. Bit-Plane Slicing (Color Image)

* ➕ RGB আলাদা করে 3 টা চ্যানেলেই বিট প্লেন slicing

### 3. Plane Reconstruction

* ➕ শুধু গুরুত্বপূর্ণ planes দিয়ে কিভাবে মূল ছবির structure ফেরত আনা যায়

---

## 🔧 Step 1: Grayscale Bit-Plane Slicing (কোডসহ)

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load grayscale image
img = cv2.imread('scenery1.png', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(12, 6))
plt.subplot(2, 5, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

# Step 2: Extract 8 bit-planes
for i in range(8):
    bit_plane = (img >> i) & 1
    bit_plane_img = bit_plane * 255  # convert binary to visible image
    plt.subplot(2, 5, i+2)
    plt.imshow(bit_plane_img, cmap='gray')
    plt.title(f"Bit Plane {i}")
    plt.axis('off')

plt.tight_layout()
plt.show()
```

📌 **তুমি কি দেখবে?**

* Plane 0 → noise
* Plane 7 → full structure

---

## 🔧 Step 2: Reconstruction from High Bit-Planes Only

```python
# Only MSB planes (6,7)
reconstructed = ((img >> 6) & 1) * 64 + ((img >> 7) & 1) * 128

plt.figure(figsize=(6, 3))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(reconstructed, cmap='gray')
plt.title("Reconstructed (6+7)")
plt.axis('off')
plt.tight_layout()
plt.show()
```

---

## 🔧 Step 3: RGB Color Image Plane Slicing

```python
img = cv2.imread('scenery1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

colors = ['Red', 'Green', 'Blue']

for c in range(3):  # loop through channels
    plt.figure(figsize=(12, 6))
    for i in range(8):
        plane = ((img[:, :, c] >> i) & 1) * 255
        plt.subplot(2, 4, i+1)
        plt.imshow(plane, cmap='gray')
        plt.title(f"{colors[c]} Plane {i}")
        plt.axis('off')
    plt.suptitle(f"{colors[c]} Channel Bit-Planes", fontsize=16)
    plt.tight_layout()
    plt.show()
```

---


