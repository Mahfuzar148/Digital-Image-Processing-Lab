
---

# 📘 থিওরি ব্যাখ্যা

---

## ১. ইমেজ রিপ্রেজেন্টেশন

একটা কালার ইমেজকে আমরা **3D array (Height × Width × Channels)** আকারে রাখতে পারি।

* **Height (x)** → সারি (row)
* **Width (y)** → কলাম (column)
* **Channels (c)** → রঙের জন্য আলাদা মান (R, G, B → 3 channel)

তাহলে একটা পিক্সেল লেখা যায়:

$$
f(x, y, c)
$$

যেখানে,

* $f(x, y, 0)$ → লাল (Red) মান
* $f(x, y, 1)$ → সবুজ (Green) মান
* $f(x, y, 2)$ → নীল (Blue) মান

---

## ২. 4D থেকে 3D কনভার্শন

PNG ইমেজ অনেক সময় **RGBA** ফরম্যাটে থাকে।

* R → Red
* G → Green
* B → Blue
* A → Alpha (transparency)

তাহলে shape হয় → `(height, width, 4)`

তুমি শুধু **RGB দরকার**, তাই নিচ্ছো প্রথম 3 channel:

$$
img\_3D = img\_4D[:, :, :3]
$$

---

## ৩. ট্রান্সফরমেশন ফাংশন

তুমি যে ফাংশন লিখেছো:

$$
g(x, y, c) = \max(f(x, y, c)) - f(x, y, c)
$$

এর মানে হলো:

* $f(x, y, c)$ → আসল ইমেজের কোনো একটা পিক্সেল ভ্যালু (channel অনুযায়ী)
* $\max(f(x, y, c))$ → পুরো ইমেজে ওই channel এর সর্বোচ্চ intensity মান
* ওই সর্বোচ্চ মান থেকে পিক্সেল ভ্যালুকে বাদ দিলে **negative transformation** হয়

---

## ৪. Negative Image (Image Inversion)

Negative বা inverted image এ:

* কালো → সাদা হয়ে যায়
* সাদা → কালো হয়ে যায়
* মাঝারি মান → উল্টা দিকে চলে যায়

👉 ধরো একটা গ্রেস্কেল উদাহরণ:

* Original pixel intensity = 50 (0–255 scale)
* Max intensity = 255
* Negative pixel = $255 - 50 = 205$

তাহলে কালো রঙ উল্টে সাদা হয়, উজ্জ্বল রঙ উল্টে অন্ধকার হয়।

---

## ৫. চ্যানেলভিত্তিক ইমেজ আলাদা করা

তুমি কোডে আলাদা করে প্রতিটি channel ভিজুয়ালাইজ করেছো:

* **Red channel** → `cmap='Reds'` দিয়ে আঁকা
* **Green channel** → `cmap='Greens'` দিয়ে আঁকা
* **Blue channel** → `cmap='Blues'` দিয়ে আঁকা

এতে বোঝা যায় কোন পিক্সেল কতটুকু contribution দিচ্ছে লাল, সবুজ আর নীলে।

---

## ৬. ভিজুয়ালাইজেশন

তুমি `subplot` ব্যবহার করে একসাথে ৫টা জিনিস দেখাচ্ছো:

1. আসল ইমেজ (RGB)
2. শুধু Red channel
3. শুধু Green channel
4. শুধু Blue channel
5. Negative image

এতে একটা ছবিকে বিভিন্ন আঙ্গিকে বিশ্লেষণ করা যায়।

---

# ✅ সারাংশ

* ইমেজ হলো 3D ম্যাট্রিক্স → প্রতিটি পিক্সেল হলো \[R, G, B]
* ট্রান্সফরমেশন:

$$
g(x,y,c) = \max(f(x,y,c)) - f(x,y,c)
$$

এটা **negative image** তৈরি করে

* Negative image = আসল ছবির উল্টো কালার
* চ্যানেল আলাদা করলে বোঝা যায় প্রতিটি রঙের intensity distribution

---


## ✅ কোড

```python
'''  
Given an image, this script load the image, convert it from 4D to 3D, perform the given transformations:
g(x, y, c) = max(f(x, y, c)) - f(x, y, c) 

here, f(x, y, c) is the pixel value at position (x, y) for channel c = 3.
'''
import matplotlib.pyplot as plt

def main():
    #================  Load the image ========================================
    img_path = "/home/mohon/4_1/cse4161/images/rgb2.png"
    img_4D = plt.imread(img_path)

    #===============  Convert 3D from 4D =====================================
    img_3D = img_4D[:, :, :3]

    #============== perform transformation(prepare negative image)  ==========
    img_negative = img_3D.max() - img_3D

    #==============  display the original image ==============================
    plt.figure(figsize=(20, 20))
    plt.subplot(3, 2, 1)
    plt.imshow(img_3D) 

    #============= display red channel image ================================
    plt.subplot(3,2,2)
    plt.imshow(img_3D[:, :, 0], cmap = 'Reds')
    
    #============  display green channel image =============================
    plt.subplot(3, 2, 3)
    plt.imshow(img_3D[:, :, 1], cmap = 'Greens')

    #=============  dispaly the blue channel image ========================
    plt.subplot(3,2,4)
    plt.imshow(img_3D[:, :, 2], cmap = 'Blues')

    #============== display the transformed image =========================
    plt.subplot(3, 2, 5)
    plt.imshow(img_negative)

    plt.show()
    plt.close()

if __name__ == '__main__': 
    main()
```

---

## 🧾 ব্যাখ্যা

### ১. ডকস্ট্রিং (Problem statement অংশ)

```python
'''
Given an image, this script load the image, convert it from 4D to 3D, perform the given transformations:
g(x, y, c) = max(f(x, y, c)) - f(x, y, c) 
'''
```

* এখানে বলা হচ্ছে:

  * ইমেজ লোড করব
  * যদি 4D (RGBA) হয় তাহলে 3D (RGB) তে রূপান্তর করব
  * তারপর প্রতিটি পিক্সেলে ট্রান্সফরমেশন করব

ফর্মুলা:

$$
g(x,y,c) = \max(f(x,y,c)) - f(x,y,c)
$$

মানে হলো, প্রতিটি পিক্সেলের মানকে (f) উল্টে দেওয়া হবে তার সর্বোচ্চ মানের সাথে সম্পর্ক রেখে (negative image তৈরি করার জন্য)।

---

### ২. লাইব্রেরি ইমপোর্ট

```python
import matplotlib.pyplot as plt
```

* `matplotlib.pyplot` ব্যবহার করছি ইমেজ লোড, ভিজুয়ালাইজ এবং শো করার জন্য।

---

### ৩. ইমেজ লোড

```python
img_path = "/home/mohon/4_1/cse4161/images/rgb2.png"
img_4D = plt.imread(img_path)
```

* `plt.imread()` দিয়ে ইমেজ পড়া হচ্ছে
* যদি PNG হয়, সাধারণত shape হয় `(height, width, 4)` (RGBA → 4 channel)

---

### ৪. 4D থেকে 3D কনভার্শন

```python
img_3D = img_4D[:, :, :3]
```

* এখানে শুধু প্রথম ৩টা channel (R, G, B) নেওয়া হয়েছে
* Alpha (transparency) বাদ দেওয়া হয়েছে
* এখন shape হবে `(height, width, 3)`

---

### ৫. নেগেটিভ ট্রান্সফরমেশন

```python
img_negative = img_3D.max() - img_3D
```

* `img_3D.max()` → ইমেজের সর্বোচ্চ intensity মান বের করে (সকল চ্যানেল মিলিয়ে একটাই max)
* তারপর প্রতিটি পিক্সেলের মান সেই সর্বোচ্চ মান থেকে বাদ দিচ্ছে
* এতে **negative image** পাওয়া যাচ্ছে (কালো → সাদা, সাদা → কালো ইত্যাদি)

---

### ৬. ইমেজ ও চ্যানেলগুলো দেখানো

```python
plt.figure(figsize=(20, 20))
plt.subplot(3, 2, 1)
plt.imshow(img_3D)
```

* মূল ইমেজ (RGB) দেখানো হচ্ছে

```python
plt.subplot(3,2,2)
plt.imshow(img_3D[:, :, 0], cmap = 'Reds')
```

* শুধুমাত্র **Red channel** আলাদা করে দেখানো হচ্ছে

```python
plt.subplot(3, 2, 3)
plt.imshow(img_3D[:, :, 1], cmap = 'Greens')
```

* শুধুমাত্র **Green channel**

```python
plt.subplot(3,2,4)
plt.imshow(img_3D[:, :, 2], cmap = 'Blues')
```

* শুধুমাত্র **Blue channel**

```python
plt.subplot(3, 2, 5)
plt.imshow(img_negative)
```

* সর্বশেষ **negative image** দেখানো হচ্ছে

---

### ৭. Show এবং Close

```python
plt.show()
plt.close()
```

* `show()` → সবগুলো ইমেজ উইন্ডোতে প্রদর্শন করবে
* `close()` → figure বন্ধ করবে

---

## 🔎 সারাংশ

* **Original image** → RGB তে কনভার্ট
* **Channel separation** → R, G, B আলাদা দেখা
* **Transformation** → $g(x,y,c)=\max(f)-f(x,y,c)$ দিয়ে negative বানানো
* **Visualization** → সবগুলো subplot এ পাশাপাশি দেখানো হয়েছে

---

