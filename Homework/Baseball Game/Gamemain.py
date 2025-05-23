from gamedata import Baseball

class GameMain :
    def __init__(self) :
        self.game_list = []

    def start(self) :
        while True :
            print("[1] 게임 시작")
            print("[2] 통계 출력")
            print("[0] 게임 종료")
            sel = input("메뉴 선택 : ")
            
            if   sel == "1" :
                self.game_start()
            elif sel == "2" :
                self.show_statisticis()
            else :
                return
    
    def game_start(self) :
        user = Baseball()
        user.start()
        self.game_list.append(user)
    
    def show_statisticis(self) :
        for lst in self.game_list :
            print(lst.computer)
            for lst_2 in lst.player_recode :
                print("플레이어 입력 : " , lst_2["person"] , "스트라이크 : " , lst_2["strike"] , "볼 : " , lst_2["ball"] , "아웃 : " , lst_2["out"] , "카운트 : " , lst_2["count"])

if __name__ == "__main__" :
    game = GameMain()
    game.start()