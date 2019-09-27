import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test2.png', 0)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
# plt.show()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]
hist, bins = np.histogram(img2.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()
plt.plot(cdf_normalized, color='y')
plt.hist(img2.flatten(), 256, [0, 256], color='g')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')

plt.show()
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(2, 2))
cl1 = clahe.apply(img)
plt.imshow(np.hstack((img, img2, cl1)), cmap='gray')
plt.show()
