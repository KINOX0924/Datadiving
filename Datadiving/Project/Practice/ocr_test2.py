import cv2
import pytesseract as tess
import numpy as np

class TesseractOCR :
    # 테서렉트 엔진을 사용하기 위한 엔진 모듈을 불러오는 코드
    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # tess.pytesseract.tesseract_cmd = r"D:\UTILL\Tesseract\tesseract.exe"
    
    def __init__(self , path) :
        self.image = cv2.imread(path)       # 영수증 이미지가 있는 경로와 이미지를 불러오는 코드
        
        # if self.image == None :
        #     raise FileNotFoundError(f"이미지를 불러올 수 없습니다.")
        
        # 이미지가 너무 작을 경우를 대비해서 확대시키는 함수를 적용
        # 작은 이미지는 2배로 확대 진행
        h , w = self.image.shape[:2]
        if h < 1000 :
            self.image = cv2.resize(self.image , (w*2 , h*2) , interpolation = cv2.INTER_CUBIC)
            
        self.clahe = cv2.createCLAHE(clipLimit = 2.0 , tileGridSize = (8 , 8)) # 흑백 대비를 자동 조정하는 CLAHE 코드 작성
    
    def transGray(self) :
        self.gray_image = cv2.cvtColor(self.image , cv2.COLOR_BGR2GRAY)         # 이미지 흑백처리 진행
        self.gray_image = cv2.bilateralFilter(self.gray_image , 9 , 75 , 75)    # 이미지 내 글자의 엣지는 보존하고 노이즈는 제거 진행
        self.gray_image = cv2.GaussianBlur(self.gray_image , (5 , 5) , 0)       # 가우시안 블러 적용
        self.gray_image = self.clahe.apply(self.gray_image)                     # CLAHE 적용(흑백 대비)
        # 블러와 clahe 의 순서를 변경
        
        # 흑백처리된 이미지의 노이즈를 제거 -> 대비가 너무 심해짐
        # self.gray_image = cv2.medianBlur(self.gray_image , 3)

    def transThresh(self) :
        self.thresh = cv2.adaptiveThreshold( self.gray_image , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 31 , 10)  # 어댑티브 이진화 진행
        
        # 종이 자체의 노이즈를 제거 , 내부 구멍 메워서 글자와 노이즈의 혼동을 감소
        K1 = cv2.getStructuringElement(cv2.MORPH_RECT , (2,2))
        K2 = cv2.getStructuringElement(cv2.MORPH_RECT , (3,3))
        
        opened  = cv2.morphologyEx(self.thresh , cv2.MORPH_OPEN , K1)
        cleaned = cv2.morphologyEx(opened     , cv2.MORPH_CLOSE , K2)
        
        # 영수증 영역만 추출하여 남기기
        cnts , _ = cv2.findContours(cleaned , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts , key = cv2.contourArea , reverse = True)
        x , y , w , h = cv2.boundingRect(cnts[0])
        cropped = cleaned[ y:y+h , x:x+w]   
        
        # 영수증 자동 수직 보정처리 진행
        self.thresh = self.deskew(cropped)
        
        # 이진화 처리 진행
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
    # 화이트리스트를 사용하여 허용 문자만 인식하도록 함
    def exportText(self) :
        custom_config = (
            r"--oem 3" 
            r"--psm 4" 
            r"-l kor+eng"
            r"-c tessedit_char_whitelist=0123456789-/:.가-힣A-Za-z"
            )
        export_text = tess.image_to_string(self.thresh , config = custom_config)
        
        return export_text

if __name__ == "__main__" :
    image_path = r"..\Test_Image\receipt_3.jpg"
    
    ORC = TesseractOCR(image_path)
    ORC.transGray()
    ORC.transThresh()
    ORC.createImage()
    
    export_text = ORC.exportText()
    print(export_text)