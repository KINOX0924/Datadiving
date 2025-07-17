# 크롤링 = 웹스크래핑
# 웹사이트 마다 데이터를 갖고 오는 방식이 다름
# 계속 웹사이트가 업그레이드가 되어서, 너무 많이들 하니깐 막는 기술도 늘어남

# 서버쪽에서 보내는 응답을 받아옴
# html(일반 웹서버) , json 형태(restpul api 서버)
# html > 이 문서를 분석해서 데이터만 추출(파싱이라고 함)
# html 문서로부터 데이터를 파싱하는 알고리즘 BeautifulSoup -> 설치를 해야함

# 셀레니움 - 크롬을 만들다가 디버깅용 툴을 만듬 , 사용이 어려움
# 이벤트나 자바스크립트 호출이 가능함


# 1. 파이썬에서 requests 모듈을 사용해서 문서를 불러오자
# 웹클라이언트 > request(요청) > 웹서버
#           < response(응답) <
import requests
from bs4 import BeautifulSoup
response = requests.get("http://www.pythonscraping.com/exercises/exercise1.html")
print("응답코드 : " , response.status_code)
# 200 이면 성공 , 404 , 페이지 없음 , 403 권한 없음 , 500 서버 에러

if response.status_code == 200 :
    # response.text => 정보를 받아올 때 문자열로 받아옴
    # response.content => binary 모드로 가져옴 , 이미지나 동영상을 처리할 때
    print(response.text)
    
    bs = BeautifulSoup(response.text , "html.parser")
    # 이 상태로 이미 파싱이 끝나서 내부에 DOM 구조를 가지고 있음
    
    print(bs.title.text)
    # <title>태그</title>
    print(bs.h1.text)
else :
    print("error")