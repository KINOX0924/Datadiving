# 은행 계좌 프로그램
# 고객 명단(리스트) -> 고객(계좌번호(유일) , 고객명 , 아이디 , 비밀번호 , 잔고)
# 고객은 아이디와 비밀번호를 사용해서 잔고에 접근 -> 잔고 조회 / 금액 입금 / 금액 인출
# 관리자는 고객 명단에 접근 -> 고객 생성 / 고객 삭제 / 고객 수정 / 고객 조회


# 외부 모듈 호출
import random
import pickle

# 단말기 클래스 생성
# 고객 정보가 저장되고 고객과 관리자는 해당 단말기를 이용하여 기능 접근이 가능
class Terminal :
    # 터미널에는 고객정보가 저장되어 있음
    customer_list = [
        {"ACCOUNT_NUMBER" : "1001-8876285430" , "NAME" : "김예빈" , "ID" : "KIMM" , "PASSWORD" : "aaa1" , "BALANCE" : 785321},
        {"ACCOUNT_NUMBER" : "1001-2696634905" , "NAME" : "이지후" , "ID" : "LEEE" , "PASSWORD" : "bbb2" , "BALANCE" : 23987 },
        {"ACCOUNT_NUMBER" : "1001-4060584195" , "NAME" : "박서준" , "ID" : "PARK" , "PASSWORD" : "ccc3" , "BALANCE" : 956123},
        {"ACCOUNT_NUMBER" : "1001-8574222639" , "NAME" : "최수아" , "ID" : "CHOI" , "PASSWORD" : "ddd4" , "BALANCE" : 412789},
        {"ACCOUNT_NUMBER" : "1001-3206020354" , "NAME" : "정하연" , "ID" : "JUNG" , "PASSWORD" : "eee5" , "BALANCE" : 159357}
    ]
    
    def __init__(self) :
        self.customer = {"ACCOUNT_NUMBER" : "" , "NAME" : "" , "ID" : "" , "PASSWORD" : "" , "BALANCE" : 100}

# 고객 클래스 생성
# 고객의 기본적인 정보를 생성하는 클래스
class Customer :
    def __init__(self) :
        self.account_number   = ""
        self.account_name     = ""
        self.account_id       = ""
        self.account_password = ""
        self.account_balance  = 0

# 관리자 클래스 생성
# 관리자의 기능이 담긴 클래스
class Admin :
    def __init__(self) :
        pass
    
    def creCus(self) :
        account = Customer()
        account.account_number = self.creAccnum()
        account.account_name   = input("고객 이름 입력 : ")
    
    # 은행을 인식하는 기본 계좌번호를 제외한 나머지 계좌번호를 랜덤으로 생성하는 함수
    def creAccnum(self) :
        create_account_number = ["1" , "0", "0" , "1" , "-"] 
        for i in range(0,10) :
            create_account_number.append(str(random.randint(0,9)))
        
        new_account_number = "".join(create_account_number)
        return new_account_number   # 생성된 계좌번호는 리턴하여 생성된 고객 객체의 계좌번호에 입력
    
    # 고객이 ID 를 입력받는 함수
    def creId(self) :
        while True :
            create_name = input("사용할 아이디를 입력 : ")
            
            self.chkId(create_name)    # 고객이 입력하여 사용하고 싶은 아이디의 적정성을 확인하기 위해 적정성 확인 함수 호출
    
    def chkId(self , create_name) :
        for i , v in enumerate(Terminal.customer_list) :
            if create_name == v["ID"] :
                print("이미 같은 아이디가 존재합니다.")
                print("다른 아이디를 입력해주세요.")
                return
        
        if len(create_name) < 4 :
            print("아이디는 최소 4글자 이상 입력해주세요.")
            print("아이디를 다시 입력해주세요.")
            return
        
        if " " in create_name :
            print("아이디 내에 공백이 존재합니다.")
            print("아이디를 다시 입력해주세요.")
            return

# 시작 코드
if __name__ == "__main__" :
    admin = Admin()
    admin.creId()