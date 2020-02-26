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
#60-90
def rotate_img(theta,img):
    ori_shape= np.array(img.shape)
    cmssc = np.zeros((2,2))
    cmssc[0] = [np.cos(np.pi*theta/180),-np.sin(np.pi*theta/180)]
    cmssc[1] = [np.sin(np.pi*theta/180),np.cos(np.pi*theta/180)]
    ex_h_top = np.floor(np.dot(cmssc,[0,ori_shape[1]])[0] +1)
    pad_h = np.uint32(np.abs(np.floor(np.dot(cmssc,[0,ori_shape[1]])[0])))    
    ex_h =np.uint32(np.abs(ex_h_top))
    ex_h_botton = np.uint32(np.abs(np.floor(np.dot(cmssc,[ori_shape[0],0])[0] +1)))
    pd_h = (ex_h + pad_h)
    ex_w =np.uint32(np.floor(np.dot(cmssc,ori_shape)[1])+1)
    res_img =  np.zeros([pd_h,ex_w])

    for x in range(0,ori_shape[0]):
        for y in range(0,ori_shape[1]):
            tmp_x_y = np.dot(cmssc,[x,y])
            tmp_x_y[0]= np.abs(np.floor(tmp_x_y[0]+pad_h+1))
            tmp_x_y[1]= np.abs(np.floor(tmp_x_y[1]+1))
            res_img[np.uint32(tmp_x_y[0]),np.uint32(tmp_x_y[1])] = img[x,y]

    return res_img