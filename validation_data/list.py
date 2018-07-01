import glob
import csv

img_list = glob.glob("*.tif")
with open("val_img_list.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(img_list)
