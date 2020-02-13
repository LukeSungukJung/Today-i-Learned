import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np

sujihye = cv2.imread('./goddess.jpg')

b, g, r = cv2.split(sujihye)
original = cv2.merge([r,g,b])

#skimage.io.imshow(original)



def customCDF(img):
    r_hist_array = np.zeros(256)
    
    for r in img[0]:
        r_hist_array[img[r]]+=1
    g_hist_array = np.zeros(256)
    for g in img[1]:
        g_hist_array[img[g]]+=1
    b_hist_array = np.zeros(256)
    for b in img[2]:
        b_hist_array[img[b]]+=1
    print(r_hist_array.shape)
    print(g_hist_array.shape)
    print(b_hist_array.shape)
    
customCDF(original)