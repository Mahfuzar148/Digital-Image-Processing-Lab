import cv2
import matplotlib.pyplot as plt

img = cv2.imread("flower.png")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


img1 = plt.imread("flower.png")
gray_img1 = 0.299*img1[:,:,0] + 0.587*img1[:,:,1] + 0.114*img1[:,:,2]

plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.imshow(gray_img,cmap='gray')
plt.axis("off")

plt.subplot(2,1,2)
plt.imshow(gray_img1,cmap='gray')
plt.axis('off')

plt.show()

