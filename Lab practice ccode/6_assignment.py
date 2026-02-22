import cv2
import matplotlib.pyplot as plt
import numpy as np


# =====================================================
# Manual Convolution Function (Same + Valid)
# =====================================================
def manual_filter2D(image, kernel, mode='same'):

    img_h, img_w = image.shape
    k_h, k_w = kernel.shape

    # Flip kernel (true convolution)
    kernel = np.flipud(np.fliplr(kernel))

    if mode == 'same':
        pad_h = k_h // 2
        pad_w = k_w // 2

        padded_img = np.pad(image,
                            ((pad_h, pad_h), (pad_w, pad_w)),
                            mode='constant',
                            constant_values=0)

        output = np.zeros((img_h, img_w))

        for i in range(img_h):
            for j in range(img_w):
                region = padded_img[i:i+k_h, j:j+k_w]
                output[i, j] = np.sum(region * kernel)

    elif mode == 'valid':

        out_h = img_h - k_h + 1
        out_w = img_w - k_w + 1

        output = np.zeros((out_h, out_w))

        for i in range(out_h):
            for j in range(out_w):
                region = image[i:i+k_h, j:j+k_w]
                output[i, j] = np.sum(region * kernel)

    return output


# =====================================================
# Kernels
# =====================================================

kernel_avg = np.ones((3,3), dtype=np.float32) / 9

sobel_x = np.array([[-1,0,1],
                    [-2,0,2],
                    [-1,0,1]])

sobel_y = np.array([[-1,-2,-1],
                    [0,0,0],
                    [1,2,1]])

prewitt_x = np.array([[-1,0,1],
                      [-1,0,1],
                      [-1,0,1]])

prewitt_y = np.array([[-1,-1,-1],
                      [0,0,0],
                      [1,1,1]])

scharr_x = np.array([[-3,0,3],
                     [-10,0,10],
                     [-3,0,3]])

scharr_y = np.array([[-3,-10,-3],
                     [0,0,0],
                     [3,10,3]])

laplace = np.array([[0,-1,0],
                    [-1,4,-1],
                    [0,-1,0]])

# Custom kernels
custom1 = np.array([[1,-1,1],
                    [-1,1,-1],
                    [1,-1,1]])

custom2 = np.array([[0,1,0],
                    [1,-4,1],
                    [0,1,0]])

custom3 = np.array([[2,-1,0],
                    [-1,0,1],
                    [0,1,-2]])

custom4 = np.array([[1,2,1],
                    [0,0,0],
                    [-1,-2,-1]])


# =====================================================
# MAIN
# =====================================================
def main():

    img = cv2.imread("flower_img.png", cv2.IMREAD_GRAYSCALE)

    kernels = {
        "Average": kernel_avg,
        "Sobel X": sobel_x,
        "Sobel Y": sobel_y,
        "Prewitt X": prewitt_x,
        "Prewitt Y": prewitt_y,
        "Scharr X": scharr_x,
        "Scharr Y": scharr_y,
        "Laplace": laplace
    }

    plt.figure(figsize=(20, 14))

    # Show original
    plt.subplot(4,5,1)
    plt.imshow(img, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    index = 2

    for name, kernel in kernels.items():

        # SAME
        result_same = manual_filter2D(img, kernel, mode='same')
        result_same = np.clip(result_same, 0, 255).astype(np.uint8)

        # VALID
        result_valid = manual_filter2D(img, kernel, mode='valid')
        result_valid = np.clip(result_valid, 0, 255).astype(np.uint8)

        # Show SAME
        plt.subplot(4,5,index)
        plt.imshow(result_same, cmap='gray')
        plt.title(name + " (Same)")
        plt.axis('off')
        index += 1

        # Show VALID
        plt.subplot(4,5,index)
        plt.imshow(result_valid, cmap='gray')
        plt.title(name + " (Valid)")
        plt.axis('off')
        index += 1

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()