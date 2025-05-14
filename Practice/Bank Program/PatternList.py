# 주로 사용하는 패턴을 모아두고 그것으로 검증 진행하는 함수들의 모음
import re

# //FIXME [1] 관리자 모듈 수정 작업 전에 이것 먼저 수정 - 패턴 설정 필요
def checkPhoneNumber(phone_number) :
    phonenumber_pattern = r"^\d{3}-\d{3,4}-\d{4}\b"
    search_phonenumber = pattern.finditer(phone_number)
    
    for item in search_phonenumber :
        print(item.group())
    
    if search_phonenumber == None :
        return None
    else :
        return search_phonenumber


if __name__ == "__main__" :
    number = checkPhoneNumber("010-1155-5511")