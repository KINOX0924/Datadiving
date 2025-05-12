# 회원관리 - 회원번호 , 회원아이디 , 패스워드 , 이름 , 전화번호 , 이메일    = 관리자
# 게시판   - 회원번호 , 글번호 , 제목 , 내용 , 작성일 , 조회수             = 이용자

# 회원가입 / 수정 / 탈퇴 , 자기 정보 조회(패스워드 입력하면)

# 게시판에 게시글 작성 - 회원 번호 , 제목 , 내용 , 작성일(Date 라는 라이브러리 - 챗 GPT) , 조회수 0 으로 시작
# 읽어보기
# 수정 (글쓴이 에게만) - 회원번호랑 패스워드 입력하면
# 삭제 (글쓴이 에게만) - 회원번호랑 패스워드 입력하면

# 랜덤 회원번호 생성을 위한 랜덤 모듈 호출
import random
import pickle   # 추후 추가 예정

class Mainhub :
    member_list   = [
        {"MEMBER_NUMBER" : "73921" , "ID" : "KIMM" , "PASSWORD" : "a1b2C3d" , "NAME" : "김민지" , "PHONE" : "010-1234-5678" , "EMAIL" : "minji1234@gmail.com"},
        {"MEMBER_NUMBER" : "10582" , "ID" : "LEEE" , "PASSWORD" : "Q9w8E7r" , "NAME" : "이서윤" , "PHONE" : "010-9876-5432" , "EMAIL" : "seoyun5678@gmail.com"},
        {"MEMBER_NUMBER" : "45603" , "ID" : "PARK" , "PASSWORD" : "zXcVbN4" , "NAME" : "박지우" , "PHONE" : "010-1122-3344" , "EMAIL" : "jiwoo9999@gmail.com"},
        {"MEMBER_NUMBER" : "91276" , "ID" : "CHOI" , "PASSWORD" : "mLoKiJ6" , "NAME" : "최수아" , "PHONE" : "010-5555-7777" , "EMAIL" : "sua0000@gmail.com"},
        {"MEMBER_NUMBER" : "28349" , "ID" : "JUNG" , "PASSWORD" : "p1o2I3u" , "NAME" : "정하준" , "PHONE" : "010-4321-8765" , "EMAIL" : "hajun0101@gmail.com"}
    ]
    post_list     = []
    admin_account = {"ADMIN_ID" : "admin" , "ADMIN_PASSWORD" : "admin"}
    
    def __init__(self) :
        self.member = {"MEMBER_NUMBER" : "" , "ID" : "" , "PASSWORD" : "" , "NAME" : "" , "PHONE" : "" , "EMAIL" : ""}
        
    def printTerminalMenu(self) :
        print("===== 게시판 이용 프로그램 메뉴 =====")
        print("[1] | 이용자 접속")  # 현재 이용 불가
        print("[2] | 관리자 접속")
        print()
        print("[0] | 프로그램 종료")
    
    def terminalStart(self) :
        terminal_menu_list = [None , self.memberStart , self.adminStart]
        self.printTerminalMenu()
        
        while True :
            select_menu = int(input("메뉴 선택 : "))
            if select_menu > 0 and select_menu <= len(terminal_menu_list) :
                terminal_menu_list[select_menu]()
            elif select_menu == 0 :
                return
            else :
                print("메뉴를 잘못 선택하였습니다.")
    
    def memberStart(self) :
        pass
    
    def adminStart(self) :
        admin_login_id       = input("관리자 접속 계정을 입력하세요 : ")
        admin_login_password = input("관리자 접속 비밀번호를 입력하세요 : ")
        
        if self.admin_account["ADMIN_ID"] == admin_login_id and self.admin_account["ADMIN_PASSWORD"] == admin_login_password :
            terminal = Admin()
        else :
            print("관리자 아이디 또는 비밀번호가 잘못 입력되었습니다.")

# 회원이 접속하여 사용할 수 있는 클래스
class Member :
    def __init__ (self) :
        pass
    
    pass

# 관리자가 접속하여 사용할 수 있는 클래스
class Admin :
    def __init__(self) :
        pass
    
    # 회원 가입을 위한 함수
    # 회원 가입의 경우 멤버 클래스에서도 동일하게 사용할 수 있어야 함
    def upSign(self) :
        member = Mainhub()
        member.member["MEMBER_NUMBER"] = self.creNumber()
        member.member["ID"]            = input("사용할 아이디 입력 : ")
        member.member["PASSWORD"]      = input("사용할 패스워드 입력 : ")
        member.member["NAME"]          = input("본인 이름 입력 : ")
        member.member["PHONE"]         = input("연락처 입력(예시 : 010-0000-0000) : ")
        member.member["EMAIL"]         = input("이메일 입력 : ")
        Mainhub.member_list.append(member)
        print(f"{member.member["NAME"]} 님의 {member.member["ID"]} 계정이 정상적으로 생성되었습니다.")
    
    # 회원 가입 시 회원 번호를 랜덤으로 생성하기 위한 함수
    # 회원 번호만 가지고는 삭제 및 수정을 할 수 없음
    def creNumber(self) :
        create_number = []
        for r in range(0,6) :
            create_number.append(str(random.randint(0,9)))
        create_number = "".join(create_number)
        
        return create_number
    
    # 회원 정보를 삭제할 수 있는 함수
    # 일단 회원 정보를 검색한 뒤에 회원 정보에 맞는 비밀번호를 입력하면 삭제가 진행됨
    # 비밀번호가 일치하지 않으면 삭제가 이루어지지 않음
    def delMember(self) :
        search_member_information = self.searchMember(False)
        del_member_password       = input(f"{search_member_information["ID"]} | 계정의 비밀번호를 입력 : ")
        
        for i , v in enumerate(Mainhub.member_list) :
            if v == search_member_information and v["PASSWORD"] == del_member_password :
                Mainhub.member_list.remove(v)
                print(f"{search_member_information["NAME"]} 님의 계정이 정상적으로 삭제되었습니다.")
                return
        print("비밀번호가 일치하지 않습니다.")
        
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
    
    # 검색된 회원 정보를 출력하는 함수
    def printInformation(self , information) :
        print(f"회원번호 : {information["MEMBER_NUMBER"]} ||" , end = "\t")
        print(f"아이디 : {information["ID"]}" , end = "\t")
        print(f"이름 : {information["NAME"]}" , end = "\t")
        print(f"연락처 : {information["PHONE"]}" , end = "\t")
        print(f"이메일 : {information["EMAIL"]}")
        
    # 관리자 클래스 메인 메뉴 출력 함수
    def printAdminMenu(self) :
        print("===== 관리자 접속 완료 =====")
        print("[1] | 회원 등록")
        print("[2] | 회원 검색")
        print("[3] | 회원 삭제")
        print("[4] | 회원 수정")
        print()
        print("[0] | 관리자 접속 종료")
        
    # 관리자 메인 메뉴 시작 함수
    def startAdmin(self) :
        admin_menu_list = [None , self.upSign , self.searchMember , self.delMember , self.modifyMember]
        
        

if __name__ == "__main__" :
    member = Admin()
    member.modifyMember()
    member.searchMember(True)