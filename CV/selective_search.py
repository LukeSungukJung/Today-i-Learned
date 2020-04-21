from PIL import Image
import numpy as np
cup = Image.open('./cup.jpeg')
cup_resized = cup.resize((299, 299))
cup_resized = np.asarray(cup_resized.rotate(270, Image.NEAREST, expand = 1))

#cup_resized.save('299x299_cup.png')

from skimage.io import imshow


imshow(np.asarray(cup_resized))

from selective_search import selective_search


#ss_res = selective_search(cup_resized)


def draw_line(line_list,img):
    res =  img
    img_shape =  res.shape
    #print(img_shape)
    res.setflags(write=1)
    
    for fone in line_list:
        one=list(fone)
        for i,oo in enumerate(one):
            if oo == img_shape[0] or oo == img_shape[1]:
                
                one[i] = oo-2
        x1y1 = (one[0],one[1])
        x1y2 = (one[0],one[3])
        x2y1 = (one[2],one[1])
        x2y2 = (one[2],one[3])
        
        res[x1y1[0]:x2y1[0], x1y1[1]+1,] = np.asarray([255,0,0])
        res[x1y1[0]+1, x1y1[1]:x1y2[1],] = np.asarray([255,0,0])
        res[x1y2[0]:x2y2[0], x1y2[1]+1,] = np.asarray([255,0,0])
        res[x2y1[0]+1, x2y1[1]:x2y2[1],] = np.asarray([255,0,0])
        
    return res
