import cv2

img = cv2.imread("input.jpg")
if img is None:
    raise FileNotFoundError("Put an image named input.jpg in this folder.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

cv2.imwrite("gray.jpg", gray)
cv2.imwrite("edges.jpg", edges)

print("Saved gray.jpg and edges.jpg")
