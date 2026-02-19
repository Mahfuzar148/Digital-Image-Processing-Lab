import cv2
import numpy as np

# Constants
WIDTH, HEIGHT = 320, 240
HIST_HEIGHT = 150
TITLE_HEIGHT = 30
FONT = cv2.FONT_HERSHEY_SIMPLEX


# Draw histogram function
def draw_histogram(image, width=WIDTH, height=HIST_HEIGHT):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist = cv2.normalize(hist, hist, 0, height, cv2.NORM_MINMAX).flatten()

    hist_img = np.zeros((height, width), dtype=np.uint8)
    bin_w = width // 256

    for i in range(256):
        x = i * bin_w
        y = int(hist[i])
        cv2.line(hist_img, (x, height), (x, height - y), 255, thickness=bin_w)

    return cv2.cvtColor(hist_img, cv2.COLOR_GRAY2BGR)


# Add title above image
def add_title(image, title, height=TITLE_HEIGHT, width=WIDTH):
    title_img = np.zeros((height, width, 3), dtype=np.uint8)

    text_size = cv2.getTextSize(title, FONT, 0.6, 2)[0]
    x = (width - text_size[0]) // 2
    y = (height + text_size[1]) // 2

    cv2.putText(title_img, title, (x, y),
                FONT, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

    return np.vstack((title_img, image))


# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (WIDTH, HEIGHT))

    # ===== Original =====
    orig_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    orig_hist = draw_histogram(orig_gray)
    orig_stack = np.vstack((frame, orig_hist))
    orig_stack = add_title(orig_stack, "Original")

    # ===== Linear Mapping (Brightened) =====
    bright = cv2.convertScaleAbs(frame, alpha=1.2, beta=50)
    bright_gray = cv2.cvtColor(bright, cv2.COLOR_BGR2GRAY)
    bright_hist = draw_histogram(bright_gray)
    bright_stack = np.vstack((bright, bright_hist))
    bright_stack = add_title(bright_stack, "Brightened (Linear)")

    # ===== Nonlinear Mapping (Negative) =====
    negative = cv2.bitwise_not(frame)
    negative_gray = cv2.cvtColor(negative, cv2.COLOR_BGR2GRAY)
    negative_hist = draw_histogram(negative_gray)
    negative_stack = np.vstack((negative, negative_hist))
    negative_stack = add_title(negative_stack, "Negative (Nonlinear)")

    # ===== Grayscale =====
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    gray_hist = draw_histogram(gray)
    gray_stack = np.vstack((gray_bgr, gray_hist))
    gray_stack = add_title(gray_stack, "Grayscale")

    # ===== Combine All Frames =====
    final = np.hstack((orig_stack, bright_stack, negative_stack, gray_stack))

    # Show output
    cv2.imshow("Face + Linear & Nonlinear Mappings with Histograms", final)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
