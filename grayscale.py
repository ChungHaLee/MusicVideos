import cv2
import numpy as np
import os

def saturate_contrast1(p, num):
    pic = p.copy()
    pic = pic.astype('int64')
    pic = np.clip(pic*num, 0, 255)
    pic = pic.astype('uint8')
    return pic

def saturate_contrast2(p, num):
    pic = p.copy()
    pic = pic.astype('int32')
    pic = np.clip(pic+(pic-128)*num, 0, 255)
    pic = pic.astype('uint8')
    return pic



def colortogray():
    file_path = './coverart'
    for filename in os.listdir(file_path):
        print(filename)
        if filename == '.DS_Store':
            pass
        else:
            img = cv2.imread("./coverart/%s"%filename, 0) # imgs 폴더에 png 이미지 불러오기
            contrast_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
            contrast_img = saturate_contrast2(contrast_img, 0.5)
            cv2.imwrite("./grayscale_coverart/%s"%filename, contrast_img) # imgs 폴더에 png 이미지 저장


colortogray()