
---

### Frequency-domain Circular Low-Pass Filter (Ideal LPF) — Serial Steps

1. **ইমেজ লোড (গ্রেস্কেল):**
   `img = cv2.imread('path', 0)`
   (color হলে পরে নোট দেখো)

2. **DFT/Fourier নেওয়া:**

   * `f = np.fft.fft2(img)`
   * **shift** করে low frequencies কে center এ আনো: `fshift = np.fft.fftshift(f)`

3. **মাস্কের সাইজ ঠিক করা:**

   * `rows, cols = img.shape`
   * `mask = np.zeros((rows, cols), np.uint8)`  ← (ইমেজের সাইজের সমান ম্যাট্রিক্স)

4. **সার্কুলার Low-Pass মাস্ক বানানো (`cv2.circle`):**

   * `center = (cols//2, rows//2)`
   * `radius = R` (তোমার cutoff; যেমন 30, 60, 80 — বড় হলে বেশি blur)
   * `cv2.circle(mask, center, radius, 1, -1)`
     এখানে **1 (সাদা)** মানে pass করতে দেবে; বাকি **0 (কালো)** ব্লক করবে। `-1` = filled circle।

5. **মাস্ককে complex ডাটার সাথে মিল করানো:**

   * `fshift_masked = fshift * mask`
     (mask dtype `uint8` হলেও numpy broadcast করে multiply হবে; চাইলে `mask.astype(np.float32)` করতে পারো)

6. **Inverse shift + Inverse FFT:**

   * `ishift = np.fft.ifftshift(fshift_masked)`
   * `img_back_complex = np.fft.ifft2(ishift)`

7. **Magnitude/Real নেওয়া + normalize:**

   * `img_back = np.abs(img_back_complex)`
   * `img_lp = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)`

8. **আউটপুট দেখা/সেভ করা:**

   * `cv2.imshow('LPF', img_lp)` / `cv2.imwrite('lpf.png', img_lp)`

---

### এখানে “masking” কীভাবে apply হচ্ছে?

* তুমি যে **`mask`** বানালে (center-এ filled white circle), সেটা frequency plane-এ **low frequency components (DC এবং তার আশেপাশের)** রাখছে (white=1 → pass), আর **high frequency (edge/detail) অংশগুলো** কেটে দিচ্ছে (black=0 → block)।
* `fshift * mask` এই multiply-টাই হলো **masking**—element-wise multiplication দিয়ে নির্দিষ্ট frequency band পাস/ব্লক করা।

---

### কাট-অফ রেডিয়াস (R) কীভাবে বাছবে?

* ছোট R → **কঠোর blur** (details বেশ কেটে যাবে)
* বড় R → **কম blur**, বেশি ডিটেইল থাকবে
* সাধারণ guideline: `R ≈ min(rows, cols) / 10` দিয়ে শুরু করে চোখে দেখে টিউন করো।

---

### Ideal vs Gaussian/Butterworth (smooth edges why?)

* **Ideal LPF (তুমি এখন যেটা করলে):** sharp cutoff → ring/halo (Gibbs) artifact হতে পারে।
* **Gaussian LPF:** smooth falloff → কম ringing, আরও natural blur।

  * Gaussian mask: `mask = exp( -D^2 / (2*sigma^2) )` যেখানে `D` = distance from center
* **Butterworth LPF:** order `n` দিয়ে sharpness নিয়ন্ত্রণ করা যায়:
  `H(u,v) = 1 / (1 + (D/D0)^(2n))`

(চাইলেই পরে আমি Gaussian/Butterworth mask formula সহ কোডও দেখাতে পারি।)

---

### Color ইমেজ হলে (দুটি পথ)

**পথ–A (প্রতিটি চ্যানেলে FFT):**

* `b,g,r = cv2.split(img_color)`
* উপরের 2–7 স্টেপ **প্রতি চ্যানেলে** করে শেষে `cv2.merge([b_lp, g_lp, r_lp])`
  **পথ–B (HSV-V বা YCrCb-Y):**
* Color → HSV, **V channel** এ LPF তারপর আবার merge → BGR।
* এটি অনেক সময় visually ভালো লাগে (brightness/smooth এ কাজ হয়; hue/sat কম নষ্ট হয়)।

---

### Optional (কিছু প্র্যাকটিক্যাল টিপস)

* **Padding/optimal size:** বড় ফ্রিকোয়েন্সি আর্টিফ্যাক্ট কমাতে border reflect padding কাজে লাগে; বা `cv2.getOptimalDFTSize` দিয়ে সাইজ optimize করতে পারো (OpenCV-র `cv2.dft` ইউজ করলে)।
* **OpenCV DFT API** (numpy FFT এর বদলে):

  * `dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)`
  * channels = 2 (real, imag) → তখন mask–ও 2-channel করতে হয়: `mask2 = cv2.merge([mask, mask])`
  * multiply: `fshift_masked = dft_shift * mask2`
  * inverse: `cv2.idft(...)` + magnitude: `cv2.magnitude(...)`
* **Normalization:** inverse FFT এর পর magnitude কে 0–255 এ নিয়ে আসতে `cv2.normalize` ব্যবহার করো।
* **Visualization:** frequency spectrum দেখতে চাইলে: `20*np.log(np.abs(fshift)+1)` নিয়ে দেখে বুঝতে পারবে radius ঠিক আছে কি না।

---

### Quick Python (NumPy FFT) Skeleton

```python
import cv2, numpy as np

img = cv2.imread('in.png', 0)

# FFT + shift
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# mask
rows, cols = img.shape
mask = np.zeros((rows, cols), np.uint8)
center = (cols//2, rows//2)
radius = 60  # try: 30/60/90
cv2.circle(mask, center, radius, 1, -1)

# apply mask
fshift_masked = fshift * mask

# inverse
ishift = np.fft.ifftshift(fshift_masked)
img_back = np.fft.ifft2(ishift)
img_back = np.abs(img_back)

# normalize to 8-bit
out = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
cv2.imwrite('lpf.png', out)
```

---

### সংক্ষিপ্ত চেকলিস্ট (তোমার প্রশ্ন ধরে):

* [x] **ইমেজের সাইজের সমান matrix** (mask) নিলে — ঠিক
* [x] `cv2.circle` দিয়ে **centered filled circle** আঁকবে — ঠিক
* [x] **Fourier shift** করা স্পেকট্রামের সাথে **multiply** করবে — ঠিক
* [x] **Inverse shift + inverse FFT** → magnitude → **normalize** → আউটপুট — করতে হবে
* [x] Color হলে per-channel বা V/Y-channel এ করো — বোনাস
* [x] Ideal LPF এ ringing হলে Gaussian/Butterworth ট্রাই করো — বেস্ট প্র্যাকটিস

