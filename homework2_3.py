#MSSV: N20DCCN134
#HO VA TEN: TRỊNH THANH SƠN
import cv2
J1 = cv2.imread("img/homework2/lena512color.jpg")
cv2.imshow("J1", J1)
cv2.waitKey(0)
cv2.destroyAllWindows()
J2 = J1.copy()
J2[:, :, 0] = J1[:, :, 2]
J2[:, :, 1] = J1[:, :, 0]
J2[:, :, 2] = J1[:, :, 1]
cv2.imshow("Original Image", J1)
cv2.imshow("J2 - Swapped Image", J2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("img/homework2/lena512color_swapped.jpg", J2)
