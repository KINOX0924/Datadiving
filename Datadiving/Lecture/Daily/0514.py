# 5월 14일 강의

# 정규 표현식
# 복잡한 문자열을 처리할 때 사용하는 기법으로 파이썬 뿐만이 아니라 문자열을 사용하는 모든 곳에서 사용하는 일종의 형식 언어
# 패턴은 문자열 \ - 이건 기본적으로 escape 문자로 사용하기에 패턴에서는 \ 문자 자체가 필요한건지 아닌지 모르기에 항상 escape 탈출 문자인 'r' 을 붙혀야 함

import re

# pattern = r"비"

# text = "하늘에 비가 오고 있습니다. 어제도 비가 내렸고 오늘도 비가 내리고 있습니다. 비가 계속해서 내리고 있습니다. 목요일에도 비가 내린답니다. 주말에는 비가 안 내린답니다."

# regex  = re.compile(pattern)
# result = regex.findall(text)
# print(text)
# print(result)



# zipcode = input("우편번호 입력 : ")

# pattern = r"\d{5}$"
# # \d = 숫자 , {5} = 다섯개 , $ = 이것으로 끝내라
# regex   = re.compile(pattern)
# result  = regex.match(zipcode)
# # match 함수의 특징 : 시작 단어에 매칭하는 값이 있어야함

# if result != None :
#     print("형식이 일치합니다.")
# else :
#     print("잘못된 형식입니다.")



# text_1 = "I like star"
# text_2 = "star is beautiful"

# pattern = "star"
# print(re.match(pattern , text_1))
# print(re.match(pattern , text_2))

# matchObj = re.match(pattern , text_2)
# print(matchObj.group())
# print(matchObj.start())
# print(matchObj.end())
# print(matchObj.span())
# # .group()  : 패턴과 일치하는 단어를 추출
# # .start()  : 패턴과 일치하는 단어가 시작하는 인덱스
# # .end()    : 패턴과 일치하는 단어가 끝나는 인덱스
# # .span()   : 패턴과 일치하는 단어가 시작하는 인덱스와 끝나는 인덱스를 튜플 형태로 반환

# print(re.search(pattern , text_1))
# print(re.search(pattern , text_2))

# matchObj_1 = re.search(pattern , text_1)
# print(matchObj_1.group())
# print(matchObj_1.start())
# print(matchObj_1.end())
# print(matchObj_1.span())

# matchObj_2 = re.search(pattern , text_2)
# print(matchObj_2.group())
# print(matchObj_2.start())
# print(matchObj_2.end())
# print(matchObj_2.span())


# text = "
#     phone : 010-0000-0000 email:test1@nate.com
#     phone : 010-1111-1111 email:test2@naver.com
#     phone : 010-2222-2222 email:test3@gmail.com
#     phone : 02-345-9090 email:dseisk@hanmail.netasdasd
#     "
# print()
# print("--- 전화번호 추출하기 ---")
# phonepattern = r"\d{2,3}-\d{3,4}-\d{4}"

# matchObj = re.findall(phonepattern , text)
# for item in matchObj :
#     print(item)

# print("--- 이메일 추출하기 ---") 
# emailpattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b"
# # \b 가 없는 경우 이메일 형식 패턴을 인식하지 못 함(바운더리 : 경계)
# matchObj = re.findall(emailpattern , text)
# for item in matchObj:
#     print(item)
    
# matchObj = re.finditer(phonepattern , text)
# for item in matchObj :
#     print(item)
#     print(item.group())
#     print(item.span())

# pattern = "phone"
# result  = re.sub(pattern , "smartphone" , text)
# print(result)

# result  = re.sub(pattern , "smartphone" , text , count = 2)
# print(result)


# pattern = r"abc"

# text =["abc" , "abcd" , "abc15" , "dabc" , "" , "s" , "I love kabcde"]
# repattern = re.compile(pattern)

# for item in text :
#     result = repattern.search(item)
#     if result :
#         print(item , "-O")
#     else :
#         print(item , "-X")



# pattern = r"^[p|P]ython\b"

# text = ["python" , "Python" , "PYTHON" , "PYthon" , "12python" , "python3"]
# repttern = re.compile(pattern)

# for item in text :
#     result = repttern.search(item)
#     if result :
#         print(item , "-O")
#     else :
#         print(item , "-X")
        
# contents = "문의 사항이 있으면 010-1234-6789 으로 연락 주시기 바랍니다."

# pattern = r"(\d{3})-(\d{4})-(\d{4})"
# regex = re.compile(pattern)
# result = regex.search(contents)

# if result != None :
#     phone1 = result.group(1)

# contents = """
#            우리커피숍 100-90-12345
#            영풍문고 101-91-12121
#            영미청과 102-92-23451
#            황금코인 103-89-13579
#            우리문구 104-91-24689
#            옆집회사 105-82-12345
#            """

# pattern = r"(\d{3})-(\d{2})-(\d{5})"
# regex   = re.compile(pattern)
# result  = regex.finditer(contents)

# for item in result :
#     if int(item.group(2)) >= 90 and int(item.group(2)) <= 99 :
#         print(item.group(1) + "-" + item.group(2) + "-" + item.group(3))


# MySQL 다운로드
