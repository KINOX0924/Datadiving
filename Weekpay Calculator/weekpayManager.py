from weekpay import Person

class Paymanager :
    
    def __init__(self) :
        self.person_list = [
            Person("홍길동" , 9700 , 20) ,
            Person("최길동" , 7700 , 25) ,
            Person("김길동" , 5700 , 15) ,
            Person("이길동" , 6500 , 35) ,
            Person("양길동" , 10700 , 10)
        ]
    
    def outPut(self) :
        for i in self.person_list :
            i.outPut()
            
    def search(self) :
        name = input("찾을 이름 입력 : ")
        result_list = list(filter(lambda x : x.name == name , self.person_list))
        if len(result_list) == 0 :
            print("데이터가 없습니다")
            return
        
        for i in result_list :
            i.outPut()
            
    def modify(self) :
        name = input("찾을 이름 입력 : ")
        result_list = list(filter(lambda x : name in x.name , self.person_list))
        if len(result_list) == 0 :
            print("데이터가 없습니다")
            return
        
        for i , w in enumerate(result_list) :
            print(i , end = "\t")
            w.outPut()

        sel = int(input("수정할 대상을 입력하세요(숫자로) : "))
        temp = result_list[sel]
        temp.name = input("이름 : ")
        temp.perpay = int(input("시간당 급여액 : "))
        temp.worktime = int(input("근무 시간 : "))
        temp.calPay()
        
        
    def delete(self) :
        name = input("찾을 이름 입력 : ")
        result_list = list(filter(lambda x : name in x.name , self.person_list))
        if len(result_list) == 0 :
            print("데이터가 없습니다.")
            return
        
        for i , w in enumerate(result_list) :
            print(i , end = "\t")
            w.outPut()
        sel = int(input("삭제할 대상을 입력하세요(숫자로) : "))
        self.person_list.remove(result_list[sel])
    
    def start(self) :
        print("start")

if __name__ == "__main__" : 
    mgr = Paymanager()
    mgr.outPut()
    mgr.modify()
    mgr.outPut()
    mgr.delete()
    mgr.outPut()