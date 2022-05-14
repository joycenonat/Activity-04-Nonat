import cv2
filepath = "original.jpg"
image = cv2.imread(filepath,1)
cv2.imshow("Nonat",image)
cv2.waitkey(0)
cv2.destroyAllWindows()