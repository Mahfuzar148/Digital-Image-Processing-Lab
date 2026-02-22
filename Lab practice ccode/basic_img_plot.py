
import matplotlib.pyplot as plt


def main():
    img_path = "flower.png"
    img = plt.imread(img_path)
    
    print(img.shape)
    
    print(img[:5,:5,0]) # 5 pixel value of red channel
    print(img[:5,:5,1]) # 5 pixel value of green channel
    print(img[:5,:5,2]) # 5 pixel value of blue channel
    print(f"Max pixel value : {img.max()} ")
    print(f"Min pixel value : {img.min()}")
    
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()