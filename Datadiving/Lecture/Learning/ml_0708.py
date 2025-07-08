"""
# diavetes = 당뇨병과 관련된 요소들이 있음 , 1년 뒤에 값들을 예측해야 함
# 알고리즘 중에 Knn 이웃 , 의사결정 트리 , 랜덤포레스트 등... 분류 뿐만 아니라 회귀도 지원함

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor , GradientBoostingRegressor
from sklearn.linear_model import LinearRegression , Ridge , Lasso
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

data = load_diabetes()
print(data["target"])
print(data["data"])
print(data["DESCR"])
# bunch 라는 클래스여서 자료 정리가 잘되어 있음
# 즉 이상치 , 누락치 , 결측치까지 다 정리가 되어 있는 데이터 파일
# 이상치 , 누락치 , 결측치를 정리하는 것은 pandas , numpy 의 역할

# 데이터 저장
X = data["data"]
y = data["target"]

# 데이터 쪼개기
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234)
print(X_train.shape)
print(y_train.shape)

# 선형 모델
model = LinearRegression()
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
# 선형회귀모델의 경우 score 함수를 썼을 때 결정 계수라는 것이 있음
# 결정 계수가 1 이면 완벽하게 예측을 한 것이고 , 0 이면 거의 예측 불가 , 음수일 경우 심각하게 역으로 가고 있는 것

print("===== 선형 모델 =====")
print("훈련세트 평가 : " , model.score(X_train , y_train))
print("테스트세트 평가 : " , model.score(X_test , y_test))

# 리지 모델
model = Ridge(alpha = 0.1)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 리지 모델 =====")
print("훈련세트 평가 : " , model.score(X_train , y_train))
print("테스트세트 평가 : " , model.score(X_test , y_test))

# 랏쏘
model = Lasso(alpha = 0.1)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 랏쏘 모델 =====")
print("훈련세트 평가 : " , model.score(X_train , y_train))
print("테스트세트 평가 : " , model.score(X_test , y_test))

# 의사결정트리
model = DecisionTreeRegressor()
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 의사결정트리 =====")
print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))
print("특성 중요도 : " , model.feature_importances_)

# 랜덤포레스트
model = RandomForestRegressor(random_state = 0 , max_depth = 3 , n_estimators = 300)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 랜덤포레스트 =====")
print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))

# 7월 8일은 여기서부터 정리 시작 -------
# 그라디언트 부스트 (앙상블계열)
# 약한 학습기들을 통해서 학습을 하고 보정작업을 거쳐서 결과를 찾아냄
# learning_rate : 머신러닝이 학습하는 속도를 조절함 , 너무 높으면 최적 위치를 못 찾을 수 있고 ,
# 너무 낮으면 아무 천천히 느리게 학습을 진행하고 아무리 가도 최저점에 못 도달할 수도 있음
# GridSearch : 하이퍼파라미터를 주면 알아서 테스트를 하면서 적절한 파라미터를 찾아냄(엄청 오래 걸림)

# 그라디언트 부스트의 종류
# 사이킷런 그라디언트 부스트
# xgboost 그라디언트 부스트     conda install xgboost
# LightGBM 그라디언트 부스트    conda install LightGBM : 실행 안될 시 Microsoft Visual C++ Build tools 설치 필요
model = GradientBoostingRegressor(random_state = 0 , max_depth = 3 , n_estimators = 10 , learning_rate = 0.1)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 그라디언트 부스트 =====")
print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))

# xgboost 그라디언트 부스트
model = XGBRegressor(random_state = 0 , max_depth = 3 , n_estimators = 10 , learning_rate = 0.1)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== xgboost 그라디언트 부스트 =====")
print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))
"""

"""
# 보스턴 집값 데이터 가져오기(fetch)
# fetch 로 되는 함수들은 데이터 용량이 너무 커서 별도의 다운을 요구하는 함수
from sklearn.datasets import fetch_openml
boston_data = fetch_openml("boston" , version = 1)

print(type(boston_data))
print(boston_data.keys())

X = boston_data["data"]
y = boston_data["target"]

print(X.shape)
print(y.shape)
"""



# *** 이미지 분류 ***
# sklearn 에서 load_digits() -> 손으로 쓴 숫자(미국의 우편번호 나누기 때 수집된 데이터)
# 이미지 => 디지털화 하는 과정에서 흑백은 2차원 배열이고 , 컬러는 3차원 배열
# 따라서 이미지가 10장이 있고 각 이미지 크기가 150 x 150 이라고 한다면 150 x 150 이 특성의 개수가 됨

# 이미지를 읽어서 numpy 배열로 바꾸어야 함 => 파이썬의 PIL 라이브러리로 제공됨

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor , GradientBoostingRegressor
import numpy as np

# [1] 데이터 준비
data = load_digits()
X = data["data"]
y = data["target"]

print(X.shape)
print(X[:10])

# 이미지 출력 확인
print(data.images[:10])
images = data.images

# 이미지 출력 함수
def drawNumbers() :
    """
    # 이미지 한개 출력
    plt.figure(figsize = (10,4))            # figsize : 차트의 크기
    plt.imshow(images[0] , cmap = "gray_r") # cmap : 팔레트(gray_r : 회색으로 표현)
    plt.show()
    """

    # 이미지 여러개 출력 (화면 분할 필요)
    plt.figure(figsize = (10 , 4))  # 차트의 전체 크기를 지정하고 나서 작게 나누려면 subplot 함수를 사용함

    # 2 , 5 로 쪼개면 10 개의 화면이 만들어지고 각 분할 위치에 번호가 붙음
    # 1 , 2 , 3 , 4 , 5
    # 6 , 7 , 8 , 9 , 10
    for i in range(10) :
        plt.subplot(2 , 5 , i + 1) # 내가 내보낼 위치 지정
        # interpolation : 이미지 보간법
        plt.imshow(images[i] , cmap = "gray_r" , interpolation = "nearest")
        plt.title(f"Label : {y[i]}")
        plt.axis("off") # 축 없애기
        
    # 레이아웃을 이쁘게 다시 정리하라는 코드
    plt.tight_layout()
    plt.suptitle("첫 10개 Digits 이미지" , y = 1.00 , fontsize = 16)
    # y 는 제목이 출력될 위치를 말하는데 0 에 가까울수록 아래로 , 1.05 는 영역 바깥쪽에 놓으라는 의미
    plt.show()
    
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1 , test_size = 0.3)
model = LogisticRegression(solver = "liblinear" , multi_class = "auto" , max_iter = 5000 , random_state = 0)
# solver = 모델 계수를 찾아가는 방법 , 보통 데이터셋이 적을 때는 liblinear 을 사용
# multi_class = "auto" : 다중 분류일 때 사용
# max_iter = 5000 : 계수를 찾아갈때 학습을 얼마나 반복할지를 정하는 것
model.fit(X_train , y_train)

print("===== 로지스틱회귀 분석 =====")
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))

# Knn 이웃 알고리즘
model = KNeighborsRegressor(n_neighbors = 3)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== Knn 이웃 알고리즘 =====")
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))

# 의사결정트리
model = DecisionTreeRegressor(random_state = 1)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 의사결정트리 =====")
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))

# 랜덤포레스트
model = RandomForestRegressor(random_state = 0 , max_depth = 3 , n_estimators = 100)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 랜덤포레스트 =====")
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))

# 그라디언트부스팅
model = GradientBoostingRegressor(random_state = 0 , max_depth = 5 , n_estimators = 100 , learning_rate = 0.1)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("===== 그라디언트부스팅 =====")
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))