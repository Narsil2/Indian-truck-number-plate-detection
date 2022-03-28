from PIL import Image
import pytesseract
import os
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/tesseract.exe"
for imageName in os.listdir(r"C:/Users/upend\Desktop\SIH Datasets/trial images"):
    inputFolder = os.path.join(
        r"C:/Users/upend\Desktop\SIH Datasets/trial images", imageName)
    img = Image.open(inputFolder)

    configuration = ("-l eng --oem 1 --psm 8")

    text = pytesseract.image_to_string(
        img, lang="eng", config=configuration)

    file1 = open(r"Output.txt", "a+")

    file1.write(imageName+"\n")

    file1.write(text+"\n")
    file1.close()

print("Open File- Output.txt to view result(will be saved in cloud)")
