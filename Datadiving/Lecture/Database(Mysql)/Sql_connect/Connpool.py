from sqlalchemy import create_engine , text
from sqlalchemy.exc import SQLAlchemyError

# SQLAlchemy 가 PyMySQL 을 내부적으로 사용하며 Pool 지원
engine = create_engine(
    "mysql+pymysql://root:1234@localhost/mydb" ,
    pool_size = 10 ,        # 최대 연결수
    max_overflow = 5 ,      # 초과 시 추가 연결 수
    pool_recycle = 3600     # 재활용 시간
    )

# 연결 객체를 얻는 법
try :
    conn = engine.connect()
    print("데이터베이스 연결 성공")
except SQLAlchemyError as e :
    print("데이터베이스 연결 실패")
    
result = conn.execute(text("select * from emp"))
for row in result :
    print(row)

rows = result.mappings().all()
for row in rows :
  print(dict(row))
conn.close()

conn = engine.connect()
sql = text("""
           insert into emp (empno , ename , sal) values (:empno , :ename , :sal)
           """)

# conn.execute(sql , [{'empno' : 10000 , 'ename' : '우즈' , 'sal' : 8800}])
# conn.commit()
# conn.close()