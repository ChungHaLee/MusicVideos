import os
from keras_segmentation.pretrained import pspnet_50_ADE_20K , pspnet_101_cityscapes, pspnet_101_voc12

model = pspnet_50_ADE_20K() # load the pretrained model trained on ADE20k dataset

# model = pspnet_101_cityscapes() # load the pretrained model trained on Cityscapes dataset

# model = pspnet_101_voc12() # load the pretrained model trained on Pascal VOC 2012 dataset

# load any of the 3 pretrained models



def segmentation():
    file_path = './grayscale_coverart'
    for filename in os.listdir(file_path):
        out = model.predict_segmentation(
            inp="./grayscale_coverart/%s"%filename,
            out_fname="./segmentated_result/%s"%filename
        )

segmentation()