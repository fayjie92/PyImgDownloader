#!/usr/bin/env python3
########################################
# Image Downloader from Search Engines #
########################################
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat

import os
from pyimg_downloader import PyImgDownloader
from utils.parser import get_parser



if __name__ == '__main__':
    args = get_parser()

    pid = PyImgDownloader(search_engine=args.engine,
                          search_query=args.query,
                          n_images=args.n_images,
                          log=args.log
                          )

    if args.engine == 'Google':
        save_dir_path = './Images/Google/'
        if not os.path.exists(save_dir_path):
            os.makedirs(save_dir_path)

        pid.download_google_images(save_dir=save_dir_path)

    if args.engine == 'Bing':
        save_dir_path = './Images/Bing/'
        if not os.path.exists(save_dir_path):
            os.makedirs(save_dir_path)

        pid.download_bing_images(save_dir=save_dir_path)

    if args.engine == 'DuckDuckGo':
        save_dir_path = './Images/DuckDuckGo/'
        if not os.path.exists(save_dir_path):
            os.makedirs(save_dir_path)

        pid.download_duckduckgo_images(save_dir=save_dir_path)
        


   