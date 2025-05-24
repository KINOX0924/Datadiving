import random

class Baseball :
    def __init__(self) :
        self.computer      = [-1,-1,-1]  # -1 = null
        self.player        = [-1,-1,-1]
        self.count         = 0           # 게임 회차
        self.player_recode = []
    
    def init_computer(self) :
        chk_number = 0
        while chk_number <= 2 :
            number = random.randint(0,9)
            if number not in self.computer :
                self.computer[chk_number] = number
                chk_number += 1
    
    def init_person(self) :
        number = input("숫자 세 개를 입력하세요(예 : 0 1 2) : ")
        number_list = number.strip().split(" ")
        self.player[0] = int(number_list[0])
        self.player[1] = int(number_list[1])
        self.player[2] = int(number_list[2])
    
    def getResult(self) :
        strike = 0
        ball   = 0
        out    = 0
        
        for i in range(0,3) :
            if self.player[i] in self.computer :
                if self.player[i] == self.computer[i] :
                    strike += 1
                else :
                    ball += 1
            else :
                out += 1
        return strike , ball , out
    
    def start(self) :
        flag = False    # 아직 3 스트라이크가 아님을 나타내기 위한 변수
        self.init_computer()
        while flag == False and self.count <= 5 :
            self.init_person()
            strike , ball , out = self.getResult()
            print(self.computer)            # 완성 후 삭제
            print(f"스트라이크 : {strike} | 볼 : {ball} | 아웃 : {out}")
            self.player_recode.append({"person" : [x for x in self.player] , "strike" : strike , "ball" : ball , "out" : out , "count" : self.count})
            if strike == 3 :
                flag = True
            self.count += 1

if __name__ == "__main__" :
    p = Baseball()
    p.start()