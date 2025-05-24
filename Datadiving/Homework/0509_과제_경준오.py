# 주급 계산
# 저장 / 불러오기 기능 추가 하기
# 주급 계산 시 연장 수당(20시간 이상 근무 시 초과 근무분에 대한 50% 가산) 추가

import pickle

class Worker :
    def __init__(self) :
        self.name        = ""
        self.paypertime  = 0
        self.worktime    = 0
        self.overtime    = 0
        self.weekpay     = 0

    def getOverwork(self) :
        if self.worktime > 20 :
            self.overtime = self.worktime - 20

    def getWeekpay(self) :
        normal_pay = self.paypertime * (self.worktime - self.overtime)
        over_pay   = int(self.paypertime * 1.5 * self.overtime)

        self.weekpay = normal_pay + over_pay

    def calWeekpay(self) :
        self.getOverwork()
        self.getWeekpay()

    def insertWorker(self) :
        self.name       = input("근무자 이름 입력 : ")
        self.paypertime = int(input("시간당 급여액 입력 : "))
        self.worktime   = int(input("주간 근무 시간 입력 : "))

    def printWorker(self) :
        print(f"근무자명 : {self.name}" , end = "\t")
        print(f"시간당 급여액 : {self.paypertime} 원" , end = "\t")
        print(f"총 근무시간 : {self.worktime} 시간" , end = "\t")
        print(f"연장 근무시간 : {self.overtime} 시간" , end = "\t")
        print(f"총 주급: {self.weekpay} 원")



class Workermanager :
    def __init__(self) :
        self.worker_list = []

    # 근무자 정보 입력
    def addWorker(self) :
        worker = Worker()
        worker.insertWorker()
        worker.calWeekpay()
        self.worker_list.append(worker)

    # 근무자 정보 출력
    def printWorkerlist(self) :
        for worker in self.worker_list :
            worker.printWorker()

    # 근무자 정보 검색
    def searchWorker(self) :
        worker_name   = input("검색할 근무자 이름 입력 : ")
        worker_list_1 = list(filter(lambda x : worker_name in x.name , self.worker_list))

        if len(worker_list_1) <= 0 :
            print("검색된 데이터가 없습니다.")
            return

        for w in worker_list_1 :
            w.printWorker()

    # 근무자 정보 수정
    def modifyWorker(self) :
        worker_name   = input("수정할 근무자 이름 입력 : ")
        worker_list_1 = list(filter(lambda x : worker_name in x.name , self.worker_list))

        if len(worker_list_1) <= 0 :
            print("검색된 데이터가 없습니다.")
            return

        for i , w in enumerate(worker_list_1) :
            print(f"번호 : [{i}]" , end = "\t")
            w.printWorker()
        select = int(input("수정할 근무자 번호 입력 : "))
        modify = worker_list_1[select]

        for i , w in enumerate(self.worker_list) :
            if w == modify :
                w.name       = input("근무자 이름 입력 : ")
                w.paypertime = int(input("시간당 급여액 입력 : "))
                w.worktime   = int(input("주간 근무 시간 입력 :"))
                w.calWeekpay()

    # 근무자 정보 삭제
    def deleteWorker(self) :
        worker_name   = input("삭제할 근무자 이름 입력 : ")
        worker_list_1 = list(filter(lambda x : worker_name in x.name , self.worker_list))

        if len(worker_list_1) <= 0 :
            print("검색된 데이터가 없습니다.")
            return

        for i , w in enumerate(worker_list_1) :
            print(f"번호 : [{i}]" , end = "\t")
            w.printWorker()
        select = int(input("삭제할 근무자 번호 입력 : "))
        self.worker_list.remove(worker_list_1[select])

    # 근무자 정보 저장
    def saveWorkerlist(self) :
        data = self.worker_list
        with open("worker_list.bin" , "wb") as file :
            pickle.dump(data , file)
        print("근무자 정보 저장 완료")
        print("저장 파일명 : worker_list.bin")

    # 근무자 정보 읽기
    def loadWorkerlist(self) :
        with open("worker_list.bin" , "rb") as file :
            self.worker_list = pickle.load(file)
        print("근무자 정보 읽기 완료")

    # 메인 메뉴 항목 출력
    def printMenu(self) :
        print("====== [메뉴] ======")
        print("[1] 근무자 정보 입력")
        print("[2] 근무자 정보 출력")
        print("[3] 근무자 정보 검색")
        print("[4] 근무자 정보 수정")
        print("[5] 근무자 정보 삭제")
        print("[6] 근무자 정보 저장")
        print("[7] 근무자 정보 읽기")
        print("[0] 프로그램 종료")
        print("====== [메뉴] ======")

    # 메인 메뉴 시작
    def menuStart(self) :
        menu_list = [None , self.addWorker , self.printWorkerlist , self.searchWorker , self.modifyWorker , self.deleteWorker , self.saveWorkerlist , self.loadWorkerlist]

        while True :
            self.printMenu()
            select = int(input("메뉴 선택 : "))

            if select > 0 and select < len(menu_list) :
                menu_list[select]()
            elif select == 0 :
                return False
            else :
                print("메뉴를 잘못 선택하셨습니다.")


if __name__ == "__main__" :
    program = Workermanager()
    program.menuStart()