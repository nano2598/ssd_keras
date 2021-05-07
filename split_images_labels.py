# This file can be run to prepare the data to be input into the SSD structure implementation of,
# https://github.com/pierluigiferrari/ssd_keras, which was used as a basis for this project. Set the
# path to the labels csv file as well as to a folder containing the images at the top. This script will then divide the
# filenames into a training and validation set, and create csv files for each.

import os
import random
import cv2

# Creating empty lists to store data (images), labels, and filenames
data = []
labels = []
filenames = []

# TODO set paths
labels_path = "WashingtonOBRace/WashingtonOBRace/corners.csv"
images_path = "WashingtonOBRace/WashingtonOBRace/"
rows = open(labels_path).read().strip().split("\n")

# Loop over the rows
for row in rows:
	# Break the row into the filename and bounding box coordinates
	row = row.split(",")
	filename = row[0]
	filenames.append(filename) # Save all the filenames

# Converted to a set to keep only unique names, then back to a list
filenames = set(filenames)
filenames = list(filenames)
random.shuffle(filenames)

# Separating training and validation filenames
n_imgs = len(filenames)
train_portion = int(n_imgs * 0.7)

train_filenames = filenames[0:train_portion]
test_filenames = filenames[train_portion:]

train_lines = []
test_lines = []

# Already appending a header to the csv files for each of the sets
header = "filename, xmin, xmax, ymin, ymax, classid\n"
train_lines.append(header)
test_lines.append(header)

# Setting source path and destination path (to put images in a folder without the labels)
src_dir = "WashingtonOBRace/WashingtonOBRace/"
dst_dir = "all_images/"
if not os.path.isdir("all_images"):
	os.mkdir("all_images")

# going through every row of the original given labels again
for i, row in enumerate(rows):
	# Again separating name from coordinates
	row = row.split(",")
	img_name = row[0]
	# Image is read using openCV to resize, so that all images are the same size. You can set your own size here.
	img_path = os.path.join(src_dir, img_name)
	image = cv2.imread(img_path)
	h = image.shape[0]
	w = image.shape[1]
	new_size = 340      #TODO set size

	# Coordinates have to be made relative, and then absolute again according to the new size
	xmin = int((float(row[1]) / w) * new_size)
	xmax = int((float(row[5]) / w) * new_size)
	ymin = int((float(row[2]) / h) * new_size)
	ymax = int((float(row[6]) / h) * new_size)

	# These two if statements are used to essentially separate the lines that have to be written for each set
	if img_name in train_filenames:
		line = f"{img_name}, {xmin}, {xmax}, {ymin}, {ymax}, 1\n"
		train_lines.append(line)

	if img_name in test_filenames:
		line = f"{img_name}, {xmin}, {xmax}, {ymin}, {ymax}, 1\n"
		test_lines.append(line)

	# Resizing image and writing them to destination directory
	image = cv2.resize(image, (new_size, new_size))
	cv2.imwrite(os.path.join(dst_dir, img_name), image)

# Stripping any trailing spaces or new lines
train_lines[-1] = train_lines[-1].rstrip()
test_lines[-1] = test_lines[-1].rstrip()

# Finally writing the previously determined lines for each set to their respective csv files
with open("train_labels.csv", "w") as f:
	f.writelines(train_lines)
with open("test_labels.csv", "w") as f:
	f.writelines(test_lines)

