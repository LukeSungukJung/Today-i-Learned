#todo mirroring with average laplacian and sobel median


import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np

sujihye = cv2.imread('./goddess2.jpg')

b, g, r = cv2.split(sujihye)
original = cv2.merge([r,g,b])



skimage.io.imshow(original)

#only 3x3 5x5 7x7 ......
def makeLaplacian_filter(w,h):
    res = np.zeros((w,h))
    center_x = w//2
    center_y = h//2
    res[center_x][center_y]= 2**(w-1)
    center_val = res[center_x][center_y]
   # print(center_val,div_val,w_i)
    ypm=1
    xpm=1
    div_val=2
    res[center_x-xpm][center_y] = center_val/np.sqrt(center_val)
    res[center_x][center_y-ypm] = center_val/np.sqrt(center_val)
    res[center_x+xpm][center_y] = center_val/np.sqrt(center_val)
    res[center_x][center_y+ypm] = center_val/np.sqrt(center_val)
    center_val = res[center_x][center_y+ypm]
    center_val = res[center_x-xpm][center_y]/div_val
    xpm+=1
    ypm+=1
    while((center_x+xpm)<w):
        res[center_x-xpm][center_y] = center_val
        res[center_x][center_y-ypm] = center_val
        res[center_x+xpm][center_y] = center_val
        res[center_x][center_y+ypm] = center_val
        xpm+=1
        ypm+=1
        center_val = res[center_x-xpm][center_y]/div_val
    res[center_x-xpm+1][center_y] = 1
    res[center_x][center_y-ypm+1] = 1
    res[center_x+xpm-1][center_y] = 1
    res[center_x][center_y+ypm-1] = 1
    return res
        
        
    
    