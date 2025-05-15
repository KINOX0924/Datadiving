# 주로 사용하는 패턴을 모아두고 그것으로 검증 진행하는 함수들의 모음
import re
import random
import datetime

# //FIXME [1] 관리자 모듈 수정 작업 전에 이것 먼저 수정 - 패턴 설정 필요 //TODO [1] 수정 완료 | [1-1] 2차 수정 완료
def checkPhoneNumber(phone_number) :
    phonenumber_pattern  = r"^\d{3}-\d{3,4}-\d{4}\b"
    checked_phone_number = re.match(phonenumber_pattern , phone_number)
    # match 함수를 쓰지 않고 find 를 반환하면 None 값이 들어가지 않음
    # None 을 넣고 싶으면 search 나 match 함수를 사용
    
    if checked_phone_number == None :
        return False
    return True

def checkBirthday(customer_birthday) :
    birthday_pattern         = r"^\d{6}\b"
    checked_birthday_pattern = re.match(birthday_pattern , customer_birthday)
    
    if checked_birthday_pattern == None :
        return False
    return True

# //FIXME [1] 뒤 7자리 숫자 중 첫번째 숫자가 1 에서 8 사이의 숫자만 들어갈 수 있도록 수정 //TODO [1] 수정 완료
# //FIXME [2] 뒤 7자리 숫자 중 첫번째 숫자가 3 , 4 , 7 , 8 인경우 현재 연도의 두 자리 숫자를 초과하지 못하도록 수정 //TODO [2] 수정 완료
def checkResidentNumber(resident_number) :
    resident_number_pattern = r"^\d{6}-[1-8]{1}\d{6}\b"
    checked_resident_number = re.match(resident_number_pattern , resident_number)
    
    year_2000_list = ["3" , "4" , "7" , "8"]
    
    year = datetime.datetime.today()
    year = int(year.strftime("%Y")[2:4])
    
    if checked_resident_number == None or (int(checked_resident_number.group()[:2]) > year and checked_resident_number.group()[7] in year_2000_list) :
        return False
    return True

def checkAnswer(answer) :
    answer_pattern = r"^\w\b"
    checked_Answer = re.match(answer_pattern , answer)
    
    if checked_Answer == None :
        return False
    return True

def checkId(id) :
    id_pattern = r"^[a-zA-Z0-9_]{5,10}$"
    checked_Id = re.match(id_pattern , id)
    
    if checked_Id == None :
        return False
    return True

def checkPassword(password) :
    password_pattern = r"^[0-9A-Za-z.?!@#$%^&*]{8,20}\b"
    checked_Password = re.match(password_pattern , password)
    
    if checked_Password == None :
        return False
    return True

def createPassword() :
    new_password = []
    
    for index in range(0,8) :
        now = random.randint(1,3)
        if   now == 1 :
            new_password.append(str(random.randint(0,9)))
        elif now == 2 :
            new_password.append(chr(random.randint(65,90)))
        elif now == 3 :
            new_password.append(chr(random.randint(97,122)))
    new_password = "".join(new_password)
    return new_password

if __name__ == "__main__" :
    pass