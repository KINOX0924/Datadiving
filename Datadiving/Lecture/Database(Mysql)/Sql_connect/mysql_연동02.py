import pymysql

class Database :
    # 초기 생성자 / 공유 클래스
    def __init__(self) :
        self.db = pymysql.connect(
            host     = 'localhost' ,
            user     = 'user03' ,
            password = '1234' ,
            db       = 'project1' ,
            port     = 3306
        )
    
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    # insert , update , delete
    # DB 가 한 곳에서 다 실행될 수 있도록 하는 것
    def execute(self , query , args = ()) :
        # args = tuple 기본값
        print(args)
        self.cursor.execute(query , args)
        self.db.commit()
    
    # 스칼라 서브 쿼리 등 데이터를 딱 한개만 가져오고 싶을 때 사용하는 것
    # scalar 쿼리 포함 / select * from tb_member
    # fetchone = 첫번째 레코드 값만 반환함
    def executeOne(self , query , args = ()) :
        self.cursor.execute(query , args)
        row = self.cursor.fetchone()
        
        return row
    
    # 조회한 모든 레코드 값을 반환하고 싶을 때 사용
    def executeAll(self , query , args = ()) :
        self.cursor.execute(query , args)
        rows = self.cursor.fetchall()
        
        return rows
    
    # 정해진 레코드 값만 가져오고 싶을 때 사용
    def executeMany(self , query , count, args = ()) :
        self.curosr.execute(query , args)
        rows = self.cursor.fetchmany(count)
        
        return rows
    
    def close(self) :
        if self.db.open :
            self.db.close()