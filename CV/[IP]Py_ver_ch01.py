import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
sujihye = cv2.imread('./goddess.jpg')



b, g, r = cv2.split(sujihye)
image2 =cv2.merge([r,g,b])

grayScale=np.uint8((r*0.3+g*0.6+b*0.1))
skimage.io.imshow(grayScale)
