# p_ 무언가를 출력하는 함수들
# add_ 무언가를 입력하는 함수들
# sch_ 무언가를 찾아내는 함수들
# cal_ 무언가를 계산하는 함수들

class EmployeeTerminal :
    def __init__(self) :
        pass
    
    def p_mainMenu(self) :
        print("\n====================")
        print("[1] | 직원 로그인")
        print("[0] | 프로그램 종료")
    
    def p_workMenu(self , employee_number) :
        menu_list = [
            None ,
            ["[1] | 개인 금융 업무" , "[2] | 본인 정보 수정" , "[3] | "]
        ]