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
        plt.title(f'{color_name.capitalize()} Image {s}',fontsize=10)
        plt.axis('off')
        index += 1
plt.savefig('color_shade.png', bbox_inches='tight')  # Save the figure
plt.subplots_adjust(hspace=0.6,wspace=0.1)  # Adjust subplots to fit
plt.show()