import pandas as pd
import numpy  as np

"""
# 판다스 1
# 결측치 처리 방법
data = pd.read_csv("./data/data.csv")

print(data.head())
print(data.info())
print(data.describe())

# data 의 height , weight 필드에 결측치(NaN) 가 있는 지 확인
print(data["height"].isnull().sum())
print(data["weight"].isnull().sum())

# data 전체 필드에서 결측치(NaN) 가 있는 지 확인
print(data.isnull().sum())


# 누락값(결측치) 대체하기
# 대체값을 사용할때는 보통 평균값 혹은 중간값을 사용함
# 평균값의 경우 최대값과 최소값 편차가 클 경우에는 평균값보다는 중갑값이 집단을 대표하는 경우가 더 많음
mean_height = data["height"].mean()
mean_weight = data["weight"].mean()

# fillna(대체값 , inplace = True)
# inplace 가 True 인 경우 원본데이터를 변경하며 그게 아니라면 반드시 반환을 받아야함
data["height"].fillna(mean_height , inplace = True)
data["weight"].fillna(mean_weight , inplace = True)

print("누락데이터 교체 후")
print(data.isnull().sum())


# 중복값 제거하기
data2 = {
    "passenger_code" : ["A101" , "A102" , "A103" , "A101" , "A104" , "A101" , "A103"] ,
    "target"         : ["광주" , "서울" , "부산" , "광주" , "대구" , "광주" , "부산"] ,
    "price"          : [25000 , 27000 , 45000 , 25000 , 35000 , 27000 , 45000]
}

data_frame2 = pd.DataFrame(data2)
print(data_frame2)

print("중복 데이터")
column = data_frame2["passenger_code"].duplicated() # 중복된 데이터를 확인하여 True(중복이다) 또는 False(중복이 아니다) 로 보여줌
print(column)

# 중복 삭제(일반)
print("중복 삭제 후")
data_frame2_1 = data_frame2.drop_duplicates()   # 삭제된 데이터를 반환 , 전체 필드가 완전히 중복되는 데이터만 삭제함
print(data_frame2_1)

# 중복 삭제(subset 사용)
print("서브셋을 사용한 중복 삭제 후")
data_frame2_2 = data_frame2.drop_duplicates(subset = ["passenger_code" , "target"])
print(data_frame2_2)
"""

"""
# 판다스 2
# 정규화 과정
# 머신러닝은 수치화가 가능해야 머신러닝을 진행할 수 있음
# 예를 들어 연비가 A , B , C , D 라는 문자열이 있을 때 이것을 어떻게 수치화를 할 수 있는가?
# 연비를 카테고리 타입으로 변경하여 A , B , C , D 이 네개의 타입을 제외한 타입은 프로그램으로 넣을 수 없게 차단을 함
# 카테고리화 할 수 없는 문자열은 삭제함
# 이후 A = 1 , B = 2 , C = 3 , D = 4 로 판단하도록 값을 넣어주어야 함

data = pd.read_csv("./data/auto-mpg.csv")
print(data.info())
print(data.head())

# 컬럼명 변경하기 => 프로그램 안에서 변경
data.columns = ["mpg" , "cyl" , "disp" , "power" , "weight" , "acce" , "model"]
print(data.head())

# 정규화 (정규화 하고자 하는 값 - 최소값) / (최대값 - 최소값)
data["mpg2"] = (data["mpg"] - data["mpg"].min()) / (data["mpg"].max() - data["mpg"].min())
print(data.head())

# 단위 환산
mpg_unit = 1.60934 / 3.78541
data["kpl"] = (data["mpg"] * mpg_unit).round(2) # 소수점이하 2자리 반올림
print(data.head())

# 타입 전환
print(data.dtypes)
print(data.head())
print(data["disp"].unique())

# 잘못된 데이터를 NaN 으로 먼저 바꾼다.
data["disp"].replace("?" , np.nan , inplace = True)
print(data.head())
print(data.isnull().sum())

data.dropna(subset = ["disp"] , axis = 0 , inplace = True)
print(data.head())
print(data.dtypes)
# ↑ 이 부분까지는 데이터의 NaN 부분이 있을 경우 삭제를 진행하는 과정

data["disp"] = data["disp"].astype("float")
print(data.dtypes)

data["model"] = data["model"].astype("category")
print(data.dtypes)

# DataFrame 의 버그(카테고리) - 그 범위를 벗어나는 데이터는 받으면 안됨
# 카테고리 타입에 데이터를 추가했더니 스스로 float 타읍으로 변경되는 것을 허용하면 안됨

data.loc[len(data)] = {"mpg" : 90 , "model" : 93}
# 모델 타입이 카테고리라서 없는 카테고리 값을 추가할 경우에 오류가 발생함
# 파일을 읽을 때 범위가 결정되어서 93 이 해당사항이 없어서 에러가 발생함
# 반드시 범주형으로 되어야 할 것들을 범주형으로 바꾸어주어야 함

print(data.dtypes)
print(data["model"].value_counts())
# model 필드의 타입이 int64 로 변경되었음
"""

"""
# 판다스 3
# 구간 나누기

# 데이터를 읽어오고 확인함
data = pd.read_csv("./data/auto-mpg.csv")
print(data.info())
print(data.head())

# 데이터의 필드명(열) 을 변경함
data.columns = ["mpg" , "cyl" , "disp" , "power" , "weight" , "acce" , "model"]
print(data.dtypes)

# 잘못된 데이터(NaN) 를 제거하고 타입을 전환함
data["disp"].replace("?" , np.nan , inplace = True)
data.dropna(subset = ["disp"] , axis = 0 , inplace = True)
data["disp"] = data["disp"].astype("float")

# 모델별을 범주로 변경함
data["model"] = data["model"].astype("category")

# 구간을 나눌 필드의 NaN 값을 제거하고 , histogram 함수를 사용하여 구간을 나눌 필드와 구간의 개수를 매개변수도 전달함
# count = 각 구간별 데이터 개수 , bin_dividers = 구간 정보
print(data["power"])
print(data["power"].isnull().sum(axis = 0))
data.dropna(subset = ["power"] , inplace = True)
count , bin_dividers = np.histogram(data["power"] , bins = 4)
# bin_dividers = np.array([40 , 120 , 140 , 200 , 300]) # 직접 부여가능
print(bin_dividers)

# 구간의 이름 작성
bin_names = ["D" , "C" , "B" , "A"]

# data 에 새로운 필드를 만들고 cut 함수를 사용하여 구간을 나누어줌
# x 인자는 구간을 나눌 필드 , bins 는 histogram 함수로 생성간 구간 정보 ,
# labels 는 구간 이름이 든 것 , include_lowest 는 애매한 경계값일때는 위로 올릴지 아래로 내릴지를 결정
data["grade"] = pd.cut( x = data["power"] , bins = bin_dividers , labels = bin_names , include_lowest = True)
print(data)


# 원 핫 인코딩 - 사이킷런 라이브러리 설치 필요함 (scikit-learn)
# 사이킷런의 모든 모델은 입력값이 2차원이어야 함 (무조건 ndarray [ numpy 2차원 배열 - 2D ])
grade = data["grade"]
print(type(grade))

# 2D 형식으로 변경
Y_class = np.array(grade) #1D array
print(Y_class[:5])

Y_class = Y_class.reshape(-1 , 1)   # 축이 하나 추가되어서 2D 타입이 됨
print(Y_class[:5])

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()   # 원 핫 인코딩 객체 생성
enc.fit(Y_class)        # 내부적으로 저 배열을 읽어들여서 어떻게 변형할지에 대한 정보가 내부에 저장됨

Y_class_onehot = enc.transform(Y_class).toarray()
print(Y_class_onehot)
"""

"""
# 판다스 4

# 문제 1. Data 폴더 내의 iris 파일을 읽어서 누락된 데이터가 어떤 필드에 몇개 있는 지 찾아내세요
raw_data = pd.read_csv("./data/iris_2.csv")
print(raw_data.isnull().sum())
# 누락된 데이터 또는 NaN 데이터 없음

# 문제 2. 누락된 데이터들을 평균치로 대체하세요
mean_sepal_length = raw_data["sepal.length"].mean()
mean_sepal_width  = raw_data["sepal.width"].mean()
mean_petal_length = raw_data["petal.length"].mean()
mean_petal_width  = raw_data["petal.width"].mean()

raw_data["sepal.length"].fillna(mean_sepal_length , inplace = True)
raw_data["sepal.width"].fillna(mean_sepal_width , inplace = True)
raw_data["petal.length"].fillna(mean_petal_length , inplace = True)
raw_data["petal.width"].fillna(mean_petal_width , inplace = True)
print(raw_data.isnull().sum())

# 문제 3. sepal.length , sepal.width , petal.width 세 개의 필드에 정규화를 진행하세요
raw_data["sepal.length2"] = (raw_data["sepal.length"] - raw_data["sepal.length"].min()) / (raw_data["sepal.length"].max() - raw_data["sepal.length"].min())
raw_data["sepal.width2"] = (raw_data["sepal.width"] - raw_data["sepal.width"].min()) / (raw_data["sepal.width"].max() - raw_data["sepal.width"].min())
raw_data["petal.width2"] = (raw_data["petal.width"] - raw_data["petal.width"].min()) / (raw_data["petal.width"].max() - raw_data["petal.width"].min())
print(raw_data)

# 문제 4. petal.length 필드를 3개의 구간으로 나누어서 A , B , C 이라고 구간을 붙여서 petal_grade 필드를 추가하세요
count , bin_dividers = np.histogram(raw_data["petal.length"] , bins = 3)
print(bin_dividers)

bin_names = [ "C" , "B" , "A" ]

raw_data["petal.grade"] = pd.cut( x = raw_data["petal.length"] , bins = bin_dividers , labels = bin_names , include_lowest = True)
print(raw_data)

# 문제 5. 원핫 인코딩으로 전환
petal_grade = raw_data["petal.grade"]
print(type(petal_grade))

td_class = np.array(petal_grade)
td_class = td_class.reshape(-1 , 1)
print(td_class)

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(td_class)

td_class_onehot = enc.transform(td_class).toarray()
td_class_recovery = np.argmax(td_class_onehot , axis = 1).reshape(-1 , 1)
print(td_class_onehot)
print(td_class_recovery)
"""

# 판다스 5

# 정규식
import re

# pattern = r"비"
# regex   = re.compile(pattern)   # re.compile 을 해서 패턴을 내부 객체에 등록

# text = "하늘에 비가 오고 있습니다. 어제도 비가 왔고 오늘도 비가 오고 있습니다."

# # 패턴에 일치하는 단어 찾기
# result = regex.findall(text)    # 일치하는 단어들을 모두 찾아서 리스트 형태로 반환
# print(result)


# # 정규식 2
# pattern = "\d{5}$"

# zip_code = input("우편번호를 입력하세요 : ")
# regex = re.compile(pattern)

# # match 함수는 패턴이 반드시 시작위치에 있어야 함
# # 형식이 일치하는 것이 없으면 None 반환
# result = regex.match(zip_code)
# if result == None :
#     print("일치되는 우편번호가 없습니다.")
# else :
#     print(result)


# 정규식 3
# match 함수
text1 = "I like star"
text2 = "star is beautiful"

pattern = "star"

print(re.match(pattern , text1))
print(re.match(pattern , text2))

matchObj = re.match(pattern , text2)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())

# search 함수
# search 함수는 문자열에서 가장 먼저 나오는 패턴을 반환 , 그 이후에 같은 패턴이 나오더라도 그 패턴은 무시함
text1 = "I like star , red star , yellow star"
text2 = "star is beautiful"

pattern = "star"

print(re.search(pattern , text1))
print(re.search(pattern , text2))

matchObj = re.search(pattern , text2)
print(matchObj.group())
print(matchObj.start())
print(matchObj.end())
print(matchObj.span())

# findall 함수
# 문자열에서 패턴과 매칭되는 부분을 문자열 리스트로 반환함
# ^ : ~ 로 시작하는 || $ : ~ 로 끝나는 || \b : 경계가 있는
email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b"
phone_pattern = r"\b\d{2,3}-\d{3,4}-\d{4}\b"

text3 = """
    홍길동 phone : 010-0000-0000 email : test1@nate.com
    임꺽정 phone : 010-0000-0001 email : test2@naver.com
    장길산 phone : 010-0000-0002 email : test3@gmail.com
"""

print("전화번호 추출하기")
match_object = re.findall(phone_pattern , text3)
print(match_object)

print("이메일 추출하기")
match_object = re.findall(email_pattern , text3)
print(match_object)

# finditer 함수
# findall 과는 달리 문자열 , 리스트가 아니라 매칭 객체를 반환함
match_object = re.finditer(email_pattern , text3)
for obj in match_object :
    print(obj)
    
# sub 함수
# 문자열에 패턴과 매칭되는 부분에 대해 매칭 객체를 리스트로 반환함
# 특정한 패턴과 일치하는 문자열만 추출할 때 사용함
text = "I like stars, red star , yellow star"
pattern = "star"

replace_text = re.sub(pattern , "moon" , text)
print(replace_text)

replace_text2 = re.sub(pattern , "moon" , text , count = 2)
print(replace_text2)

# 패턴 표현 예제
pattern = r"^abc"
text = [ "abc" , "abcd" , "abc15" , "dabc" , "" , "s" ]

repattern = re.compile(pattern)

for item in text :
    result = repattern.search(item)
    if result :
        print(item , "- O")
    else :
        print(item , "- X")

# 문제 1. 사업자 번호 패턴을 추출하고 그 중 개인 사업자의 번호만 추출하기
contents = """
    우리커피숍 : 100-90-12345
    영풍문고   : 101-91-12121
    영미청과   : 102-92-23451
    황금코인   : 103-89-13579
    우리문구   : 104-91-24689
    옆집회사   : 105-82-12345
"""

pattern = r"(\d{3})-(\d{2})-(\d{5})"
result = re.findall(pattern , contents)

for item in result :
    if int(item[1]) >= 90 and int(item[1]) <= 99 :
        print(item)