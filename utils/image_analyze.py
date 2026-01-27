"""
python3 inspect.py image.jpeg
"""
import sys
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.image as img
import matplotlib.pyplot as plt

def show_channel_matrix(input_matrix, color=0):
	channel_matrix = input_matrix[:,:,color]
	#sns.heatmap(red_matrix, annot=True,  center=0, cbar=False, yticklabels=False, xticklabels=False, vmin=0, vmax=255)
	return channel_matrix

def show_thresholded_matrix(matrix):
	pass

def main(original_image):
	input_matrix = img.imread(original_image)
	print(input_matrix.shape, type(input_matrix))
	red_matrix = show_channel_matrix(input_matrix, 0)
	green_matrix = show_channel_matrix(input_matrix, 1)
	blue_matrix = show_channel_matrix(input_matrix, 2)

	print(red_matrix.shape)

	fig, axes = plt.subplots(1, 3, figsize=(8, 3))
	ax0, ax1, ax2 = axes.ravel()

	ax0.imshow(red_matrix[:, :], cmap=plt.cm.gray)
	ax0.set_title('Red channel')
	ax1.imshow(green_matrix[:, :], cmap=plt.cm.gray)
	ax1.set_title('Green channel')
	ax2.imshow(blue_matrix[:, :], cmap=plt.cm.gray)
	ax2.set_title('Blue channel')

	for a in axes:
		a.xaxis.set_visible(False)
		a.yaxis.set_visible(False)

	plt.show()
	

main(sys.argv[1])