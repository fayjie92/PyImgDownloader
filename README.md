# PyImgDownloader
This library allows users to download images from various search engines, such as Google, Bing, and DuckDuckGo. It helps in building custom image dataset for to design different machine learning algorithms.

### How to download images?
- Clone the repository.
```
git clone https://github.com/fayjie92/PyImgDownloader
```
- Create either a conda environment or a virtual environment (venv).
``` 
conda create -n myenv python==3.10  # for conda
python3 venv venv   # for venv
```
- Activate the environment and install required libraries.
```
conda activate myenv    # for conda
source venv/bin/activate    # for venv

pip3 install -r requirements.txt   
```
- Run the 'main.py' to download images.
```
python3 main.py -e <search engine: Google| Bing | DuckDuckGo> -q <"Search Term 1" "Search Term 2" ...> -n <number of images to download>
```
for example, ```python3 main.py -e Google -q  "wild cat" "canine dog" -n 10```


### How to generate image dataset?
- Run the 'main_dataset.py' to generate images of same size.
```
python3 main_dataset.py -s <image size> -d <dataset dir path>
```
for example, ```python3 main_dataset -s 300``` will generate '300 x 300' size images into 'Data' directory.
