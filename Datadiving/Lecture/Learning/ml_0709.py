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
print("테스트 테슽 : " , model.score(X_test , y_test))