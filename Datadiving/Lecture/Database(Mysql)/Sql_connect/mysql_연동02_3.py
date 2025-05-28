import execute_module_re as mysql

class StudentManager :
    def p_menu(self) :
        print("[1] | 전체 학생 조회")
        print("[2] | 학생 개별 조회")
        print("[3] | 학생 정보 입력")
        print("[4] | 학생 정보 수정")
        print("[5] | 학생 정보 삭제")
        print("[0] | 프로그램 종료")

    def sel_menu(self) :
        menu_list = [None , self.showAllStudent , self.showOneStudent , self.regiStudent , self.modifyStudent , self.deleteStudent]
        
        while True :
            self.p_menu()
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu > 0 and select_menu < len(menu_list) :
                    menu_list[select_menu]()
                elif select_menu == 0 :
                    return
                else :
                    print("메뉴 안의 숫자만 입력하세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    def showAllStudent(self) :
        show_all_query = "select * from tb_score"
        recodes = mysql.executePrint(show_all_query)
        
        for recode in recodes :
            print(dict(recode))
    
    def showOneStudent(self) :
        search_student_name = input("조회할 학생 이름 : ")
        
        show_sel_query = "select * from tb_score where sname like " + "'%" + search_student_name + "%'"
        recodes = mysql.executePrint(show_sel_query)
        
        for recode in recodes :
            print(dict(recode))
    
    def regiStudent(self) :
        new_student_name    = input("학생 이름 : ")
        student_kor_score   = input("국어 성적 : ")
        student_eng_score   = input("영어 성적 : ")
        student_math_score  = input("수학 성적 : ")
        student_information = [{'sname' : new_student_name , 'kor' : student_kor_score , 'eng' : student_eng_score , 'math' : student_math_score}]
        
        regi_student_query = "insert into tb_score (sname , kor , eng , math , regdate) values (:sname , :kor , :eng , :math , now())"
        mysql.execute(regi_student_query , student_information)
        
        print(f"[{new_student_name}] 님의 성적이 정상적으로 입력되었습니다.")     
    
    def modifyStudent(self) :
        self.showAllStudent()
        select_student = input("수정할 학생 아이디 입력 : ")
        
        modify_student_kor_score   = input("수정 국어 성적 : ")
        modify_student_eng_score   = input("수정 영어 성적 : ")
        modify_student_math_score  = input("수정 수학 성적 : ")
        student_information        = [{'kor' : modify_student_kor_score , 'eng' : modify_student_eng_score , 'math' : modify_student_math_score , 'id' : select_student}]
        
        modify_student_query = "update tb_score set kor = :kor , eng = :eng , math = :math where id = :id"
        mysql.execute(modify_student_query , student_information)
        
        print("데이터가 정상적으로 수정되었습니다.")
    
    def deleteStudent(self) :
        self.showAllStudent()
        select_student = input("삭제할 학생 아이디 입력 : ")
        
        student_information = [{'id' : select_student}]
        
        delete_student_query = "delete from tb_score where id = :id"
        mysql.execute(delete_student_query , student_information)
        
        print("데이터가 정상적으로 삭제되었습니다.")

if __name__ == "__main__" :
    manager = StudentManager()
    manager.sel_menu()