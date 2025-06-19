import cv2
import easyocr

img_path = r"..\Test_Image\receipt_3.jpg"
image    = cv2.imread(img_path)

gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 15 , 8)

cv2.imwrite("gray.jpg" , gray)
cv2.imwrite("thresh.jpg" , thresh)

reader  = easyocr.Reader(["ko" , "en"])
results = reader.readtext(thresh , detail = 0)

for line in results :
    print(line)
