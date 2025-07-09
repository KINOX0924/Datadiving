"""
# iris 파일
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

# 데이터 불러오기 (csv)
df = pd.read_csv("./csv_data/iris.csv")

print(df.head())
print(df.columns)
print(df.describe())
print(df.info())

# 데이터 쪼개기
X = df.iloc[: , :4]  # 전체행 , 0 ~ 3번 열 까지만
y = df.iloc[: , 4]    # 4번 열만 가져옴

print(X[:4])
print(y[:4])

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 0)
print(X_train)
print(y_train)

# 데이터 절차
# 결측치제거 
# 이상치 제거
# 스케일링(정규화 , 표준화)
# 서포트 벡터 머신 , 딥러닝

model = LogisticRegression()
model.fit(X_train , y_train)
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))
"""

"""
# penguins 파일
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# [1] 데이터 불러오기
data = pd.read_csv("./csv_data/penguins.csv")

print(data.head())
print(data.info())
print(data.describe())

# 라벨 인코딩
# 연산이 불가한 작업을 연산이 가능하게 하는 것
data.loc[data["island"] == "Torgersen" , "island"] = 1
data.loc[data["island"] == "Dream" , "island"] = 2
data.loc[data["island"] == "Biscoe" , "island"] = 3

# 성별
data.loc[data["sex"] == "male" , "sex"] = 1
data.loc[data["sex"] == "female" , "sex"] = 2

# [2] 결측치 처리하기
# 대부분의 결측치는 제거보다는 다른값으로 대체하는 것이 좋음
print(data.isnull().sum())
mean_bill_length_mm    = data["bill_length_mm"].mean()
mean_bill_depth_mm     = data["bill_depth_mm"].mean()
mean_flipper_length_mm = data["flipper_length_mm"].mean()
mean_body_mass_g       = data["body_mass_g"].mean()

data["bill_length_mm"].fillna(mean_bill_length_mm , inplace = True)
data["bill_depth_mm"].fillna(mean_bill_depth_mm , inplace = True)
data["flipper_length_mm"].fillna(mean_flipper_length_mm , inplace = True)
data["body_mass_g"].fillna(mean_body_mass_g , inplace = True)

data = data.dropna(how = "any" , axis = 0)

print(data.isnull().sum())

# [3] 데이터 쪼개기
X = data.iloc[: , 2:]
y = data.iloc[: , 1]
print(X.head())
print(y.head())

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1 , test_size = 0.3)
print(X_train.shape)
print(y_train.shape)

model = LogisticRegression()
model.fit(X_train , y_train)

print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
"""

"""
# Diamond 파일
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# [1] 데이터 불러오기
data = pd.read_csv("./csv_data/diamond.csv")

print(data.head())
print(data.info())
print(data.describe())

# [2] 라벨 인코딩
# value_count()
print(data["Clarity"].value_counts())
print(data["Clarity"].unique())

# Color 라벨링
for index , color in enumerate(data["Color"].unique()) :
    data.loc[data["Color"] == color , "Color"] = index + 1
    
# Clartiy 라벨링
for index , clartiy in enumerate(data["Clarity"].unique()) :
    data.loc[data["Clarity"] == clartiy , "Clarity"] = index + 1

# Polish 라벨링
for index , polish in enumerate(data["Polish"].unique()) :
    data.loc[data["Polish"] == polish , "Polish"] = index + 1
    
# Symmetry 라벨링
for index , symmetry in enumerate(data["Symmetry"].unique()) :
    data.loc[data["Symmetry"] == symmetry , "Symmetry"] = index + 1
    
# Report 라벨링
for index , report in enumerate(data["Report"].unique()) :
    data.loc[data["Report"] == report , "Report"] = index + 1

# [3] 결측치 처리하기
print(data.isnull().sum())  # 현재 결측치 없음

# [4] 데이터 쪼개기
X_1 = data.iloc[: , 0]
X_2 = data.iloc[: , 2:]

X = pd.concat([X_1 , X_2] , axis = 1)
print(X.head())

y = data.iloc[: , 1]
print(y.head())

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1 , test_size = 0.3)
print(X_train.shape)
print(y_train.shape)

model = LogisticRegression()
model.fit(X_train , y_train)

print("훈련세트 : " , model.score(X_train , y_train))
print("테스트 테스트 : " , model.score(X_test , y_test))
"""

"""
# 이상치 - 통계는 확률 , 특이한 값들
# 일반적인 특정값의 범위를 벗어나는 값들을 이상치라고 함

# boxplot - 이상치를 시각적으로 확인
# 최소값 , 최대값 , 4분위수(25% , 50% , 75%)
# 아래/위에 동그라미가 있으면 이상치가 있다는 것

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.Series([1 , 2 , np.nan , 4 , 5 , 6 , np.nan , 8 , 9 , 10])
a [a.isna()] = 100

# boxplot 그리기
# 보고서에 요소들의 박스플롯 중요함
# 데이터 분포도 등을 확인할 때 중요함
plt.figure(figsize = (8,6))
plt.boxplot(a , vert = True)    # vert : 방향을 나타내며 True 는 수직 , False 는 수평
plt.show()

# 이상치 상한과 하한을 찾는 공식
# 하한은 1/4 분위수(Q1) - 1.5 * (Q3 - Q1) 이것보다 작으면 이상치
# 하한은 1/4 분위수(Q3) + 1.5 * (Q3 - Q1) 이것보다 크면 이상치
def outfliers_iqr(data) :
    q1 , q3 = np.percentile(data , [25 , 75])
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return lower_bound , upper_bound

lower_bound , upper_bound = outfliers_iqr(a)
print("하한 : " , lower_bound)
print("상한 : " , upper_bound)

a [a<lower_bound] = lower_bound
a [a>upper_bound] = upper_bound

plt.boxplot(a , vert = True)    # vert : 방향을 나타내며 True 는 수직 , False 는 수평
plt.show()

# boxplot 의 사각형 그림이 가운데쯤 있으면 대칭형 정규분포를 의미
# 위로 올라가면 Q3 에 치우치는(오른쪽으로 쏠린) 그래포
# 아래로 내려가면 Q1 에 치우치틑(왼쪽으로 쏠린) 그래프
"""
"""
# 지도 학습 , 비지도 학습 , 강화 학습
# 강화 학습 - 게임 , 알파고 등 (채찍과 당근)

# 지도 학습(출력 결과를 알고 있을 때)

# 비지도 학습(출력 결과를 알 수 없음)
# - 결과를 모르고 라벨링이 없는 학습 , 반드시 그렇지는 않지만 대체 뭘 분석해야 할 지 모르고 결과도 예측하기 어려움
# - 그래서 지도 학습 전 단계에서 데이터 분석용으로 많이 사용함
# 스케일링( 4가지 , standardScalar , RobustScalar , MinMaxScalar , Mormalize)
# 차원축소 :
# 고차원데이터(특성이 아주 많은 경우 , 사진 , 3차원 => 1차원) 시간도 많이 걸리고 ,
# 사진처럼 정밀하게 그리는 경우와 캐리커처(특징만 가지로 그리는 그림) 을 그렸을 때는 캐리커처가 더 빠르다
# 때로는 차원축소로 할 때 성과가 더 좋은 경우도 있다.
# 주 성분 분석 :
# 분산을 가지고 분산이 큰 거로 주 성분을 찾아냄
# 암환자 데이터의 경우 특성이 많을 경우 유용함
# 연관성 분석 (장바구니 분석) :
# 월마트의 기저귀하고 맥주가 같은 장바구니에 많이 들어갈 줄 모르고 한 분석
# 숫자로 다 바꾸고 -> 벡터로 다 바꾸고 , 숫자로 바꾸기만 하면 연산이 가능

import pandas as pd

data = {
    "feature1" : [160 , 165 , 170 , 175 , 180 , 155 , 190 , 172 , 168 , 178] ,
    "feature2" : [3000 , 3200 , 3500 , 4900 , 4800 , 6000 , 2800 , 3300 , 5600 , 4700] ,
    "feature3" : [3 , 2 , 1 , 4 , 4 , 6 , 12 , 13 , 11 , 6]
}

data_frame = pd.DataFrame(data)
print(data_frame)

from sklearn.preprocessing import StandardScaler , RobustScaler , MinMaxScaler , Normalizer , MaxAbsScaler

# StandardScalar : 데이터가 정규분포를 따른다고 가정할 때 많이 사용함
# 모델 특성이 스케일링에 민감할 때도 많이 사용
# 서포트벡터머신 , 로지스틱 , 딥러닝일 때 유용함. 이상치에 매우 많이 민감함
ss = StandardScaler() 
data_frame_scaled = ss.fit_transform(data_frame)
print(data_frame_scaled)

# RobustScaler : 데이터에 이상치가 많으면 StandardScalar 대신 사용할 수 있음
ss = RobustScaler()
data_frame_scaled = ss.fit_transform(data_frame)
print(data_frame_scaled)

# MinMaxScaler : 특성값의 범위가 명확히 0 ~ 1 사이에 와야할 때(이미지 , 특정신경망)
ss = MinMaxScaler()
data_frame_scaled = ss.fit_transform(data_frame)
print(data_frame_scaled)

# Normalizer : 주로 텍스트 분석 , 군집 분석(클러스터링)에 유용함
ss = Normalizer()
data_frame_scaled = ss.fit_transform(data_frame)
print(data_frame_scaled)


# 서포트 벡터 머신
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

cancer = load_breast_cancer()
print(cancer.keys())

X = cancer["data"]
y = cancer["target"]



X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1)
model = SVC()   # 스케일링을 하지 않은 서포트 벡터 머신
model.fit(X_train , y_train)
print("스케일링을 하지 않은 서포트 벡터 머신")
print("학습 세트" , model.score(X_train , y_train))
print("테스트 세트" , model.score(X_test , y_test))

model = LogisticRegression()    # 로지스틱 알고리즘
model.fit(X_train , y_train)
print("스케일링을 하지 않은 로지스틱 알고리즘")
print("학습 세트" , model.score(X_train , y_train))
print("테스트 세트" , model.score(X_test , y_test))


# 스케일링 진행
ss = StandardScaler()
X_scaled = ss.fit_transform(X)
print(X_scaled)

X_train_scale , X_test_scale , y_train_scale , y_test_scale = train_test_split(X_scaled , y , random_state = 1)
model = SVC()   # 스케일링을 한 서포트 벡터 머신
model.fit(X_train_scale , y_train_scale)
print("스케일링 서포트 벡터 머신")
print("학습 세트" , model.score(X_train_scale , y_train_scale))
print("테스트 세트" , model.score(X_test_scale , y_test_scale))

model = LogisticRegression()    # 스케일링을 한 로지스틱 알고리즘
model.fit(X_train_scale , y_train_scale)
print("스케일링 로지스틱 알고리즘")
print("학습 세트" , model.score(X_train_scale , y_train_scale))
print("테스트 세트" , model.score(X_test_scale , y_test_scale))
"""

# 타이타닉 데이터
# 결측치 처리
# 이상값 처리
# 스케일링 진행
# 알고리즘 학습 및 평가

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# [1] 데이터 불러오기
data = pd.read_csv("./csv_data/train_and_test2.csv")

print(data.head())
print(data.info())
print(data.describe())


# [2] 결측치 처리
print(data.isnull().sum())
mean_embarked = data["Embarked"].mean()

data["Embarked"].fillna(mean_embarked , inplace = True)

print(data.isnull().sum())
y = data["survived"]
X = data.iloc[: , :6]

# [3] 이상치 처리
def outfliers_iqr(data) :
    q1 , q3 = np.percentile(data , [25 , 75])
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return lower_bound , upper_bound

lower_bound , upper_bound = outfliers_iqr(X)
print(lower_bound)
print(upper_bound)

X [ X < lower_bound ] = lower_bound
X [ X > upper_bound ] = upper_bound

# [4] 스케일링 진행
ss = StandardScaler()
X_scaled = ss.fit_transform(X)

# [5] 데이터 쪼개기
X_train , X_test , y_train , y_test = train_test_split(X_scaled , y , random_state = 1)

# [6] 알고리즘 선택 및 학습 , 평가 진행
model = SVC()
model.fit(X_train , y_train)

print("학습 세트 : " , model.score(X_train , y_train))
print("테스트 세트 : " , model.score(X_test , y_test))