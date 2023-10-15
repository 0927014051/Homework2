#MSSV: N20DCCN134
#HO VA TEN: TRỊNH THANH SƠN
import numpy as np
import matplotlib.pyplot as plt
lena_data = np.fromfile('img/homework2/lena.bin', dtype=np.uint8).reshape(256, 256)
peppers_data = np.fromfile('img/homework2/peppers.bin', dtype=np.uint8).reshape(256, 256)
width, height = 256,256

lena_img = lena_data.reshape(height,width)
peppers_img = peppers_data.reshape(height,width)
plt.figure()
plt.subplot(121)
plt.imshow(lena_img, cmap='gray')
plt.title('Lena Image')

plt.subplot(122)
plt.imshow(peppers_img, cmap='gray')
plt.title('Peppers Image')

plt.show()

J = np.zeros((256, 256), dtype=np.uint8)
J[:, :128] = lena_data[:, :128]
J[:, 128:] = peppers_data[:, 128:]

plt.figure()
plt.imshow(J, cmap='gray')
plt.title('Image J')

plt.show()

K = np.zeros((256, 256), dtype=np.uint8)
K[:, :128] = J[:, 128:]
K[:, 128:] = J[:, :128]

plt.figure()
plt.imshow(K, cmap='gray')
plt.title('Image K')


plt.show()
