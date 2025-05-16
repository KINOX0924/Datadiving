# 관리자가 할 수 있는 기능
# 고객 계정 생성 - 구현 완료
# 고객 계정 삭제 (생성되어 있는 계좌가 없어야 함) - 구현 완료
# 고객 계정 수정 - 구현 완료
# 고객 계정 비밀번호 초기화 - 구현 완료

# 고객 계좌 생성
# 고객 계좌 삭제
# 고객 계좌 정지
# 고객 계좌 비밀번호 초기화

# (관리팀 및 인사팀만 가능)
# 직원 계정 생성
# 직원 계정 삭제
# 직원 계정 비밀번호 초기화

# p   = 출력 함수
# cus = 고객 계정 관련 함수
# acc = 고객 계좌 관련 함수
# em  = 직원 계정 관련 함수
# val = 유효성 검사 함수

# 모듈 호출 모음
import BankDB
import PatternList

import random
# //TODO 계좌 생성 시에 사용 예정
import datetime

class Bankmanager :
    # ===== 직원 계정 로그인
    def loginEmployee(self) :
        login_employee_id       = input("직원 계정 아이디 입력 : ")
        login_employee_password = input("직원 계정 비밀번호 입력 : ")
        flag , employee_department = BankDB.BankDatabase.loginEmployee(login_employee_id , login_employee_password)
        if flag == True :
            self.employeeMenu(employee_department)
        return
    
    # ===== 직원 메뉴 [메인 화면]
    def p_employeeMenu(self , employee_department) :
        print("===== 직원 메뉴 =====")
        print("[1] | 고객 계정 관련 작업")
        print("[2] | 고객 계좌 관련 작업")
        if employee_department == "관리팀" or employee_department == "인사팀" :
            print("[3] | 직원 계정 관련 작업")
        print("[0] | 로그아웃")
    
    # ===== 직원 메뉴 [고객 계정 관련 작업]
    def p_cus_employeeMenu(self) :
        print("===== 고객 계정 관련 작업 메뉴 =====")
        print("[1] | 고객 계정 생성")
        print("[2] | 고객 계정 삭제")
        print("[3] | 고객 계정 수정")
        print("[4] | 고객 계정 비밀번호 초기화")
        print("[0] | 이전 메뉴")
        
    # 직원 로그인 후 메뉴 선택 [메인 화면]
    def employeeMenu(self , employee_department) :
        employeemenu_list = [None , self.cus_employeeMenu]
        
        while True :
            self.p_employeeMenu(employee_department)
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
    
    # 직원 로그인 후 고객 계정 관련 작업 메뉴를 선택 후 메뉴 선택 [고객 계정 관련 작업]
    def cus_employeeMenu(self) :
        employeemenu_list = [None , self.addCustomer , self.delCustomer , self.modCustomer , self.resetCustomerPwd]
        
        while True :
            self.p_cus_employeeMenu()
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu > 0 and select_menu <= len(employeemenu_list) :
                    employeemenu_list[select_menu]()
                elif select_menu == 0 :
                    return
                else :
                    print("메뉴에 있는 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력해주세요.")
    
    # ===== 고객 계정 생성
    # 고객을 추가하기 위해서 고객의 정보를 입력받아서 DB 에 전송할 함수
    # //FIXME [1] [국적] 항목에 외국인이 가입하였을 경우를 추가 //TODO [1] 추가 완료
    # //FIXME [2] 아이디와 비밀번호를 받아서 유효성 체크 후 반환하도록 추가 //TODO [2] 추가 완료
    def addCustomer(self) :
        customer = {"customer_name" : "" , "customer_id" : "" , "customer_password" : "" , "resident_number" : "" , "customer_gender" : "" , "customer_age" : 0 , "customer_birthday" : "" , "customer_nationality" : "" , "customer_phone" : "" , "customer_account" : []}
        customer["customer_name"]        = input("고객 이름 입력 : ")
        customer["customer_id"]          = self.getId()
        customer["customer_password"]    = self.getPassword()
        customer["resident_number"]      = self.getResidentNumber()
        customer["customer_gender"]      = self.getGender(customer["resident_number"])
        customer["customer_birthday"] , customer["customer_age"] = self.getBirthAge(customer["resident_number"])
        customer["customer_nationality"] = self.getNationality(customer["resident_number"])
        customer["customer_phone"]       = self.getPhoneNumber()
        print(customer) # //TODO//FIXME 추후 삭제 필요
        BankDB.BankDatabase.insertCustomer(customer)
        
    # 고객 계정에 사용할 아이디를 받아서 유효성 체크 후 반환하는 함수
    def getId(self) :
        flag = [False , False]
        
        while flag[0] == False or flag[1] == False :
            customer_id = input("계정에 사용할 아이디 입력 : ")
            flag[0] = PatternList.checkId(customer_id)
            flag[1] = BankDB.BankDatabase.searchCustomerId(customer_id)
            if flag[0] == True and flag[1] == True :
                return customer_id
            print("사용할 수 없는 아이디입니다.")
            
    # 고객 계정에 사용할 비밀번호를 받아서 유효성 체크 후 반환하는 함수
    def getPassword(self) :
        flag = False
        
        while flag == False :
            customer_password = input("계정에 사용할 비밀번호 입력 : ")
            flag = PatternList.checkPassword(customer_password)
            if flag == True :
                return customer_password
            print("사용할 수 없는 비밀번호입니다.")
    
    # 고객의 주민번호를 받아서 유효성 체크 후 반환하는 함수
    # //OPTIMIZE return 값 수정했음 >> 제대로 들어가는 지 확인 필요(유효성 확인 필요)  //TODO 확인 완료 (0514 | 12:40)
    # //FIXME [1] 주민등록번호를 받아오는 것을 정규식을 사용하여 다시 작성 할 것 //TODO [1] 수정 완료 | 정규식과 유효검증을 하는 함수 두 개로 나눔
    def getResidentNumber(self) :
        flag = [False , False]
        
        while flag[0] == False or flag[1] == False :
            resident_number = input("[-] 를 포함한 주민등록번호 입력 : ")
            flag[0] = self.val_residentNumber(resident_number)
            flag[1] = PatternList.checkResidentNumber(resident_number)
            if flag[0] == True and flag[1] == True :
                return resident_number
            print("유효하지 않는 주민등록번호입니다.")

    # 고객에게 입력받은 주민등록번호의 앞자리가 만들어질 수 있는 날짜의 숫자인지 확인하는 함수
    # 이 함수로 입력되는 resident_number 는 str 타입
    # //FIXME [1] 이미 int 타입으로 들어온 것이라 int 전환은 필요 없음 >> 코드를 더 짧게 줄일 수 있음 >> 최외부 try - except 구문 필요 없을 듯 //TODO [1] 수정 완료
    # //FIXME [2] 기존 int 타입으로 들어오던 주민번호를 정규식 사용을 위해서 str 타입으로 변경 >> 따라서 str 로 주민번호를 감쌀 필요가 사라짐 //TODO [2] 수정 완료
    # //FIXME [3] 숫자가 아닌 문자가 들어올 경우 오류가 발생됨 //TODO [3] 수정 완료
    # //FIXME [4] 외국인이 가입하였을 경우를 추가 //TODO [4] 추가 완료
    def val_residentNumber(self , resident_number) :
        try :
            year  = int(resident_number[:2])
            month = int(resident_number[2:4])
            day   = int(resident_number[4:6])
        except ValueError :
            return False
        
        if resident_number[7] == "1" or resident_number[7] == "2" or \
           resident_number[7] == "5" or resident_number[7] == "6" :
            year = 1900 + year
        else :
            year = 2000 + year
        
        try :
            datetime.date(year , month , day)
            return True
        except ValueError :
            return False
  
    # 고객의 주민번호를 확인하여 남성인지 여성인지 확인하고 성별을 반환하는 함수
    # 이 함수로 입력되는 resident_number 는 str 타입
    def getGender(self , resident_number) :
        if int(resident_number[7]) % 2 == 1 :
            return "male"
        return "female"
    
    # 고객의 주민번호를 사용하여 생일과 나이를 반환하는 함수
    # 이 함수로 입력되는 resident_number 는 str 타입
    # //FIXME [1] 코드 더 짧게 수정 필요 //TODO [1] 수정 완료
    # //FIXME [2] 외국인이 가입하였을 경우를 추가 //TODO [2] 추가 완료
    def getBirthAge(self , resident_number) :
        if resident_number[7] == "1" or resident_number[7] == "2" or \
           resident_number[7] == "5" or resident_number[7] == "6" :
            year = 1900 + int(resident_number[:2])
        else :
            year = 2000 + int(resident_number[:2])

        month = int(resident_number[2:4])
        day   = int(resident_number[4:6])
        
        now             = datetime.datetime.today()
        birthday        = datetime.date(year , month , day)
        format_birthday = birthday.strftime("%Y-%m-%d")
        return format_birthday , (now.year - birthday.year)
    
    # 고객의 주민번호를 사용하여 국적이 '대한민국' 인지 , '외국' 인지 확인하여 반환하는 함수
    def getNationality(self , resident_number) :
        if int(resident_number[7]) <= 4 :
            return "대한민국"
        return "외국인"
    
    # 고객의 연락처를 입력받아서 유효성 체크 후 반환하는 함수
    # 현재 대한민국에서 가운데 네 자리는 4 자리를 사용함 / 하지만 3 자리가 있을 수도 있음
    # //FIXME [1] 정규식 패턴을 사용해서 숫자가 7 자리 또는 8 자리만 들어올 수 있도록 수정 //TODO [1] 수정 완료
    # //FIXME [2] 변수를 사용하지 않고 리턴값에서 계산해서 나가도록 수정 //TODO [2] 수정 완료
    def getPhoneNumber(self) :
        flag = False
        
        while flag == False :
            phone_number = input("[-] 를 포함한 휴대전화 번호 입력 : ")
            
            flag = PatternList.checkPhoneNumber(phone_number)
            if flag == True :
                return phone_number
            print("유효하지 않는 휴대폰 번호 형식입니다.")
            
    # 고객의 이름과 고객 계정의 비밀번호를 입력 받아서 고객 정보를 받아오는 함수
    def searchCustomerInformation(self) :
        customer_name        = input("고객 이름 입력 : ")
        customer_password    = input("계정 비밀번호 입력 : ")
        customer_information = BankDB.BankDatabase.searchCustomer(customer_name , customer_password)
        
        return customer_information
    
    # 고객 계정 삭제 함수
    # //FIXME [1] 생년월일이 아닌 계정 비밀번호를 받아서 삭제할 수 있도록 수정 필요 //TODO [1] 수정 완료
    # //FIXME [2] 고객 이름과 계정 비밀번호를 입력받아서 고객 정보를 받아오는 행위가 자주 사용될 듯 하여 별도 함수로 제작하기
    def delCustomer(self) :
        while True :
            customer_information = self.searchCustomerInformation
            if customer_information != None :
                BankDB.BankDatabase.deleteCustomer(customer_information)
                return
            print("이름과 계정 비밀번호를 다시 확인해주세요.")
    
    # //FIXME [1] 수정하고 싶은 항목을 선택해서 수정할 수 있도록 변경 필요 //TODO [1] 변경 완료
    # //FIXME [2] 생년월일이 아닌 계정 비밀번호를 받아서 수정할 수 있도록 수정 필요 //TODO [2] 수정 완료
    # 고객 계정 정보 수정 함수
    def modCustomer(self) :
        while True :
            customer_name     = input("고객 이름 입력 : ")
            customer_password = input("계정 비밀번호 입력 : ")
            customer_information = BankDB.BankDatabase.searchCustomer(customer_name , customer_password)
            if customer_information != None :
                self.modCustomerDetail(customer_information)
                return
            print("이름과 계정 비밀번호를 다시 확인해주세요.")
    
    # 고객 계정 정보 수정 메뉴
    # 주민등록번호 변경 시 생일 , 성별 , 나이 , 국적 등 관련된 정보가 바로 같이 변경이 되어야 함
    def p_modCustomer(self , customer_name) :
        print(f"[{customer_name}] 님 계정의 수정할 항목 선택")
        print("===== 항목 =====")
        print("[1] | 이름 변경")
        print("[2] | 주민등록번호 변경")
        print("[3] | 연락처 변경")
        print("[0] | 메뉴 종료")
    
    # 고객 계정 정보 수정 함수(상세)
    def modCustomerDetail(self , customer_information) :
        modify_menu_list = [None , 1 , 2 , 3]
        
        while True :
            self.p_modCustomer(customer_information["customer_name"])
            try :
                select_menu = int(input("수정 항목 선택 : "))
                if select_menu > 0 and select_menu <= len(modify_menu_list) :
                    BankDB.BankDatabase.modifyCustomer(customer_information , select_menu)
                    if select_menu == 1 or select_menu == 2 :
                        return
                elif select_menu == 0 :
                    print("계정 정보 수정을 종료합니다.")
                    return
                else :
                   print("메뉴에 있는 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    # 고객 계정 비밀번호 초기화
    def resetCustomerPwd(self) :
        while True :
            customer_name     = input("고객 이름 입력 : ")
            customer_password = input("계정 비밀번호 입력 : ")
            customer_information = BankDB.BankDatabase.searchCustomer(customer_name , customer_password)
            if customer_information != None :
                BankDB.BankDatabase.resetCustomerPassword(customer_information)
                return
            print("이름과 계정 비밀번호를 다시 확인해주세요.")
    
    # ===== 직원 메뉴 [고객 계좌 관련 작업]
    def p_acc_employeeMenu(self) :
        print("===== 고객 계좌 관련 작업 메뉴 =====")
        print("[1] | 일반계좌 생성")
        print("[2] | 적금계좌 생성")
        print("[3] | 예금계좌 생성")
        print("[4] | 청약계좌 생성")
        print("[5] | 주식계좌 생성")
        print("[0] | 이전 메뉴")
    
    #//FIXME [1] 제작 진행 중
    # ===== 고객 계좌 생성
    def addAccountMenu(self) :
        
        
# 시작
if __name__ == "__main__" :
    manager = Bankmanager()
    manager.loginEmployee()