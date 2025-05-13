from BankDB import BankDatabase
import random

class Bankmanager :
    def addCustomer(self) :
        customer = {"customer_name" : "" , "customer_gender" : "" , "resident_number" : "" , "customer_age" : 0 , "customer_birthday" : "" , "customer_nationality" : "대한민국" , "customer_phone" : "010-0000-0000" , "customer_account" : []}
        customer["customer_name"]   = input("고객 이름 입력 : ")
        customer["customer_gender"] = self.selGender()
        customer["resident_number"] = self.getResidentNumber()
    
    def selGender(self) :
        gender_list = [None , "male" , "female"]
        while True :
            try :
                select_menu = int(input("성별 선택 [1] 남성 | [2] 여성 : "))
                if select_menu > 0 and select_menu <= len(gender_list) :
                    return gender_list[select_menu]
                else :
                    print("[1] 또는 [2] 만 입력하세요.")
            except ValueError :
                print("잘못된 입력입니다. 다시 입력하세요.")
    
    def getResidentNumber(self) :
        resident_number = input("주민번호 입력 : ")
        
                
# 시작
if __name__ == "__main__" :
    manager = Bankmanager()
    manager.addCustomer()