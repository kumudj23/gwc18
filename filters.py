# Rename this file to be "filters.py"
# Add commands to import modules here.

from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename)


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    image.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image, filename):
    image.save(filename)
