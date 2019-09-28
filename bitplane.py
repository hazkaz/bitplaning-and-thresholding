import numpy as np
import cv2
import argparse


def _int_to_bit_array(img):
    bit_array = []
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            bit_array.append(np.binary_repr(img[i][j], width=8))
    return bit_array


def _extract_planes(binary_value, planes, binary_threshold):
    acc = []
    for pos in planes:
        plane_power_of_two = pow(2, pos)
        bit_plane_value = int(binary_value, 2) & plane_power_of_two
        acc.append(bit_plane_value)
    if binary_threshold:
        return 255 if sum(acc) > 0 else 0
    else:
        return sum(acc)


def bit_plane(image, planes, binary_threshold=True):
    img_in_1_d = _int_to_bit_array(image)
    bitplaned_image = []
    for b in img_in_1_d:
        bitplaned_image.append(_extract_planes(b, planes, binary_threshold))
    bitplaned_img_in_1_d = np.array(bitplaned_image, dtype='uint8')
    bitplaned_img_in_2_d = np.reshape(bitplaned_img_in_1_d, image.shape)
    return bitplaned_img_in_2_d


def threshold_image(image, start, end=255, binary_threshold=True):
    threshold_image_values = []
    if binary_threshold:
        for b in image.reshape(-1):
            threshold_image_values.append(255 if (b > start) and (b < end) else 0)
    else:
        for b in image.reshape(-1):
            threshold_image_values.append(b if (b > start) and (b < end) else 0)
    threshold_image_in_1_d = np.array(threshold_image_values, dtype='uint8')
    threshold_image_in_2_d = np.reshape(threshold_image_in_1_d, image.shape)
    return threshold_image_in_2_d


def main():
    parser = argparse.ArgumentParser(
        description='Bitplane or Threshold an image file in greyscale')
    parser.add_argument('image_file', type=str, help='file to bitplane')
    parser.add_argument('--bitplanes', type=int,
                        nargs='+', help='planes to select')
    parser.add_argument('--threshold', nargs=2, type=int,
                        help='threshold low and high values')
    args = parser.parse_args()

    # Read image in gray-scale
    img = cv2.imread(args.image_file, 0)

    planes = args.bitplanes
    threshold = args.threshold

    if planes is not None:
        # extract required planes and convert back to 2D
        bitplaned_img = bit_plane(img, planes)
        output_file_name = "bitplaned-out" + \
                           "-".join(map(lambda x: str(x), planes)) + ".jpeg"
        print("writing bitplaned image to " + output_file_name)
        cv2.imwrite(output_file_name, bitplaned_img)

    if threshold is not None:
        # extract required pixels and convert back to 2D
        threshold_image_value = threshold_image(img, threshold[0], threshold[1])
        output_file_name = "threshold-out" + \
                           "-".join(map(lambda x: str(x), threshold)) + ".jpeg"
        print("writing thresholded image to " + output_file_name)
        cv2.imwrite(output_file_name, threshold_image_value)


if __name__ == "__main__":
    main()
