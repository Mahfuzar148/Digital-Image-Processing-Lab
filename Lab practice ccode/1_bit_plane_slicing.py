import cv2
import matplotlib.pyplot as plt
import numpy as np


def bit_plane_slicing(img):
    bit_planes= []
    weighted_planes = []
    for i in range(8):
        bit = (img>>i)&1
        visual_plane = bit*255
        weighted_plane = bit*(2**i)
        bit_planes.append(visual_plane)
        weighted_planes.append(weighted_plane)
    return bit_planes,weighted_planes

def main():
    img = cv2.imread('flower.png',0)
    
    bit_planes,weighted_planes = bit_plane_slicing(img)
    
    reconstructed = np.zeros_like(img).astype(np.uint8)
    for i in weighted_planes:
        reconstructed +=i
    
    plt.figure(figsize=(18,12))
    
    plt.subplot(5,2,1)
    plt.title('Original image')
    plt.imshow(img,cmap='gray')
    plt.axis('off')
    
    plt.subplot(5,2,2)
    plt.title('Reconstructed image')
    plt.imshow(reconstructed,cmap='gray')
    plt.axis('off')
    
    for i in range(8):
        
        plt.subplot(5,2,i+3)
        plt.title(f'bit_plane{i+1}')
        plt.imshow(bit_planes[i],cmap='gray')
        plt.axis('off')
    
    
    plt.tight_layout()
    plt.show()
    

if __name__ == '__main__' :
    main()    