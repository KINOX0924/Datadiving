# 커넥션 풀이 적용된 execute module

from sqlalchemy import create_engine , text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    "mysql+pymysql://root:1234@localhost/mydb" ,
    pool_size    = 10 ,
    max_overflow = 5 ,
    pool_recycle = 3600
    )
    
def execute(query , args = []) :
    try :
        connection = engine.connect()
    except SQLAlchemyError as error :
        print("데이터베이스 연결 실패")
    
    sql_query = text(query , args = [])
    connection.execute(sql_query , args)
    connection.commit()
    connection.close()
    
def executePrint(query) :
    try :
        connection = engine.connect()
    except SQLAlchemyError as error :
        print("데이터베이스 연결 실패")
        
    sql_query = text(query)
    data      = connection.execute(sql_query)
    recodes   = data.mappings().all()
    
    connection.close()
    return recodes