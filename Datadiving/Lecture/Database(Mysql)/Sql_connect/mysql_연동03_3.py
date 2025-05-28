import execute_module_re as exe_module
from sqlalchemy import text

class ScoreManager :
    def __init__ (self) :
        pass
    
    def output(self) :
        print_sql = "select * from tb_score"
        recodes   = exe_module.executePrint(print_sql)
        
        for recode in recodes :
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


if __name__ == "__main__" :
    student_manager = ScoreManager()
    student_manager.regiStudent()
    student_manager.output()