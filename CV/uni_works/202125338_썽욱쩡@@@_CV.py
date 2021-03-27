import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./goose.jpg')


r_channel = img[:,:,0]
g_channel = img[:,:,1]
b_channel = img[:,:,2]

def hist_equalization(img_1d):
    hist_list = np.zeros(256)
    entire_pixel =img_1d.shape[0]*img_1d.shape[1]
   

    for y in img_1d:
        for x in y:
            hist_list[x]+=1
    plt_x = np.zeros(256)
    for i,_ in enumerate(plt_x):
        plt_x[i] = i
    #plt.plot(plt_x,hist_list)
    max_pix= 0;
    
    
    for m in range(len(hist_list)-1,0,-1):
        if hist_list[m]!=0:
            max_pix= m
            break;
    
            
    
b    L_n = max_pix/entire_pixel
    regular_hist = np.round(hist_list*L_n)

    cdf_reg = []
    for i,v in enumerate(regular_hist):
        if(i==0):
            cdf_reg.append(v)
        else:
             cdf_reg.append(v+cdf_reg[len(cdf_reg)-1])
    cdf_reg = np.round(cdf_reg)
    
    reg_1d_img=  np.zeros((img_1d.shape[0],img_1d.shape[1]))
    
    for iy,y in enumerate(img_1d):
        for ix,x in enumerate(y):
            reg_1d_img[iy][ix] = cdf_reg[x]
        
    return reg_1d_img
    
r_reg = hist_equalization(r_channel)
g_reg = hist_equalization(g_channel)
b_reg = hist_equalization(b_channel)


def combine_r_g_b(r,g,b):
    result = np.zeros((r.shape[0],r.shape[1],3))
    result[:,:,0]= r
    result[:,:,1]= g
    result[:,:,2] =b
    return result

res = np.int16(combine_r_g_b(r_reg,g_reg,b_reg))

plt.imshow(res)
#plt.imshow(img)