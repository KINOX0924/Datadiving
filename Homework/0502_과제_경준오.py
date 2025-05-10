# 좀 더 깔끔하게 코딩하고 싶어요 ㅠㅠ
# 외부 모듈 호출 -----
import random

# 전역 변수/리스트/딕셔너리 -----
setting_number = 3                  # 컴퓨터가 생성할 숫자 설정
game_count = 0

computer_number = []
user_number = []

score_now = {"OUT" : 0 , "STRIKE" : 0 , "BALL" : 0}
score_game = {"HOMERUN" : 0 , "LOSE" : 0 , "PERCENTAGE" : 0.00}

statistics_now = []
statistics_all = []

# 컴퓨터 -----
# 컴퓨터 - 입력값 생성
def getNumberComputer() :
    global computer_number , setting_number

    computer_number.clear()

    for i in range(0,setting_number) :
        computer_number.append(str(random.randint(0,9)))
    chkNumberComputer()

# 컴퓨터 - 생성된 입력값이 중복되지 않는 지 확인
def chkNumberComputer() :
    global computer_number , setting_number

    computer_number = list(set(computer_number))
    while len(computer_number) < setting_number :
        computer_number.append(str(random.randint(0,9)))
        computer_number = list(set(computer_number))

# 유저 -----
# 유저 - 숫자 세 개를 입력
def getNumber() :
    global user_number , setting_number
    chkList = [False , False]

    while chkList[0] == False or chkList[1] == False :
        user_number.clear()
        for i in range(0,setting_number) :
            user_number.append(input(f"{i+1} 번째 숫자를 입력하세요 : "))
        chkList[0] = chkNumberUserOne(user_number)
        chkList[1] = chkNumberUserTwo(user_number)

# 유저 - 유저가 입력한 것이 한 자리만 입력한 것인지 확인
def chkNumberUserOne(list_1) :
    global setting_number

    for i in range(0,setting_number) :
        if len(list_1[i]) > 1 or len(list_1[i]) <= 0 :
            print("오입력되었습니다. 다시 입력해주세요.")
            return False
        if ord(list_1[i]) > ord("9") or ord(list_1[i]) < ord("0") :
            print("0 과 9 사이의 숫자만 입력해주세요.")
            return False
    return True

# 유저 - 유저가 입력한 세 개의 숫자에 중복된 숫자가 있는 지 확인
def chkNumberUserTwo(list_1) :
    global setting_number

    list_1 = list(set(list_1))
    if len(list_1) < setting_number :
        print("중복된 숫자가 존재합니다. 다시 입력해주세요.")
        return False
    return True

# 판정 -----
# 아웃 확인
def outScoreCount() :
    global score_now , setting_number , computer_number , user_number

    score_now = {"OUT" : setting_number ** 2 , "STRIKE" : 0 , "BALL" : 0}
    strikeCount = 0

    for i in range(0,setting_number) :
        for j in range(0,setting_number) :
            if user_number[i] == computer_number[j] :
                strikeCount += 1
                score_now["OUT"] -= 1
    if score_now["OUT"] % setting_number == 0 and strikeCount < setting_number :
        score_now["OUT"] = score_now["OUT"] // setting_number
    elif score_now["OUT"] == setting_number * 2 and strikeCount == setting_number :
        score_now["OUT"] = 0
    else :
        score_now["OUT"] = score_now["OUT"] % setting_number

# 스트라이크 및 볼 확인
def strikeNballScoreCount() :
    global score_now , setting_number , computer_number , user_number

    for i in range(0,setting_number) :
        if user_number[i] == computer_number[i] :
            score_now["STRIKE"] += 1

    while (score_now["OUT"] + score_now["STRIKE"] + score_now["BALL"]) < 3 :
        score_now["BALL"] += 1

# 출력 -----
def scorePrint(number_1,number_2) :
    global score_now , setting_number , computer_number , user_number

    print("아웃 : " , score_now["OUT"] , end = "\t")
    print("스트라이크 : " , score_now["STRIKE"] , end = "\t\t")
    print("볼 : " , score_now["BALL"])
    print(f"남은 기회 : {number_2 - number_1}")

# 통계 -----
# 게임 회차 / 컴퓨터가 생성한 숫자 / 유저가 입력했던 숫자
def getNowStatistics(number_1,number_2) :
    global computer_number , statistics_all , statistics_now , user_number

    if number_1 == 0 :
        statistics_now.clear()
        str_1 = "".join(computer_number)
        statistics_now.append(number_2)
        statistics_now.append(str_1)
        return
    str_1 = "".join(user_number)
    statistics_now.append(str_1)

# 승리 횟수 / 패배 횟수 / 승률 계산
def getEndStatistics() :
    global score_game
    score_game["PERCENTAGE"] = int((score_game["HOMERUN"] / (score_game["HOMERUN"] + score_game["LOSE"])) * 100)

# 통계값 출력 1 - 승/패/승률 출력
def printStatistics() :
    global score_game
    print("승리한 횟수 : " , score_game["HOMERUN"]    , "회" , end = "\t")
    print("패배한 횟수 : " , score_game["LOSE"]       , "회" , end = "\t")
    print("전체 승률 : "   , score_game["PERCENTAGE"] , "%")
    printStatisticsTwo()

# 통계값 출력 2 - 회차/컴퓨터 입력값/회차별 입력값/결과 출력
def printStatisticsTwo() :
    global statistics_all

    for i in range(0,len(statistics_all)) :
        count = 1
        for j in range(0,len(statistics_all[i])) :
            if j == 0 :
                print(f"게임 회차 : {statistics_all[i][j]}" , end = "\t")
            elif j == 1 :
                print(f"컴퓨터가 입력한 숫자 : {statistics_all[i][j]}" , end = "\t")
            elif j == len(statistics_all[i]) - 1 :
                print(f"게임 결과 : {statistics_all[i][j]}")
            else :
                print(f"{count} 회차 입력값 : {statistics_all[i][j]}" , end = "\t")
                count += 1

# 승/패 판정
def winNlose(number_1,number_2) :
    global setting_number , score_game , score_now , computer_number , statistics_now , statistics_all
    str_1 = "".join(computer_number)

    if score_now["STRIKE"] == setting_number :
        print("홈런!!")
        score_game["HOMERUN"] += 1
        statistics_now.append("홈런")
        statistics_all.append(list(statistics_now))
        return True
    elif number_1 == number_2 :
        print("패배")
        print(f"컴퓨터가 생성한 숫자 : {str_1}")
        score_game["LOSE"] += 1
        statistics_now.append("패배")
        statistics_all.append(list(statistics_now))
        return True
    return False

# 시작
def gameStart() :
    global game_count
    game_count += 1
    limitCount = 0
    userLife = 6

    getNumberComputer()
    getNowStatistics(limitCount,game_count)

    while True :
        limitCount += 1
        getNumber()
        getNowStatistics(limitCount,game_count)
        outScoreCount()
        strikeNballScoreCount()
        scorePrint(limitCount,userLife)
        print(computer_number , "테스트용 - 컴퓨터 숫자 보여주기")          # 테스트용
        if winNlose(limitCount,userLife) == True :
            getEndStatistics()
            return

# 메인 메뉴
def menu() :
    while True :
        print("[1] 게임 시작")
        print("[2] 전체 통계")
        print("[0] 프로그램 종료")
        sel = input("메뉴 선택 : ")

        if sel == "1" :
            gameStart()
        elif sel == "2" :
            printStatistics()
        elif sel == "0" :
            return
        else :
            print("메뉴를 다시 선택해주세요.")

menu()