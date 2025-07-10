"""
# 주성분 분석
# 특성이 아주 많을 때(고차원) , 암환자 같은 30개의 특성을 갖거나 이미지 처럼 3차원 특성을 가지졌을 때
# 주성분 분석은 원래의 특성을 가지고 원래의 특성들의 특이점을 잘 설명해낼 수 있는 새로운 특성을 만들어냄

# 특성을 변환시켜서 새로운 특성을 만들어내지만 이 '새로운 특성' 이 정확히 무엇이라고 하기는 어려움
# 학습 시간을 줄일 수 있고 짧은 시간에 높은 학습 효과를 가져옴(비지도 학습의 일종 => 시각화)

# 분석 시 상관관계를 확인함 , 이 상관관계를 구함
# 1에 가까우면 양의 상관관계이고 , -1 에 가까우면 음의 상관관계 , 0 에 가까우면 별 관계없음
# 이러한 상관관계를 시각화한 것을 (산포도 행렬 , Scattermatrix) 라고 함
# 특성태 특성의 관계를 차트로 그리는 거라서 특성이 4개면 16개의 차트를 그리고 , 특성이 30 개면 30 * 30 으로 900 개의 차트를 그림
# 각 성분별로 히스토그램을 그리거나 히트맵을 활용함

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris , load_breast_cancer
import seaborn as sns
import pandas as pd
import numpy as np

iris = load_iris()
# Bunch => DataFrame
iris_data = pd.DataFrame(iris["data"] , columns = iris["feature_names"])
iris_data["target"] = iris["target"]

print(iris_data.head())

# seaborn 에서 산포도행렬(pairplot)
sns.pairplot(iris_data , hue = "target")

# setosa , vesicolor , versinica 세 가지 색상을 다르게 표현함
plt.show()


# 특성이 많을 경우에 상관관계 시각화 - 히스토그램
# 악성과 양성 두 개의 클래스를 갖는 데이터들의 집합 , 두 클래스 별로 각자 데이터를 모아서 히스토그램을 그려보자
# 히스토그램이 특성의 개수 만큼 나옴 , 히스토그램이 데이터의 분포도를 확인하기 좋은 차트
# 구간을 나누어서 히스토그램 그림

# 데이터를 악성과 양성으로 쪼갬
cancer = load_breast_cancer()
cancer_data = cancer["data"]
cancer_target = cancer["target"]

# 악성끼리 모음
mailgnant = cancer_data[cancer_target == 0] # 악성 종양 데이터만 모음
benign    = cancer_data[cancer_target == 1] # 양성 종양 데이터만 모음

print(mailgnant.shape)
print(benign.shape)

# 히스토그램 30 개
# 차트 안에 작은 차트를 계속 생성 (15 * 2 라서 30 개) , 각각의 공간에 차트 하나만 생성
# 반환값이 차트 자체와 축에 대한 정보 , figsize = (10 , 20) 차트 전체의 크기(width * height)
fig , axes = plt.subplots( 15 , 2 , figsize = (10 , 20))

ax = axes.ravel() # 축에 대한 정보를 가져옴
for i in range(30) :    # 특성의 개수 - 30개
    # 구간 나누기
    count , bins = np.histogram(cancer_data[: , i] , bins = 50) # i 번째 열에 대해서 구간을 50개로 나누어라
    # count = 각 구간별 데이터 개수
    # bins  = 구간 리스트
    ax[i].hist(mailgnant[: , i] , bins = bins , color = "purple" , alpha = 0.5) # 악성 데이터를 보라색으로
    ax[i].hist(benign[: , i] , bins = bins , color = "green" , alpha = 0.5)     # 양성 데이터를 초록색으로
    
    # 제목
    ax[i].set_title(cancer["feature_names"][i])
    ax[i].set_yticks(())    # Y 축 제거
    
ax[0].set_xlabel("Feature_Size")
ax[0].set_ylabel("Frequency")
ax[0].legend(["mailgnant" , "benign"] , loc = "best")
fig.tight_layout()  # 차트 재정렬
plt.show()



# 히트맵 산포도행렬 못 그릴 때 자주 사용하는 차트 (상관관계를 확인할 수 있음)
# [1] 상관관계 행렬을 만듬
correlation_matrix = iris_data.corr()    # 데이터 프레임이 corr 이라는 함수가 있어서 상관계수를 알아서 계산함
print(correlation_matrix[:10])

# [2] 히트맵 그리기
annot = True    # 차트의 줄 속성 , 히트맵의 셀에 값을 표시함 , False 면 표시하지 않음
cmap  = "coolwarm" # 히트맵에서 가장 많이 사용하는 색상 , 양의 관계를 빨간색 , 음의 관계는 파란색
fmt   = ".2f"      # 표시될 숫자의 소수점 자리수 지정

sns.heatmap(correlation_matrix , annot = annot , cmap = cmap , fmt = fmt , linewidths = .5)  # 셀 사이에 선추가
plt.xticks(rotation = 45 , ha = "right")    # x 축 레이블 회전
plt.yticks(rotation = 0)
plt.tight_layout()

plt.show()
"""

"""
# 주성분 분석 2
# PCA(주성분 분석) - 차원축소
# 특성이 너무 많을 때 각 특성들로부터 새로운 특성을 만들어내는 것을 말함
# fit , transform , PCA 뽑아내고 PCA 자료로 다시 학습

from sklearn.datasets import load_breast_cancer , load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

cancer = load_digits()
X = cancer["data"]
y = cancer["target"]

# 스케일링
scaler = StandardScaler()
scaler.fit(X)

X_scaled = scaler.transform(X)

# 주성분 분석
from sklearn.decomposition import PCA
pca = PCA(n_components = 10) # 성분의 개수 지정
pca.fit(X_scaled)   # 학습
X_pca = pca.transform(X_scaled)

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 0)
X_train_scale , X_test_scale , y_train , y_test = train_test_split(X_scaled , y , random_state = 0)
X_train_pca , X_test_pca , y_train_pca , y_test_pca = train_test_split(X_pca , y , random_state = 0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train , y_train)
print("기본 값")
print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))

model.fit(X_train_scale , y_train)
print("스케일링 후")
print("훈련세트 : " , model.score(X_train_scale , y_train))
print("테스트세트 : " , model.score(X_test_scale , y_test))

model.fit(X_train_pca , y_train)
print("주성분 분석 후")
print("훈련세트 : " , model.score(X_train_pca , y_train))
print("테스트세트 : " , model.score(X_test_pca , y_test))
"""

# 군집 분석(클러스터링)
# 결과를 주지 않고 그냥 데이터를 가지고 분류하는 것
# np.random.normal = 평균 , 표준편차 , 형태 - 평균과 표준편차를 만족하는 가우스 분포를 따르는 데이터를 만듬

"""
import numpy as np
a = np.random.normal(173 , 15 ,1000)

print(a)

import matplotlib.pyplot as plt
plt.figure(figsize = (10 , 6))
plt.hist(a , bins = 30)
plt.show()
"""

"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

np.random.seed(42)
x1 = np.random.normal(0 , 1 , (50 , 2))     # 형태가 튜플로 2차원으로 생성됨
x2 = np.random.normal(5 , 1 , (50 , 2))     # 형태가 튜플로 2차원으로 생성됨
x3 = np.random.normal(2.5 , 1 , (50 , 2))   # 형태가 튜플로 2차원으로 생성됨

# 데이터를 합침
# concatenate - 인자들이 dataframe 이어야 함
# np.vstack 을 사용해서 세로로 합침

# X = np.vstack((x1 , x2 , x3))   # 매개변수를 튜플로 전달해야함
X = load_iris()["data"]
print(X.shape)  # y 없음 , y 를 알 수 없음

# n_clusters = 3  : 몇 개가 묶였는지는 알려주어야 효율적인 군집분석이 가능함(x1 , x2 , x3)
# 원래의 군집 개수보다 적을 때는 그나마 차이가 덜 한 군집끼리 합침 => 정보가 손실될 수 있고 해석도 어려워짐
# 원래의 군집 개수보다 많을 때는 강제로 군집을 더 쪼갬 => 마찬가지로 정보가 손실될 수 있고 해석이 이상해짐
# n_clusters 의 개수를 모를 경우에는 엘보우 실루엣 또는 전문가의 견해로 판단해야함
Kmeans = KMeans(n_clusters = 5 , random_state = 42)
Kmeans.fit(X)

y_kmeans = Kmeans.predict(X)
print(y_kmeans[:20])

# 군집 분석 시 각 군집의 중심값을 가져옴
center = Kmeans.cluster_centers_
print("중심값 : " , center)

# 시각화
plt.figure(figsize = (8,6))
plt.scatter(X[:,2] , X[:,3] , c = y_kmeans , cmap = "viridis" , s = 50 , alpha = 0.6)
plt.scatter(center[:,0] , center[:,1] , c = "red" , s = 200 , marker = "X" , label = "centorids")
plt.legend()
plt.grid()
plt.show()
"""

"""
# Kflod 검증
# 과대 적합을 막기위해 훈련셋과 테스트셋을 나눔
# 5개의 그룹이 있다면 , 1 ~ 4 는 훈련셋 , 5 는 테스트셋으로 훈련하고 다음으로 2 ~ 5 는 훈련셋 , 1 은 테스트셋으로 훈련하고를 반복하고
# 최종으로 돈 다음 score 의 평균값을 냄

# 데이터가 너무 많아지면 문제가 발생됨
# 그래서 문제 발생을 막기 위해 딥러닝에서 Hold Out 이라는 검증 기법을 사용함
# 훈련셋 , 검증셋 , 테스트셋으로 나누어서 각자 학습을 해서 결과를 냄

from sklearn.datasets import load_iris
from sklearn.model_selection import KFold , StratifiedKFold #(개선 버전)
from sklearn.tree import DecisionTreeClassifier

data = load_iris()

X = data["data"]
y = data["target"]

train_score = []
test_score  = []

kfold = KFold(n_splits = 5) # 몇 개의 그룹으로 데이터를 나눌 지 설정
for train_index , test_index in kfold.split(X) :
    # print(train_index)
    # print(test_index)
    X_train = X[train_index]
    y_train = y[train_index]
    X_test  = X[test_index]
    y_test  = y[test_index]
    
    print(y_train)
    print(y_test)
    

sfk = StratifiedKFold(n_splits = 5) # 몇 개의 그룹으로 데이터를 나눌 지 설정
for train_index , test_index in sfk.split(X , y) :
    # print(train_index)
    # print(test_index)
    X_train = X[train_index]
    y_train = y[train_index]
    X_test  = X[test_index]
    y_test  = y[test_index]
    
    # print(y_train)
    # print(y_test)
    model = DecisionTreeClassifier()
    model.fit(X_train , y_train)
    train_score.append(model.score(X_train , y_train))
    test_score.append(model.score(X_test , y_test))
    
print(train_score)
print(test_score)

# cross_val_score : 교차검증에 사용되는 함수
from sklearn.model_selection import cross_val_score
model = DecisionTreeClassifier()

result = cross_val_score(model , X , y , scoring = "accuracy" , cv = 5)  # scoreing = 정밀도로 설정 , cv : 몇 번 접을 것인지
print(result)
"""

# 머신러닝
# 학습하고 결과 나옴 , 계속 학습 안하고 모델 저장했다가 불러와서 새로운 데이터셋 => 예측이 가능

# 딥러닝
# 엄청난 데이터 양 , 할때마다 학습하면 힘듬 , 저장했다가 일부 절차 중에 빼고 다른 걸 넣을 수 있음
# 미리 학습된 요소들과 내가 만든 새로운 데이터들을 가지고 학습 가능
# 미리 학습된 이미지셋도 텍스트셋 데이터 자체 어마어마해야함
# 텍스트의 가장 큰 문제점 => 기반이 되었던 학습데이터가 어느 분야인지가 중요함