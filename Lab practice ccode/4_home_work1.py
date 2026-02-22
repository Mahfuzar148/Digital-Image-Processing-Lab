import cv2
import matplotlib.pyplot as plt
import numpy as np

limit1 = 100
limit2 = 180

# ---------------- Histogram ----------------
def histogram(img):
    return np.bincount(img.ravel(), minlength=256)

# ---------------- Step Threshold 1 ----------------
def step1(img):
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] >= limit1:
                out[i,j] = 255
    return out

# ---------------- Step Threshold 2 ----------------
def step2(img):
    out = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if limit1 <= img[i,j] <= limit2:
                out[i,j] = 127
    return out

# ---------------- Step Threshold 3 ----------------
def step3(img):
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] < limit1:
                out[i,j] = 0
            elif limit1 <= img[i,j] <= limit2:
                out[i,j] = 127
            else:
                out[i,j] = 255
    return out

# ---------------- Log Transformation ----------------
def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    return (c * np.log(1 + img)).astype(np.uint8)

# ---------------- Gamma Transformation ----------------
def gamma_transform(img, gamma=0.5):
    normalized = img / 255.0
    return np.uint8(255 * (normalized ** gamma))

# ---------------- Main ----------------
def main():
    img = cv2.imread("flower.png", 0)

    img1 = step1(img)
    img2 = step2(img)
    img3 = step3(img)
    img4 = log_transform(img)
    img5 = gamma_transform(img, 0.5)

    images = [img, img1, img2, img3, img4, img5]
    titles = ["Original",
              "Step Threshold 1",
              "Step Threshold 2",
              "Step Threshold 3",
              "Log Transform",
              "Gamma Transform"]

    plt.figure(figsize=(15,10))

    for i in range(len(images)):
        plt.subplot(3,4,i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis('off')

        plt.subplot(3,4,i+7)
        plt.bar(range(256), histogram(images[i]))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()