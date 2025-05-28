import execute_module_re as exe_module
from sqlalchemy import text

class ScoreManager :
    def __init__ (self) :
        pass
    
    def output(self) :
        print_sql = "select * from tb_score"
        recodes   = exe_module.executePrint(print_sql)
        
        for recode in recodes :
            print(f"[아이디] | {recode["id"]}" , end = "\t")
            print(f"[이름] | {recode["sname"]}" , end = "\t")
            print(f"[국어] | {recode["kor"]} 점" , end = "\t")
            print(f"[영어] | {recode["eng"]} 점" , end = "\t")
            print(f"[수학] | {recode["math"]} 점")
    
    def regiStudent(self) :
        insert_sql = """
                     insert into tb_score(sname , kor , eng , math , regdate)
                     values(:sname , :kor , :eng , :math , now())
                     """
        
        sname = input("이름 입력 : ")
        kor   = input("국어 성적 입력 : ")
        eng   = input("영어 성적 입력 : ")
        math  = input("수학 성적 입력 : ")
        exe_module.execute(insert_sql , [{"sname" : sname , "kor" : kor , "eng" : eng , "math" : math}])
    
    def deleteStudent(self) :
        self.output()
        select_student_id = input("삭제할 학생 아이디 입력 : ")
        
        delete_sql = """
                     delete from tb_score where id = :id
                     """
        exe_module.execute(delete_sql , [{"id" : select_student_id}])
    
    def output2(self) :
        print_sql = """
                    select 'all' GRADE , count(*)
                    from tb_score
                    
                    union all

                    select GRADE , count(GRADE) as GRADE_COUNT
                    from (
                        select
                        case
                        when(A.kor + A.eng + A.math) / 3 >= 90 then "수"
                        when(A.kor + A.eng + A.math) / 3 >= 80 then "우"
                        when(A.kor + A.eng + A.math) / 3 >= 70 then "미"
                        when(A.kor + A.eng + A.math) / 3 >= 60 then "양"
                        else "가"
                        end as GRADE
                        from tb_score A
                    ) as B
                    group by GRADE
                    order by
                        case GRADE
                            when "all" then 1
                            when "수" then 2
                            when "우" then 3
                            when "미" then 4
                            when "양" then 5
                            else 6
                        end;
                    """
                    
        recodes = exe_module.executePrint(print_sql)
        
        for recode in recodes :
            if recode["GRADE"] == "all" :
                print(f"[전체 학생 수]\t: {recode["count(*)"]}")
            else :
                print(f"[등급 [{recode["GRADE"]}]]\t: {recode["count(*)"]}")
    
    def output3(self) :
        print_sql = """
                    select concat(A.last_name , " " , A.first_name) as CUSTOMER_NAME , B.postal_code , B.address , B.district , B.phone
                    from customer A
                    join address B on A.address_id = B.address_id;
                    """
        
        recodes = exe_module.executePrint(print_sql)
        
        for recode in recodes :
            print(f"[CUSTOMER NAME] : {recode["CUSTOMER_NAME"]}" , end = "\t")
            print(f"[POSTAL CODE] : {recode["postal_code"]}" , end = "\t")
            print(f"[ADDRESS] : {recode["address"]}" , end = "\t")
            print(f"[DISTRICT] : {recode["district"]}" , end = "\t")
            print(f"[PHONE] : {recode["phone"]}")
        
if __name__ == "__main__" :
    student_manager = ScoreManager()
    student_manager.output3()