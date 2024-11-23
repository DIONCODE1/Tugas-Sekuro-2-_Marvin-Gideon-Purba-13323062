import cv2
import numpy as np

# Load the image
image = cv2.imread("frame_0000.png")

# Create a blank mask with the same dimensions as the image (grayscale)
mask = np.zeros(image.shape[:2], dtype="uint8")

# Define a circular region (center, radius)
center = (image.shape[1] // 2, image.shape[0] // 2)  # center of the image
radius = 100  # radius in pixels

# Draw the circle on the mask (255 is white, the mask area)
cv2.circle(mask, center, radius, 255, -1)

# Apply the mask using bitwise_and
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Show the original image, mask, and result
cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
