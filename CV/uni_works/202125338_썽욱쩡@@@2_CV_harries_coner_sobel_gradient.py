import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./ham.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
height,width=  img.shape[0],img.shape[1]

def make_xy_sobel_mask(kernal_size=3):
    kernal_center  =kernal_size//2
    x_sobel = np.ones((kernal_size,kernal_size))
    x_sobel[kernal_center] = np.zeros(kernal_size)
    for i,xi in enumerate(x_sobel):
        if i < kernal_center:
            x_sobel[i][kernal_center] +=1
        elif i == kernal_center:
            continue
        else:
            x_sobel[i]*=-1
            x_sobel[i][kernal_center] -=1
    return x_sobel.T*-1,x_sobel,kernal_center



def mirror_padding(img,kernal_center_size=1):
    height,width = img.shape[0],img.shape[1]
    padding_res = np.zeros((height+2*kernal_center_size,width+2*kernal_center_size))
    padding_res[kernal_center_size:kernal_center_size+height,kernal_center_size:width+kernal_center_size] = img
    
    padding_res[kernal_center_size:height+kernal_center_size,0:kernal_center_size] = img[0:height,kernal_center_size:0:-1]
    padding_res[kernal_center_size:height+kernal_center_size,kernal_center_size+width:width+2*kernal_center_size] = img[0:height,width:width-kernal_center_size-1:-1]
    
    padding_res[kernal_center_size:0:-1,0:width+kernal_center_size*2] = padding_res[kernal_center_size:kernal_center_size*2,0:width+2*kernal_center_size]
    
    padding_res[kernal_center_size+height:kernal_center_size*2+height,0:width+kernal_center_size*2] = padding_res[kernal_center_size+height-1:height-1:-1,0:width+2*kernal_center_size]

    return padding_res
    

def getting_xy_deriviation_img(padded_img,pad_size,x_filter,y_filter,origin_h,origin_w):
    dx = np.zeros((origin_h,origin_w))
    dy = np.zeros((origin_h,origin_w))

    for h in range(pad_size,origin_h+pad_size):
        for w in range(pad_size,origin_w+pad_size):
           dx[h-pad_size,w-pad_size] = np.sum(padded_img[h-pad_size:h+pad_size+1,w-pad_size:w+pad_size+1]*x_sobel)
           dy[h-pad_size,w-pad_size] = np.sum(padded_img[h-pad_size:h+pad_size+1,w-pad_size:w+pad_size+1]*y_sobel)
    return dx,dy

    
def crf(dx,dy):
    res = (dx*dx -dx*dy) - K* np.square(dx*dx+dy*dy)
    return res

def findConer(crf_res,th=0.5):
    res = np.zeros(crf_res.shape)
    for hi,h in enumerate(crf_res> th):
        for wi,w in enumerate(h):
            if w == False:
                continue
            else:
                res[hi][wi]=1
    
    return res
    
    
    
kernal_size = 3

x_sobel,y_sobel,pad_size = make_xy_sobel_mask(kernal_size)

mirror_padded_img = mirror_padding(img,pad_size)

dx,dy = getting_xy_deriviation_img(mirror_padded_img,pad_size,x_sobel,y_sobel,height,width)

K = 0.04

crf_res = crf(dx,dy)

res = findConer(crf_res)



