
---
# 🖼️ Image Channel Visualizer & Negative Image Generator

This Python script uses `matplotlib` and `NumPy` to:

- Load and display a color image
- Extract and visualize Red, Green, and Blue channels separately
- Generate and show the **negative** version of the image
- Demonstrate practical usage of **NumPy slicing** for image processing

---

## 🚀 Features

- ✅ Works with RGB and RGBA images
- 🎨 Separates image into Red, Green, and Blue channels
- 🔁 Creates a negative version using pixel inversion
- 🖼️ Uses subplot layout to compare original, channels, and negative

---

## 📸 Output Views

- Original Image  
- Red Channel (`cmap='Reds'`)  
- Green Channel (`cmap='Greens'`)  
- Blue Channel (`cmap='Blues'`)  
- Negative Image (`255 - pixel`)

---

## ▶️ How to Run

```bash
python image_channel_and_negative_visualizer.py
````

> ⚠️ Make sure the image path inside the script is valid (e.g., `'F:/6TH SEMISTER/Python Code/OIF.jpeg'`)

---

## 📦 Requirements

Install the required package using:

```bash
pip install matplotlib
```

NumPy is included with matplotlib, so no need to install separately in most cases.

---

## 🧠 Educational Use

This project is great for students and beginners who want to learn:

* ✅ How RGB images are structured in NumPy arrays
* ✅ How to apply slicing (`img[row, col, channel]`)
* ✅ How to visualize each channel and create image effects
* ✅ Basic use of `matplotlib.pyplot` for image display

---

## 📂 File Overview

| File Name                                  | Description                               |
| ------------------------------------------ | ----------------------------------------- |
| `image_channel_and_negative_visualizer.py` | Main script file                          |
| `OIF.jpeg` *(optional)*                    | Sample image file (update path as needed) |

---

## 👤 Author

**Md. Mahfuzar Rahman**
*Created for learning and sharing image processing concepts with Python and NumPy.*

---

## 📝 License

This project is open-source and free to use for **educational and personal learning** purposes.
Feel free to modify, improve, and share!



