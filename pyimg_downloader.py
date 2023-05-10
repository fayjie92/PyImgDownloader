#!/usr/bin/env python3
########################################
# Image Downloader from Search Engines #
########################################
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat


import time
import logging
# search engines
from pygoogle_image import image    # google
from bing_image_downloader import downloader    # bing
import DuckDuckGoImages as ddg  # duckduckgo
# logging
from utils.logger import create_logger, logger_as_print


class PyImgDownloader():
    def __init__(self, 
                 search_engine, 
                 search_query, 
                 n_images,
                 log=False
                 ):
        
        self.search_engine = search_engine
        self.search_query = search_query
        self.n_images = n_images
        if log==True:
            self.logger = create_logger()
        else:
            self.logger = logger_as_print()


    def download_google_images(self, save_dir):
        time_start = time.time()
        self.logger.info(f'Downloading images from {self.search_engine}')   # logger
        
        for idx in range(len(self.search_query)):
            self.logger.info(f'Search query: "{self.search_query[idx]}"')   # logger
            image.download(self.search_query[idx], limit=self.n_images, directory=save_dir) # pygoogle_image function
            
        time_end = time.time()
        self.logger.info(f'Images are downloaded in: "{save_dir}"') # logger
        self.logger.info(f'Time elapsed: {time_end-time_start:.2f}s')   # logger
    

    def download_bing_images(self, 
                             save_dir,
                             adult_filter_off=False,  
                             force_replace=False, 
                             timeout=60, 
                             verbose=True,
                             ):
        time_start = time.time()
        self.logger.info(f'Downloading images from {self.search_engine} (adult content: {adult_filter_off})')   # logger
        
        for idx in range(len(self.search_query)):
            self.logger.info(f'Search query: "{self.search_query[idx]}"')   # logger
            downloader.download(self.search_query[idx], limit=self.n_images, output_dir=save_dir, 
                            adult_filter_off=adult_filter_off, 
                            force_replace=force_replace, 
                            timeout=timeout, 
                            verbose=verbose)
        
        time_end = time.time()
        self.logger.info(f'Images are downloaded in: "{save_dir}"') # logger
        self.logger.info(f'Time elapsed: {time_end-time_start:.2f}s')   # logger
    
   
    def download_duckduckgo_images(self, 
                                   save_dir,
                                   thumnails=False,
                                   parellel=False,
                                   shuffle=False,
                                   remove_folder=False,
                                   safe_search=False,
                                   license=ddg.ALL):
        time_start = time.time()
        self.logger.info(f'Downloading images from {self.search_engine} [save search: {safe_search}, parellel download: {parellel}, thumnails save: {thumnails}')   # logger
        
        for idx in range(len(self.search_query)):
            self.logger.info(f'Search query: "{self.search_query[idx]}"')   # logger
            ddg.download(self.search_query[idx], max_urls= self.n_images, folder=save_dir,
                        thumbnails=thumnails,
                        parallel=parellel, # make it true to do parellel downloading (faster)
                        shuffle=shuffle,
                        remove_folder=remove_folder,
                        safe_search=safe_search,
                        license=license
                        )
            
        time_end = time.time()
        self.logger.info(f'Images are downloaded in: "{save_dir}"') # logger
        self.logger.info(f'Time elapsed: {time_end-time_start:.2f}s')   # logger
        
    

