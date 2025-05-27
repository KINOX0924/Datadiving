from execute_module import Database

class StudentManager :
    def p_menu(self) :
        print("===== ===== ===== =====")
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
        Data = Database()
        show_query = "select A.id , A.sname , A.kor , A.eng , A.math , (A.kor + A.eng + A.math) as Total_score , round((A.kor + A.eng + A.math) / 3 , 0) as Aver_score from tb_score A"
        
        recodes = Data.executeAll(show_query)
        
        for recode in recodes :
            print(f"학생 아이디 : [{recode["id"]}] || 성명 : [{recode["sname"]}] 국어성적 : [{recode["kor"]}] 영어성적 : [{recode["eng"]}] 수학성적 : [{recode["math"]}] 총합 : [{recode["Total_score"]}] 평균 : [{recode["Aver_score"]}]")
        
        Data.close()
    
    def showOneStudent(self) :
        Data = Database()
        select_show_query = "select A.id , A.sname , A.kor , A.eng , A.math , (A.kor + A.eng + A.math) as Total_score , round((A.kor + A.eng + A.math) / 3 , 0) as Aver_score from tb_score A where sname = %s"
        
        search_student_name = input("조회 학생 이름 입력 : ")
        
        recode = Data.executeOne(select_show_query , (search_student_name))
        if recode == None :
            print("조회된 학생이 없습니다. 이름을 다시 확인해주세요.")
            Data.close()
            return
        print(f"학생 아이디 : [{recode["id"]}] || 성명 : [{recode["sname"]}] 국어성적 : [{recode["kor"]}] 영어성적 : [{recode["eng"]}] 수학성적 : [{recode["math"]}] 총합 : [{recode["Total_score"]}] 평균 : [{recode["Aver_score"]}]")
        Data.close()
    
    def regiStudent(self) :
        Data = Database()
        insert_query = "insert into tb_score(sname , kor , eng , math , regdate) values(%s , %s , %s , %s , now())"
        
        new_name = input("이름 입력 : ")
        new_student_kor = input("국어 성적 입력 : ")
        new_student_eng = input("영어 성적 입력 : ")
        new_student_math = input("수학 성적 입력 : ")
        
        Data.execute(insert_query , (new_name , new_student_kor , new_student_eng , new_student_math))
        Data.close()
        
        print(f"[{new_name}] 학생 정보 입력 완료")
    
    def modifyStudent(self) :
        Data = Database()
        self.showAllStudent()
        modify_query = "update tb_score set kor = %s , eng = %s , math = %s where id = %s"
        select_student_id = input("수정 필요한 학생 아이디 입력 : ")
        
        modify_student_kor = input("국어 성적 입력 : ")
        modify_student_eng = input("영어 성적 입력 : ")
        modify_student_math = input("수학 성적 입력 : ")
        
        Data.execute(modify_query , (modify_student_kor , modify_student_eng , modify_student_math , select_student_id))
        Data.close()
    
    def deleteStudent(self) :
        Data = Database()
        self.showAllStudent()
        delete_query = "delete from tb_score where id = %s"
        select_student_id = input("삭제 필요한 학생 아이디 입력 : ")
        
        Data.execute(delete_query , (select_student_id))
        Data.close()


if __name__ == "__main__" :
    manager = StudentManager()
    manager.sel_menu()