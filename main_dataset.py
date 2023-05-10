#!/usr/bin/env python3
########################################
# Image Downloader from Search Engines #
########################################
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat


import os
from img_to_dataset import GenerateDataset
from utils.parser import dataset_parser
from utils.filepaths_images_txt import imagepath_txt as imgtxt



if __name__ == '__main__':
    args = dataset_parser()
    imgtxt()

    if not os.path.exists(args.dataset_dir):
        os.makedirs(args.dataset_dir)

    my_dataset = GenerateDataset(imgpath_txtfile='./Images/ImagePaths.txt',
                    imgsize=args.image_size,
                    dataset_dir=args.dataset_dir,
                    log=args.log)
    
    my_dataset.process_image()
    


