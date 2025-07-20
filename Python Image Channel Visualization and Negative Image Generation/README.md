# 🖼️ Image Channel Visualizer & Negative Image Generator

This Python script uses `matplotlib` and `NumPy` to:

- Load and display a color image
- Extract and visualize Red, Green, and Blue channels separately
- Create and show a **negative** of the image
- Demonstrate **NumPy slicing** and basic image manipulation

---

## 🚀 Features

- ✅ Works with RGB and RGBA images
- 🎨 Separates image into individual R, G, B channels
- 🔁 Converts image to negative using NumPy logic
- 🖼️ Subplot layout for easy comparison

---

## 📸 Sample Views

- ✅ Original Image  
- 🔴 Red Channel (`cmap='Reds'`)  
- 🟢 Green Channel (`cmap='Greens'`)  
- 🔵 Blue Channel (`cmap='Blues'`)  
- 🖤 Negative Image (`255 - original_pixel`)

---

## ▶️ How to Run

```bash
python image_channel_and_negative_visualizer.py
