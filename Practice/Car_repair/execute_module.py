from sqlalchemy import create_engine , text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/repairdb" ,
    pool_size    = 10 ,
    max_overflow = 5 ,
    pool_recycle = 3600
)

def execute(query , args = None) :
        try :
            with engine.begin() as connection :
                connection.execute(text(query) , args)
        except SQLAlchemyError as Error :
            print(f"DB 접속 실패 또는 쿼리 실행 불가 \n>>>>> 오류 메세지 : {Error} <<<<<")

def p_execute(query , args = None) :
        try :
            with engine.begin() as connection :
                data = connection.execute(text(query) , args)
                recodes = data.mappings().all()
                
                return recodes
        except SQLAlchemyError as Error :
            print(f"DB 접속 실패 또는 쿼리 실행 불가 \n>>>>> 오류 메세지 : {Error} <<<<<")
