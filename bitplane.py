import numpy as np
import cv2
import sys
import argparse
from matplotlib import pyplot as plt


def int_to_bit_array(img):
	list = []
	rows, cols = img.shape
	for i in range(rows):
		for j in range(cols):
			list.append(np.binary_repr(img[i][j], width=8))
	return list


def extract_planes(binary_value, planes):
	acc = []
	for pos in (x for x in planes):
		planePowerOfTwo = pow(2, pos)
		bitPlaneValue = int(binary_value, 2) & planePowerOfTwo
		acc.append(bitPlaneValue)
	return sum(acc)


def bit_plane(image, plane):
	bitplaned_image = []
	for b in image:
		bitplaned_image.append(extract_planes(b, plane))
	return np.array(bitplaned_image,dtype='uint8')


def remove_value(image, start, end=255):
	bitplaned_image = []
	for b in image:
		bitplaned_image.append(int(b, 2)
							   if (int(b, 2) > start) and (int(b, 2) < end) else 0)
	return bitplaned_image


def main():
	parser = argparse.ArgumentParser(
		description='Bitplane or Threshold an image file in greyscale')
	parser.add_argument('image_file', type=str, help='file to bitplane')
	parser.add_argument('--bitplanes', type=int,
						nargs='+', help='planes to select')
	parser.add_argument('--threshold', nargs=2, type=int,
						help='threshold low and high values')
	args = parser.parse_args()

	# Read image in grayscale
	img = cv2.imread(args.image_file, 0)
	rows, cols = img.shape

	# convert to 1D array
	img_in_1D = int_to_bit_array(img)

	planes = args.bitplanes
	threshold = args.threshold
	if(planes != None):
		# extract required planes and convert back to 2D
		bitplaned_img_in_1D = bit_plane(img_in_1D, planes)
		bitplaned_img_in_2D = np.reshape(bitplaned_img_in_1D, (rows, cols))
		equ = cv2.equalizeHist(bitplaned_img_in_2D)
		res = np.hstack((bitplaned_img_in_2D,img,equ)) #stacking images side-by-side
		output_file_name = "bitplaned-out"+"-".join(map(lambda x: str(x), planes))+".jpeg"
		print("writing bitplaned image to " + output_file_name)
		cv2.imwrite(output_file_name, res)
		plt.imshow(res,cmap='gray',vmin=0,vmax=255)
		plt.show()

	if(threshold != None):
		# extract required pixels and convert back to 2D
		threshold_image_in_1D = remove_value(
			img_in_1D, threshold[0], threshold[1])
		threshold_image_in_2D = np.reshape(threshold_image_in_1D, (rows, cols))
		output_file_name = "threshold-out"+"-".join(map(lambda x: str(x), threshold))+".jpeg"
		print("writing thresholded image to " + output_file_name)
		cv2.imwrite(output_file_name, threshold_image_in_2D)
		plt.imshow(threshold_image_in_2D)

	# plt.plot(cv2.calcHist([img],[0],None,[256],[0,256]))
	# # plt.hist(img.ravel(),256,[0,256])
	# plt.show()


if __name__ == "__main__":
	main()
