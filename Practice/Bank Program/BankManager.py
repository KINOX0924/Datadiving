# 관리자가 할 수 있는 기능
# 고객 계정 생성 - 구현 완료
# 고객 계정 삭제 (생성되어 있는 계좌가 없어야 함)
# 고객 계정 수정
# 고객 계정 비밀번호 초기화

# 고객 계좌 생성 
# 고객 계좌 삭제
# 고객 계좌 정지
# 고객 계좌 비밀번호 초기화

# 직원 계정 생성(관리팀 및 인사팀만 가능)
# 직원 계정 삭제(관리팀 및 인사팀만 가능)
# 직원 계정 비밀번호 초기화

# p   = 출력 함수
# cus = 고객 계정 관련 함수
# acc = 고객 계좌 관련 함수
# em  = 직원 계정 관련 함수

import BankDB
import random
import datetime

class Bankmanager :
    # ===== 직원 계정 로그인
    def loginEmployee(self) :
        login_employee_id       = input("직원 계정 아이디 입력 : ")
        login_employee_password = input("직원 계정 비밀번호 입력 : ")
        flag , employee_rank = BankDB.BankDatabase.loginEmployee(login_employee_id , login_employee_password)
        if flag == True :
            self.employeeMenu(employee_rank)
        return
    
    # ===== 직원 메뉴 [메인 화면]
    def p_employeeMenu(self , employee_rank) :
        print("===== 직원 메뉴 =====")
        print("[1] | 고객 계정 관련 작업")
        print("[2] | 고객 계좌 관련 작업")
        if employee_rank == "관리팀" or employee_rank == "인사팀" :
            print("[3] | 직원 계정 관련 작업")
        print("[0] | 로그아웃")
    
    # ===== 직원 메뉴 [고객 계정 관련 작업]
    def p_cus_employeeMenu(self) :
        print("===== 고객 계정 관련 작업 메뉴 =====")
        print("[1] | 고객 계정 생성")
        print("[2] | 고객 계정 삭제")
        print("[3] | 고객 계정 수정")
        print("[4] | 고객 계정 비밀번호 초기화")
        print("[0] | 로그아웃")
        
    # 직원 로그인 후 메뉴 선택
    def employeeMenu(self , employee_rank) :
        employeemenu_list = [None , self.addCustomer]
        while True :
            self.p_employeeMenu(employee_rank)
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu > 0 and select_menu <= len(employeemenu_list) :
                    employeemenu_list[select_menu]()
                elif select_menu == 0 :
                    print("로그아웃 되었습니다.")
                    return
                else :
                    print("메뉴에 있는 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력해주세요.")
    
    # ===== 고객 계정 생성
    # 고객을 추가하기 위해서 고객의 정보를 입력받아서 DB 에 전송할 함수
    def addCustomer(self) :
        customer = {"customer_name" : "" , "resident_number" : "" , "customer_gender" : "" , "customer_age" : 0 , "customer_birthday" : "" , "customer_nationality" : "대한민국" , "customer_phone" : "" , "customer_account" : []}
        customer["customer_name"]   = input("고객 이름 입력 : ")
        customer["resident_number"] = self.getResidentNumber()
        customer["customer_gender"] = self.getGender(customer["resident_number"])
        customer["customer_birthday"] , customer["customer_age"] = self.getBirthAge(customer["resident_number"])
        customer["customer_phone"]  = self.getPhoneNumber()
        BankDB.BankDatabase.insertCustomer(customer)
    
    # 고객의 주민번호를 받아서 유효성 체크 후 반환하는 함수
    def getResidentNumber(self) :
        while True :
            flag = False
            try :
                resident_number = int(input("(-) 를 제외한 주민번호 입력 : "))
                flag = self.checkResidentNumber(resident_number)
                if flag == True :
                    first_resident_number  = str(resident_number)[:6]
                    second_resident_number = str(resident_number)[6:]
                    return (first_resident_number + "-" + second_resident_number)
                print("올바른 주민번호가 아닙니다. 다시 입력해주세요.")
            except ValueError :
                print("숫자만 입력해주세요.")
    
    # 고객에게 입력받은 주민번호가 올바른 유효한 주민번호인지 확인하는 함수
    def checkResidentNumber(self , resident_number) :
        year_number  = str(resident_number)[:2]
        month_number = str(resident_number)[2:4]
        day_number   = str(resident_number)[4:6]
        
        try :
            month = int(month_number)
            day   = int(day_number)
            for century in [1900 , 2000] :
                year = century + int(year_number)
                try :
                    datetime.date(year , month , day)
                    return True
                except ValueError :
                    return False
            return False
        except ValueError :
            return False     
    
    # 고객의 주민번호를 확인하여 남성인지 여성인지 확인하고 성별을 반환하는 함수
    def getGender(self , resident_number) :
        if resident_number[7] == "1" or resident_number[7] == "3" :
            return "male"
        return "female"
    
    # 고객의 주민번호를 사용하여 생일과 나이를 반환하는 함수
    def getBirthAge(self , resident_number) :
        birth_year_list = [None , "19" , "20"]
        if resident_number[7] == "1" or resident_number[7] == "2" :
            year = int(birth_year_list[1] + resident_number[:2])
        else :
            year = int(birth_year_list[2] + resident_number[:2])
        if resident_number[2] == "0" :
            month = int(resident_number[3:4])
        else :
            month = int(resident_number[2:4])
        if resident_number[4] == "0" :
            day   = int(resident_number[5:6])
        else :
            day   = int(resident_number[4:6])
        now             = datetime.datetime.today()
        birthday        = datetime.date(year , month , day)
        format_birthday = birthday.strftime("%Y-%m-%d")
        return format_birthday , (now.year - birthday.year)
    
    # 고객의 연락처를 입력받아서 유효성 체크 후 반환하는 함수
    def getPhoneNumber(self) :
        while True :
            try :
                phone_number = int(input("(010) 과 (-) 를 제외한 휴대전화 번호 입력 : "))
                if   len(str(phone_number)) == 7 :
                    first_phone_number  = str(phone_number)[:3]
                    second_phone_number = str(phone_number)[3:7]
                    return ("010-" + first_phone_number + "-" + second_phone_number)
                elif len(str(phone_number)) == 8 :
                    first_phone_number  = str(phone_number)[:4]
                    second_phone_number = str(phone_number)[4:8]
                    return ("010-" + first_phone_number + "-" + second_phone_number)
                else :
                    print("올바른 전화번호가 아닙니다. 다시 입력하세요.")
            except ValueError :
                print("숫자만 입력해주세요.")
                
# 시작
if __name__ == "__main__" :
    manager = Bankmanager()
    manager.loginEmployee()