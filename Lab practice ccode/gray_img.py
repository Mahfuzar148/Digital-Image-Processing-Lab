import matplotlib.pyplot as plt

img = plt.imread("flower.png")

# RGB → Gray conversion
gray = 0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]

print(gray.shape)  # (H, W)

plt.imshow(gray, cmap='gray')
plt.axis('off')
plt.title("Grayscale Image")
plt.show()
