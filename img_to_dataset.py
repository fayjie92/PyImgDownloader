#!/usr/bin/env python3
########################################
# Image Downloader from Search Engines #
########################################
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat

import os
import csv
import numpy as np
from PIL import Image
import seam_carving as SC
# logging
from utils.logger import create_logger, logger_as_print

class GenerateDataset():
    def __init__(self, imgpath_txtfile, imgsize, dataset_dir, log=False):
        self.imgpath_txtfile = imgpath_txtfile
        self.imgsize = imgsize
        self.dataset_dir = dataset_dir
        self.log = log
        
        if self.log==True:
            self.logger = create_logger()

        else:
            self.logger = logger_as_print()

        if os.path.exists('./logs/image_src_dest_map.csv'):
            os.remove('./logs/image_src_dest_map.csv')

    def process_image(self):
        with open(self.imgpath_txtfile) as f:
            img_paths = f.read().splitlines()

        for idx in range(len(img_paths)):
            img = Image.open(img_paths[idx])

            # first apply aspect ratio resize and then content-aware resize.
            # It is faster then the content-aware resize.
            # This will make the images size smaller.
            # Seam Curve is faster in smaller images.
            scaled_image, scaled_image_numpy = aspect_ratio_resize(img, self.imgsize)

            width, height = scaled_image.size

            if width == height: # if image is squared then ignore content-aware resize.
                new_image = scaled_image
            else:
                # apply content-aware resize.
                # read seam-curve algorith at
                # https://faculty.runi.ac.il/arik/scweb/imret/index.html
                new_image = content_aware_resize(scaled_image_numpy, self.imgsize)
            
            # save images
            dest_img_filename = "{:04d}".format(idx)+'.jpg'
            save_img_path = self.dataset_dir+ '/'+ dest_img_filename
            new_image.save(save_img_path)

            self.logger.info(f'Source Image: {img_paths[idx]}  [{img.size[0]} X {img.size[1]}]')
            self.logger.info(f'Destination Image: {save_img_path} [{new_image.size[0]} X {new_image.size[1]}]')

            if self.log == True:
                map_src_dest_images(idx, img_paths[idx], save_img_path)



# helper functions
def aspect_ratio_resize(img, size):
    """
    Resize an image based on aspect ratio.
    Args:
        img : image 
        size -> int : size to be resized.
    Return:
        resized_img: resized image
        resized_img_np: resized image in numpy formate
    """
    width, height = img.size
    
    if width >= height:
        ratio = width/height
        new_width = int(ratio * size)
        resized_img = img.resize((new_width, size))
        resized_img_np = np.array(resized_img)
    
    elif width < height:
        ratio = height/width
        new_height = int(ratio * size)
        resized_img = img.resize((size, new_height))
        resized_img_np = np.array(resized_img)
    
    else:
        print('Image format/size is corrupted.')

    return resized_img, resized_img_np


def content_aware_resize(img_np, size):
    """
    Resize an image based on content.
    Args:
        img_np -> np.array: image
        size-> int : size to be resized.
    Return:
        resized_img: resized image
        resized_img_np: resized image in numpy formate
    """
    width, height, _ = img_np.shape
   
    if height > size:
        row_to_be_deleted = height - size
        resized_img = SC.resize(
            src=img_np,
            size= (width, height - row_to_be_deleted),
            order= 'height-first',
            keep_mask=None
        )
    
    elif width > size:
        column_to_be_deleted = width - size
        resized_img = SC.resize(
            src=img_np,
            size= (width - column_to_be_deleted, height),
            order= 'width-first',
            keep_mask=None
        )

    else:
        resized_img = img_np
    
    final_img = Image.fromarray(resized_img)
    
    return final_img


# for logging purpose
def map_src_dest_images(serial_number, src_image, dest_image):
    #if os.path.exists('./logs/image_src_dest_map.csv'):
    #    os.remove('./logs/image_src_dest_map.csv')
    with open('./logs/image_src_dest_map.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([serial_number, src_image, dest_image])
        