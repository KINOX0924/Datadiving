import cv2      # 이미지를 불러오고 전처리를 하기 위한 모듈
import easyocr  # 전처리 진행된 이미지를 OCR 처리하기 위한 모듈

# 이미지 경로를 받는 변수 -> 웹 또는 앱 사용 시 이미지를 받아오는 역할을 하게될 것
# cv2.imread 함수를 사용하여 경로에 있는 이미지를 image 라는 변수에 넣음
img_path = r"..\Test_Image\receipt_3.jpg"
image    = cv2.imread(img_path)

# 받아온 이미지에 흑백처리를 진행
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
# 흑백 처리된 이미지의 노이즈 제거 (추가)
gray = cv2.medianBlur(gray , 3)
# 노이즈 제거된 이미지에서 글자를 강조시킴 (추가)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT , (1 , 1))
# 가우시간 블러처리 진행
thresh = cv2.adaptiveThreshold(gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 15 , 8)

cv2.imwrite(r"..\Test_Image\gray.jpg" , gray)
cv2.imwrite(r"..\Test_Image\thresh.jpg" , thresh)

reader  = easyocr.Reader(["ko" , "en"])
results = reader.readtext(thresh , detail = 0)

for line in results :
    print(line)
