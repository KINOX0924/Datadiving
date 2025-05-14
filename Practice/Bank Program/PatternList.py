# 주로 사용하는 패턴을 모아두고 그것으로 검증 진행하는 함수들의 모음
import re

# //FIXME [1] 관리자 모듈 수정 작업 전에 이것 먼저 수정 - 패턴 설정 필요 //TODO [1] 수정 완료 | [1-1] 2차 수정 완료
def checkPhoneNumber(phone_number) :
    phonenumber_pattern = r"^\d{3}-\d{3,4}-\d{4}\b"
    phonenumber = re.match(phonenumber_pattern , phone_number)
    # match 함수를 쓰지 않고 find 를 반환하면 None 값이 들어가지 않음
    # None 을 넣고 싶으면 search 나 match 함수를 사용
    
    if phonenumber == None :
        return False
    return True

if __name__ == "__main__" :
    number = checkPhoneNumber("010-1155-55111")
    print(number)