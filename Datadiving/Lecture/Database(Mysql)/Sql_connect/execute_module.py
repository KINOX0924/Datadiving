import pymysql

class Database :
    # host = 본인 DB 의 ip 주소
    # user = DB 에 접속할 아이디
    # password = DB 에 접속할 비밀번호
    # db = DB 의 이름
    # port = DB 에 접속하기 위한 포트 넘버
    
    def __init__(self) :
        self.Data = pymysql.connect(
            host = 'localhost',
            user = 'user02',
            password = 'qwer1234',
            db = 'mydb',
            port = 3306
        )
        
        self.cursor = self.Data.cursor(pymysql.cursors.DictCursor)
        # self.cursor = self.Data.cursor() <- Dict 타입 출력이 싫다면 해당 코드를 사용
        
    
    # insert / update / delete 시 사용
    def execute(self , query , args = ()) :
        self.cursor.execute(query , args)
        self.Data.commit()
    
    # 데이터를 딱 하나만 가져오고 싶을 때 사용
    def executeOne(self , query , args = ()) :
        self.cursor.execute(query , args)
        recode = self.cursor.fetchone()
            
        return recode
    
    # 데이터를 전부 가져오고 싶을 때 사용
    def executeAll(self , query , args = ()) :
        self.cursor.execute(query , args)
        recodes = self.cursor.fetchall()
            
        return recodes
    
    # 데이터를 정해진 갯수 만큼만 가져오고 싶을 때 사용
    def executeMany(self , query , count , args =()) :
        self.cursor.execute(query , args)
        recodes = self.cursor.fetchmany(count)
            
        return recodes
    
    # 접속한 DB 의 접속을 끊고 싶을 때 사용
    def close(self) :
        if self.Data.open :
            self.Data.close()