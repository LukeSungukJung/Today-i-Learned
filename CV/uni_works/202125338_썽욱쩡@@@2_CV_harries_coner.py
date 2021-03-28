import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./hcf_test2.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
height,width=  img.shape[0],img.shape[1]

def mirror_padding(img,kernal_center_size=1):
    height,width = img.shape[0],img.shape[1]
    padding_res = np.zeros((height+2*kernal_center_size,width+2*kernal_center_size))
    padding_res[kernal_center_size:kernal_center_size+height,kernal_center_size:width+kernal_center_size] = img
    
    padding_res[kernal_center_size:height+kernal_center_size,0:kernal_center_size] = img[0:height,kernal_center_size:0:-1]
    padding_res[kernal_center_size:height+kernal_center_size,kernal_center_size+width:width+2*kernal_center_size] = img[0:height,width:width-kernal_center_size-1:-1]
    
    padding_res[kernal_center_size:0:-1,0:width+kernal_center_size*2] = padding_res[kernal_center_size:kernal_center_size*2,0:width+2*kernal_center_size]
    
    padding_res[kernal_center_size+height:kernal_center_size*2+height,0:width+kernal_center_size*2] = padding_res[kernal_center_size+height-1:height-1:-1,0:width+2*kernal_center_size]

    return padding_res
    

def getting_xy_deriviation_img(padded_img,kernal_size,pad_size,origin_h,origin_w):
    
    dx,dy = np.gradient(padded_img)
    dx2 = np.zeros((origin_h,origin_w))
    dy2 = np.zeros((origin_h,origin_w))
    dxdy = np.zeros((origin_h,origin_w))

    for h in range(pad_size,origin_h+pad_size):
        for w in range(pad_size,origin_w+pad_size):
           dx2[h-pad_size,w-pad_size] = np.sum(cv2.GaussianBlur(np.square(dx[h-pad_size:h+pad_size+1,w-pad_size:w+pad_size+1]),(kernal_size,kernal_size),1))
           dy2[h-pad_size,w-pad_size] = np.sum(cv2.GaussianBlur(np.square(dy[h-pad_size:h+pad_size+1,w-pad_size:w+pad_size+1]),(kernal_size,kernal_size),1))
           dxdy[h-pad_size,w-pad_size] = np.sum(cv2.GaussianBlur((dx[h-pad_size:h+pad_size+1,w-pad_size:w+pad_size+1])
                                                *(dy[h-pad_size:h+pad_size+1,w-pad_size:w+pad_size+1])
                                                ,(kernal_size,kernal_size),1))
    return dx2,dy2,dxdy

    
def crf(dx2,dy2,dxdy,kernal_size):
    res = (dx2*dy2 -np.square(dxdy)) - K* np.square(dx2+dy2)
    return res

def nms(crf_res,block_box,th=10000):
    res = np.zeros(crf_res.shape)
    for h in range(block_box,crf_res.shape[0]-block_box):
        for w in range(block_box,crf_res.shape[1]-block_box):
            if(crf_res[h][w] == np.max(crf_res[h-block_box:h+block_box,w-1:w+2]) and crf_res[h][w]>th):
               res[h][w]=crf_res[h][w]
    
    return res
    
kernal_size = 3

pad_size = kernal_size//2



mirror_padded_img = mirror_padding(img,pad_size)

dy2,dx2,dxdy = getting_xy_deriviation_img(mirror_padded_img,kernal_size,pad_size,height,width)

K = 0.04

crf_res = crf(dx2,dy2,dxdy,kernal_size)
res = nms(crf_res,pad_size,10000)*255


