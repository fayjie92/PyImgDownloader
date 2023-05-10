#!/bin/bash

### This shell script helps to clean the data after downloading.


search_dir=./Images
echo "Images directory: " $search_dir


# convert file formats (jpeg, png -> jpg)
echo "******************* Converting file formats: JPEG, PNG -> JPG *******************" 
find "$search_dir/Google" -type f -execdir mogrify -format jpg *.jpeg \; 2>/dev/null
find "$search_dir/Google" -type f -execdir mogrify -format jpg *.png \; 2>/dev/null
find "$search_dir/Bing" -type f -execdir mogrify -format jpg *.jpeg \; 2>/dev/null
find "$search_dir/Bing" -type f -execdir mogrify -format jpg *.png \; 2>/dev/null
find "$search_dir/Duck" -type f -execdir mogrify -format jpg *.jpeg \; 2>/dev/null
find "$search_dir/Duck" -type f -execdir mogrify -format jpg *.png \; 2>/dev/null

# clean-up
# delete unwanted extension files (.gif, )
echo "******************* Cleaning up unwanted file formats: GIF, ICO *******************" 
find "$search_dir/Google" -type f -name "*.gif" -exec rm -v {} \;
find "$search_dir/Bing" -type f -name "*.gif" -exec rm -v {} \;
find "$search_dir/Duck" -type f -name "*.gif" -exec rm -v {} \;
find "$search_dir/Google" -type f -name "*.png" -exec rm -v {} \;
find "$search_dir/Bing" -type f -name "*.png" -exec rm -v {} \;
find "$search_dir/Duck" -type f -name "*.png" -exec rm -v {} \;
find "$search_dir/Google" -type f -name "*.jpeg" -exec rm -v {} \;
find "$search_dir/Bing" -type f -name "*.jpeg" -exec rm -v {} \;
find "$search_dir/Duck" -type f -name "*.jpeg" -exec rm -v {} \;


echo "******************* Creating the text file (Images/ImagePaths.txt) *******************" 
# create and save the image_path_list
find "$search_dir/Google" -type f | tee -a ./Images/ImagePaths.txt; 
find "$search_dir/Bing" -type f | tee -a ./Images/ImagePaths.txt; 
find "$search_dir/Duck" -type f | tee -a ./Images/ImagePaths.txt;
