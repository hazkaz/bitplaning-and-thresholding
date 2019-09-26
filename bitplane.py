import numpy as np
import cv2
import sys
import argparse
from matplotlib import pyplot as plt

def intToBitArray(img):
    list = []
    for i in range(rows):
        for j in range(cols):
            list.append(np.binary_repr(img[i][j], width=8))

    return list


def xorPlane(binary_value, planes):
    acc = []
    for pos in (int(x) for x in planes):
        planePowerOfTwo = pow(2, pos)
        bitPlaneValue = int(binary_value, 2) & planePowerOfTwo
        acc.append(bitPlaneValue)
    return sum(acc)


def bitPlane(image, plane):
    bitplaned_image = []
    for b in image:
        bitplaned_image.append(xorPlane(b, plane))
    return bitplaned_image


def removeValue(image,start,end=255):
	bitplaned_image = []
	for b in image:
		bitplaned_image.append(int(b,2) if (int(b,2)>int(start) and int(b,2)<int(end)) else 0)
	return bitplaned_image	

parser = argparse.ArgumentParser(
    description='Bitplane an image file in greyscale')
parser.add_argument('image_file', type=str, help='file to bitplane')
parser.add_argument('bitplanes', nargs='+', help='planes to select')
args = parser.parse_args()

img = cv2.imread(args.image_file,0)
planes = args.bitplanes
rows, cols = img.shape
imgIn1D = intToBitArray(img)
imgIn1D = removeValue(imgIn1D, planes[0],planes[1])
imgIn2D = np.reshape(imgIn1D, (rows, cols))
print(imgIn2D.shape)
cv2.imwrite("out"+"-".join(planes)+".jpeg", imgIn2D)
# plt.plot(cv2.calcHist([img],[0],None,[256],[0,256]))
# # plt.hist(img.ravel(),256,[0,256])
# plt.show()