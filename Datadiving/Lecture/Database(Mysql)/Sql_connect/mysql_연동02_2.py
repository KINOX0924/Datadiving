from mysql_연동02 import Database

def output() :
    db = Database()
    sql = "select * from tb_member"
    rows = db.executeAll(sql)

    for row in rows :
        print(row)

    db.close()

def idCheck() :
    db = Database()
    check_sql = "select * from tb_member where user_id = %s"
    
    new_member_id = input("사용 아이디 입력 : ")
    
    result = db.executeOne(check_sql , new_member_id)
    if result != None :
        print("사용할 수 없는 아이디입니다.")
        db.close()
        return
    
    print("사용 가능한 아이디입니다.")
    db.close()
    return new_member_id

# 회원가입
def insertMember() :
    db = Database()
    insert_sql = "insert into tb_member(user_id , password , user_name , email , phone , regdate) values(%s , %s , %s , %s , %s , now())"
    
    new_member_id    = idCheck()
    if new_member_id == None :
        return
    new_member_pw    = input("사용 비밀번호 입력 : ")
    new_member_name  = input("이름 입력 : ")
    new_member_email = input("이메일 주소 입력 : ")
    new_member_phone = input("연락처 입력 : ")
    
    db.execute(insert_sql,(new_member_id , new_member_pw , new_member_name , new_member_email , new_member_phone))
    db.close()


if __name__ == "__main__" :
    insert = insertMember()