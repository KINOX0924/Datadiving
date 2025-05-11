# 은행 계좌 프로그램
# 고객 명단(리스트) -> 고객(계좌번호(유일) , 고객명 , 아이디 , 비밀번호 , 잔고)
# 고객은 아이디와 비밀번호를 사용해서 잔고에 접근 -> 잔고 조회 / 금액 입금 / 금액 인출
# 관리자는 고객 명단에 접근 -> 고객 생성 / 고객 삭제 / 고객 수정 / 고객 조회
# 관리자가 고객 수정 시 고객의 이름과 비밀번호 초기화만 가능

# 외부 모듈 호출
import random
import pickle

# 단말기 클래스 생성
# 고객 정보가 저장되고 고객과 관리자는 해당 단말기를 이용하여 기능 접근이 가능
class BankTerminal :
    # 터미널에는 고객정보가 저장되어 있음 / 고객 정보는 클래스 변수에 저장되며 매번 객체 생성 없이 접근 가능함
    customer_list = [
        {"ACCOUNT_NUMBER" : "1001-8876285430" , "NAME" : "김예빈" , "ID" : "KIMM" , "PASSWORD" : "aaaaa1" , "BALANCE" : 785321},
        {"ACCOUNT_NUMBER" : "1001-2696634905" , "NAME" : "이지후" , "ID" : "LEEE" , "PASSWORD" : "bbbbb2" , "BALANCE" : 23987 },
        {"ACCOUNT_NUMBER" : "1001-4060584195" , "NAME" : "박서준" , "ID" : "PARK" , "PASSWORD" : "ccccc3" , "BALANCE" : 956123},
        {"ACCOUNT_NUMBER" : "1001-8574222639" , "NAME" : "최수아" , "ID" : "CHOI" , "PASSWORD" : "ddddd4" , "BALANCE" : 412789},
        {"ACCOUNT_NUMBER" : "1001-3206020354" , "NAME" : "정하연" , "ID" : "JUNG" , "PASSWORD" : "eeeee5" , "BALANCE" : 159357}
    ]
    
    def __init__(self) :
        self.customer = {"ACCOUNT_NUMBER" : "" , "NAME" : "" , "ID" : "" , "PASSWORD" : "" , "BALANCE" : 0}

# 고객 클래스 생성
# 고객이 터미널을 이용할 때 사용하는 함수
class Customer :
    def __init__(self) :
        pass

# 관리자 클래스 생성
# 관리자가 터미널을 이용할 때 사용하는 함수
class Admin :
    def __init__(self) :
        pass
    
    # =========================== 관리자가 고객 정보를 출력할 때 사용하는 함수 =========================== #
    def printAccAdmin(self , account) :
        print(f"계좌 번호 : {account["ACCOUNT_NUMBER"]}" , end = "\t")
        print(f"이름 : {account["NAME"]}" , end = "\t")
        print(f"아이디 : {account["ID"]}" , end = "\t")
        print(f"잔고 : {account["BALANCE"]}")
    
    # =========================== 관리자가 고객의 신규 계정을 생성하는 함수 모음 =========================== #
    def creAcc(self) :
        customer = BankTerminal()
        customer.customer["ACCOUNT_NUMBER"] = self.creAccnum()
        customer.customer["NAME"]           = input("고객 이름 입력 : ")
        customer.customer["ID"]             = self.creId()
        customer.customer["PASSWORD"]       = self.crePwd()
        customer.customer["BALANCE"]        = 100  # 100 원은 계좌 생성을 확인하는 것과 축하하는 의미에서 지급
        print(f"{customer.customer["NAME"]} 님의 계좌가 성공적으로 생성되었습니다.")
        print(f"계좌 생성을 축하하는 의미에서 {customer.customer["NAME"]} 님의 계좌에 100 원을 입금해드렸습니다.")
    
    # ====== 은행을 인식하는 기본 계좌번호를 제외한 나머지 계좌번호를 랜덤으로 생성하는 함수
    def creAccnum(self) :
        create_account_number = ["1" , "0", "0" , "1" , "-"] 
        for i in range(0,10) :
            create_account_number.append(str(random.randint(0,9)))
        
        new_account_number = "".join(create_account_number)
        return new_account_number
        # 생성된 계좌번호는 리턴하여 생성중인 고객 객체의 계좌번호에 입력
    
    # ====== 관리자가 생성중인 고객의 신규 계정의 아이디를 입력받는 함수
    def creId(self) :
        flag = False
        # 고객이 입력한 아이디의 체크가 끝나는지 확인하는 함수
        
        while flag == False :
            create_name = input("사용할 아이디 입력 : ")
            
            flag = self.effectChkId(create_name)
            # 고객이 입력하여 사용하고 싶은 아이디의 적정성을 확인하기 위해 적정성 확인 함수 호출
        return create_name
        
    # ====== 고객이 입력한 아이디의 유효성을 확인하는 함수
    def effectChkId(self , create_name) :
        # 터미널에 접근하여 고객 정보를 확인하고 중복되는 아이디가 있는 지 확인
        for v in BankTerminal.customer_list :
            if create_name == v["ID"] :
                print("이미 같은 아이디가 존재합니다.\n다른 아이디를 입력해주세요.\n")
                return False
        
        if len(create_name) < 4 :
            print("아이디는 최소 4글자 이상 입력해주세요.\n아이디를 다시 입력해주세요.\n")
            return False
        elif " " in create_name :
            print("아이디 내에 공백이 존재합니다.\n아이디를 다시 입력해주세요.\n")
            return False
        return True
        # 아이디 중복 체크 , 최소 길이 , 공백 존재 확인 후 오류 있으면 False 반환 / 없으면 True 반환
    
    # ===== 관리자가 생성중인 고객의 신규 계정의 비밀번호를 입력받는 함수
    # [1] 비밀번호를 두 번 입력받아 더블 체크가 가능하도록 함
    # [2] 비밀번호의 유효성을 검사
    def crePwd(self) :
        flag = [False , False]
        while flag[0] == False or flag[1] == False :
            create_password_one = input("사용할 비밀번호 입력 : ")
            create_password_two = input("비밀번호 재입력      : ")
            
            flag[1] = self.effectChkPwd(create_password_one)
            if flag[1] == True :
                flag[0] = self.doubleChkPwd(create_password_one , create_password_two)
        return create_password_two
    
    # 입력받은 두 개의 비밀번호가 일치하는 지 확인
    def doubleChkPwd(self , create_password_one , create_password_two) :
        if create_password_one != create_password_two :
            print("비밀번호가 일치하지 않습니다.\n비밀번호를 다시 입력해주세요.\n")
            return False
        return True
    
    # 입력받은 비밀번호의 유효성을 확인
    def effectChkPwd(self , create_password) :
        if len(create_password) < 5 :
            print("비밀번호는 최소 5글자 이상 입력해주세요.\n비밀번호를 다시 입력해주세요.\n")
            return False
        elif " " in create_password :
            print("비밀번호 내에 공백이 존재합니다.\n비밀번호를 다시 입력해주세요.\n")
            return False
        return True
    
    # =========================== 관리자가 고객의 계좌을 검색할 때 사용하는 함수  =========================== #
    def searchAcc(self) :
        flag = False
        
        while flag == False :
            account_number = input("고객 계좌번호 검색 : ")
            if len(account_number) == 15 :
                account_copy = next(filter(lambda x : account_number == x["ACCOUNT_NUMBER"] , BankTerminal.customer_list) , None)
                if account_copy == None :
                    print("은행 데이터베이스에 존재하지 않는 계좌번호입니다.")
                    flag = False
                else :
                    flag = True
            else :
                print("잘못된 계좌번호입니다.")
                flag = False
            
        self.printAccAdmin(account_copy)
        return account_copy

# 시작 코드
if __name__ == "__main__" :
    admin = Admin()
    admin.searchAcc()