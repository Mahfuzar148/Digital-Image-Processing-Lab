
---

### ✅ Python Code (with OpenCV and Matplotlib):

```python
import cv2
import matplotlib.pyplot as plt

# Load the images using OpenCV (BGR format by default)
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')

# Convert BGR to RGB for correct color display in matplotlib
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Set up a figure with specified size
plt.figure(figsize=(10,5))

# Display the first image
plt.subplot(1, 2, 1)  # (rows, columns, position)
plt.imshow(img1)
plt.title('Image 1')
plt.axis('off')  # Hide axis ticks

# Display the second image
plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.title('Image 2')
plt.axis('off')

# Show the figure window
plt.show()
```

---

### 📄 Documentation / Explanation:

#### 📌 1. **Import Required Libraries**

```python
import cv2
import matplotlib.pyplot as plt
```

* `cv2`: OpenCV library for image reading and processing.
* `matplotlib.pyplot`: Used for plotting and visualizing images inline (especially in Jupyter Notebook).

---

#### 📌 2. **Image Loading**

```python
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
```

* `cv2.imread()` reads the image in **BGR format** by default.
* `'img1.png'` and `'img2.png'` should be in the **same folder as your code** or provide full path.

---

#### 📌 3. **Color Conversion (BGR to RGB)**

```python
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
```

* Converts BGR (OpenCV default) to RGB, because **Matplotlib expects RGB** for correct display.
* Without this step, the colors will look incorrect (e.g., blue appears red).

---

#### 📌 4. **Plot Configuration**

```python
plt.figure(figsize=(10,5))
```

* Initializes the figure.
* `figsize=(10,5)` sets the window size: 10 inches wide × 5 inches tall.

---

#### 📌 5. **Displaying Images Side-by-Side**

```python
plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.title('Image 1')
plt.axis('off')
```

* `subplot(1,2,1)`: 1 row, 2 columns, show image in 1st position.
* `imshow(img1)`: displays the image.
* `axis('off')`: removes axis tick marks.

Same logic is repeated for `img2` in the second position.

---

#### 📌 6. **Show the Plot Window**

```python
plt.show()
```

* Renders the final plot with both images displayed side-by-side.

---
