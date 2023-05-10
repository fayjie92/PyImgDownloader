#!/usr/bin/env python3
########################################
# Image Downloader from Search Engines #
########################################
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat

import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="PyImgDownloader")
    # configs
    parser.add_argument('-e', '--engine', default='google', choices=['Google', 'Bing', 'DuckDuckGo'],
                        help='search engine from where images will be downloaded.')
    parser.add_argument('-q', '--query', nargs='+', type=str, default=['mango', 'banana'], 
                        help='search terms to be searched in the engine.')
    parser.add_argument('-n', '--n_images', type=int, default=5, 
                        help='no. of images to be downloaded. (default=5)')
    parser.add_argument('-l', '--log', default=False, action=argparse.BooleanOptionalAction, 
                        help='logging: True/False')
     
    return parser.parse_args()