# 데이터 분류

# 절차
# [1] 데이터 준비 ( 이 과정이 약 80% 에 해당함 )
"""
- 데이터 수집
- 결측치 처리
- 이상치 처리
- 정규화
- 주성분 분석
- 차원축소
- 카테고리화
- 원핫인코딩
- 기타 작업
"""
# [2] 데이터셋을 두 개로 나눔 , '훈련셋' 과 '테스트셋' 으로 나눔
# *전부 다 학습을 시키면 과대적합인지 , 과소적합인지 미래 예측력이 있는 지 알 수 없음
# 따라서 6:4 , 7:3 , 8:2 정도로 나누어서 테스트가 가능하도록 , 훈련셋에만 맞추어지면 안됨
# [3] 알고리즘 선택(Knn 이웃 알고리즘 , 분류에서 가장 심플한 알고리즘) 을 선택
# 분류 알고리즘 : 로지스틱 회귀 분석 , 서포트벡터머신 , 의사결정 트리 , 랜덤포레스트 , 그라디언트부스팅 등등등
# 을 선택하여 학습을 진행 , 각 알고리즘마다 성능(학습을 좀 더 잘하게) 을 올릴수 있는 하이퍼 파라미터가 있는데 이걸 찾아내는 과정이 필요함
# [4] 예측 진행
# [5] 성능 평가를 함

# 필요 라이브러리
# conda install numpy scipy scikit-learn matplotlib ipython pandas imageio pillow graphviz python-graphviz

"""
# [1] 데이터 준비
from sklearn.datasets import load_iris  # iris 데이터셋을 가져옴
data = load_iris()  # Bunch 라는 클래스 타입 데이터를 가져옴

# print(data.keys())
# print("타겟 이름 : " , data["target_names"])
# print("파일명 : " , data["filename"])
# print("데이터설명")
# print(data["DESCR"])


# [2] 데이터 분류
# X 에는 데이터를 가져오고 , 소문자 y 에는 데이터의 타겟을 가져옴
X = data["data"]    # ndarray 2차원 배열
y = data["target"]  # ndarray 1차원 배열
# print(X[:10])
# print(y)

# 데이터를 랜덤하게 섞어서 여기서 70% 를 추출함
# 아래 사이킷런 모델 셀렉션의 traing_test_split 가 데이터를 랜덤하게 섞어서 나누어주는 역할을 함
from sklearn.model_selection import train_test_split

# 튜플로 반환되며 , random_state 인자가 시드(Seed) 역할을 하고 , 계속 같은 데이터를 내보내고 싶으면 이 값을 고정하면 됨
# test_size 에 비율을 넣어주면 해당 비율대로 데이터를 나누며 특별한 지정이 없다면 0.25 정도로 나눔
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234 , test_size = 0.3)
print(X_train.shape)
print(X_test.shape)

# 데이터 전체를 확인하기 위해서, 산점행렬(특성이 4개면 각 특성대 특성으로만 그릴 수 있어서 차트 4 X 4 = 16개)
# 특성이 10개가 되면 10 X 10 = 100 개 차트가 만들어짐
# 따라서 특성이 낮을 때 주로 만들며 많으면 만들기 어려워짐
# scatter_matrix 차트가 직접 노가다로 그릴 수도 있고 , Dataframe 이 제공할 수도 있음 , 아니면 Seaborn 차트를 사용해야함
# numpy 배열을 데이터프레임 형식으로 환
import pandas as pd
iris_df = pd.DataFrame(X , columns = data["feature_names"]) # numpy 배열과 컬럼명으로 데이터프레임 생성

import matplotlib.pyplot as plt # 모든 차트는 matplotlib.pyplot 라이브러리가 필요함
# c              : 각 점의 색상을 지정 ( 0 , 1 , 2 ) 모두 다른색 지정
# figsize        : 차트의 크기를 설정하는 것으로 inch 단위
# marker         : 분포도에 찍히는 점의 모양을 설정
# hist_kwds = {} : # 대각선의 히스토그램의 구간 개수
# s              : 점의 크기
# alpha          : 투명도 , 1 이 불투명이고 0 으로 갈수록 투명함
pd.plotting.scatter_matrix( iris_df , c = y , figsize = (15 , 15) , marker = 'o' , hist_kwds = {"bins" : 20} , s = 60 , alpha = 0.8)
plt.show()

# Knn 이웃 알고리즘 (내 옆집에 누가 사는가?)
# 거기로 가장 가까운 거리에 누가 있는가를 판단하며 거리를 재는 방식을 선택할 수 있으나 주로 유클리드 기하학을 사용함
# 몇 명까지를 이웃으로 볼 것인지를 지정할 수 있으며 주로 홀수로 지정함
# 이 알고리즘은 회귀 , 분류 둘 다 가능
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 3)   # 이웃의 수를 3명으로 지정

# [3] 학습 시작
# 학습한 내용은 모델 자체가 지니고 있음
# 충분히 모델의 하이퍼 파라미터가 지정되어서 최대한의 학습효과를 얻었다고 생각하면 모델을 저장해놓고 다시 불러와서 재사용 가능
model.fit(X_train , y_train)

# [4] 예측하기
# 본래의 테스트셋인 y_test 와 비교
y_pred = model.predict(X_test)  # 테스트셋으로 예측한 데이터를 반환함

print(y_pred)
print(y_test)


# [5] 평가하기
# 모델 평가 시 주의사항
# 예측률이 높은 게 좋은 모델은 맞음
# 하지만 모델 자체는 우수하지만 암환자를 암환자가 아니라고 판단할 경우와
# 모델 자체는 성능이 조금 떨어지지만 암환자가 아닌 환자를 암환자라고 판단하는 경우 중에서는
# 후자가 더 사람에게는 더 좋은 모델이라고 할 수 있음
print("훈련셋 평가 : "  , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))

# 클래스 이름으로 출력
class_names = list(data["target_names"])
for i , j in zip(y_pred , y_test) :
    print("예측 : {:20s} 실제 : {:20s}".format(class_names[i] , class_names[j]))
"""
    
"""
# [1] 데이터 가져오기
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
print(data.keys())

print("타겟이름 : " , data["target_names"])
print("특성이름 : " , data["feature_names"])
print("파일명" , data["filename"])
print("데이터설명")
print(data["DESCR"])

# [2] 데이터 분류
X = data["data"]
y = data["target"]

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234 , test_size = 0.4)
print(X_train.shape)
print(X_test.shape)

import pandas as pd
breast_cancer_df = pd.DataFrame(X , columns = data["feature_names"]) 

from sklearn.neighbors import KNeighborsClassifier
# for 문으로 이웃의 개수를 증가시켜서 확인하도록 변경
# 적당한 하이퍼 파라미터를 고르는 것
# 이 때 이웃의 개수는 원 특성의 개수를 넘기면 안됨
n_neighors = 10
trainscoreList = list()
testscoreList = list()

for i in range(1 , n_neighors + 1) :
    model = KNeighborsClassifier(n_neighbors = i) # 이웃의 개수
    model.fit(X_train , y_train)
    score1 = model.score(X_train , y_train)
    score2 = model.score(X_test , y_test)
    trainscoreList.append(score1)
    testscoreList.append(score2)

import matplotlib.pyplot as plt
plt.plot(range(1 , len(trainscoreList) + 1) , trainscoreList , label = "train")
plt.plot(range(1 , len(testscoreList) + 1) , testscoreList , label = "test")
plt.show()

# model = KNeighborsClassifier(n_neighbors = 2)

# # [3] 학습하기
# model.fit(X_train , y_train)

# # [4] 예측하기
# y_pred = model.predict(X_test)

# print(y_pred)
# print(y_test)

# # [5] 평가하기
# print("훈련셋 평가 : "  , model.score(X_train , y_train))
# print("테스트셋 평가 : " , model.score(X_test , y_test))
"""

"""
# 윤년 머신러닝
# 입력 데이터 : [[1],[2],[3],[4],[5],[6],[7] ......]
# 출력 데이터 : [0,0,0,1,0,0,0,1 .......]

# [1] 데이터 생성(전처리까지)
# 1년부터 2025년까지 데이터 입력

# 먼저 윤년인지 아닌지를 데이터 라벨링하는 함수를 하나 생성
def isLeap(year) :
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
        return 1
    return 0

# 데이터(X) 와 라벨링값(y) 리스트를 생성
X = []
y = []

for i in range(1,2026) :
    X.append(i)
    y.append(isLeap(i))

print(X[2000:])
print(y[2000:])

# 머신러닝에서 X 는 반드시 ndarray(2D) , y 는 반드시 ndarray(1D)
# numpy array 로 변환
import numpy as np
# X 리스트를 ndarray 로 바꾸고 차원 하나를 추가하여 2D 형태로 변환함
X = np.array(X)
X = X.reshape(-1,1)
print(X.shape)

y = np.array(y)
print(y.shape)

# [2] 데이터 훈련셋과 테스트셋으로 구분
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1 , test_size = 0.3)

# [3] 알고리즘 모델 선택
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(X_train , y_train)

print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
"""

"""
# 선형 회귀분석
import numpy as np

# 특성(입력데이터) - 공부 시간
X = [20,19,17,18,12,14,10,9,16,6,5,10,20,8,15]

# 성적(출력데이터)
y = [100,100,90,90,60,70,40,70,40,30,100,30,10,70,60]

X = np.array(X)
y = np.array(y)

X = X.reshape(-1,1)
print(X.shape)
print(y.shape)

# 데이터 쪼개기
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train , y_train)
y_pred = model.predict(X_test)

print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
print("기울기 : " , model.coef_)
print("절편 : " , model.intercept_)

y_pred2 = X_test * model.coef_ + model.intercept_
print(y_test)
print(y_pred)
print(y_pred2)
# 다중 회귀 분석의 경우가중치가 많음
# 각 독립변수마다 별도의 가중치를 가져옴


# Knn 이웃 알고리즘 회귀알고리즘
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()

model.fit(X_train , y_train)
y_pred = model.predict(X_test)
print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
print(y_test)
print(y_pred)
"""

"""
# 더미 데이터 생성
import mglearn
X , y = mglearn.datasets.make_wave(n_samples = 30)

print(X[:10])
print(y[:10])
"""

"""
# 다중 회귀 분석
# 다중 회귀 분석은 공분산(특성 간에 서로 영향을 주고받는 것) 을 따져보고 필요 없는 특성은 제거해야함
# R 은 기본적으로 필요 없는 특성을 제거해주는 것이 있지만 파이썬은 없어서 사용자가 직접 제거해야함
# 보스톤 집값

url = "https://lib.stat.cmu.edu/datasets/boston"
import pandas as pd     # 다양한 유형의 데이터가 있을 때 처리 방법
import numpy as np

# 분리 문자가 공백이 아니고(\s+) , skiprows = 22 줄을 건너 뛰고 , header = 헤더가 없음)
data_frame = pd.read_csv(url , sep = "\s+" , skiprows = 22 , header = None)
print(data_frame.head(10))

# np 에는 hstack 함수가 있음 , 수평방향으로 배열을 이어붙이는 함수
# 짝수행에 홀수를 가져다 붙이면 됨
X = np.hstack([data_frame.values[::2 , : ] , data_frame.values[1::2 , :2]])
print(X.shape)

# 이 열이 target
# 행의 개수가 같아야 머신러닝 연산을 수행할 수 있음 , 결과가 입력한 데이터 개수만큼 있어야함
y = data_frame.values[1::2 , 2]
print(y.shape)

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(X_train , y_train)

print("LinearRegression")
print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
print("기울기들 :" , model.coef_)
print("절편 : " , model.intercept_)

# 선형회귀분석 : 다중공선성문제 , 여러 특성간에 서로 너무 밀접해서 필요없는 요소들을 고려하지 않음
# 특성의 개수가 많으면 많을수록 처리 능력이 떨어짐

# 라쏘
# 보스톤 데이터의 특성의 개수는 13개이고 가중치(기울기) 도 13개 나옴
# 가중치가 너무 크거나 작으면 훈련 데이터셋에 초점이 맞추어짐(과대적합)
# 따라서 가중치를 규제하는 알고리즘으로 라쏘는 가중치를 0 에 가깝게 하다가 불필요한 요소가 있으면 아예 0 으로 만들기도 함
# 따라서 모델을 심플하게 만듬(L2 정규화)
# 하이퍼 파라미터 alpha 라는 값이 있는데 이걸 0 으로 놓으면 규제를 아무것도 안하겠다는 의미(LinearRegression 과 똑같이 움직임)
# 반대로 alpha 를 높이면 규제가 높아지는데 이 적절한 alpha 값을 찾는 것이 중요함

from sklearn.linear_model import Lasso
model = Lasso(alpha = 10)

model.fit(X_train , y_train)

print("Lasso")
print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
print("기울기들 :" , model.coef_)
print("절편 : " , model.intercept_)

# 리지
# 라쏘가 비슷하지만 가중치를 완전히 0 으로 만드는 것은 불가능함(L1 정규화)

from sklearn.linear_model import Ridge
model = Ridge(alpha = 10)

model.fit(X_train , y_train)

print("Ridge")
print("훈련셋 : " , model.score(X_train , y_train))
print("테스트셋 : " , model.score(X_test , y_test))
print("기울기들 :" , model.coef_)
print("절편 : " , model.intercept_)

# alpha 값이 적절해야함
# 머신러닝 알고리즘은 하이퍼파라미터값을 사용자가 수작업으로 찾아야 함
# 딥러닝은 자동으로 찾음
"""

"""
# 로지스틱 회귀분석
from sklearn.datasets import load_iris
data = load_iris()

X = data["data"]
y = data["target"]

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234 , test_size = 0.3)
print(X_train.shape)
print(X_test.shape)

import pandas as pd
iris_df = pd.DataFrame(X , columns = data["feature_names"])

import matplotlib.pyplot as plt 
pd.plotting.scatter_matrix( iris_df , c = y , figsize = (15 , 15) , marker = 'o' , hist_kwds = {"bins" : 20} , s = 60 , alpha = 0.8)
plt.show()

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(X_train , y_train)

print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))
print("가중치 : " , model.coef_)
print("절편 : " , model.intercept_)
"""

# 의사결정트리
# 필연적으로 과대적합이 됨
# 의사결정트리 알고리즘은 특성의 중요도 파악용으로 주로 사용함
import numpy as np
from sklearn.datasets import load_iris
data = load_iris()

X = data["data"]
y = data["target"]

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234 , test_size = 0.3)
print(X_train.shape)
print(X_test.shape)

import pandas as pd
iris_df = pd.DataFrame(X , columns = data["feature_names"])

import matplotlib.pyplot as plt 
pd.plotting.scatter_matrix( iris_df , c = y , figsize = (15 , 15) , marker = 'o' , hist_kwds = {"bins" : 20} , s = 60 , alpha = 0.8)
plt.show()

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state = 1)
# 트리시작이 랜덤이어서 시드를 잡아주지 않으면 만들어질때마다 다르게 나옴

model.fit(X_train , y_train)
print("의사결정트리")
print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))
print("특성 중요도 : " , model.feature_importances_)

# 특성 중요도를 수평 막대 차트로 그리기
import matplotlib.pyplot as plt
def treeChart(model , feature_name) :
    # 수평막대 개수 구하기 : 특성의 개수만큼 구하기
    n_features = len(model.feature_importances_)
    # barh = 수평막대그래프
    
    plt.barh(np.arange(n_features) , model.feature_importances_ , align = "center")
    plt.xticks(np.arange(n_features) , feature_name) # y 축 눈금
    plt.ylim(-1 , n_features) # 눈금 범위
    plt.show()
    
treeChart(model , np.array(data["feature_names"]))


# 랜덤포레스트
# 의사결정트리를 랜덤하게 많이 만들어서 평균값을 따져서 예측함
# 앙상블의 일종 , 잘못 구성하면 과대적합의 위험을 지니고 있음(트리 계열 알고리즘의 문제점)

from sklearn.ensemble import RandomForestClassifier
# max_depth : 트리의 최대 깊이를 설정
# n_estimators : 트리의 개수(트리의 개수가 너무 작으면 과대적합이 일어나고 , 너무 많으면 시간이 많이 걸림)
model = RandomForestClassifier(random_state = 0 , max_depth = 3 , n_estimators = 1000)
model.fit(X_train , y_train)

print("랜덤포레스트")
print("훈련셋 평가 : " , model.score(X_train , y_train))
print("테스트셋 평가 : " , model.score(X_test , y_test))