import numpy as np
import cv2

#create a image array
img = cv2.imread("WIN_20170511_13_06_18_Pro.jpg",cv2.IMREAD_GRAYSCALE)
row ,col = img.shape
#convert each interger pixel value of given image to a bit pixel value of 8-
 #bits
def intToBitArray(img) :
    list = []

    for i in range(row):
        for j in range(col):
             list.append (np.binary_repr( img[i][j] ,width=8  ) )

    return list #the binary_repr() fucntion returns binary values but in 
                #string 
                #, not integer, which has it's own perk as you will notice   

 #as variable name says ,it's list of pixel values in binary , but in 1 
 #dimension
imgIn1D = intToBitArray(img)
#reshaping above 1D array to a matrix aka image
imgIn2D = np.reshape(imgIn1D , (360,640) )
def bitplane(bitImgVal , img1D ):

'''
this function extracts the specific bit out of each binary pixel values of 
the matrix
for example , if bitImgVal = 3 , then , third bit of each pixel is extracted

:param bitImgVal: specifies the position of bit to be extracted
:param img1D: image which is to be compressed
:return: now returns 1 dimensional list of bits
'''
    bitList = [  int(   i[bitImgVal]  )    for i in img1D]

    return bitList
#i don't know why but the multiplication factor is : 2^(n-1) where n is the 
bit number
#example, if binary pixel value is 11001010 and n = 3 , factor = 2^(3-1)
#image represented by 8th bit plane
eightbitimg = np.array( bitplane(0, imgIn1D ) ) * 128

#image represented by 7th bit plane
sevenbitimg = np.array( bitplane(1,imgIn1D) ) * 64

#bitplane of 8th and 7th bit
combine = eightbitimg + sevenbitimg
comb = np.reshape(combine,(row,col))

#save combined plane image
cv2.imwrite("comb.jpeg",comb)

#save eight bit plane
eightbitimg = np.reshape(eightbitimg,(row,col))
cv2.imwrite("8bitvalue.jpg" , eightbitimg )

#save eight bit plane
sevenbitimg = np.reshape(sevenbitimg,(row,col))
cv2.imwrite("7bitvalue.jpg",sevenbitimg)

#grayscale version of original image
gray = cv2.imread("WIN_20170511_13_06_18_Pro.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("gray.jpeg",gray)