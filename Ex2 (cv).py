import cv2

# Load the image
image = cv2.imread(r"C:\Users\paulo\Desktop\pasta\print.png")

# Display the image
cv2.imshow("Image", image)

# Wait for the user to press a key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()