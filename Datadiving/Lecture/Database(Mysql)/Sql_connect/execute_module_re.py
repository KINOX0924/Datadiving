from sqlalchemy import create_engine , text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/sakila" ,   # "mysql+pymysql://계정:비밀번호@ip주소:포트주소/DB명"
    pool_size    = 10 ,                                 # 초기 엔진 연결자 수   
    max_overflow = 5 ,                                  # 초기 연결자 수를 초과했을 때마다 생성할 연결할 수
    pool_recycle = 3600                                 # 재활용 시간(사용자의 종료 후 남은 연결자를 삭제하기 전까지의 시간)
    )

# with 사용으로 'close' 없이 자동으로 DB 접속 종료가 되도록 변경
# engine.begin() 을 사용하여 트랜잭션의 원자성(다 되거나 , 하나도 안 되거나) 을 구현
# 기존 sql_query = text(query) 를 바로 text 되어 execute 되도록 변경

def execute(query , args = None) :
    try :
        with engine.begin() as connection :
            connection.execute(text(query) , args)
    except SQLAlchemyError as Error :
        print(f"DB 접속 실패 또는 쿼리 실행 불가 \n>>>>> 오류 메세지 : {Error} <<<<<")

def executePrint(query , args = None) :
    try :
        with engine.begin() as connection :
            data    = connection.execute(text(query) , args)
            recodes = data.mappings().all()
            
            return recodes
    except SQLAlchemyError as Error :
        print(f"DB 접속 실패 또는 쿼리 실행 불가 \n>>>>> 오류 메세지 : {Error} <<<<<")