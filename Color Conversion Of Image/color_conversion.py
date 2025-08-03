import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('F:/7th semister/DIP LAB/image/scenery1.png')

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


white_img = np.ones_like(img)*255  # Create a white image

black_img = np.zeros_like(img)   # Create a black image

red_img = np.copy(white_img)
red_img[:,:,1] = 0  # Set green channel to 0
red_img[:,:,2] = 0  # Set blue channel to 0

# Create a green image
green_img = np.copy(white_img)
green_img[:,:,0] = 0  # Set red channel to 0
green_img[:,:,2] = 0  # Set blue channel to 0

blue_img = np.copy(black_img)
blue_img[:,:,2] = 255  # Set blue channel to 255

intensity_values = [20, 50, 80,120,160,180,200,220,230,255]  # Red intensity steps




plt.figure(figsize=(30,25))

# Original image
plt.subplot(5,10,1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Black image
plt.subplot(5,10,2)
plt.imshow(black_img)
plt.title('Black Image')
plt.axis('off')

# White image
plt.subplot(5,10,3)
plt.imshow(white_img)
plt.title('White Image')
plt.axis('off')



# Red-tinted image

for i,intensity in enumerate(intensity_values):
    red_img[:,:,0] = intensity  # Set red channel intensity
    
    plt.subplot(5,10,4+i)
    plt.imshow(red_img)
    plt.title(f'Red {intensity}')
    plt.axis('off')

# Green-tinted image
for i,intensity in enumerate(intensity_values):
    green_img[:,:,1] = intensity  # Set green channel intensity
    
    plt.subplot(5,10,14+i)
    plt.imshow(green_img)
    plt.title(f'Green {intensity}')
    plt.axis('off')

# Blue-tinted image
for i,intensity in enumerate(intensity_values):
    blue_img[:,:,2] = intensity  # Set blue channel intensity
    
    plt.subplot(5,10,24+i)
    plt.imshow(blue_img)
    plt.title(f'Blue {intensity}')
    plt.axis('off')
    
#plt.savefig('color_conversion.png', dpi=300,bbox_inches='tight')  # Save the figure as a PNG file
    
plt.tight_layout()
plt.show()
