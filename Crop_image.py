from PIL import Image
import os

directory = ""  # path to the directory containing the images if the folder of image in local disk d "D:/ Folder name"
crop_height = 100  # set the desired crop height  

# Keep in mind before croping the image you should have a backup copy of images otherwise it would be so hard to  revert the image 

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # filter only image files
        filepath = os.path.join(directory, filename)
        with Image.open(filepath) as img:
            width, height = img.size
            img = img.crop((0, 0, width, height - crop_height))  # crop from bottom
            img.save(filepath)