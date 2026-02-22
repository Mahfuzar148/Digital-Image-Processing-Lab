import matplotlib.pyplot as plt


def main():
    
    img_path = "flower.png"
    img = plt.imread(img_path)
    
    
    neg_img = img.max()-img
    
    red_img = img[:,:,0]
    green_img = img[:,:,1]
    blue_img = img[:,:,2]
    
    
    plt.figure(figsize=(16,8))
    
    plt.subplot(3,2,1)
    plt.title("Original image")
    plt.imshow(img)
    plt.axis('off')
    
    plt.subplot(3,2,2)
    plt.title("Negative image")
    plt.imshow(neg_img)
    plt.axis('off')
    
    plt.subplot(3,2,3)
    plt.title("Red channel image")
    plt.imshow(red_img,cmap='Reds')
    plt.axis('off')
    
    plt.subplot(3,2,4)
    plt.title("Green image")
    plt.imshow(green_img,cmap='Greens')
    plt.axis('off')
    
    plt.subplot(3,2,5)
    plt.title("Blue image")
    plt.imshow(blue_img,cmap='Blues')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    plt.close()
  
    
if __name__ == "__main__":
    main()