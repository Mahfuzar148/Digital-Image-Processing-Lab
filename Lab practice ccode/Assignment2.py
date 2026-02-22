import matplotlib.pyplot as plt
import numpy as np

# Image size
h, w = 200, 200

# 3 shades (dark → medium → full)
shades = [85, 170, 255]

# RGB base colors
colors = {
    "White":   [1, 1, 1],
    "Red":     [1, 0, 0],
    "Green":   [0, 1, 0],
    "Blue":    [0, 0, 1],
    "Cyan":    [0, 1, 1],
    "Magenta": [1, 0, 1],
    "Yellow":  [1, 1, 0]
}

plt.figure(figsize=(8, 12))

# Loop through each color
for row, (name, base) in enumerate(colors.items()):
    
    # Loop through each shade
    for col, s in enumerate(shades):
        
        # Create black image
        img = np.zeros((h, w, 3), dtype=np.uint8)
        
        # Apply shade
        img[:, :, 0] = base[0] * s
        img[:, :, 1] = base[1] * s
        img[:, :, 2] = base[2] * s
        
        # Display in subplot
        plt.subplot(len(colors), 3, row*3 + col + 1)
        plt.imshow(img)
        plt.title(f"{name}\nShade {s}")
        plt.axis("off")

plt.tight_layout()
plt.show()
