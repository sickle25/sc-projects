"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: To remove different things in image. But it need more data.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red_avg = red
    green_avg = green
    blue_avg = blue
    color_distance = ((red_avg-pixel.red)**2+(green_avg-pixel.green)**2+(blue_avg-pixel.blue)**2)
    ans = math.sqrt(color_distance)
    return ans



def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    for i in range(len(pixels)):
        list = pixels[i]
        red += list.red
        green += list.green
        blue += list.blue
    red = int(red/len(pixels))
    green = int(green/len(pixels))
    blue = int(blue/len(pixels))
    list = [red, green, blue]


    return list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """

    list = get_average(pixels)

    red_avg = list[0]
    green_avg = list[1]
    blue_avg = list[2]

    # Set a number that does not affect the comparison
    cd = get_pixel_dist(pixels[0], red_avg, green_avg, blue_avg)
    best_pixel = pixels[0]

    # Choose the PIXEL with the smallest color distance as the best PIXEL
    for i in range(len(pixels)):
        ans = get_pixel_dist(pixels[i], red_avg, green_avg, blue_avg)
        if ans < cd:
            best_pixel = pixels[i]



    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########



    for x in range(result.width):
        for y in range(result.height):
            result_pixel = result.get_pixel(x, y)

            # Take out the pixels of the same position (x,y) in different pictures to list.
            pixels = []
            for z in range(len(images)):
                pic = images[z]
                pic_pixel = pic.get_pixel(x, y)
                pixels.append(pic_pixel)

            best_pixel = get_best_pixel(pixels)

            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue


    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
