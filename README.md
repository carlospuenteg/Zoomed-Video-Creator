# Zoomed Video Creator

## Description

This is a simple script that creates a video from a set of images, zooming from the first image to the last one and vice versa.

## Results (from a set of 10 images)

#### Zoooming out

https://github.com/carlospuenteg/carlospuenteg/assets/65092569/df1aec83-f5f7-446b-b56c-12b9f47b174e

#### Zooming in

https://github.com/carlospuenteg/carlospuenteg/assets/65092569/4fc76ee5-e83b-49e9-b87b-5186758a67a3


## 2. Getting Started

### Install Requirements

```bash
python3 -m pip install -r requirements.txt
```

If that doesn't work, you can try:

```bash
py -m pip install -r requirements.txt
```


### Upload input images

Put the images you want to use in the `input` folder, sorted numerically, with names like: `1.png`, `2.png`, ...


### Run the script

```bash
python3 main.py
```

## How to use

1. Put the images you want to use in the `input` folder, with the names: `1.png`, `2.png`, ...
2. Run the script: `python3 main.py`
3. The output video will be in the `output` folder, named `zoom_out.mp4` and `zoom_in.mp4`