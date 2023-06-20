import cv2
import numpy as np
# Load the knee OA image
img = cv2.imread('image.jpeg', cv2.IMREAD_COLOR)

# Convert the image to grays
# cale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter to smooth the image while preserving edges
gray_filtered = cv2.bilateralFilter(gray, 5, 75, 75)

# Apply Otsu's thresholding to segment the bone and cartilage regions
_, thresholded = cv2.threshold(gray_filtered, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply morphological closing to fill in gaps in the cartilage region
kernel = np.ones((5, 5), np.uint8)
closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

# Invert the closing mask to obtain a mask of all parts except the cartilage region
mask = cv2.bitwise_not(closing)

# Create a three-channel image with all white pixels
white_image = np.ones((img.shape[0], img.shape[1], 3), np.uint8) * 255

# Apply the mask to make all bone parts black
white_image[mask == 255] = [0, 0, 0]
# cv2.imshow(cv2.cvtColor(heat, cv2.COLOR_BGR2RGB))
# Display the original and processed images
cv2.imshow('Original', img)
cv2.imshow( white_image,cmap = "rainbow")
cv2.waitKey(0)
cv2.destroyAllWindows()
