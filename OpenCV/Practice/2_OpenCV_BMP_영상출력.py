import cv2

img = cv2.imread("./images/Lena.bmp")   # 이미지의 경로를 가져옴
if img is None :                                      # 이미지 경로를 읽지 못 해서 이미지를 못 읽어 올 경우
    print("이미지 경로가 잘못 설정되었거나 이미지가 없습니다.") # 왼쪽과 같은 문구를 출력
else :

    cv2.imshow("image" , img)   # 이미지를 제대로 읽었다면
    cv2.waitKey(0)              # 아무 키나 눌릴때까지 기다리고
    cv2.destroyAllWindows()     # 키가 눌리면 열렸던 모든 창을 닫음
