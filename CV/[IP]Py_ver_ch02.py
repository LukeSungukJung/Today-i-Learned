import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
sujihye = cv2.imread('./goddess.jpg')



b, g, r = cv2.split(sujihye)
scale64image =cv2.merge([np.floor(r/64)*64,np.floor(g/64)*64,np.floor(b/64)*64])

#skimage.io.imshow(scale64image)

scale128image=cv2.merge([np.floor(r/128)*128,np.floor(g/128)*128,np.floor(b/128)*128])

#skimage.io.imshow(scale128image2)

orginal = cv2.merge([r,g,b])

#ans = skimage.io.imshow(cv2.resize(orginal,(300,300)))


def rgb_bilinear_interpolation(img,row,col):
    res_img = np.zeros((row,col,3))
    
    o_w=img.shape[0]
    o_h=img.shape[1]
    
    x_scale=o_w/row
    y_scale=o_h/col
    

    for i in range(0,row):
        for j in range(0,col):
            py= j*y_scale -1
            px= i*x_scale -1
            s= px -np.floor(px) 
            t= py -np.floor(py)
            
            res_img[i,j,:]=(1-s)*(1-t)*img[int(np.floor(px)),int(np.floor(py)),:]+ \
            (s)*(t)*img[int(np.floor(px)+1),int(np.floor(py)+1),:]+ \
            (1-s)*(t)*img[int(np.floor(px)+1),int(np.floor(py)),:]+ \
            (s)*(1-t)*img[int(np.floor(px)),int(np.floor(py))+1,:]
                
    return res_img

ans = skimage.io.imshow(np.uint8(rgb_bilinear_interpolation(orginal,600,600)))  