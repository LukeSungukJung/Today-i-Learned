import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import cv2
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
import PIL
from PIL import Image
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras import layers, models, optimizers
from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint


DATA_PATH='/home/malgus/다운로드/kakr3';

TRAIN_PATH = os.path.join(DATA_PATH,'train')
TEST_PATH = os.path.join(DATA_PATH,'test')


df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

train_imgs =[]

nb_train_sample = df_train.shape[0] * 0.75
nb_validation_sample = df_train.shape[0] - nb_train_sample
nb_test_sample = df_test.shape[0]

plt.figure(figsize=(15,6))
sns.countplot(df_train["class"], order=df_train["class"].value_counts(ascending=True).index)

img_size=224
cropped_train_img =[]
cropped_test_img = []
train_arr = os.listdir(TRAIN_PATH)
test_arr = os.listdir(TEST_PATH)
def crop_boxing_img(train_arr,test_arr, margin=16, imsize=(img_size, img_size)):
    for img_name in train_arr:
        img = PIL.Image.open(os.path.join(TRAIN_PATH, img_name))
        pos = df_train.loc[df_train["img_file"] == img_name, ['bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2']].values.reshape(-1)

        width, height = img.size
        x1 = max(0, pos[0] - margin)
        y1 = max(0, pos[1] - margin)
        x2 = min(pos[2] + margin, width)
        y2 = min(pos[3] + margin, height)

        cropped_train_img.append(np.asarray(img.crop((x1, y1, x2, y2)).resize(imsize)))
        
    for img_name in test_arr:
        img = PIL.Image.open(os.path.join(TEST_PATH, img_name))
        pos = df_train.loc[df_train["img_file"] == img_name, ['bbox_x1', 'bbox_y1', 'bbox_x2', 'bbox_y2']].values.reshape(-1)

        width, height = img.size
        x1 = max(0, pos[0] - margin)
        y1 = max(0, pos[1] - margin)
        x2 = min(pos[2] + margin, width)
        y2 = min(pos[3] + margin, height)

        cropped_test_img.append(img.crop((x1, y1, x2, y2)).resize(imsize))   
        
        
crop_boxing_img(train_arr,test_arr)

TRAIN_CROPPED_PATH = './cropped_train'
TEST_CROPPED_PATH = './cropped_test'
VALID_CROPPED_PATH = './cropped_valid'

if (os.path.isdir(TRAIN_CROPPED_PATH) == False):
    os.mkdir(TRAIN_CROPPED_PATH)
if (os.path.isdir(TEST_CROPPED_PATH) == False):
    os.mkdir(TEST_CROPPED_PATH)
if (os.path.isdir(VALID_CROPPED_PATH) == False):
    os.mkdir(VALID_CROPPED_PATH)


def get_random_eraser(p=0.5, s_l=0.02, s_h=0.4, r_1=0.3, r_2=1/0.3, v_l=0, v_h=255, pixel_level=False):
    def eraser(input_img):
        img_h, img_w, img_c = input_img.shape
        p_1 = np.random.rand()

        if p_1 > p:
            return input_img

        while True:
            s = np.random.uniform(s_l, s_h) * img_h * img_w
            r = np.random.uniform(r_1, r_2)
            w = int(np.sqrt(s / r))
            h = int(np.sqrt(s * r))
            left = np.random.randint(0, img_w)
            top = np.random.randint(0, img_h)
            if left + w <= img_w and top + h <= img_h:
                break
        if pixel_level:
            c = np.random.uniform(v_l, v_h, (h, w, img_c))
        else:
            c = np.random.uniform(v_l, v_h)

        input_img[top:top + h, left:left + w, :] = c

        return input_img

    return eraser


