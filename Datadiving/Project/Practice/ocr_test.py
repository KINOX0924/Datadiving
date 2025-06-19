import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image     = cv2.imread("../Test_Image/receipt_3.jpg")
hsv_image = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)

lower_blue = np.array([90 , 50 , 50])
upper_blue = np.array([130 , 255 , 255])
blue_mask  = cv2.inRange(hsv_image , lower_blue , upper_blue)
blue_ratio = np.sum(blue_mask > 0) / (image.shape[0] * image.shape[1])

try :
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
except :
    gray = image.copy()

if blue_ratio > 0.03 :
    processed = cv2.adaptiveThreshold(gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 15 , 8)
else :
    processed = cv2.threshold(gray , 150 , 255 , cv2.THRESH_BINARY_INV)

text = pytesseract.image_to_string(processed , lang="kor+eng")

print(text)