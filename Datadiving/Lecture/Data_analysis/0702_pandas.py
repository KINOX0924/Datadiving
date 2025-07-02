import pandas as pd
import numpy  as np
"""
# 판다스 1
data = {
    "name"  : ["홍길동" , "임꺽정" , "장길산" , "홍경래" , "이상민" , "김수경"] ,
    "kor"   : [90 , 80 , 70 , 70 , 60 , 70] ,
    "eng"   : [80 , 70 , 60 , 50 , 77 , 56] ,
    "mat"   : [90 , 70 , 70 , 60 , 88 , 99]
}

data_frame = pd.DataFrame(data)
print(data_frame.head())        # 앞의 다섯명에 대한 데이터만 나옴
print(data_frame.head(10))      # 안에 숫자를 넣으면 넣은 숫자만큼 확인 가능

# 지정한 열만 출력하고 싶을 때
print(data_frame["name"])
print(data_frame["kor"])
print(data_frame["eng"])

# 조회 작업은 주로 iloc 또는 loc 로 하는 것이 좋음
# [: , "name" : "eng"] [행 전체 , "name" 부터 "eng" 까지 출력]
print(data_frame.loc[: , "name" : "eng"])

# 건너 뛰면서 출력
print(data_frame.loc[: , ["name" , "eng" , "mat"]])

# 양쪽 모두 슬라이싱 가능
print(data_frame.loc[[1,3,5] , ["name" , "kor"]])

# iloc : 인덱스를 사용하여 접근 가능
print(data_frame.iloc[[1,3,5] , [0,2]])

# 주로 분석하다가 부분집합을 가져와서 상세히 봐야할 때
data_frame2 = data_frame.loc[[0,2,4] , ["name" , "eng" , "mat"]]
print(data_frame2)  # 인덱스는 유지된 상태

data_frame2 = data_frame2.reset_index()
print(data_frame2)
"""

"""
# 판다스 2
# 시리즈 벡터 연산 : 인덱스가 다르더라도 자동으로 키 값으로 정렬하여 연산됨

data1 = {"kor" : 90 , "eng" : 70 , "mat" : 80}
data2 = {"kor" : 90 , "eng" : 70 , "mat" : 80}
data3 = {"mat" : 90 , "kor" : 70 , "eng" : 80}
# data4 = {"eng" : 90 , "mat" : 70 , "kor" : 80}
data4 = {"eng" : 90 , "mat" : 70 }  # 키가 없으면 NaN 으로 받아들이게 되고 , NaN 에는 연산이 불가능함

series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)
series4 = pd.Series(data4)

# NaN 값이 있는 경우  "+" 를 사용할 수 없기에 add 를 사용하여 NaN 값에 채워줄 값을 정해주어야 함
#result1 = series1 + series2 + series3 + series4
result1 = series1.add(series2 , fill_value = 0).add(series3 , fill_value = 0).add(series4 , fill_value = 0)
result2 = result1 / 4

print(f"총점 : {result1}")
print(f"평균 : {result2}")
"""

"""
# 판다스 3

data1 = {"kor" : 90 , "eng" : 70 , "mat" : 80}
data2 = {"kor" : 90 , "eng" : 70 , "mat" : 80}
data3 = {"mat" : 90 , "kor" : 70 , "eng" : 80}
data4 = {"eng" : 90 , "mat" : 70 , "kor" : 80}


# 판다스 2.0 이후에 append 함수가 사라짐 , 아래의 ._append 함수는 너무 옛날 거라 사용하지 않음
# data_frame = pd.DataFrame()
# data_frame = data_frame._append(data1 , ignore_index = True)
# print(data_frame)


# 따라서 데이터 프레임에 데이터를 추가하기 위해서는 DataFrame 에 먼저 열을 추가하고 , loc 를 사용해서 추가가 필요함
data_frame = pd.DataFrame(columns = ["kor" , "eng" , "mat"])
data_frame.loc[len(data_frame)] = data1
data_frame.loc[len(data_frame)] = data2
data_frame.loc[len(data_frame)] = data3
print(data_frame)

# 여러 개의 데이터 프레임을 합치기
data_frame = pd.concat([
    pd.DataFrame([data1]) ,
    pd.DataFrame([data2]) ,
    pd.DataFrame([data3])
] , ignore_index = True)

print(data_frame)

data_frame["total"] = data_frame["kor"] + data_frame["eng"] + data_frame["mat"]
data_frame["avg"]   = data_frame["total"] / 3
print(data_frame)

# 문제 1. 데이터 추가하기
data = {
    "fruits" : ["망고" , "딸기" , "수박" , "파인애플"] ,
    "price"  : [2500 , 5000 , 10000 , 7000] ,
    "count"  : [5 , 2 , 2 , 4]
}

data_frame2 = pd.DataFrame(data)
data_frame2.loc[len(data_frame2)] = {"fruits" : "사과" , "price" : 3500 , "count" : 10}
print(data_frame2)

# 데이터 삭제하기
# axis = 0 : 행 , axis = 1 : 열
# 열단위 삭제 (drop)
data_frame3 = data_frame2.drop("price" , axis = 1)
print(data_frame3)

data_frame4 = data_frame2.drop(0 , axis = 0)
print(data_frame4)

# 문제 2. 테이블 데이터 만들고 추가 및 새로운 total 필드 적용
data_frame = pd.DataFrame(columns = ["X1" , "X2" , "X3" , "X4"])
data_frame.loc[len(data_frame)] = {"X1" : 2.9 , "X2" : 9.2 , "X3" : 13.2 , "X4" : 2}
data_frame.loc[len(data_frame)] = {"X1" : 2.4 , "X2" : 8.7 , "X3" : 11.5 , "X4" : 3}
data_frame.loc[len(data_frame)] = {"X1" : 2   , "X2" : 7.2 , "X3" : 10.8 , "X4" : 4}
data_frame.loc[len(data_frame)] = {"X1" : 2.3 , "X2" : 8.5 , "X3" : 12.3 , "X4" : 2}
data_frame.loc[len(data_frame)] = {"X1" : 3.2 , "X2" : 9.6 , "X3" : 12.6 , "X4" : 3}
print(data_frame)

data_frame.loc[len(data_frame)] = {"X1" : 10 , "X2" : 20 , "X3" : 30 , "X4" : 40}
print(data_frame)

data_frame["total"] = data_frame["X1"] + data_frame["X2"] + data_frame["X3"] + data_frame["X4"]
print(data_frame)
"""

"""
# 판다스 4

# 외부 파일 읽고 쓰기
# 파일을 읽을 때 데이터 프레임으로 만들면 자동으로 인덱스가 부여됨
data_frame = pd.read_csv("./data/score.csv")
print(data_frame.head())

# 열 확인
print("컬럼명 : " , data_frame.columns)
print("인덱스 : " , data_frame.index)

# 키 값에 하이픈(-) 이 들어가는 경우 이렇게 사용할 수 없음
data_frame["total"] = data_frame.kor + data_frame.eng + data_frame.mat
data_frame["avg"]   = data_frame.total // 3
print(data_frame)

data_frame.to_csv("score_result1.csv" , mode = "w") # 인덱스를 자동으로 추가됨 , 한글 깨짐
data_frame.to_csv("score_result2.csv" , mode = "w" , index = False , encoding = "utf-8-sig")
"""

"""
# 판다스 5 - DataFrame API
# 데이터를 분석하기 위한 API
data_frame = pd.read_csv("./data/auto-mpg.csv")
print(data_frame.head())
print(data_frame.tail())

row , column = data_frame.shape
print("데이터 전체 개수 : " , row , column)

# 데이터 정보 요약 확인
print(data_frame.info())

# 통계량 - 기초통계학 중요 : 평균 , 개수 , 표쥰편차(std) , 최소값 , 최대값 , 중간값(2/4) , 1/4 분위수
print(data_frame.describe())

data_frame2 = pd.read_csv("./data/iris.csv")
print(data_frame2.head())

print(data_frame2.info())
print(data_frame2.describe())

# 데이터에 조건 부여하기
# data[조건식] : 조건식이 True 인 데이터셋만 가져옴
print(data_frame["cylinders"] == 8)
data_frame3 = data_frame[ data_frame["cylinders"] == 8 ]
print(data_frame.shape)
print(data_frame3.shape)

print(data_frame3.head())
print(data_frame3["cylinders"].value_counts())

# 카테고리 타입 : 평균이나 표준값 따위가 의미가 없는 데이터 타입
# 예:)) 엔진의 실린더의 개수
# value_counts() - 분할표
print(data_frame["cylinders"].value_counts())


# 모델 발표 연도가 70 이고 , 연비가 25 이상
# 판다스에는 별도의 and , or 연산자가 없으나 비트연산자로 사용할 수 있음 ( | = or , & = and)
data_frame4 = data_frame[np.logical_and( data_frame["model-year"] == 70 , data_frame["mpg"] >= 25)]
print(data_frame4)
print(data_frame4.shape[0])

# 문제 1. 80년대에 나온 제품들을 모델과 개수로 나타내기
df1 = data_frame[ data_frame["model-year"] == 80 ]
print(df1["model-year"].value_counts())

# 문제 2. 73 , 78 , 76 년에 나온 제품만 모두 출력하기
df2 = data_frame[np.logical_or( data_frame["model-year"] == 73 , data_frame["model-year"] == 78 , data_frame["model-year"] == 76 )]
print(df2)

# 문제 3. 80 년대에 출시한 제품들 중에서 연비가 25 이상인 제품의 정보만 출력하기
df3 = data_frame[np.logical_and( data_frame["model-year"] >= 80 , data_frame["model-year"] <= 89 )]
df3 = df3[df3["mpg"] >= 25]
print(df3)

# 문제 4. 70 년대에 출시된 모델 중에서 실린더가 4개인 제품의 정보만 출력하기
df4 = data_frame[np.logical_and( data_frame["model-year"] >= 70 , data_frame["model-year"] <= 79 )]
df4 = df4[df4["cylinders"] == 4]
print(df4)

# 문제 5. 80 년대에 출시된 모델들은 실린더 개수와 제품개수로 출력하기
df5 = data_frame[np.logical_and( data_frame["model-year"] >= 80 , data_frame["model-year"] <= 89 )]
print(df5["cylinders"].value_counts())
"""

"""
# 판다스 6
# 분석
# 분석에서 데이터는 분석 방법에 따라 크게 두 종류가 있음
# 연속형 데이터 : 평균 값이 중요함 => 회귀분석
# 비연속형 데이터(범주형) : 평균 값이 아니라 발생 빈도수가 중요 => 분류분석 , 로지스틱 회귀 , 랜덤포레스트

data = pd.read_csv("./data/auto-mpg.csv")
print(data)

# 평균 , 최대 , 최소
print("연비 평균 : " , data["mpg"].mean())
print("연비 최대 : " , data["mpg"].max())
print("연비 최소 : " , data["mpg"].min())

data2 = pd.read_csv("./data/iris.csv")
# 문제 1. iris 데이터셋에 몇 개의 필드가 있고 각 필드의 타입이 무엇인지 확인
print(data2.info())

# 문제 2. 맨 앞의 데이터를 7개만 출력
print(data2.head(7))

# 문제 3. iris 데이터셋의 통계량을 확인(평균 , 표준편차 , 중값값 , 사분위수)
print(data2.describe())

# 문제 4. variety 가 Setosa 인 데이터의 통계량을 출력
df_setosa = data2[data2["variety"] == "Setosa"]
print(df_setosa.describe())

# 문제 5. Setosa , Virginica , Versicolor 의 sepal.length 값의 평균값을 출력
df_virginica = data2[data2["variety"] == "Virginica"]
df_versicolor = data2[data2["variety"] == "Versicolor"]

print(df_setosa["sepal.length"].mean())
print(df_virginica["sepal.length"].mean())
print(df_versicolor["sepal.length"].mean())

# 문제 6. 꽃의 종류가 Setosa 이면서 sepal.length 길이가 5cm 이상인 것의 개수를 출력
df_setosa_five = df_setosa[df_setosa["sepal.length"] >= 5]
print(df_setosa_five["sepal.length"].value_counts())
"""

# 판다스 7
# NaN 확인

s1 = pd.Series([1,2,3,4,np.nan])    # 파일에 NaN 값이 있는 경우는 상관없는데 프로그램에서 직접 NaN 을 넣어주기 위해서는 np.nan 으로 넣어줌

print(s1.isnull())          # [False , False , False , False , True]
print(s1.isnull().sum())    # False 는 0 이고 True 는 1 이니깐 .sum() 을 사용하면 NaN 의 개수를 세는 것

# dropna 함수
data = pd.read_csv("./data/data.csv")
print(data.shape)
print(data.info())
print(data.describe())

print(data["height"].value_counts())
print(data["height"].value_counts(dropna = False))

print(data.isnull().sum())

# 결측지가 발생하면 행이나 열을 삭제시키거나 평균값이나 중간값으로 대체함
# 하지만 만약 표준 편차가 크면 평균값보다 중간값으로 대체하는 것이 좋음

data2 = data.dropna( how = "any" , axis = 0) # 행중에 NaN 값이 있으면 행 전체를 삭세
print(data2.shape)

data2 = data.dropna( how = "any" , axis = 1) # 열중에 NaN 값이 있으면 삭제
print(data2.shape)

# thresh 옵션
# 최소한의 실효성 있는 데이터의 개수를 유지
data2 = data.dropna( thresh = 28 , axis = 1 ) # 데이터 개수가 27 개인 열은 삭제됨
print(data2.shape)
print(data2.head())

data = pd.read_csv("./data/auto-mpg.csv")
print(data.info())

print(data["horsepower"].isnull().sum())
data = data.dropna(how = "any" , axis = 0)
print(data.info())