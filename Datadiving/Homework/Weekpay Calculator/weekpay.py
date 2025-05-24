# 저장 / 불러오기 기능 추가
# 계산에 연장 수당(20시간 이상 근무 시 50% 가산)
class Person :
    def __init__(self , name = "" , paypertime = 0 , worktime = 0) :
        self.name       = name
        self.paypertime = paypertime
        self.worktime   = worktime
        self.calPay()
    
    def calPay(self) :
        self.totalpay = self.paypertime * self.worktime
    
    def outPut(self) :
        print("이름 : " , self.name , "\t시간당 급여액 : " , self.paypertime , "\t근무 시간 : " , self.worktime , "\t총 주급 : " , self.totalpay)

if __name__ == "__main__" :
    w1 = Person("A")
    w1.outPut()