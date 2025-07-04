import datetime
# import pytz
import calendar
# import pandas as pd
# import numpy as np
from datetime import datetime , date , timedelta
from wordcloud import WordCloud
import nltk
from collections import Counter 
from konlpy.corpus import kolaw
from konlpy.tag import  Okt
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import  ImageColorGenerator
from PIL import Image
import random

"""
# 판다스 1

today = datetime.now() # 현재 날짜와 시간 정보를 받음
print(today)

# 파이썬의 dir 함수가 있음 , 기본적으로 내부 구조를 보여줌
print(dir(datetime))

# 날짜와 날짜의 연산을 수행하려면 날짜를 date 클래스나 datetime 클래스로 바꾸어야 연산이 가능함
day1 = date(2025,7,31)
print(day1)

# 타임스탬프
value = 1567345678
timestamp = date.fromtimestamp(value)
print("date = " , timestamp)

# 날짜 추출
print(today.year)
print(today.month)
print(today.day)

print(today.hour)
print(today.minute)
print(today.second)

# weekday()
print(today.weekday())

# 마지막 날짜를 추출하기
day_1 = date(2025,7,4)
day_2 = date(2025,12,31)
d_day = day_2 - day_1
print(d_day)
print(type(d_day))

# 지금부터 N 시간 뒤의 시간을 구하기
current = datetime.today()  # 현재 시간과 날짜를 구함
after = current + timedelta(hours = 3)
print(f"현재 시간 : {current}")
print(f"3시간 후  : {after}")

# 지금부터 10일 뒤의 시간을 구하기
current = datetime.today()
after = current + timedelta(days = 10)
print(f"현재 시간 : {current}")
print(f"10일 후   : {after}")

# 2주 10시간 전 시간을 구하기
current = datetime.today()
after = current + timedelta(weeks = -2 , hours = -4)
print(f"현재 시간 : {current}")
print(f"2주 4시간 전 : {after}")

# 서식 날짜 데이터 바꾸기
print(today.strftime("%Y-%m-%d"))
print(today.strftime("%H:%M:%S"))
print(today.strftime("%Y-%m-%d %H:%M:%S %B"))

# timezone
# 각 나라별 시간 정보를 가져옴
format = "%Y-%m-%d %B %H:%M:%S"
local  = datetime.now()
print("현재 지역 시간 : " , local.strftime(format))

tz_NY = pytz.timezone("America/New_york")
local = datetime.now(tz_NY)
print("뉴욕 현재 시간 : " , local.strftime(format))

tz_LD = pytz.timezone("Europe/London")
local = datetime.now(tz_LD)
print("런던 현재 시간 : " , local.strftime(format))

# 달의 마지막 날짜 구하기
start_day , last_day = calendar.monthrange(2025,7)
print(start_day)
print(last_day)

for month in range(1,13) :
    start_day , last_day = calendar.monthrange(2025 , month)
    print(f"{month} 월의 마지막 날은 {last_day} 입니다.")

# date_range
days = pd.date_range(start = "2019-09-01" , end = "2019-09-30")
print(days)

# periods 와 freq 는 서로 조합이 됨
# freq 는 기본적으로 "D"
days = pd.date_range(start = "2019-01-01" , periods = 60)
print(days)

days = pd.date_range(start = "2019-10-01" , end = "2019-10-30" , freq = "W-MON")
print(days)

# 더미 데이터 생성 방법
# np.random.randn 함수는 가우스 분포를 따르는 더미 데이터 값을 랜덤하게 생성
# 가우스 분포를 따르는 실수값이 중요한 이유 :

# 통계학자들이 자연계에서 얻어지는 모든 값을 분석한 결과 대부분의 경우
# 양극단으로 갈수록 작아지고, 중간값으로 갈 수록 커지는 종모양의 차트가 만들어짐 => 정규분포

# 따라서 가우스 분포를 따르는 랜덤값을 더미 데이터로 만드는 것이 중요함


np.random.seed(0) # 시드가 같으면 랜덤값이 일정하게 같은 랜덤값이 나옴
ts = pd.Series(np.random.randn(12) , index = pd.date_range(start = "2025-12-01" , periods = 12 , freq = "M"))
print(ts)

print(ts.resample("W").mean())
"""

"""
# 형태소 분석
# pip install konlpy

from konlpy.tag import Kkma , Hannanum , Okt
from konlpy.utils import pprint
"""
msg = """
    오픈소스를 이용하여 형태소 분석을 배워봅시다. 형태소 분석을 지원하는 라이브러리가 많습니다. 
    각자 어떻게 분석하는 지 살펴보겠습니다. 
    이건 Kkma 모듈 입니다.
"""
"""
kkma = Kkma()
print(kkma.sentences(msg))  # 문장 분석
print(kkma.morphs(msg))     # 형태소로 분석
print(kkma.nouns(msg))      # 명사를 추출
print(kkma.pos(msg))        # 품사 태깅 진행

kkma = Hannanum()
print(kkma.analyze(msg))
print(kkma.morphs(msg))
print(kkma.nouns(msg))
print(kkma.pos(msg))

twitter = Okt()
print(twitter.morphs(msg))
print(twitter.nouns(msg))
print(twitter.pos(msg))
"""

# wordcloud 차트
# pip install pytagcloud
# pip install pygame
# pip install WordCloud
# pip install simplejson

"""
# 단어를 직접 넣어서 진행
tag = [
    ("school" , 30) ,
    ("rainbow" , 30) ,
    ("cloud" , 30) ,
    ("world" , 300) ,
    ("peach" , 130) ,
    ("pink" , 50) ,
    ("blue" , 60) ,
    ("graphic" , 100) ,
    ("smart" , 200) ,
    ("fun" , 150) , 
    ("cool" , 200) , 
    ("sexy" , 100) ,
    ("한글" , 200)
]

taglist = pytagcloud.make_tags(tag , maxsize = 50)
print(taglist)

pytagcloud.create_tag_image(taglist , "wordcloud.jpg" , size = (600 , 600) , fontname = "Korean" , rectangular = True)
webbrowser.open("wordcloud.jpg")
"""

"""
# 파일을 읽어서 단어를 추출
file = open("./data/data1.txt" , encoding = "utf-8")
text = file.read() # 텍스트 파일 읽기

# 파일로부터 명사 추출
okt = Okt()
nouns = okt.nouns(text) # 명사로 분해하기
nounsCounter = Counter(nouns) # 명사를 다 세서 (단어 , 카운트) 형태 데이터 전달
# print(nounsCounter[:5])

tag = nounsCounter.most_common(100) # 모든 단어로 차트를 그리면 너무 복잡해보이니 빈도수를 기반으로 정렬한 다음 100 개만 가져와서 차트를 그림

taglist = pytagcloud.make_tags(tag , maxsize = 50)
print(taglist)

pytagcloud.create_tag_image(taglist , "wordcloud2.jpg" , size = (600 , 600) , fontname = "Korean" , rectangular = True)
webbrowser.open("wordcloud2.jpg")
"""

"""
# Word Cloud 3
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = open("./data/alice.txt")
text = file.read()

wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud , interpolation = "bilinear")  # interpolation : 이미지를 조금 이뻐보이게 보정 처리
plt.axis("off") # 눈금 보이지 않게 함
plt.show()
"""

"""
# Word Cloud 4
# 한국 법률 말뭉치
text = kolaw.open("constitution.txt").read()
print(text[:200])

# 한글 처리
# plt 라이브러리는 한글 지원을 하지 않음 , 따라서 한글을 사용하기 위해서는 폰트를 지정해주어야함
# 단, word cloud 가 아닌 plt 에 폰트를 지정해주어야함
fontpath  = "C://Windows/fonts/malgun.ttf"
wordcloud = WordCloud(font_path = fontpath).generate(text)
wordcloud.to_file("image1.png")
plt.imshow(wordcloud , interpolation = "bilinear")  # interpolation : 이미지를 조금 이뻐보이게 보정 처리
plt.axis("off") # 눈금 보이지 않게 함
plt.show()
"""

# Word Cloud 5
# 토큰이 문장에서 단어를 하나씩 분리
# 토큰나이저 : 문자에서 단어를 분리해내는 라이브러리
nltk.download("punkt_tab")  # 토큰나이저 다운받는 코드
# 한국어는 Okt 를 사용하면 됨 , 같은 역할

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text = open("./data/alice.txt" , "r").read()
tokens_en = word_tokenize(text)
# print(tokens_en)

data = Counter(tokens_en)   # 각 단어의 개수를 셈
print(data)

# 주로 많이 사용하는 단어 위주로 앞에서 100 개만 사용
data = data.most_common(100)
temp_data = dict(data)  # Counter 타입을 Dict 타입으로 변환

mask_image = np.array(Image.open("./image/alice_color.png"))
fontpath = "C://Windows/fonts/malgun.ttf"
# 마스크 이미지 사용시 이미지가 numpy 형태의 배열로 전달되어야 함
wordcloud = WordCloud(font_path = fontpath , mask = mask_image).generate_from_frequencies(temp_data)
plt.imshow(wordcloud , interpolation = "bilinear")
plt.axis("off")
plt.show()