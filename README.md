# Image Cropping Tool

## Overview
This is a Python script that allows users to crop multiple images at once. The script uses the Pillow library to open and manipulate image files. Users can specify a directory containing the images they wish to crop, as well as the desired crop height. The script will then crop each image from the bottom by the specified height, and save the cropped images with the same file names as the original images.

## Requirements
- Python 3.x
- Pillow library

## Installation
1. Clone or download the repository to your local machine.
2. Install the Pillow library by running the following command in your terminal:
    ```bash
    pip install pillow
    ```

## Usage
1. Open the `crop_images.py` script in your preferred text editor.
2. Modify the `directory` and `crop_height` variables to suit your needs. 
   - `directory`: The path to the directory containing the images you wish to crop.
   - `crop_height`: The desired crop height in pixels. 
3. Save the changes to the script.
4. Run the script by executing the following command in your terminal:
    ```bash
    python crop_images.py
    ```
5. The script will process each image in the specified directory and crop it from the bottom by the specified height. The cropped images will be saved in the same directory as the original images, with the same file names but with "_cropped" added to the end.
6. Once the script has completed processing all images, it will print a message to the console indicating how many images were processed and how many were successfully cropped.

## Notes
- Only .jpg and .png images are supported.
- Cropping an image permanently deletes the cropped area, so be sure to make a backup of your original images before running this script.
- The script will only crop images in the specified directory, and will not search subdirectories.
- If an image fails to crop for any reason, the script will skip that image and move on to the next one.
- If you encounter any issues or have any questions, please feel free to open an issue in the repository.

 
