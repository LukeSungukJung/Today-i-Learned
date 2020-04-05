import cv2
import matplotlib.pyplot as plt
import skimage
import numpy as np
from skimage.color import rgb2gray
from skimage.color import rgb2gray
sujihye = cv2.imread('./goddess2.jpg')


b, g, r = cv2.split(sujihye)

r_hist_array = np.zeros(256)
g_hist_array = np.zeros(256)
b_hist_array = np.zeros(256)
gray_hist = np.zeros(256)
for ri in r:
    r_hist_array[ri]+=1
    
plt.plot(r_hist_array)
for gi in g:
    g_hist_array[gi]+=1  
plt.plot(g_hist_array)
for bi in b:
    b_hist_array[bi]+=1  
plt.plot(b_hist_array)
plt.show()

original = cv2.merge([r,g,b])

gray_tester = rgb2gray(original)
gray_tester = np.uint8(np.floor(gray_tester*255)+1)

for go in gray_tester:
    gray_hist[go] +=1
plt.plot(gray_hist)
plt.show()

proper_k =0

for pxi,val in enumerate(gray_hist):
  #  print(gray_hist[pxi:])
  #  print(gray_hist[:pxi])
    
    ipi1 =0
    for pi,val in enumerate(gray_hist[:pxi]):
        ipi1+= pi*val
    m1 = 1/np.sum(gray_hist[:pxi])*ipi1
    ipi2 =0
    for pi,val in enumerate(gray_hist[pxi:]):
        ipi2+= pi*val
    m2 =1/np.sum(gray_hist[pxi:])*ipi2
    
    if(m1  + m2 == float('nan')):
        continue
    
  #  print(m1  + m2)
    
skimage.io.imshow(gray_tester)

