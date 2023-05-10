#!/usr/bin/env python3
########################################
# Image Downloader from Search Engines #
########################################
# @author: Abdur R. Fayjie
# @email. fayjie92@gmail.com
# @date: 18-02-2023, Sat

import os
import subprocess

# depends on the create_image_paths.sh 

def imagepath_txt():
    """
    Creates file paths for the images.
    Cleans the unwanted file formats, .gif, .ico, etc.
    Converts all .JPEG, .PNG to .JPG format.
    """
    if os.path.exists('./Images/image_paths.txt'):
        os.remove('./Images/image_paths.txt')
    os.system("chmod 777 -R utils/create_image_paths.sh")
    #permission_code = subprocess.run(["chmod", "777", "-R", "./utils/create_image_paths.sh"])
    exit_code = subprocess.call('./utils/create_image_paths.sh')
    #print(exit_code)
    if exit_code == 0:
        print('Created file "./Images/ImagePaths.txt"')
    else:
        print('Failed! Check the create_image_paths.sh file')

    