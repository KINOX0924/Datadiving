from sqlalchemy import create_engine , text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    "mysql+pymysql://root:1234@localhost:3306/mydb" ,
    pool_size    = 10 ,
    max_overflow = 5 ,
    pool_recycle = 3600
    )

# [1] 데이터 출력
with engine.connect() as connection :
    sql = "select empno , ename , sal from emp"
    
    result = connection.execute(text(sql))
    
    for row in result.all() :
        print(row)
    
    result = connection.execute(text(sql))
    rows = result.mappings().all()
    for row in rows :
        print(row)
        
# [2] 데이터 검색
search_name = "JA"
print(search_name)

with engine.connect() as connection :
    sql = "select * from emp where ename like '%" + search_name + "%'"
    
    result = connection.execute(text(sql))
    temp   = result.all()
    
    if len(temp) == 0 :
        print("없음")
    else : 
        # rows = result.mappings().all()
        for row in temp :
            print(row)

# [3] 데이터 추가

# with engine.connect() as connection :
#     sql = "select ifnull(max(empno) , 0) + 1 from emp"
#     result = connection.execute(text(sql))
#     empno = result.all()[0][0]
    
#     sql = "insert into emp (empno , ename , sal) values (:empno , :ename , :sal)"
#     connection.execute(text(sql) , [{"empno" : empno , "ename" : "GILDONG Jr" , "sal" : 750}])
#     connection.commit()


# 아래의 현재 상태로는 test1 에는 입력이 되지만 , test2 에는 입력이 되지 않음
# 트랜잭션의 원자성(전부 되거나 , 하나라도 안 되거나) 이 지켜지지 않는 상태
# with engine.connect() as connection :
#     sql = "select ifnull(max(id) , 0) + 1 from test1"
    
#     result = connection.execute(text(sql))
#     id = result.all()[0][0]
    
#     sql = "insert into test1 (id , field) values (:id , :field)"
#     connection.execute(text(sql) , [{"id" : id , "field" : "test"}])
#     connection.commit()
    
#     sql = "insert into test2 (id , field) values (:id , :field)"
#     connection.execute(text(sql) , [{"id" : id , "field" : "test12345678912345678910"}])
#     connection.commit()


# with enigne 에서 connect() 에서 begin() 으로 변경
# 각 execute 에서의 commit() 을 삭제
with engine.begin() as connection :
    sql = "select ifnull(max(id) , 0) + 1 from test1"
    
    result = connection.execute(text(sql))
    id = result.all()[0][0]
    
    sql = "insert into test1 (id , field) values (:id , :field)"
    connection.execute(text(sql) , [{"id" : id , "field" : "test"}])
    
    sql = "insert into test2 (id , field) values (:id , :field)"
    connection.execute(text(sql) , [{"id" : id , "field" : "test1"}])