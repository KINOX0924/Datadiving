# 고객 정보가 저장되는 모듈(파일)

class BankDatabase :
    __customer_ist = []
    # 고객 리스트
    # 고객 정보
    # 이름 , 성별 , 주민등록번호 , 나이 , 생년월일 , 국적 , 휴대폰 번호 , 계좌
    # 계좌 정보 (계좌 안에서 또 다른 딕셔너리로 구분)
    # 계좌 정보 (형태 : 일반계좌(1001) , 적금계좌(1002) , 예금계좌(1003) , 청약계좌(2001)) , 계좌 번호
    
    __account_list  = []
    account_type    = {"일반계좌" : "1001" , "적금계좌" : "1002" , "예금계좌" : "1003" , "청약계좌" : "2001" , "주식계좌" : "7077"}
    # 계좌 리스트 정보
    # 계좌 종류 , 계좌 번호 , 개설일 , 잔액 , 계좌 상태
    
    __trade_history = []
    # 거래 내역 정보
    # 계좌 종류 , 계좌 번호 , 이름 , 입금/출금 구분 , 거래된 금액 , 이체 된 곳
    
    __employee_accout_list    = [
        {"employee_name" : "마스터 계정" , "employee_id" : "master" , "employee_password" : "q1w2e3" , "department" : "관리팀" , "rank" : "마스터 계정"}
    ]
    # 직원 계정 리스트
    # 은행의 직원 계정이 저장되는 리스트
    # 직원 이름 , 직원 아이디 , 직원 비밀번호 , 부서 , 직급
    
    # ===== 관리자 전용 함수 모음
    # 고객 가입
    @classmethod
    def insertCustomer(cls , customer_information) :
        for index , value in enumerate(cls.__customer_ist) :
            if customer_information["customer_name"]   == value["customer_name"] and \
               customer_information["resident_number"] == value["resident_number"] :
                 print(f"{customer_information["customer_name"]} 님은 이미 생성된 계정이 존재합니다.")
                 return
        cls.__customer_list.append(customer_information)
        print(f"{customer_information["customer_name"]} 님의 계정이 정상적으로 생성되었습니다.")

# 시작
if __name__ == "__main__" :
    terminal = BankDatabase()