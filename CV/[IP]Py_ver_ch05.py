import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
from skimage.color import rgb2gray
from skimage.color import rgb2gray
sujihye = cv2.imread('./goddess2.jpg')


b, g, r = cv2.split(sujihye)
original = cv2.merge([r,g,b])
gray_tester = rgb2gray(original)

skimage.io.imshow(original)
#ans =skimage.transform.rotate(original,60)

def rotate_img(theta,img):
    ori_shape= np.array(img.shape)
    cmssc = np.zeros((2,2))
    cmssc[0] = [np.cos(np.pi*theta/180),-np.sin(np.pi*theta/180)]
    cmssc[1] = [np.sin(np.pi*theta/180),np.cos(np.pi*theta/180)]
    ex_h = ori_shape[0] - np.floor(np.dot(cmssc,[ori_shape[0],0])[0] +1)
    ex_h = ex_h+ np.abs(ex_h+np.dot(cmssc,[0,ori_shape[1]])[0])
    ex_h = np.uint32(np.floor(ex_h)+1)
    res_w =np.uint32(np.floor(np.dot(cmssc,ori_shape)[1])+1)
    res_img =  np.zeros([ex_h+ori_shape[0],res_w])
    return res_img