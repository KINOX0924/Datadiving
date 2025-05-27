# conda create
# pip install pymysql
# mysql ver 8 부터 문제가 있을 경우 pip install cryptography

# [1] DB 연결
# [2] 데이터 읽고 쓰기
# [3] 연결 끊기


# import pymysql
# connection = pymysql.connect(
#     host     = 'localhost',  # ip localhost = 127.0.0.1
#     user     = 'user02',     # ID
#     password = 'qwer1234',   # PASSWORD
#     db       = 'mydb',       # DB 명
#     port     = 3306          # 포트명
# )

# cursor = connection.cursor()      # 커서를 가져와야 함
# print("접속 성공")

# # ===== ===== ===== ===== 데이터 가져오기
# # 데이터 가져오기
# # select 쿼리를 실행하고 나서 값을 반환하지 않고 파이썬은 내부에 가지고 있음
# sql = "select * from emp"
# cursor.execute(sql)

# # create user 'user'@'localhost' identified by 'qwer1234';
# # grant all privileges on (DB).* to 'user'@'localhost';
# # drop user user

# # 파이썬은 데이터를 가지고 올 때 튜플 타입으로 가져옴
# # fetchall = 데이터 전부 가져오기
# rows = cursor.fetchall()
# for row in rows :
#     print(type(row) , row)

# # 데이터 다시 가져오기
# sql = "select * from emp where empno = 7900"
# cursor.execute(sql)

# # fetchone = 데이터 하나만 가져오기
# row = cursor.fetchone()
# print(row)

# # 데이터 다시 가져오기
# # fetchmany = 데이터 지정한 값 만큼 가져오기
# sql = "select * from emp where empno < 8000"
# cursor.execute(sql)
# rows = cursor.fetchmany(3)
# for row in rows :
#     print(type(row) , row)
    
# # 데이터를 가져올 때 dict 타입으로 가져오기
# cursor = connection.cursor(pymysql.cursors.DictCursor)
# cursor.execute(sql)

# rows = cursor.fetchall()
# for row in rows :
#     print(type(row) , row)

# # 연결 종료
# connection.close()




# # 파라미터 처리
# import pymysql
# connection = pymysql.connect(
#     host     = 'localhost',  # ip localhost = 127.0.0.1
#     user     = 'user02',     # ID
#     password = 'qwer1234',   # PASSWORD
#     db       = 'mydb',       # DB 명
#     port     = 3306          # 포트명
# )

# cursor = connection.cursor(pymysql.cursors.DictCursor)

# # 검색할 데이터 값 입력받기
# ename = "SCOTT"
# sql   = "select * from emp where ename ='"+ename+"'"

# print(sql)
# cursor.execute(sql)

# rows = cursor.fetchall()
# print("데이터 개수" , len(rows))

# for row in rows :
#     print(row["empno"] , row["ename"] , row["sal"])


# 데이터 입력하기(insert)
# sql = """
#     insert into emp(empno , ename , sal)
#     values(%s , %s , %s)
# """

# 데이터를 입력받아 넣은 뒤에는 반드시 commit 을 실행해야 내용이 들어감
# cursor.execute(sql,(7784 , 'SCALETT' , 2700))
# connection.commit()

# sql = """
#     select ifnull(max(empno) , 0) + 1 id from emp
# """
# cursor.execute(sql)
# row = cursor.fetchone()
# print(row)


# sql = """
#     insert into emp(empno , ename , sal)
#     values(%s , %s , %s)
# """
# cursor.execute( sql , (row['id'] , 'SCALETT' , 2850))
# connection.commit()


# connection.close()

# 전체보기
# 추가 : 입력받아서 데이터 넣기
# 수정
# update 테이블명 set 필드 1 = '갑1' , 필드2 = '갑2' where 절
# delete from 테이블명 where id -1
# 검색


# import pymysql
# connection = pymysql.connect(
#     host     = 'localhost',  # ip localhost = 127.0.0.1
#     user     = 'user02',     # ID
#     password = 'qwer1234',   # PASSWORD
#     db       = 'mydb',       # DB 명
#     port     = 3306          # 포트명
# )

# cursor = connection.cursor(pymysql.cursors.DictCursor)

# class MySQL001 :
#     def p_menu(self) :
#         print("===== ===== ===== =====")
#         print("[1] | 데이터 전체 보기")
#         print("[2] | 학생 데이터 입력")
#         print("[3] | 학생 데이터 수정")
#         print("[4] | 학생 데이터 삭제")
#         print("[5] | 학생 데이터 개별 조회")
#         print("[0] | 프로그램 종료")
    
#     def sel_menu(self) :
#         menu_list = [None , self.showAllData , self.insertStudentData , self.updateStudentData , self.deleteStudentData , self.showStudentData]
        
#         while True :
#             self.p_menu()
#             try :
#                 select_menu = int(input("메뉴 선택 : "))
#                 if select_menu > 0 and select_menu < len(menu_list) :
#                     menu_list[select_menu]()
#                 elif select_menu == 0 :
#                     connection.close()
#                     return
#                 else :
#                     print("메뉴에 있는 숫자만 입력하세요.")
#             except ValueError :
#                 print("숫자만 입력하세요.")
    
#     def showAllData(self) :
#         show_query = "select * from tb_score"
#         cursor.execute(show_query)

#         rows = cursor.fetchall()
#         for row in rows :
#             print(f"아이디 : [{row["id"]}] || 이름 : [{row["sname"]}] || 국어성적 : [{row["kor"]}] 영어성적 : [{row["eng"]}] 수학성적 : [{row["math"]}]")
    
#     def insertStudentData(self) :
#         insert_query = "insert into tb_score(sname , kor , eng , math , regdate) values(%s , %s , %s , %s , now())"
        
#         student_name = input("학생 이름 입력 : ")
#         kor_score    = input("국어 성적 : ")
#         eng_score    = input("영어 성적 : ")
#         math_score   = input("수학 성적 : ")
        
#         cursor.execute(insert_query , (student_name , kor_score , eng_score , math_score))
#         connection.commit()
    
#     def updateStudentData(self) :
#         self.showAllData()
#         update_query = "update tb_score set kor = %s , eng = %s , math = %s where id = %s"
        
#         select_student = input("수정 학생 아이디 입력 : ")
#         kor_score    = input("국어 성적 : ")
#         eng_score    = input("영어 성적 : ")
#         math_score   = input("수학 성적 : ")
        
#         cursor.execute(update_query , (kor_score , eng_score , math_score , select_student))
#         connection.commit()
    
#     def deleteStudentData(self) :
#         self.showAllData()
#         delete_query = "delete from tb_score where id = %s"
        
#         select_student = input("삭제 학생 아이디 입력 : ")
#         cursor.execute(delete_query , select_student)
#         connection.commit()
    
#     def showStudentData(self) :
#         student_name = input("조회 학생 이름 : ")
        
#         search_query = "select * from tb_score A where A.sname like %s"
#         cursor.execute(search_query , "%" + student_name + "%")
#         rows = cursor.fetchall()
        
#         for row in rows :
#             print(f"아이디 : [{row["id"]}] || 이름 : [{row["sname"]}] || 국어성적 : [{row["kor"]}] 영어성적 : [{row["eng"]}] 수학성적 : [{row["math"]}]")

# if __name__ == "__main__" :
#     practice = MySQL001()
#     practice.sel_menu()





import pymysql
connection = pymysql.connect(
    host     = 'localhost',  # ip localhost = 127.0.0.1
    user     = 'user02',     # ID
    password = 'qwer1234',   # PASSWORD
    db       = 'mydb',       # DB 명
    port     = 3306          # 포트명
)

cursor = connection.cursor(pymysql.cursors.DictCursor)

class CalculatorWeekpay :
    def p_menu(self) :
        print("===== ===== ===== =====")
        print("[1] | 사원 전체 조회")
        print("[2] | 주급 계산 조회")
        print("[3] | 사원 정보 입력")
        print("[4] | 사원 정보 수정")
        print("[5] | 특정 사원 조회")
        print("[6] | 사원 정보 삭제")
        print("[0] | 프로그램 종료")
        
    def sel_menu(self) :
        menu_list = [None , self.showAllEmployee , self.calWeekpay , self.insertEmployee , self.modifyEmployee , self.searchEmployee , self.deleteEmployee]
        
        while True :
            self.p_menu()
            try :
                select_menu = int(input("메뉴 선택 : "))
                if select_menu > 0 and select_menu < len(menu_list) :
                    menu_list[select_menu]()
                elif select_menu == 0 :
                    connection.close()
                    return
                else : 
                    print("메뉴에 있는 숫자만 선택하세요.")
            except ValueError :
                print("숫자만 입력하세요.")
    
    def showAllEmployee(self) :
        show_query = "select * from tb_weekpay"
        
        cursor.execute(show_query)
        employees = cursor.fetchall()
        
        for employee in employees :
            print(f"사원번호 : [{employee["id"]}] || 사원명 : [{employee["cname"]}] 근무 시간 : [{employee["work_time"]}] 시간당 급여액 [{employee["time_per_pay"]}]")
    
    def calWeekpay(self) :
        self.showAllEmployee()
    
        cal_query = """
                    select A.id , A.cname , A.work_time , A.time_per_pay , case when A.work_time > 20 then ((A.work_time - 20) * (A.time_per_pay * 1.5)) + (20 * A.time_per_pay) else A.work_time * A.time_per_pay end as total_pay
                    from tb_weekpay A
                    where A.id = %s
        """
        
        select_employee = input("계산할 사원 아이디 입력 : ")

        cursor.execute(cal_query , select_employee)
        employee = cursor.fetchone()
        print(f"사원번호 : [{employee["id"]}] || 사원명 : [{employee["cname"]}] 근무 시간 : [{employee["work_time"]}] 시간당 급여액 [{employee["time_per_pay"]}] || 최종 주급 : [{employee["total_pay"]}]")
    
    def insertEmployee(self) :
        employee_name         = input("사원 이름 : ")
        employee_work_time    = input("근무 시간 : ")
        employee_time_per_pay = input("주급 : ")
        
        insert_query = "insert into tb_weekpay(cname , work_time , time_per_pay , regdate) values(%s , %s , %s , now())"
        
        cursor.execute(insert_query , (employee_name , employee_work_time , employee_time_per_pay))
        connection.commit()
    
    def modifyEmployee(self) :
        modify_query = "update tb_weekpay set work_time = %s , time_per_pay = %s where id = %s"
        self.showAllEmployee()
        
        employee_id         = input("수정할 사원 아이디 : ")
        employee_work_time    = input("수정 근무 시간 : ")
        employee_time_per_pay = input("수정 주급 : ")
        
        cursor.execute(modify_query , (employee_work_time , employee_time_per_pay , employee_id))
        connection.commit()
    
    def searchEmployee(self) :
        search_query = "select * from tb_weekpay where cname like %s"
        search_name = input("검색할 사원 이름 : ")
        
        cursor.execute(search_query , "%" + search_name + "%")
        employees = cursor.fetchall()
        
        for employee in employees :
            print(f"사원번호 : [{employee["id"]}] || 사원명 : [{employee["cname"]}] 근무 시간 : [{employee["work_time"]}] 시간당 급여액 [{employee["time_per_pay"]}]")
    
    def deleteEmployee(self) :
        delete_query = "delete from tb_weekpay A where A.id = %s"
        
        self.showAllEmployee()
        
        employee_id         = input("퇴사시킬 사원 아이디 : ")
        
        cursor.execute(delete_query , employee_id)
        connection.commit()

if __name__ == "__main__" :
    Calculator = CalculatorWeekpay()
    Calculator.sel_menu()