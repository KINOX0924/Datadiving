import cv2
import pytesseract as tess
import numpy as np

class TesseractOCR :
    # 테서렉트 엔진을 사용하기 위한 엔진 모듈을 불러오는 코드
    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # tess.pytesseract.tesseract_cmd = r"D:\UTILL\Tesseract\tesseract.exe"
    
    def __init__(self , path) :
        self.image = cv2.imread(path)       # 영수증 이미지가 있는 경로와 이미지를 불러오는 코드
        
        # 이미지가 너무 작을 경우를 대비해서 확대시키는 함수를 적용
        h , w = self.image.shape[:2]
        if h < 1000 :
            self.image = cv2.resize(self.image , (w*2 , h*2) , interpolation = cv2.INTER_CUBIC)
            
        self.clahe = cv2.createCLAHE(clipLimit = 2.0 , tileGridSize = (8 , 8)) # 흑백 대비를 자동 조정하는 CLAHE 코드 작성
    
    def transGray(self) :
        self.gray_image = cv2.cvtColor(self.image , cv2.COLOR_BGR2GRAY)     # 이미지 흑백처리 진행
        self.gray_image = cv2.GaussianBlur(self.gray_image , (5 , 5) , 0)
        self.gray_image = self.clahe.apply(self.gray_image)                 # CLAHE 적용
        # 블러와 clahe 의 순서를 변경
        
        # 흑백처리된 이미지의 노이즈를 제거 -> 대비가 너무 심해짐
        # self.gray_image = cv2.medianBlur(self.gray_image , 3)

    def blur(self) :
        # 블러 처리 및 어댑티브 이진화 진행
        self.thresh = cv2.adaptiveThreshold( self.gray_image , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 31 , 10)
        self.thresh = self.deskew(self.thresh)
        
        # 흑백처리된 이미지의 블러 처리 진행 -> 별로 뛰어나지 않음
        # _, self.thresh = cv2.threshold(self.gary_image , 150 , 255 , cv2.Thresh_BINARY)

    # 흑백처리된 이미지 및 전처리 진행된 이미지를 확인하기 위한 디버깅 함수
    def createImage(self) :
        cv2.imwrite(r"..\Test_Image\gray_tesseract.jpg" , self.gray_image)
        cv2.imwrite(r"..\Test_Image\thresh_tesseract.jpg" , self.thresh)
    
    # 영수증 자동 수직 보정(Deskew)
    def deskew(self , image) :
        coords = np.column_stack(np.where(image > 0))
        angle  = cv2.minAreaRect(coords)[-1]
        
        if angle < -45 : 
            angle = -(90 + angle)
        elif angle > 45 :
            angle = 90 - angle
        else :
            angle = - angle
        
        (h , w) = image.shape[:2]
        center  = (w // 2 , h // 2)
        
        M = cv2.getRotationMatrix2D(center , angle , 1.0)
        
        return cv2.warpAffine(image , M , (w , h) , flags = cv2.INTER_CUBIC , borderMode = cv2.BORDER_REPLICATE)
    
    # 테서렉트 엔진을 사용하여 영수증에서 한글과 영어를 추출함
    # custom_config 를 사용하여 psm 모델을 바꾸면서 실험
    def exportText(self) :
        custom_config = r"--oem 3 --psm 4 -l kor+eng"
        export_text   = tess.image_to_string(self.thresh , config = custom_config)
        
        return export_text

if __name__ == "__main__" :
    image_path = r"..\Test_Image\receipt_2.jpg"
    
    ORC = TesseractOCR(image_path)
    ORC.transGray()
    ORC.blur()
    ORC.createImage()
    
    export_text = ORC.exportText()
    print(export_text)