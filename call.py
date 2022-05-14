import cv2
import os

while True:
	imgnme = input("\n Image name [put '.jpg' at the end of the name]: " )
	flag = input("\n Choose [0] for gray image or [1] for colored image: ")

	if os.path.exists(imgnme) and flag == '0':
		image= cv2.imread(imgnme, 0)
		cv2.imshow(imgnme, image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		break
	elif os.path.exists(imgnme) and flag == '1':
		image= cv2.imread(imgnme, 1)
		cv2.imshow(imgnme, image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()