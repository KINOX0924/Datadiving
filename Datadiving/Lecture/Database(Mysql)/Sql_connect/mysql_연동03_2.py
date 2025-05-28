import execute_module_re as exe_module
from sqlalchemy import text

class ScoreData :
    def __init__(self , sname = "" , kor = 0 , eng = 0 , math = 0) :
        self.sname    = sname
        self.kor     = kor
        self.eng     = eng
        self.math    = math
        
        self.process()
    
    def ouput(self) :
        print(f"{self.sname}" , end  = "\t")
        print(f"{self.kor}" , end  = "\t")
        print(f"{self.eng}" , end  = "\t")
        print(f"{self.math}" , end  = "\t")
        print(f"{self.total}" , end  = "\t")
        print(f"{self.average}" , end  = "\t")
        print(f"{self.grade}")
    
    def process(self) :
        self.total = self.kor + self.eng + self.math
        self.average = self.total / 3
        
        if   self.average >= 90 :
            self.grade = "수"
        elif self.average >= 80 :
            self.grade = "우"
        elif self.average >= 70 :
            self.grade = "미"
        elif self.average >= 60 :
            self.grade = "양"
        else :
            self.grade = "가"

if __name__ == "__main__" :
    show_sql = "select * from tb_score"
    recodes = exe_module.executePrint(show_sql)
    
    for recode in recodes :
        student = ScoreData(recode["sname"] , recode["kor"] , recode["eng"] , recode["math"])
        student.ouput()