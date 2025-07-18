# Buetifulsoup 를 이용해서 html 파싱
# 로컬에 있는 문서를 읽어서 마싱하는 것만 진행
from bs4 import BeautifulSoup

html = open("./test1.html" , encoding = "utf-8")
doc  = html.read()
# 파일의 크기가 작아서 파일을 한번에 다 읽음

html.close()
soup = BeautifulSoup(doc , "html.parser")
# html => DOM 구조로 되어 있음

# find , findAll
# find = ("태그" , "속성") - 첫번째 것만
# findAll = ("태그" , "속성") - 언제나 list 형태로 반환하고, 인덱싱이나 for 문으로 접근 가능

# 태그 객체 가져오기
title_tag = soup.find("title")
# 타이틀 태그 객체를 통째로 가져옴

print(title_tag)        # 태그까지 모두 보여줌
print(title_tag.text)   # 태그 안에 텍스트만 보여줌

# H1 태그 가져오기
h1 = soup.find("h1")    # 첫 번째 것 하나만 가져옴
print(h1.text)

# H1 태그 전체 가져오기
h1list = soup.findAll("h1")
for h1 in h1list :
    print(h1.text)
    
# css Selector : id 하고 class 이용하기
hList = soup.find("h1" , id = "title1")
hList = soup.find("h1" , {"id" : "title1"})
# id 의 경우 두 개는 같은 문법
for h1 in hList :
    print(h1.text)

hList = soup.find("h1" , class_ = "title_red")
hList = soup.find("h1" , {"class" : "title_red"})
# class 의 경우 두 개는 같은 문법
for h1 in hList :
    print(h1.text)
    
# ul 태그 가져오기
ul = soup.find("ul" , {"class" : "coffee"})
print(ul)
# 못 찾으면 None 값이 옴

liList = ul.find_all("li")
for li in liList :
    print(li.text)

# table 태그 가져오기
table = soup.find("table" , {"id" : "productList"})
trList = table.findAll("tr")

for tr in trList :
    tdList = tr.findAll("td")
    for td in tdList :
        print(td.text)