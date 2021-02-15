import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

sample1  = cv2.imread('./sample1.jpeg')
sample2  = cv2.imread('./sample2.jpeg')

img_width=300
img_height = 300
img_channel = 3
sample2  = cv2.resize(sample2,(img_width,img_height))



def CutMix(img1,img2):
    img_width=img1.shape[1]
    img_height=img1.shape[0]
    while(1):
        ratio = np.round(np.random.uniform(),2)
        absolute_rwv = np.int(img_width*np.sqrt(1-ratio))
        absolute_rhv = np.int(img_height*np.sqrt(1-ratio))
        
        sample1_binary_filter_base = np.ones((img_height,img_width))
        sample2_binary_filter_base = np.zeros((img_height,img_width))
        
            
        point_x = np.int(np.random.uniform(0,img_width))
        if point_x+absolute_rwv>img_width:
            continue
    
        point_y = np.int(np.random.uniform(0,img_height))
        if point_y+absolute_rhv>img_height:
            continue
        break
    
    #print(point_x,",",point_y)
    
    sample1_binary_filter_base[point_y:point_y+absolute_rhv,
                               point_x:point_x+absolute_rwv] =np.zeros((absolute_rhv,absolute_rwv))
    
    sample2_binary_filter_base[point_y:point_y+absolute_rhv,
                               point_x:point_x+absolute_rwv] =np.ones((absolute_rhv,absolute_rwv))
    

    processed_sample1 = np.zeros((img_width,img_height,3))
    roi_processed_sample2 = np.zeros((img_width,img_height,3))
    for ch in range(0,img_channel):
        processed_sample1[:,:,ch] = sample1_binary_filter_base*img1[:,:,ch]
        roi_processed_sample2[:,:,ch] =sample2_binary_filter_base*img2[:,:,ch]
    
    mixed_img =processed_sample1+roi_processed_sample2
    
    return mixed_img,ratio