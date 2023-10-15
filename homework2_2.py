#MSSV: N20DCCN134
#HO VA TEN: TRỊNH THANH SƠN
import cv2
help(cv2.imread)
help(cv2.imwrite)

J1 = cv2.imread("img/homework2/lena512color.jpg")
J2 = 255 - J1
cv2.imshow("Original Image", J1)
cv2.imshow("J2 (Photographic Negative)", J2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("img/homework2/Lena.jpg", J2)
