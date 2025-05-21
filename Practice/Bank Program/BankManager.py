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
    # //FIXME [1] 입력값 오류 시 에러 발생됨 //TODO [1] 계정 확인 후 로그인 실패 시 반환값과 변수의 값이 일치하지 않아서 생긴 오류로 수정 완료
    # ===== 직원 계정 로그인
    def loginEmployee(self) :
        login_employee_id          = input("직원 계정 아이디 입력 : ")
        login_employee_password    = input("직원 계정 비밀번호 입력 : ")
        flag , employee_department = BankDB.BankDatabase.loginEmployee(login_employee_id , login_employee_password)
        if flag == True :
            self.employeeMenu(employee_department)
        return
    
    # ===== 직원 메뉴 [메인 화면]
    def p_employeeMenu(self , employee_department) :
        print("===== ===== 직원 메뉴 ===== =====")
        print("[1] | 고객 계정 관련 작업")
        print("[2] | 고객 계좌 관련 작업")
        if employee_department == "관리팀" or employee_department == "개발1팀" or employee_department == "개발2팀" or employee_department == "유지보수팀":
            print("[3] | 직원 계정 관련 작업")
        print("[0] | 로그아웃")
        print("===== ===== ===== ===== ===== =====")
    
    # ===== 직원 메뉴 [고객 계정 관련 작업]
    def p_cus_employeeMenu(self) :
        print("===== ===== 고객 계정 관련 작업 메뉴 ===== =====")
        print("[1] | 고객 계정 생성")
        print("[2] | 고객 계정 삭제")
        print("[3] | 고객 계정 수정")
        print("[4] | 고객 계정 비밀번호 초기화")
        print("[0] | 이전 메뉴")
        print("===== ===== ===== ===== ===== =====")
        
    # 직원 로그인 후 메뉴 선택 [메인 화면]
    def employeeMenu(self , employee_department) :
        employeemenu_list = [None , self.cus_employeeMenu , self.accountMenu]
        
        while True :
            self.p_employeeMenu(employee_department)
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu > 0 and select_menu < len(employeemenu_list) :
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
                if select_menu > 0 and select_menu < len(employeemenu_list) :
                    employeemenu_list[select_menu]()
                elif select_menu == 0 :
                    return
                else :
                    print("메뉴에 있는 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력해주세요.")
    
    # ===== 고객 계정 관련 작업 함수
    # 고객을 추가하기 위해서 고객의 정보를 입력받아서 DB 에 전송할 함수
    # //FIXME [1] [국적] 항목에 외국인이 가입하였을 경우를 추가 //TODO [1] 추가 완료
    # //FIXME [2] 아이디와 비밀번호를 받아서 유효성 체크 후 반환하도록 추가 //TODO [2] 추가 완료
    def addCustomer(self) :
        customer = {"customer_name" : "" , "customer_id" : "" , "customer_password" : "" , "resident_number" : "" , "customer_gender" : "" , "customer_age" : 0 , "customer_birthday" : "" , "customer_nationality" : "" , "customer_phone" : "" , "customer_account" : []}
        customer["customer_name"]        = input("고객 이름 입력 : ")
        customer["customer_id"]          = self.getId()
        customer["customer_password"]    = self.getPassword(0)
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
            
    # 계정 및 계좌에 사용할 비밀번호를 받아서 유효성 체크 후 반환하는 함수
    #//FIXME [1] 계정과 계좌 비밀번호를 받을 때 구분해서 출력이 다르도록 수정 //TODO [1] 수정 완료
    def getPassword(self , select_type) :
        flag = False
        type_list = ["고객계정" , "고객계좌" , "직원계정"]
        
        while flag == False :
            customer_password = input(f"{type_list[select_type]}에 사용할 비밀번호 입력 : ")
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
        customer_information = None
        
        while customer_information == None :
            customer_name        = input("고객 이름 입력 : ")
            customer_password    = input("계정 비밀번호 입력 : ")
            customer_information = BankDB.BankDatabase.searchCustomer(customer_name , customer_password)
            if customer_information == None :
                print("고객 이름 또는 비밀번호를 다시 확인해주세요.")
        
        return customer_information
    
    # 고객 계정 삭제 함수
    # //FIXME [1] 생년월일이 아닌 계정 비밀번호를 받아서 삭제할 수 있도록 수정 필요 //TODO [1] 수정 완료
    # //FIXME [2] 고객 이름과 계정 비밀번호를 입력받아서 고객 정보를 받아오는 행위가 자주 사용될 듯 하여 별도 함수로 제작하기 //TODO [2] 추가 함수를 제작하여 완료
    def delCustomer(self) :
        while True :
            customer_information = self.searchCustomerInformation()
            if customer_information != None :
                BankDB.BankDatabase.deleteCustomer(customer_information)
                return
            print("이름과 계정 비밀번호를 다시 확인해주세요.")
    
    # //FIXME [1] 수정하고 싶은 항목을 선택해서 수정할 수 있도록 변경 필요 //TODO [1] 변경 완료
    # //FIXME [2] 생년월일이 아닌 계정 비밀번호를 받아서 수정할 수 있도록 수정 필요 //TODO [2] 수정 완료
    # 고객 계정 정보 수정 함수
    def modCustomer(self) :
        while True :
            customer_information = self.searchCustomerInformation()
            if customer_information != None :
                self.modCustomerDetail(customer_information)
                return
            print("이름과 계정 비밀번호를 다시 확인해주세요.")
    
    # 고객 계정 정보 수정 메뉴
    # 주민등록번호 변경 시 생일 , 성별 , 나이 , 국적 등 관련된 정보가 바로 같이 변경이 되어야 함
    def p_modCustomer(self , customer_name) :
        print(f"[{customer_name}] 님 계정의 수정할 항목 선택")
        print("===== ===== 항목 ===== =====")
        print("[1] | 이름 변경")
        print("[2] | 주민등록번호 변경")
        print("[3] | 연락처 변경")
        print("[0] | 메뉴 종료")
        print("===== ===== ===== ===== ===== =====")
    
    # 고객 계정 정보 수정 함수(상세)
    def modCustomerDetail(self , customer_information) :
        modify_menu_list = [None , 1 , 2 , 3]
        
        while True :
            self.p_modCustomer(customer_information["customer_name"])
            try :
                select_menu = int(input("수정 항목 선택 : "))
                if select_menu > 0 and select_menu < len(modify_menu_list) :
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
        print("===== ===== 고객 계좌 관련 작업 메뉴 ===== =====")
        print("[1] | 계좌 생성")
        print("[2] | 계좌 삭제")
        print("[3] | 계좌 비활성화")
        print("[4] | 계좌 활성화")
        print("[5] | 계좌 비밀번호 초기화")
        print("[0] | 이전 메뉴")
        print("===== ===== ===== ===== ===== =====")
    
    def p_acc_add_employeeMenu(self) :
        print("===== ===== 생성 계좌 선택 메뉴 ===== =====")
        print("[1] | 일반계좌 생성")
        print("[2] | 적금계좌 생성")
        print("[3] | 예금계좌 생성")
        print("[4] | 청약계좌 생성")
        print("[5] | 주식계좌 생성")
        print("[0] | 이전 메뉴")
        print("===== ===== ===== ===== ===== =====")
    
    # ===== 고객 계좌 생성 관련 함수
    def accountMenu(self) :
        account_menu_list = [None , self.addAccountMenu , self.delAccount , self.inActiveAccount , self.activeAccount , self.resetPwdAccount]
        
        while True :
            self.p_acc_employeeMenu()
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu > 0 and select_menu < len(account_menu_list) :
                    account_menu_list[select_menu]()
                    return
                elif select_menu == 0 :
                    return
                else :
                    print("메뉴에 있는 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    # 고객 계좌 생성 메뉴 선택 함수
    def addAccountMenu(self) :
        add_account_menu_list = [ 1 , 2 , 3 , 4 , 5 ]
        
        while True :
            self.p_acc_add_employeeMenu()
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu in add_account_menu_list :
                    self.addAccount(select_menu)
                    return
                elif select_menu == 0 :
                    return
                else :
                    print("메뉴에 있는 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    # //FIXME [1] customer_information["customer_account"] 가 빈 항목일경우 if 에서 오류 발생됨 //TODO [1] 수정 완료
    # 고객 계좌 생성 함수
    def addAccount(self , account_type) :
        account_type_list = [None , "일반계좌" , "적금계좌" , "예금계좌" , "청약계좌" , "주식계좌" , "1001" , "1002" , "1003" , "2001" , "7077"]
        
        customer_information = self.searchCustomerInformation()
        if len(customer_information["customer_account"]) >= 5 and customer_information["customer_account"] != [] :
            print(f"[{customer_information["customer_name"]}] 님은 계좌 생성 한도에 도달하여 더 이상 계좌를 생성할 수 없습니다.")
            return
        BankDB.BankDatabase.addCustomerAccount(customer_information , account_type_list[account_type + 5] , account_type_list[account_type])
    
    # //FIXME [1] 고객 정보를 오입력하여 로그인이 정상적으로 이루어지지 않은 경우 오류 발생됨 //TODO [1] 수정 완료 - 고객 정보를 받는 함수에 반복문 사용
    # 고객 계좌 정보를 확인받고 삭제하는 함수
    def delAccount(self) :
        customer_information = self.searchCustomerInformation()
        if len(customer_information["customer_account"]) == 0 :
            print(f"[{customer_information["customer_name"]}] 님은 생성된 계좌가 없습니다.")
            return
        select_account_number = self.selAccount(customer_information , 0)
        BankDB.BankDatabase.delCustomerAccount(customer_information , select_account_number)
    
    # 고객 계좌 정보를 확인받고 비활성화하는 함수
    def inActiveAccount(self) :
        customer_information = self.searchCustomerInformation()
        if len(customer_information["customer_account"]) == 0 :
            print(f"[{customer_information["customer_name"]}] 님은 생성된 계좌가 없습니다.")
            return
        select_account_number = self.selAccount(customer_information , 1)
        BankDB.BankDatabase.inActiveCustomerAccount(customer_information , select_account_number)
        
    # 고객 계좌 정보를 확인받고 활성화하는 함수
    def activeAccount(self) :
        customer_information = self.searchCustomerInformation()
        if len(customer_information["customer_account"]) == 0 :
            print(f"[{customer_information["customer_name"]}] 님은 생성된 계좌가 없습니다.")
            return
        select_account_number = self.selAccount(customer_information , 2)
        BankDB.BankDatabase.activeCustomerAccount(customer_information , select_account_number)
    
    # 고객의 계좌를 조회하고 계좌의 비밀번호를 초기화하는 함수
    def resetPwdAccount(self) :
        customer_information = self.searchCustomerInformation()
        if len(customer_information["customer_account"]) == 0 :
            print(f"[{customer_information["customer_name"]}] 님은 생성된 계좌가 없습니다.")
            return
        select_account_number = self.selAccount(customer_information , 3)
        BankDB.BankDatabase.resetCustomerAccountPassword(customer_information , select_account_number)
                
    # //FIXME [1] 더 짧게 함수를 쪼개서 만들어야함 //TODO [1] 별도 출력만 하는 함수를 만들어서 수정 완료
    # //FIXME [2] 숫자가 아닌 값이 입력될 때 오류는 안 나오지만 반복이 풀리고 메뉴를 나오게 됨 //TODO [2] 수정 완료
    # //FIXME [3] 메뉴 리스트를 사용하여 동일한 함수를 여러번 작성되지 않게 함 //TODO [3] 수정 완료
    # 고객이 계좌를 선택하고 선택한 숫자를 리턴하는 함수
    def selAccount(self , customer_information , select_menu) :
        index_list = self.p_customerAccount(customer_information , 1)
        menu_list  = ["삭제할" , "비설성화할" , "활성화할" , "비밀번호를 초기화할"]
        
        while True :
            try :
                select_account_number = int(input(f"{menu_list[select_menu]} 계좌 번호 입력 : ")) - 1
                if select_account_number not in index_list :
                    print("선택할 수 없는 번호입니다.")
                else :
                    return select_account_number
            except ValueError :
                print("숫자만 입력해주세요.")
    
    # //FIXME [1] 계좌가 inacitve 상태인데 비활성화라고 뜨지 않음 //TODO [1] 수정완료 - DB 모듈에서 부등호가 잘못됨
    # 고객의 계좌를 조회하고 필요에 따라 필요 정보를 리턴하는 함수
    def p_customerAccount(self , customer_information , pls_return) :
        index_list = []
        
        for index , account in enumerate(customer_information["customer_account"]) :
            account_condtion = "활성화"
            if account["account_condition"] == "inactive" :
                account_condtion = "비활성화"
            print("===== ===== ===== ===== ===== =====")
            print(f"[{index + 1}] | 계좌 종류 : [{account["account_name"]}]")
            print(f"계좌 상태 : [{account["account_balance"]}]")
            print(f"계좌 상태 : [{account_condtion}]\n")
            index_list.append(int(index))
        
        if pls_return == 1 :
            return index_list
        return
    
    # ===== 직원 메뉴 [직원 계정 관련 작업]
    # 직원 계정의 경우 비밀번호 수정이 바로 가능하도록 설정 / 고객 계정은 비밀번호를 불러오지 못하고 초기화만 됨
    def p_em_employeeMenu(self) :
        print("===== ===== 직원 계정 관련 작업 메뉴 ===== =====")
        print("[1] | 직원 계정 생성")
        print("[2] | 직원 계정 삭제")
        print("[3] | 직원 계정 수정")
        print("[0] | 이전 메뉴")
        print("===== ===== ===== ===== ===== =====")
    
    # 직원 계정 관련 메뉴 선택 함수
    def employeeAccountMenu(self) :
        employee_account_menu_list = [None]
        
        while True :
            self.p_em_employeeMenu()
            try :
                select_menu = int(input(""))
                if select_menu > 0 and select_menu < len(employee_account_menu_list) :
                    employee_account_menu_list[select_menu]()
                elif select_menu == 0 :
                    return
                else :
                    print("메뉴에 있는 숫자만 입력해주세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    # 직원 계정 생성 함수
    def addemployeeAccount(self) :
        employee = {"employee_name" : "" , "employee_id" : "" , "employee_password" : "" , "employee_department" : "" , "employee_rank" : "" , "employee_resident_number" : "" , "employee_condition" : "재직"}
        
        employee["employee_name"]            = input("사원 이름 입력 : ")
        employee["employee_id"]              = input("사원 계정 아이디 입력 : ")
        employee["employee_password"]        = self.getPassword(2)
        employee["employee_department"]      = self.selDepartment()
        employee["employee_resident_number"] = self.getResidentNumber()
        employee["employee_rank"]            = self.selRank()
    
    # 부서의 리스트를 출력하는 함수
    def p_selDepartment(self) :
        print("===== ===== 부서 리스트 ===== =====")
        print("[1] | 관리팀")
        print("[2] | 총무팀")
        print("[3] | 영업팀")
        print("[4] | 마케팅팀")
        print("[5] | 기획팀")
        print("[6] | 개발1팀")
        print("[7] | 개발2팀")
        print("[8] | 유지보수팀")
        print("===== ===== ===== ===== ===== =====")
    
    # 부서 리스트에 대한 값을 입력받아서 반환하는 함수
    def selDepartment(self) :
        department_list = [None , "관리팀" , "총무팀" , "영업팀" , "마케팅팀" , "기획팀" , "개발1팀" , "개발2팀" , "유지보수팀"]
        
        while True :
            self.p_selDepartment()
            try :
                select_menu = int(input("부서 선택 : "))
                if select_menu > 0 and len(department_list) :
                    return department_list[select_menu]
                else :
                    print("리스트에 있는 숫자만 입력해주세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    def p_selRank(self) :
        print("===== ===== 직급 리스트 ===== =====")
        print("[1] | 인턴")
        print("[2] | 사원")
        print("[3] | 주임")
        print("[4] | 팀장")
        print("[5] | 부장")
        print("[6] | 전무")
        print("[7] | 이사")
        print("[8] | 사장")
        print("[9] | 대표")
        print("===== ===== ===== ===== ===== =====")
    
    # 부서 리스트에 대한 값을 입력받아서 반환하는 함수
    def selRank(self) :
        rank_list = [None , "인턴" , "사원" , "주임" , "팀장" , "부장" , "전무" , "이사" , "사장" , "대표"]
        
        while True :
            self.p_selRank()
            try :
                select_menu = int(input("직급 선택 : "))
                if select_menu > 0 and len(rank_list) :
                    return rank_list[select_menu]
                else :
                    print("리스트에 있는 숫자만 입력해주세요.")
            except ValueError :
                print("숫자만 입력하세요.")
        
# 시작
if __name__ == "__main__" :
    manager = Bankmanager()
    manager.loginEmployee()