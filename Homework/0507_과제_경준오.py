# 가위 : 1 , 바위 : 2 , 보 : 3

import random

class Game_main :

    def __init__(self) :
        self.win  = 0
        self.lose = 0
        self.draw = 0
        self.getStart()

    def inSert(self) :
        self.check   = False
        while self.check == False :
            self.selUser = input("가위[1] , 바위[2] , 보[3] : ")
            self.check = self.numberChk(self.selUser)
        if self.selUser     == "1" :
            self.selUserKor = "가위"
        elif self.selUser   == "2" :
            self.selUserKor = "바위"
        else :
            self.selUserKor = "보"
        return self.selUser

    def numberChk(self,number) :
        if len(number) != 1 :
            print("다시 입력해주세요.")
            return False
        elif ord(number) > ord("3") or ord(number) < ord("1") :
            print("다시 입력해주세요.")
            return False
        return True

    def getNumber(self) :
        self.Number = str(random.randint(1,3))
        if self.Number     == "1" :
            self.NumberKor = "가위"
        elif self.Number   == "2" :
            self.NumberKor = "바위"
        else :
            self.NumberKor = "보"
        return self.Number

    def getScore(self) :
        if (self.selUser == "1" and self.Number == "3") or (self.selUser == "3" and self.Number == "2") or (self.selUser == "2" and self.Number == "1") :
            self.win += 1
        elif (self.selUser == self.Number) :
            self.draw += 1
        else :
            self.lose += 1

    def outPut(self) :
        print("유저 선택 : " , self.selUserKor , "\t컴퓨터 선택 : " , self.NumberKor , "\t\t승리 회수 : " , self.win , "\t패배 회수 : " , self.lose , "\t무승부 : " , self.draw)

    def getStart(self) :
        self.menu_list = {"1" : self.inSert}
        while True :
            self.getMenu()
            self.select = input("메뉴를 선택해주세요 : ")
            if self.select in self.menu_list.keys() :
                self.menu_list[self.select]()
                self.getNumber()
                self.getScore()
                self.outPut()
            else :
                return

    def getMenu(self) :
            print("[1] 게임시작")
            print("[0] 프로그램 종료")

if __name__ == "__main__" :
    p1 = Game_main()