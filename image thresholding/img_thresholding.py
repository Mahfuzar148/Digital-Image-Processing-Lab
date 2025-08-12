import cv2
import matplotlib.pyplot as plt
import numpy as np


# ---------- Function Definitions ----------
def function1(img):
    """0–128 => 0, else => 255"""
    output = np.where(img <= 128, 0, 255)
    return output

def function2(img):
    """
    0–127 => original value
    127–190 => 127
    >190 => 255
    """
    output = np.copy(img)
    output[(img >= 127) & (img <= 190)] = 127
    output[img > 190] = 255
    return output

def function3(img):
    """
    0–100 => original value
    100–150 => 120
    150–180 => original value
    180–220 => 220
    >220 => 255
    """
    output = np.copy(img)
    output[(img >= 100) & (img <= 150)] = 120
    output[(img >= 180) & (img <= 220)] = 220
    output[img > 220] = 255
    return output

# ---------- Load Images ----------
img1 = cv2.imread("images/img1.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("images/img2.png", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("images/img3.png", cv2.IMREAD_GRAYSCALE)



# ---------- Process Images ----------
images = [img1, img2, img3]
funcs = [function1, function2, function3]
func_names = ["Function 1", "Function 2", "Function 3"]

# ---------- Plot ----------
plt.figure(figsize=(16, 12))

for i, img in enumerate(images):  # For each image (row)
    # Plot original image
    plt.subplot(len(images), 4, i*4 + 1)
    plt.imshow(img, cmap='gray')
    plt.title(f" Original Image {i+1} ")
    plt.axis('off')

    # Plot function results
    for j, func in enumerate(funcs):
        processed_img = func(img)
        plt.subplot(len(images), 4, i*4 + 2 + j)
        plt.imshow(processed_img, cmap='gray')
        plt.title(func_names[j])
        plt.axis('off')

plt.subplots_adjust(hspace=0.1,wspace=0.1)
plt.savefig("img_threshold_output.png",dpi=300,bbox_inches='tight')
plt.show()

