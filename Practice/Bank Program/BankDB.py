# 고객 정보가 저장되는 모듈(파일)

import BankManager
import PatternList

import datetime

class BankDatabase :
    __customer_list = [
        {"customer_name" : "김민준" , "resident_number" : "950315-1827345" , "customer_gender" : "male"   , "customer_age" : 30 , "customer_birthday" : "1995-03-15" , "customer_nationality" : "대한민국" , "customer_phone" : "010-8765-4321" , "customer_account" : []} ,
        {"customer_name" : "이서윤" , "resident_number" : "021122-2765901" , "customer_gender" : "female" , "customer_age" : 23 , "customer_birthday" : "2002-11-22" , "customer_nationality" : "대한민국" , "customer_phone" : "010-1234-5678" , "customer_account" : []} ,
        {"customer_name" : "박지훈" , "resident_number" : "880607-1592038" , "customer_gender" : "male"   , "customer_age" : 37 , "customer_birthday" : "1988-06-07" , "customer_nationality" : "대한민국" , "customer_phone" : "010-9876-5432" , "customer_account" : []} ,
        {"customer_name" : "정수아" , "resident_number" : "990910-2481635" , "customer_gender" : "female" , "customer_age" : 26 , "customer_birthday" : "1999-09-10" , "customer_nationality" : "대한민국" , "customer_phone" : "010-5555-1212" , "customer_account" : []} ,
        {"customer_name" : "최현우" , "resident_number" : "050128-3094756" , "customer_gender" : "male"   , "customer_age" : 20 , "customer_birthday" : "2005-01-28" , "customer_nationality" : "대한민국" , "customer_phone" : "010-3333-9999" , "customer_account" : []}
        ]
    # 고객 리스트
    # 고객 정보
    # 이름 , 성별 , 주민등록번호 , 나이 , 생년월일 , 국적 , 휴대폰 번호 , 계좌
    # 계좌 정보 (계좌 안에서 또 다른 딕셔너리로 구분)
    # 계좌 정보 (형태 : 일반계좌(1001) , 적금계좌(1002) , 예금계좌(1003) , 청약계좌(2001)) , 계좌 번호
    
    __account_list  = []
    account_type    = {"일반계좌" : "1001" , "적금계좌" : "1002" , "예금계좌" : "1003" , "청약계좌" : "2001" , "주식계좌" : "7077"}
    # 계좌 리스트 정보
    # 계좌 종류 , 계좌 번호 , 계좌 소유자명 , 계좌 비밀번호 , 개설일 , 잔액 , 계좌 상태
    
    __trade_history = []
    # 거래 내역 정보
    # 계좌 종류 , 계좌 번호 , 이름 , 입금/출금 구분 , 거래된 금액 , 이체 된 곳
    
    __employee_accout_list    = [
        {"employee_name" : "마스터 계정" , "employee_id" : "master" , "employee_password" : "q1w2e3" , "employee_department" : "관리팀" , "employee_rank" : "마스터 계정"}
    ]
    # 직원 계정 리스트
    # 은행의 직원 계정이 저장되는 리스트
    # 직원 이름 , 직원 아이디 , 직원 비밀번호 , 직원 부서 , 직원 직급
   
    __employee_account_active_history = []
    # 직원 계정 접속 기록
    # 직웝 이름 , 직원 부서 , 직원 직급 , 접속 시간 , 로그인/로그아웃
    
        
    
    # ===== 직원 전용 함수 모음
    # 직원 계정 로그인 함수
    # //FIXME [1] 직원 접속 시 로그인 기록이 히스토리에 전송되도록 해야함 //TODO [1] 추가 완료
    @classmethod
    def loginEmployee(cls , login_employee_id , login_employee_password) :
        for employee in cls.__employee_accout_list :
            if login_employee_id == employee["employee_id"] and login_employee_password == employee["employee_password"] :
                print(f"[{employee["employee_department"]}] 의 [{employee["employee_name"]}] 님이 로그인되었습니다.")
                employee_login = {"emlopyee_name" : employee["employee_name"] , "employee_department" : employee["employee_department"] , "employee_rank" : employee["employee_rank"] , "login_time" : datetime.datetime.now().strftime("%Y%m%d-%H%M") , "active" : "LOGIN"}
                cls.__employee_account_active_history.append(employee_login)
                return True , employee["employee_rank"]
        print("아이디 또는 비밀번호가 틀렸습니다.")
        return False   
    
    # 고객 계정 생성 함수
    @classmethod
    def insertCustomer(cls , customer_information) :
        for index , customer in enumerate(cls.__customer_list) :
            if customer_information["customer_name"]   == customer["customer_name"] and \
               customer_information["resident_number"] == customer["resident_number"] :
                 print(f"[{customer_information["customer_name"]}] 님은 이미 생성된 계정이 존재합니다.")
                 return
        cls.__customer_list.append(customer_information)
        print(f"[{customer_information["customer_name"]}] 님의 계정이 정상적으로 생성되었습니다.")

    # 고객 정보 전달 함수
    @classmethod
    def searchCustomer(cls , customer_name , customer_birthday) :
        for customer in cls.__customer_list :
            if customer_name == customer["customer_name"] and customer_birthday == customer["resident_number"][:6] :
                return customer
        print("고객 계정 정보를 찾을 수 없습니다.")
        return None
    
    # 고객 계정 삭제 함수
    # 삭제 전 생성되어 있는 계좌가 있는 지 확인해야 함
    # 삭제 전 한 번 더 삭제를 원하는 지 확인 필요
    @classmethod
    def deleteCustomer(cls , customer_information) :
        if len(customer_information["customer_account"]) == 0 :
            flag = False
            while flag == False :
                answer = input(f"정말로 [{customer_information["customer_name"]}] 님의 계정을 삭제하시겠습니까(Y/N) : ")
                flag = PatternList.checkAnswer(answer)
                if flag == True and (answer == "Y" or answer == "y") :
                    print(f"[{customer_information["customer_name"]}] 님의 계정이 정상적으로 삭제되었습니다.")
                    cls.__customer_list.remove(customer_information)
                    return
                elif flag == True and (answer == "N" or answer == "n") :
                    return
                flag = False
                print("다시 입력해주세요.")
        print("생성되어 있는 계좌가 존재합니다. 계좌를 모두 해지 후 삭제를 진행하세요.")
    
# 시작
if __name__ == "__main__" :
    terminal = BankDatabase()