[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/hazkaz/bitplaning-and-thresholding/blob/master/)

# Bitplaning in Python

[Bitplaning](https://www.wikiwand.com/en/Bit_plane) means to extract information of an image
along only a single bit position. In case of multiple bit positions, you can choose to either binary threshold it to see more clearly
the lower intensity bits. Bitplaning along all planes simultaneously without thresholding it will give
you back the original image.

This module allows you to extract from single/multiple bit positions.

### Installation

Copy the bitplaning module (bitplane.py) to your working directory and import it

```python
import bitplane
```

### Usage

##### Python usage

1. Read the image using openCV in grayscale
2. Pass the image to bitplane.bit_plane
3. (Optional) perform intensity thresholding with bitplane.threshold_image

```python
img = cv2.imread(args.image_file, 0)
bitplaned_img = bit_plane(img, planes)
```

##### Command-line interface

###### Usage
```bash
python bitplane.py <input-image> --bitplane [...planes to bitplane(0-7)]
```

###### Example
```bash
# bitplane along Most significant bit
python bitplane.py test2.png --bitplane 7
```


### Sample output

##### Input Image

[[https://github.com/hazkaz/bitplaning-and-thresholding/blob/master/test2.jpg|alt=input-image]]

##### Bitplaned Output

[[https://github.com/hazkaz/bitplaning-and-thresholding/blob/master/sample.png|alt=bitplaned-output-image]]