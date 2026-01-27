"""
python3 dither.py image.jpeg
"""
import sys
import numpy as np
from PIL import Image

THRESHOLD = 128

def pixel_rgb_to_grayscale(r, g, b):
	return (r + g + b) / 3

def image_to_grayscale_matrix(input_image):
	image_matrix = np.array([pixel_rgb_to_grayscale(px[0], px[1], px[2]) for px in np.array(Image.Image.getdata(input_image))])
	width, height = input_image.size
	image_matrix = image_matrix.reshape((height, width))
	return image_matrix

def create_error_matrix(grayscale_image_matrix): 
	error_matrix = np.zeros(grayscale_image_matrix.shape)
	return error_matrix

def update_error_matrix(error_matrix, error, x, y):
	(columns, rows) = error_matrix.shape
	if y < rows -1:
		error_matrix[x][y +1] += error / 16 * 7 # based on floyd-steinberg
	if x < columns -1 and y > 0: 
		error_matrix[x + 1][y - 1] += error / 16 * 3 # based on floyd-steinberg
	if x < columns -1:
		error_matrix[x + 1][y] += error / 16 * 3 # based on floyd-steinberg
	if x < columns -1 and y < rows -1: 
		error_matrix[x + 1][y + 1] += error / 16 # based on floyd-steinberg
	return error_matrix

def set_color(pixel): 
	return 0 if pixel < THRESHOLD else 255

def dither(grayscale_image_matrix, error_matrix):	
	dithered_image = np.zeros(grayscale_image_matrix.shape)
	frame = "/Users/marta/Desktop/marta/dithering/temp/{}-{}.png"
	for x, row in enumerate(grayscale_image_matrix):
		for y, pixel in enumerate(row):
			dithered_pixel = pixel + error_matrix[x][y]
			dithered_pixel_color = set_color(dithered_pixel)
			dithered_image[x][y] = dithered_pixel_color

			pixel_error = dithered_pixel - dithered_pixel_color
			error_matrix = update_error_matrix(error_matrix, pixel_error, x, y) 
			im = Image.fromarray(dithered_image.astype(np.uint8), mode="L")
			im = im.resize(
                (im.width * 10, im.height * 10),
                resample=Image.Resampling.NEAREST
            )
			print(f"Saving frame {"{:03d}".format(x)}-{"{:03d}".format(y)}")
			im.save(frame.format("{:03d}".format(x), "{:03d}".format(y)))
	im = Image.fromarray(dithered_image)
	im.show()

def main(original_image):
	input_image = Image.open(original_image)
	grayscale_image_matrix = image_to_grayscale_matrix(input_image)
	error_matrix = create_error_matrix(grayscale_image_matrix)
	dither(grayscale_image_matrix, error_matrix)

main(sys.argv[1])