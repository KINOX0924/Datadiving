import cv2
import numpy as np

params = [
    cv2.IMWRITE_JPEG_QUALITY , 5
    ]

img = cv2.imread("./images/Lena.bmp")

cv2.imwrite("./images/Lena_save.jpeg" , img , params = params)

cv2.namedWindow("./images/Lena.bmp")