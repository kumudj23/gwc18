from filters import *

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(im):
    pixelData = list(im.getdata())

    for i in range(len(pixelData)):
        pixel = pixelData[i] #3-tuple variable
        intensity = pixel[0] + pixel[1] + pixel[2]

        if intensity < 182:
            pixelData[i] = (0, 51, 76)

        elif intensity < 364:
            pixelData[i] = (217, 26, 33)

        elif intensity < 546:
            pixelData[i] = (112, 150, 158)

        else:
            pixelData[i] = (252, 227, 166)

    im.putdata(pixelData)
    return im

    #return an image object

def kumud_PopArt(im):
    data = list(im.getdata())

    for i in range(len(data)):
        pixel = data[i] #3-tuple variable

        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        intensity = red + green + blue

        if red > green and red > blue and intensity < 250:
            data[i] = (255,105,180)
        elif red > green and red > blue and intensity > 250:
            data[i] = (204, 0, 34)
        elif green > blue and green > red and intensity < 200:
            data[i] = (47, 242, 73)
        elif green > blue and green > red and intensity > 200:
            data[i] = (0, 102, 0)
        elif blue > green and blue > red and intensity < 300:
            data[i] = (0, 128, 255)
        elif blue > green and blue > red and intensity > 300:
            data[i] = (17, 0, 102)
        else:
            data[i] = (0, 0, 0)

    im.putdata(data)
    return im

def main():
    inside = load_img("skyline.jpg")
    myImage = kumud_PopArt(inside)
    save_img(myImage, "popart.jpg")
    load_img("popart.jpg")
    show_img(myImage)

if __name__ == '__main__':
    main()
