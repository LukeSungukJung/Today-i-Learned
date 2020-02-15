import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np

sujihye = cv2.imread('./goddess2.jpg')

b, g, r = cv2.split(sujihye)
original = cv2.merge([r,g,b])

#skimage.io.imshow(original)



def customHistCDF_Nomalize(img):
    r_hist_array = np.zeros(256)
    
    for r in img[:,:,0]:
        r_hist_array[img[r]]+=1
        
        
    g_hist_array = np.zeros(256)
    
    for g in img[:,:,1]:
        g_hist_array[img[g]]+=1
        
    b_hist_array = np.zeros(256)
    
    for b in img[:,:,2]:
        b_hist_array[img[b]]+=1
        
    fig= plt.figure()
    plt.plot(rgb_hist_arr[0])
    plt.plot(rgb_hist_arr[1])
    plt.plot(rgb_hist_arr[2])
    
    r_hist_array/=np.sum(r_hist_array)
    g_hist_array/=np.sum(g_hist_array)
    b_hist_array/=np.sum(b_hist_array)
    
    return r_hist_array,g_hist_array,b_hist_array
    
rgb_hist_arr =customHistCDF_Nomalize(original)


def rgb_pixel_nomalization(original):
  rn = np.zeros(r.shape)
  
  for ri,re in enumerate(r):
      for rj,ree in enumerate(re):
          rn[ri][rj] = ree/255
  bn = np.zeros(b.shape)
  
  for bi,be in enumerate(b):
      for bj,bee in enumerate(be):
          bn[bi][bj] = bee/255
          
          
  gn = np.zeros(g.shape)
  
  for gi,ge in enumerate(g):
      for gj,gee in enumerate(ge):
          gn[gi][gj] = gee/255         
  return rn,gn,bn
  
def getoutputrgbhist(rgb_hist_arr):
    for rhi,r_hist in enumerate(rgb_hist_arr[0]):
        if(rhi==0):
            continue
        else:
            rgb_hist_arr[0][rhi] = r_hist +rgb_hist_arr[0][rhi-1]
    for ghi,g_hist in enumerate(rgb_hist_arr[1]):
        if(ghi==0):
            continue
        else:
            rgb_hist_arr[1][ghi] = g_hist +rgb_hist_arr[1][ghi-1]  
            
    for bhi,b_hist in enumerate(rgb_hist_arr[2]):
        if(bhi==0):
            continue
        else:
            rgb_hist_arr[2][bhi] = b_hist +rgb_hist_arr[2][bhi-1]    
    for rhi,r_hist in enumerate(rgb_hist_arr[0]):
        rgb_hist_arr[0][rhi] *=255 
        rgb_hist_arr[0][rhi] = np.floor(rgb_hist_arr[0][rhi])
    for ghi,g_hist in enumerate(rgb_hist_arr[1]):
        rgb_hist_arr[1][ghi] *=255   
        rgb_hist_arr[1][ghi] = np.floor(rgb_hist_arr[1][ghi])
    for bhi,b_hist in enumerate(rgb_hist_arr[2]):
        rgb_hist_arr[2][bhi] *=255
        rgb_hist_arr[2][bhi] =np.floor(rgb_hist_arr[2][bhi])
getoutputrgbhist(rgb_hist_arr);



def tranform_rgb_hist_pool(rgb_hist_arr):
    res_img = np.zeros(original.shape)
    
    for r_i,r_pix_row in enumerate(original[:,:,0]):
        for r_j,r_pix in enumerate(r_pix_row):
            res_img[r_i][r_j]=rgb_hist_arr[0][r_pix]
            res_img[r_i][r_j]=np.uint8(res_img[r_i][r_j])
            
    for g_i,g_pix_row in enumerate(original[:,:,1]):
        for g_j,g_pix in enumerate(g_pix_row):
            res_img[g_i][g_j]=rgb_hist_arr[1][g_pix]
            res_img[g_i][g_j]=np.uint8(res_img[g_i][g_j])   
            
    for b_i,b_pix_row in enumerate(original[:,:,2]):
        for b_j,b_pix in enumerate(b_pix_row):
            res_img[b_i][b_j]=rgb_hist_arr[1][b_pix]
            res_img[b_i][b_j]=np.uint8(res_img[b_i][b_j])   
    return res_img

            
    
output = tranform_rgb_hist_pool(rgb_hist_arr)





