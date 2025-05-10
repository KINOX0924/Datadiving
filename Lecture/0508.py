# 5월 8일 강의
# 객체 지향으로 가위바위보 게임 만들기

# 객체지향 - 클래스(사용자가 만드는 데이터 타입)
# 클래스를 가지고 객체를 만듬
# 객체는 Heap 공간에 저장되고, 객체의 주소(참조) 를 변수에 전달
# 메모리가 부족하면 None 전달
# 객체 내부의 변수나 함수에 접근하려면 .(도트 연산자) 를 이용해 접근
# 생성자는 __init__ 라는 이름을 갖고 기본적으로 파이썬에서는 객체의 자신의 주소를 전달하기 위해서 self 라는 매개변수를 첫번째 매개변수로 가지고 다녀야 함
# 변수명이 self 일 필요는 없지만 남들도 다 self 로 쓰니깐 사용하는 것(묵시적 동의)
# 클래스 설계 패턴 - 32가지(디자인 패턴) / 단 활용도는 낮음

# 클래스(객체 지향) 의 특징
# 추상화 : 내부 구조를 몰라도 사용하는데 지장이 없음 / 추상화가 될수록 사용자는 편하지만 반대로 추상화를 만드는 사람은 어려움
# 은닉화 : 다른 언어에서는 접근 권한을 만들어서 외부로부터 특정 변수나 함수에 접근불가상황을 기본으로 함 , 하지만 파이썬에서는 기본이 public 이어서 그런것이 없음
#       : 일부 변수를 외부에 누출시키기 싫은 경우 변수나 함수 앞에 __(언더바 2개) 를 붙이면 private 로 인식
# 상속성 : 추후 설명
# 다형성 : 매개변수 기본값

# 5월 7일 과제 강사님이 코딩 - 가위바위보 게임(한 판)
# 입력 : 컴퓨터가 선택한 것 , 사람이 선택한 것 , 승부 여부
"""
import random

class GameData :
    # 변수 선언은 생성자에서 수행 >> 객체가 생성될때마다 새로운 메모리를 생성
    def __init__(self) :
        self.computer = 0
        self.person   = 0
        self.winner   = 0
    
    def gameStart(self) :
        self.computer = random.randint(1,3)
        self.person   = int(input("가위[1] | 바위[2] | 보[3] : "))
        self.winner   = self.isWinner()
    
    def isWinner(self) :
        if self.computer == self.person :
            return 3
        if (self.computer == 1 and self.person == 3) or \
           (self.computer == 2 and self.person == 1) or \
           (self.computer == 3 and self.person == 2) :
            return 1
        return 2
    
    def printLog(self) :
        print(f"컴퓨터 : {self.computer} | 사람 : {self.person} | 승부 : {self.winner}")

class Game :
    titles1 = ["" , "가위" , "바위" , "보"]
    titles2 = ["" , "컴퓨터 승" , "사람 승" , "무승부"]
    
    def __init__(self) :
        self.game_list = []
        
    def print(self,p1) :
        print(f"컴퓨터 : {self.titles1[p1.computer]}" , end = "\t")
        print(f"사람 : {self.titles1[p1.person]}" , end = "\t")
        print(f"승/패 : {self.titles2[p1.winner]}")
    
    def start(self) :
        while True :
            self.p1 = GameData()
            self.p1.gameStart()
            self.print(self.p1)
            self.game_list.append(self.p1)
            self.again = input("[1] 계속 | [0] 종료 : ")
            if self.again != "1" :
                return
    
    def printResult(self) :
        print(f"{len(self.game_list)} 번 수행함")
        for self.p1 in self.game_list :
            self.print(self.p1)
    
    def mainStart(self) :
        self.start()
        self.printResult()

if __name__ == "__main__" :
    game = Game()
    game.mainStart()
"""

# 강의 중 과제
# 항상 만들 때 한 사람 분의 데이터 파일(class) 를 생성 / 한 사람 정보 = 데이터베이스 레코드 하나
# 파이썬의 경우 파일명과 클래스명은 관계가 없음
# 성적처리 프로그램
# 이름 , 국어 , 수학 , 영어 성적 받음
# 총 점 , 평균 , 학점(A,B,C,D,F)

import pickle

class Student :
    def __init__(self) :
        self.name       = ""
        self.kor        = 0
        self.math       = 0
        self.english    = 0
        self.sum_score  = 0
        self.aver_score = 0
        self.grade      = ""
    
    def getSum(self) :
        self.sum_score = self.kor + self.math + self.english
    
    def getAverage(self) :
        self.aver_score = self.sum_score // 3
    
    def getGrade(self) :
        if self.aver_score >= 95 :
            self.grade = "A+"
        elif self.aver_score >= 90 :
            self.grade = "A"
        elif self.aver_score >= 85 :
            self.grade = "B+"
        elif self.aver_score >= 80 :
            self.grade = "B"
        elif self.aver_score >= 75 :
            self.grade = "C+"
        elif self.aver_score >= 70 :
            self.grade = "C"
        elif self.aver_score >= 65 :
            self.grade = "D+"
        elif self.aver_score >= 60 :
            self.grade = "D"
        else :
            self.grade = "F"
    
    def totalGetGrade(self) :
        self.getSum()
        self.getAverage()
        self.getGrade()
    
    def outPut(self) :
        print(f"이 름 : {self.name}\t"     , end = "\t")
        print(f"국 어 : {self.kor}"        , end = "\t")
        print(f"수 학 : {self.math}"       , end = "\t")
        print(f"영 어 : {self.english}"    , end = "\t")
        print(f"총 점 : {self.sum_score}"  , end = "\t")
        print(f"평 균 : {self.aver_score}" , end = "\t")
        print(f"등 급 : {self.grade}")
    
    def appendStudent(self) :
        self.name    =     input("학생 이름 : ")
        self.kor     = int(input("국어 성적 : "))
        self.math    = int(input("수학 성적 : "))
        self.english = int(input("영어 성적 : "))
    
class StudentManager :
    def __init__(self) :
        self.student_list = []

    # 학생 데이터 출력(전체)
    def printList(self) :
        for stu in self.student_list :
            stu.outPut()
    
    # 학생 데이터 삭제
    def delStudent(self) :
        name = input("삭제할 이름 입력 : ")
        lst  = list(filter(lambda x : name in x.name , self.student_list))
        
        if len(lst) <= 0 :
            print("찾는 데이터가 없습니다.")
            return
        
        for i , w in enumerate(lst) :
            print(f"순번 : {i}" , end = "\t")
            w.outPut()
        sel = int(input("삭제할 번호(순번) 입력 : "))
        self.student_list.remove(lst[sel])
    
    # 학생 데이터 검색(개별)
    def searchStudent(self) :
        name = input("검색할 이름 입력 : ")
        lst  = list(filter(lambda x : name in x.name , self.student_list))
        
        if len(lst) <= 0 :
            print("찾는 데이터가 없습니다.")
            return
        for w in lst :
            w.outPut()
            
    # 학생 데이터 수정
    def modifyStudent(self) :
        name = input("수정할 이름 입력 : ")
        lst = list(filter(lambda x : name in x.name , self.student_list))
        if len(lst) <= 0 :
            print("찾는 데이터가 없습니다.")
            return
        for i , w in enumerate(lst) :
            print(f"순번 : {i}" , end = "\t")
            w.outPut()
        sel = int(input("수정할 번호(순번) 입력 : "))
        modify = self.student_list[sel]
        modify.name    =     input("학생 이름 : ")
        modify.kor     = int(input("국어 성적 : "))
        modify.math    = int(input("수학 성적 : "))
        modify.english = int(input("영어 성적 : "))
        modify.totalGetGrade()
        
    # 학생 데이터 정렬(성적 내림차순)
    def arrStudent(self) :
        if len(self.student_list) <= 0 :
            print("입력된 데이터가 없습니다.")
            return
        self.student_list = sorted(self.student_list , key = lambda x : x.sum_score , reverse = True)
    
    # 학생 데이터 추가
    def addStudentData(self) :
        s = Student()
        s.appendStudent()
        s.totalGetGrade()
        self.student_list.append(s)
    
    # 학생 데이터 저장
    def serialStudentData(self) :
        data = self.student_list
        with open("student_list.bin" , "wb") as file :
            pickle.dump(data , file)
        print("학생 데이터 저장 완료")
        print("저장 파일명 : student_list.bin")
    
    # 학생 데이터 읽기
    def reserialStudentData(self) :
        with open("student_list.bin" , "rb") as file :
            self.student_list = pickle.load(file)
        print("학생 데이터 읽기 완료")
    
    def menu(self) :
        print("=====   메뉴   =====")
        print("[1] 학생 데이터 추가")   # 완료  addStudentData
        print("[2] 학생 데이터 출력")   # 완료  printList
        print("[3] 학생 데이터 검색")   # 완료  searchStudent
        print("[4] 학생 데이터 수정")   # 완료  modifyStudent
        print("[5] 학생 데이터 삭제")   # 완료  delStudent
        print("[6] 총점 순으로 정렬")   # 완료  arrStudent
        print("[7] 학생 데이터 저장")   # 완료  serialStudentData
        print("[8] 학생 데이터 읽기")   # 완료  reserialStudentData
        print("[0] 프로그램 종료")
        print("=====   메뉴   =====")
    
    def getStudent(self) :
        function_list = [None , self.addStudentData , self.printList , self.searchStudent , self.modifyStudent , self.delStudent , self.arrStudent , self.serialStudentData , self.reserialStudentData]
        
        while True :
            self.menu()
            sel = int(input("메뉴 선택 : "))
            if sel > 0 and sel < len(function_list) :
                function_list[sel]()
            elif sel == 0 :
                return
            else :
                print("메뉴 선택을 잘못하셨습니다.")

if __name__ == "__main__" :
    s = StudentManager()
    s.getStudent()