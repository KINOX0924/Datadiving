import execute_module_re as exe_module
from sqlalchemy.exc import SQLAlchemyError

class ScoreData :
    def __init__(self , sname = "" , kor = 0 , eng = 0 , math = 0) :
        self.sname    = sname
        self.kor     = kor
        self.eng     = eng
        self.math    = math
        
        self.process()
    
    def ouput(self) :
        print(f"{self.sname}\t")
        print(f"{self.kor}\t")
        print(f"{self.eng}\t")
        print(f"{self.math}\t")
        print(f"{self.total}\t")
        print(f"{self.average}\t")
        print(f"{self.grade}\t")
    
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
