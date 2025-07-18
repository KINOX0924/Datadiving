import cv2

img = cv2.imread("./images/Lena.bmp")
# 이미지의 경로를 가져옴
if img is None :
    print("이미지 경로가 잘못 설정되었거나 이미지가 없습니다.")
    # 경로가 잘못되었거나 이미지를 못 읽어 왔을 경우의 예외 처리
else :
    cv2.imshow("image" , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # 이미지를 정상적으로 읽었다면 imshow(제목 , 경로) = 이미지를 보여주고
    # waitkey(0) = 아무 키나 눌릴때까지 기다리고
    # destroyAllWindows() = 키가 눌리면 모든 창을 닫음