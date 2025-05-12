# 아직 클래스 메서드 , 프라이빗 변수를 배우기 전에 짠거라.. 그냥 처음 작성했던대로 계속 진행 작성
# 나중에 클래스 메서드 , 프라이빗 변수를 사용해서 다시 작성해볼 것
# 현재 회원 메뉴에서 게시글 조회까지 완료할 것
# 금요일 자정까지 완료할 것

# 관리자 메뉴
# 회원 등록 , 회원 검색 , 회원 삭제 , 회원 수정 , 회원 데이터 저장 , 회원 데이터 로드 , 게시물 데이터 저장 , 게시물 데이터 로드 , 관리자 비밀번호 변경

# 일반 메뉴
# 회원 로그인 , 회원 가입 , 회원 정보 수정 , 회원 탈퇴(삭제) , 전체 게시물 조회

# 회원 가입(등록) , 회원 정보 수정 , 회원 탈퇴는 관리자 메뉴와 일반 메뉴에서 같이 사용
# 회원 정보 수정 및 회원 탈퇴는 패스워드를 입력해야함

# 로그인 후 메뉴
# 게시물 등록 , 게시물 조회 , 게시물 수정 , 게시물 삭제

import random
import pickle
import datetime
# 랜덤 회원번호 생성을 위한 랜덤 모듈
# 회원 데이터 , 게시물 데이터를 저장/로드를 위한 피클 모듈
# 게시글 작성 시 연-월-일 시:분 저장을 위한 데이트 타임 모듈

# 메인 허브 클래스로 회원 데이터와 게시물 데이터가 저장되는 클래스
# 이용자로 접속할 지 , 관리자로 접속할지는 메인 허브 클래스를 통해서 시작
class Mainhub :
    member_list   = [
        {"MEMBER_NUMBER" : "73921" , "ID" : "KIMM" , "PASSWORD" : "a1b2C3d" , "NAME" : "김민지" , "PHONE" : "010-1234-5678" , "EMAIL" : "minji1234@gmail.com"},
        {"MEMBER_NUMBER" : "10582" , "ID" : "LEEE" , "PASSWORD" : "Q9w8E7r" , "NAME" : "이서윤" , "PHONE" : "010-9876-5432" , "EMAIL" : "seoyun5678@gmail.com"},
        {"MEMBER_NUMBER" : "45603" , "ID" : "PARK" , "PASSWORD" : "zXcVbN4" , "NAME" : "박지우" , "PHONE" : "010-1122-3344" , "EMAIL" : "jiwoo9999@gmail.com"},
        {"MEMBER_NUMBER" : "91276" , "ID" : "CHOI" , "PASSWORD" : "mLoKiJ6" , "NAME" : "최수아" , "PHONE" : "010-5555-7777" , "EMAIL" : "sua0000@gmail.com"},
        {"MEMBER_NUMBER" : "28349" , "ID" : "JUNG" , "PASSWORD" : "p1o2I3u" , "NAME" : "정하준" , "PHONE" : "010-4321-8765" , "EMAIL" : "hajun0101@gmail.com"}
    ]
    post_list     = [
        {"MEMBER_NUMBER" : "10582" , "ID" : "LEEE" , "BOARD_NUMBER" : 1 , "TITLE" : "이거 만들다가" , "DETAIL" : "오늘 하루가 지나갔네" , "DATE" : "2024-07-29 03 : 55" , "VIEWS" : 632},
        {"MEMBER_NUMBER" : "73921" , "ID" : "KIMM" , "BOARD_NUMBER" : 2 , "TITLE" : "저 사람 이름들" , "DETAIL" : "제미니가 만들 사람들" , "DATE" : "2025-01-15 17 : 31" , "VIEWS" : 123},
        {"MEMBER_NUMBER" : "45603" , "ID" : "PARK" , "BOARD_NUMBER" : 3 , "TITLE" : "하준이가 누굴까" , "DETAIL" : "궁금하네" , "DATE" : "2024-11-03 11 : 01" , "VIEWS" : 987},
        {"MEMBER_NUMBER" : "10582" , "ID" : "LEEE" , "BOARD_NUMBER" : 4 , "TITLE" : "빈 속에 커피 마시면" , "DETAIL" : "하루 종일 속이 쓰리다" , "DATE" : "2025-04-05 08 : 22" , "VIEWS" : 55},
        {"MEMBER_NUMBER" : "91276" , "ID" : "CHOI" , "BOARD_NUMBER" : 5 , "TITLE" : "내가 산 주식은" , "DETAIL" : "언제나 항상 파란색" , "DATE" : "2024-08-21 19 : 49" , "VIEWS" : 301}
    ]
    
    admin_account = {"ADMIN_ID" : "admin" , "ADMIN_PASSWORD" : "admin"}
    # 관리자 계정 아이디와 비밀번호
    # 관리자 계정의 아이디와 비밀번호가 일치해야 관리자 메뉴로 접속 가능
    # 관리자 계정의 아이디는 변경할 수 없고 비밀번호만 관리자 메뉴에서 변경 가능
    
    board_number_count = 5
    # 게시물 데이터에 초기화 값이 없을 경우 카운트 0 으로 수정 필요
    
    # 처음 프로그램에 접속했을 때 출력되는 메뉴
    def printTerminalMenu(self) :
        print("===== 게시판 이용 프로그램 메뉴 =====")
        print("[1] | 이용자 접속")
        print("[2] | 관리자 접속")
        print()
        print("[0] | 프로그램 종료")
    
    # 첫 메뉴 선택을 하는 함수
    def terminalStart(self) :
        terminal_menu_list = [None , self.memberStart , self.adminStart]
        
        while True :
            self.printTerminalMenu()
            select_menu = int(input("메뉴 선택 : "))
            if select_menu > 0 and select_menu <= len(terminal_menu_list) :
                terminal_menu_list[select_menu]()
            elif select_menu == 0 :
                return
            else :
                print("메뉴를 잘못 선택하였습니다.")
    
    # 메뉴에서 이용자 접속을 선택한 경우 멤버 클래스를 시작하여 회원 접속
    def memberStart(self) :
        terminal = Member()
        terminal.startMember()
    
    # 메뉴에서 관리자 접속을 선택한 경우 어드민 클래스를 시작함
    # 단 , 계정과 비밀번호를 입력받아서 일치했을 때만 접속 가능
    def adminStart(self) :
        admin_login_id       = input("관리자 접속 계정을 입력하세요 : ")
        admin_login_password = input("관리자 접속 비밀번호를 입력하세요 : ")
        
        if self.admin_account["ADMIN_ID"] == admin_login_id and self.admin_account["ADMIN_PASSWORD"] == admin_login_password :
            terminal = Admin()
            terminal.startAdmin()
        else :
            print("관리자 아이디 또는 비밀번호가 잘못 입력되었습니다.")

# 회원과 비회원이 접속하는 클래스
class Member :
    # 처음 사용자 클래스에 접속하면 출력되는 메뉴
    def printMemberTerminalMenu(self) :
        print("===== 사용자 접속 완료 =====")
        print("[1] | 회원 로그인")
        print("[2] | 회원 가입")
        print("[3] | 정보 수정")
        print("[4] | 회원 탈퇴")
        print("[5] | 게시물 조회")
        print()
        print("[0] | 사용자 접속 종료")
    
    # 회원 가입을 선택 시 어드민 계정의 회원 가입 함수를 호출하여 회원 가입 진행
    def joinMember(self) :
        new = Admin()
        new.upSign()
    
    # 정보 수정을 선택 시 어드민 계정의 회원 정보 수정 함수를 호출하여 회원 정보 수정 진행
    # 비밀번호가 없으면 수정 불가능
    def modifyMember(self) :
        modify = Admin()
        modify.modifyMember()
    
    # 회원 탈퇴 선택 시 어드민 계정의 회원 삭제 함수를 호출하여 회원 정보 삭제 진행
    # 비밀번호가 없으면 수정 불가능
    def delMember(self) :
        delete = Admin()
        delete.delMember()
    
    # 게시물 조회를 선택 할 시 현재 등록되어 있는 모든 게시물에 대한 목록을 나열 수 번호를 선택하면 게시글을 볼 수 있음
    def viewPosts(self) :
        post_number_list = []
        
        for i , v in enumerate(Mainhub.post_list) :
            print(f"게시글 번호 [{v["BOARD_NUMBER"]}] | 제목 : [{v["TITLE"]}]")
            post_number_list.append(v["BOARD_NUMBER"])
        # 메인 허브의 게시물 리스트에서 게시글 번호과 제목만 출력하고 , 게시글 번호를 리스트에 저장
        
        select_post = int(input("조회할 게시글 번호 입력 : "))
        if select_post not in post_number_list :
            print("조회할 수 없는 게시글 번호입니다.")
        else :
            for i , v in enumerate(Mainhub.post_list) :
                if select_post == v["BOARD_NUMBER"] :
                    v["VIEWS"] += 1
                    self.printPost(v)
        # 저장한 리스트와 선택한 리스트 번호를 비교하여 선택된 번호가 리스트에 없다면 조회 불가
        # 있다면 해당 게시글 번호를 이용하여 게시글 상세 조회 및 조회수 1 증가
    
    # 로그인이 성공하고 나면 보여줄 메뉴 항목 함수
    def printMemberMenu(self) :
        print("==== 회원 메뉴 =====")
        print("[1] | 게시물 등록")
        print("[2] | 게시물 조회")
        print("[3] | 게시물 수정")
        print("[4] | 게시물 삭제")
        print()
        print("[0] | 로그아웃")
    
    # 비회원 메뉴에서 선택할 수 있는 로그인
    def loginMember(self) :
        login_member_id       = input("아이디 입력 : ")
        login_member_password = input("비밀번호 입력 : ")
        
        for i , v in enumerate(Mainhub.member_list) :
            if login_member_id == v["ID"] and login_member_password == v["PASSWORD"] :
                print(f"{v["ID"]} 로그인 성공")
                member_information = v
                self.startBoardMenu(member_information)
                return
        print("계정 아이디 또는 비밀번호가 일치하지 않습니다.")
        # 로그인할 아이디와 비밀번호를 입력받음
        # 입력받은 아이디와 비밀번호를 메인 허브의 멤버 리스트에서 비교하여 둘 다 일치하는 정보다 있으면 로그인 성공
        # 실패하면 오류 문구 발생
    
    # 비회원 메뉴를 실행시킬 함수
    def startMember(self) :
        member_menu_list = [None , self.loginMember , self.joinMember , self.modifyMember , self.delMember , self.viewPosts]
        
        while True :
            self.printMemberTerminalMenu()
            select_menu = int(input("메뉴 선택 : "))
            
            if select_menu > 0 and select_menu <= len(member_menu_list) :
                member_menu_list[select_menu]()
            elif select_menu == 0 :
                return
            else :
                print("메뉴를 잘못 선택하였습니다.")
    
    # 로그인 후 회원 메뉴를 실행시킬 함수
    def startBoardMenu(self , member_information) :
        board_menu_list = [None , self.postingBoard , self.viewPost , self.modifyPost , self.delPost]
        
        while True :
            self.printMemberMenu()
            select_menu = int(input("메뉴 선택 : "))
            
            if select_menu > 0 and select_menu <= len(board_menu_list) :
                board_menu_list[select_menu](member_information)
            elif select_menu == 0 :
                return
            else :
                print("메뉴를 잘못 선택하였습니다.")
    
    # 게시물을 등록할 수 있는 함수
    def postingBoard(self , member_information) :
        Mainhub.board_number_count += 1
        new_post = {"MEMBER_NUMBER" : member_information["MEMBER_NUMBER"] , "ID" : member_information["ID"] , "BOARD_NUMBER" : Mainhub.board_number_count , "TITLE" : "" , "DETAIL" : "" , "DATE" : self.getNowDate() , "VIEWS" : 0}
        new_post["TITLE"]         = input("제목 입력 : ")
        new_post["DETAIL"]        = input("내용 입력 : ")
        
        Mainhub.post_list.append(new_post)
        print("게시물이 정상적으로 등록되었습니다.")
        # 메인 허브에 있는 게시물 번호에 카운트 + 1
        # 새로운 게시물 딕셔너리를 생성 및 초기화
        # 생성된 딕셔너리의 타이틀(제목) 과 내용(디테일) 을 입력
        # 입력 후 메인 허브의 게시물 리스트에 게시물 추가 후 안내 멘트 출력
    
    # 현재 연/월/일/시/분 을 생성하는 함수
    # 생성한 값은 게시물 등록 시 초기화 값에 들어감
    def getNowDate(self) :
        now        = datetime.datetime.now()
        format_now = now.strftime("%Y-%m-%d %H : %M")
        return format_now
    
    # 자신이 작성한 게시물만 조회할 수 있는 메뉴
    def viewPost(self , member_information) :
        post_number_list = []
        
        for i , v in enumerate(Mainhub.post_list) :
            if member_information["MEMBER_NUMBER"] == v["MEMBER_NUMBER"] and member_information["ID"] == v["ID"] :
                print(f"게시글 번호 [{v["BOARD_NUMBER"]}] | 제목 : [{v["TITLE"]}]")
                post_number_list.append(v["BOARD_NUMBER"])
        
        select_post = int(input("조회할 게시글 번호 입력 : "))
        if select_post not in post_number_list :
            print("조회할 수 없는 게시글 번호입니다.")
        else :
            for i , v in enumerate(Mainhub.post_list) :
                if select_post == v["BOARD_NUMBER"] :
                    self.printPost(v)
    # 앞서 만든 비회원 게시물 조회에서 회원 번호 , 아이디만 확인하여 자신이 만든 게시물만 조회할 수 있음
    
    # 자신이 작성한 게시물을 수정하는 함수
    def modifyPost(self , member_information) :
        post_number_list = []
        
        for i , v in enumerate(Mainhub.post_list) :
            if member_information["MEMBER_NUMBER"] == v["MEMBER_NUMBER"] and member_information["ID"] == v["ID"] :
                print(f"게시글 번호 [{v["BOARD_NUMBER"]}] | 제목 : [{v["TITLE"]}]")
                post_number_list.append(v["BOARD_NUMBER"])
        
        select_post = int(input("수정할 게시글 번호 입력 : "))
        if select_post not in post_number_list :
            print("조회할 수 없는 게시글 번호입니다.")
        else :
            for i , v in enumerate(Mainhub.post_list) :
                if select_post == v["BOARD_NUMBER"] :
                    v["TITLE"]  = input("수정할 제목 입력 : ")
                    v["DETAIL"] = input("수정할 내용 입력 : ")
                    v["DATE"]   = self.getNowDate()
                    print("게시물이 정상적으로 수정되었습니다.")
    # 앞서 만든 게시물 조회 함수를 응용하여 검색된 게시물에서 제목과 내용만 수정할 수 있는 함수
    # 게시물의 번호와 아이디 , 회원 번호 등은 변경되지 않으며 제목 , 내용 , 날짜(수정한 날짜) 만 변경됨
    
    # 자신이 작성한 게시물을 삭제하는 함수
    def delPost(self , member_information) :
        post_number_list = []
        
        for i , v in enumerate(Mainhub.post_list) :
            if member_information["MEMBER_NUMBER"] == v["MEMBER_NUMBER"] and member_information["ID"] == v["ID"] :
                print(f"게시글 번호 [{v["BOARD_NUMBER"]}] | 제목 : [{v["TITLE"]}]")
                post_number_list.append(v["BOARD_NUMBER"])
        
        select_post = int(input("수정할 게시글 번호 입력 : "))
        if select_post not in post_number_list :
            print("조회할 수 없는 게시글 번호입니다.")
        else :
            for i , v in enumerate(Mainhub.post_list) :
                if select_post == v["BOARD_NUMBER"] :
                    print("게시물이 정상적으로 삭제되었습니다.")
                    Mainhub.post_list.remove(v)
    # 앞서 만든 게시물 조회 함수를 응용하여 찾아낸 게시물 중 자신이 만든 게시물의 번호를 사용하여 삭제

    # 게시글 내용을 출력하는 함수
    def printPost(self , post) :
        print(f"제목 : [{post["TITLE"]}]")
        print(f"내용\n{post["DETAIL"]}")
        print(f"게시글 번호 : [{post["BOARD_NUMBER"]}] | 작성자 : {post["ID"]}\t | 게시일 : {post["DATE"]}\t | 조회수 : {post["VIEWS"]}")

# 관리자가 접속하여 사용할 수 있는 클래스
class Admin :
    # 회원 가입을 위한 함수
    # 회원 가입의 경우 멤버 클래스에서도 동일하게 사용할 수 있어야 함
    def upSign(self) :
        member = {"MEMBER_NUMBER" : self.creNumber() , "ID" : "" , "PASSWORD" : "" , "NAME" : "" , "PHONE" : "" , "EMAIL" : ""}
        
        member["ID"]            = input("생성할 아이디 입력 : ")
        member["PASSWORD"]      = input("사용할 패스워드 입력 : ")
        member["NAME"]          = input("계정 이름 입력 : ")
        member["PHONE"]         = input("연락처 입력(예시 : 010-0000-0000) : ")
        member["EMAIL"]         = input("이메일 입력 : ")
        Mainhub.member_list.append(member)
        print(f"{member["NAME"]} 님의 {member["ID"]} 계정이 정상적으로 생성되었습니다.")
    
    # 회원 가입 시 회원 번호를 랜덤으로 생성하기 위한 함수
    # 여섯자리 숫자가 랜덤으로 생성되며 회원 가입 시 초기화 값에 자동으로 입력됨
    def creNumber(self) :
        create_number = []
        for r in range(0,6) :
            create_number.append(str(random.randint(0,9)))
        create_number = "".join(create_number)
        
        return create_number
    
    # 회원 정보를 삭제할 수 있는 함수
    def delMember(self) :
        search_member_information = self.searchMember(False)
        del_member_password       = input(f"{search_member_information["ID"]} | 계정의 비밀번호를 입력 : ")
        
        for i , v in enumerate(Mainhub.member_list) :
            if v == search_member_information and v["PASSWORD"] == del_member_password :
                Mainhub.member_list.remove(v)
                print(f"{search_member_information["NAME"]} 님의 계정이 정상적으로 삭제되었습니다.")
                return
        print("비밀번호가 일치하지 않습니다.")
        # 일단 회원 정보를 검색한 뒤에 회원 정보에 맞는 비밀번호를 입력하면 삭제가 진행됨
        # 비밀번호가 일치하지 않으면 삭제가 이루어지지 않음
        
    # 회원 정보를 수정할 수 있는 함수
    def modifyMember(self) :
        search_member_information = self.searchMember(False)
        modify_member_password    = input(f"{search_member_information["ID"]} | 계정의 비밀번호를 입력 : ")
        
        for i , v in enumerate(Mainhub.member_list) :
            if v == search_member_information and v["PASSWORD"] == modify_member_password :
                v["NAME"]     = input("수정 이름 입력 : ")
                v["PASSWORD"] = input("수정 비밀번호 입력 : ")
                v["PHONE"]    = input("수정 연락처 입력 : ")
                v["EMAIL"]    = input("수정 이메일 입력 : ")
                print(f"{search_member_information["NAME"]} 님의 계정이 정상적으로 수정되었습니다.")
                return
        print("비밀번호가 일치하지 않습니다.")
        # 마찬가지로 먼저 회원 정보를 검색한 뒤에 맞는 비밀번호를 입력하면 수정 가능
        # 이름과 비밀번호 , 연락처 , 이메일만 수정 가능
    
    # 회원 정보를 조회할 수 있는 함수
    def searchMember(self , plsprint) :
        flag = False
        
        while flag == False :
            search_id = input("찾고자 하는 계정의 아이디를 입력하세요 : ")
            if len(search_id) > 0 :
                member_list_copy = next(filter(lambda x : search_id == x["ID"] , Mainhub.member_list) , None)
                if member_list_copy == None :
                    print("입력하신 아이디를 찾을 수 없습니다.")
                    flag = False
                else :
                    if plsprint == True :
                            self.printInformation(member_list_copy)
                            flag = True
                    flag = True
        return member_list_copy
        # 아이디를 사용해서 조회할 수 있으며 비밀번호를 출력되지 않음
    
    # 검색된 회원 정보를 출력하는 함수
    def printInformation(self , information) :
        print(f"회원번호 : {information["MEMBER_NUMBER"]} ||" , end = "\t")
        print(f"아이디 : {information["ID"]}" , end = "\t")
        print(f"이름 : {information["NAME"]}" , end = "\t")
        print(f"연락처 : {information["PHONE"]}" , end = "\t")
        print(f"이메일 : {information["EMAIL"]}")
    
    # 회원 데이터를 외부로 저장하는 함수
    def saveMemberData(self) :
        with open("member_list.bin" , "wb") as file :
            pickle.dump(Mainhub.member_list , file)
        print("회원 데이터를 성공적으로 저장하였습니다.")
        print("저장 파일명 : member_list.bin")
    
    # 회원 데이터를 외부에서 읽어오는 함수
    def loadMemberData(self) :
        with open("member_list.bin" , "rb") as file :
            Mainhub.member_list = pickle.load(file)
        print("회원 데이터를 성공적으로 로드하였습니다.")
    
    # 게시물 데이터를 외부로 저장하는 함수
    def savePostData(self) :
        with open("post_list.bin" , "wb") as file :
            pickle.dump(Mainhub.post_list , file)
        print("게시물 데이터를 성공적으로 저장하였습니다.")
        print("저장 파일명 : post_list.bin")
    
    # 게시물 데이터를 외부에서 읽어오는 함수
    def loadPostData(self) :
        with open("post_list.bin" , "rb") as file :
            Mainhub.post_list = pickle.load(file)
        print("게시물 데이터를 성공적으로 로드하였습니다.")
        
    # 관리자 계정의 비밀번호를 변경하는 함수
    def reAdminPwd(self) :
        while True :
            admin_password = input("관리자 비밀번호 확인 : ")
            if admin_password == Mainhub.admin_account["ADMIN_PASSWORD"] :
                Mainhub.admin_account["ADMIN_PASSWORD"] = input("변경할 관리자 비밀번호 입력 : ")
                print("성공적으로 관리자 비밀번호가 변경되었습니다.")
                return
            else :
                print("관리자 비밀번호가 다릅니다.")
                return
        # 관리자 비밀번호를 먼저 재확인 후 비밀번호가 일치하면 변경 가능
        
    # 관리자 클래스 메인 메뉴 출력 함수
    def printAdminMenu(self) :
        print("===== 관리자 접속 완료 =====")
        print("[1] | 회원 등록")
        print("[2] | 회원 검색")
        print("[3] | 회원 삭제")
        print("[4] | 회원 수정")
        print("[5] | 회원 데이터 저장")
        print("[6] | 회원 데이터 로드")
        print("[7] | 게시물 데이터 저장")
        print("[8] | 게시물 데이터 로드")
        print("[9] | 관리자 비밀번호 변경")
        print()
        print("[0] | 관리자 접속 종료")
        
    # 관리자 메인 메뉴 시작 함수
    def startAdmin(self) :
        admin_menu_list = [None , self.upSign , self.searchMember , self.delMember , self.modifyMember , self.saveMemberData , self.loadMemberData , self.savePostData , self.loadPostData , self.reAdminPwd]
        
        while True :
            self.printAdminMenu()
            select_menu = int(input("메뉴 선택 : "))
            
            if select_menu > 0 and select_menu <= len(admin_menu_list) :
                if select_menu == 2 :
                    admin_menu_list[select_menu](True)
                else :
                    admin_menu_list[select_menu]()
            elif select_menu == 0 :
                return
            else :
                print("메뉴를 잘못 선택하였습니다.")
        

if __name__ == "__main__" :
    user = Mainhub()
    user.terminalStart()