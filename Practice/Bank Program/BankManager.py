from BankDB import BankDatabase

class Bankmanager :
    def addCustomer(self) :
        customer = {"customer_name" : "" , "customer_gender" : "" , "resident_number" : "" , "customer_birthday" : "" , "customer_nationality" : "대한민국" , "customer_phone" : "010-0000-0000" , "customer_account" : {}}
        customer["customer_name"] = input("고객 이름 입력 : ")
    
    def selGender(self) :
        gender_list = [None , "male" , "female"]
        while True :
            try :
                select_menu = int(input("성별 선택 [1] 남성 | [2] 여성 : "))
                if select_menu 
            except ValueError :
                print("잘못된 입력입니다. 다시 입력해주세요.")
                
        

# 시작
if __name__ == "__main__" :
    manager = Bankmanager()
    manager.addCustomer()