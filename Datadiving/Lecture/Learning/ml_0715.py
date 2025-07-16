"""
# GridSearchCV 는 사이킷런에서 제공하고 있는 것으로 , optuna 는 다른 곳에서 제공하고 있는 것
# pip install optuna

import optuna
import numpy  as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC # SVC 가 하이퍼파라미터가 많음
from sklearn.metrics import classification_report , accuracy_score
from sklearn.ensemble import RandomForestClassifier
# classfication_report = 분류 모델 중에서도 이진 분류 평가 라이브러리
# accuracy_score = 단순 정확도 판단 기준 평가 라이브러리

# GridSearchCV : 파라미터를 주면 각 파라미터 별로 전체 조합을 만들어서 다 돌려봄

data_set = load_breast_cancer()

# 데이터 셋을 데이터프레임 구조로
X = pd.DataFrame(data_set.data , columns = data_set.feature_names)
y = data_set.target                 # 0 이 악성 , 1 이 양성 => 둘의 값을 반전 시키는 것이 나중에 모델 평가 시에 더 편함
y_change = np.where(y == 0 , 1 , 0) # 0 ==> 1 로 , 1 ==> 0 으로

# 특성의 개수
print(np.unique(y_change , return_counts = True))
# (array([0, 1]), array([357, 212]))
print(*np.unique(y_change , return_counts = True))
# [0 , 1] [357 , 212]
print(zip(*np.unique(y_change , return_counts = True)))
# (0 , 357) (1 , 212)
print(dict(zip(*np.unique(y_change , return_counts = True))))
# {np.int64(0): np.int64(357), np.int64(1): np.int64(212)}

print("유방암 데이터셋 정보 : ")
print(f"특성 개수 {X.shape[1]}")
print(f"샘플 개수 {X.shape[0]}")
print(f"클래스 분포도 ( 0 : 양성 , 1 : 악성) {dict(zip(*np.unique(y_change , return_counts = True)))}")

# 악성인 사람과 양성인 사람 간의 데이터 불균형 상태(예를 들면 지금같은 암 데이터) 일 경우에 훈련셋과 테스트셋을 쪼갤 때 그 균형을 유지하면서 쪼갤 필요가 있음
X_train , X_test , y_train , y_test = train_test_split(X , y_change , random_state = 1234 , test_size = 0.2 , stratify = y_change)

print("훈련 데이터 셋")
print(X_train.shape , X_test.shape)
print(f"y_train 분포 : {dict(zip(*np.unique(y_train , return_counts = True)))}")
print(f"y_test 분포 : {dict(zip(*np.unique(y_test , return_counts = True)))}")

# 라이브러리 경향 : 콜백함수를 만들어서 파라미터로 전달
# 옵투나가 호출할 콜백함수를 만들어야 함
def objective(trial) :  # 매개변수명을 마음대로 설정
    # 옵투나를 통해 탐색할 하이퍼파라미터 범위를 정의함
    max_depth = trial.suggest_int("max_depth" , 5 , 20) # 그리드서치 5 ~ 20 까지 설정
    # 트리의 최대깊이
    min_samples_leaf = trial.suggest_int("min_samples_leaf" , 1 , 10)
    # 리프 노드가 되기 위한 최소 샘플 수
    min_samples_split = trial.suggest_int("min_samples_split" , 2 , 10)
    n_estimators = trial.suggest_int("n_estimators" , 50 , 100)
    
    model = RandomForestClassifier(
        max_depth = max_depth ,
        min_samples_leaf = min_samples_leaf ,
        min_samples_split = min_samples_split ,
        n_estimators = n_estimators ,
        random_state = 42 ,
        n_jobs = -1
        )
    # 내부 프로세스 CPU 개수 *2 라서 -1 을 주면 알아서 최대치를 사용하게 됨
    
    model.fit(X_train , y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test , y_pred)  # 예측 정확도
    return accuracy # 반드시 마지막에 리턴 필요 , 목적값

# 옵투나 스터디 생성
study = optuna.create_study(direction = "maximize")
# 옵투나가 이익을 최대화하는 방향으로 study 객체를 만듬
print("옵투나 최적화 시작(50회 시도)")
study.optimize(objective , n_trials = 50)
# 콜백함수를 전달하고, 회수를 지정함
# optimize(최적화) = 최적화 함수

print(f"최고 정확도 : {study.best_trial.value}")
print(f"최적의 하이퍼파라미터 : {study.best_params}")
"""

"""
# 파이프라인
# 전체적으로 유기적인 연결라인을 가지고 한번에 처리할 수 있도록 함
# 회귀 평가와 분류 평가 : 머신 러닝 모델이 갖고 있는 score 함수 사용
# 회귀 스코어 : 결정계수 R제곱 , 분류 : 정확도를 기준 , 불균형에 대해서는 이 기준을 적용할 수 있음

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import classification_report   # 분류 레포트

data_set = load_iris()
X = data_set.data
y = data_set.target

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state = 1234)

# 파이프라인 정의하기
pipe_line = Pipeline(
    [
        ("scaler" , StandardScaler()) , # 데이터 스케일링 정의
        ("svc" , SVC(kernel = "rbf" , C = 1.0 , gamma = "scale"))
    ]
)

pipe_line.fit(X_train , y_train)
y_pred = pipe_line.predict(X_test)

# 성능평가
print(classification_report(y_test , y_pred))

# 그리드 서치의 estimator 에 pipeline 을 전달해서 학습할 수 있음
"""

"""
# 파이프라인_그리드 서치
import numpy  as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split , GridSearchCV , StratifiedKFold
from sklearn.svm import SVC # SVC 가 하이퍼파라미터가 많음
from sklearn.metrics import classification_report , accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , MinMaxScaler
from sklearn.linear_model import LogisticRegression
# classfication_report = 분류 모델 중에서도 이진 분류 평가 라이브러리
# accuracy_score = 단순 정확도 판단 기준 평가 라이브러리

# GridSearchCV : 파라미터를 주면 각 파라미터 별로 전체 조합을 만들어서 다 돌려봄

data_set = load_breast_cancer()

X = data_set.data
y = data_set.target

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234)

# 파이프라인 구축
# 파이프라인과 그리드서치 간에 파라미터 주는 규칙
# 파이프라인에서 모델 앞에 classfier 주면 매개변수가 C 면 classifier__C
pipeline = Pipeline(
    steps = [
        ("scaler" , StandardScaler()) ,
        ("classifier" , LogisticRegression(random_state = 42))
    ]
)

# 그리드 서치 구축
param_grid = {
    "scaler" : [StandardScaler() , MinMaxScaler()] ,
    "classifier__C" : [0.01 , 0.1 , 10 , 100] ,
    "classifier__solver" : ["liblinear" , "lbfgs"]
}

# 그리드 서치 만들기
grid_search = GridSearchCV(
    estimator = pipeline ,
    param_grid = param_grid ,
    # cv 의 숫자 : Kfold 검증 , 타겟이 불균형 세트 일때
    cv = StratifiedKFold(n_splits = 5 , shuffle = True , random_state = 42) ,
    scoring = "roc_auc" , # roc 곡선
    # 암환자처럼 잘못 예측한 경우가 위험한 경우 또는 데이터 불균형이 클때 accuracy 만으로는 한계가 있어 roc-auc 로 판단함
    n_jobs = -1 ,   # 프로세스 개수 최적화
    verbose = 2 # 학습중인 과정을 상세하게 보여줌
)

grid_search.fit(X_train , y_train)
print("최적 파라미터")
print(grid_search.best_params_)

print("최고 점수")
print(grid_search.best_score_)
"""

"""
# 파이프라인-옵투나
import optuna
import numpy  as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC # SVC 가 하이퍼파라미터가 많음
from sklearn.metrics import classification_report , accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , MinMaxScaler
# classfication_report = 분류 모델 중에서도 이진 분류 평가 라이브러리
# accuracy_score = 단순 정확도 판단 기준 평가 라이브러리

# GridSearchCV : 파라미터를 주면 각 파라미터 별로 전체 조합을 만들어서 다 돌려봄

data_set = load_breast_cancer()

# 데이터 셋을 데이터프레임 구조로
X = pd.DataFrame(data_set.data , columns = data_set.feature_names)
y = data_set.target                 # 0 이 악성 , 1 이 양성 => 둘의 값을 반전 시키는 것이 나중에 모델 평가 시에 더 편함
y_change = np.where(y == 0 , 1 , 0) # 0 ==> 1 로 , 1 ==> 0 으로

# 특성의 개수
print(np.unique(y_change , return_counts = True))
# (array([0, 1]), array([357, 212]))
print(*np.unique(y_change , return_counts = True))
# [0 , 1] [357 , 212]
print(zip(*np.unique(y_change , return_counts = True)))
# (0 , 357) (1 , 212)
print(dict(zip(*np.unique(y_change , return_counts = True))))
# {np.int64(0): np.int64(357), np.int64(1): np.int64(212)}

print("유방암 데이터셋 정보 : ")
print(f"특성 개수 {X.shape[1]}")
print(f"샘플 개수 {X.shape[0]}")
print(f"클래스 분포도 ( 0 : 양성 , 1 : 악성) {dict(zip(*np.unique(y_change , return_counts = True)))}")

# 악성인 사람과 양성인 사람 간의 데이터 불균형 상태(예를 들면 지금같은 암 데이터) 일 경우에 훈련셋과 테스트셋을 쪼갤 때 그 균형을 유지하면서 쪼갤 필요가 있음
X_train , X_test , y_train , y_test = train_test_split(X , y_change , random_state = 1234 , test_size = 0.2 , stratify = y_change)

print("훈련 데이터 셋")
print(X_train.shape , X_test.shape)
print(f"y_train 분포 : {dict(zip(*np.unique(y_train , return_counts = True)))}")
print(f"y_test 분포 : {dict(zip(*np.unique(y_test , return_counts = True)))}")

# 라이브러리 경향 : 콜백함수를 만들어서 파라미터로 전달
# 옵투나가 호출할 콜백함수를 만들어야 함
def objective(trial) :  # 매개변수명을 마음대로 설정
    # 옵투나를 통해 탐색할 하이퍼파라미터 범위를 정의함
    max_depth = trial.suggest_int("max_depth" , 5 , 20) # 그리드서치 5 ~ 20 까지 설정
    # 트리의 최대깊이
    min_samples_leaf = trial.suggest_int("min_samples_leaf" , 1 , 10)
    # 리프 노드가 되기 위한 최소 샘플 수
    min_samples_split = trial.suggest_int("min_samples_split" , 2 , 10)
    n_estimators = trial.suggest_int("n_estimators" , 50 , 100)
    
    model = RandomForestClassifier(
        max_depth = max_depth ,
        min_samples_leaf = min_samples_leaf ,
        min_samples_split = min_samples_split ,
        n_estimators = n_estimators ,
        random_state = 42 ,
        n_jobs = -1
        )
    
    pipe_line = Pipeline(
        [
            ("scaler" , StandardScaler()) ,
            ("classifier" , model)
        ]
    )
    
    
    # 내부 프로세스 CPU 개수 *2 라서 -1 을 주면 알아서 최대치를 사용하게 됨
    
    pipe_line.fit(X_train , y_train)
    y_pred = pipe_line.predict(X_test)
    
    accuracy = accuracy_score(y_test , y_pred)  # 예측 정확도
    return accuracy # 반드시 마지막에 리턴 필요 , 목적값

# 옵투나 스터디 생성
study = optuna.create_study(direction = "maximize")
# 옵투나가 이익을 최대화하는 방향으로 study 객체를 만듬
print("옵투나 최적화 시작(50회 시도)")
study.optimize(objective , n_trials = 50)
# 콜백함수를 전달하고, 회수를 지정함
# optimize(최적화) = 최적화 함수

print(f"최고 정확도 : {study.best_trial.value}")
print(f"최적의 하이퍼파라미터 : {study.best_params}")
"""
"""
# 캘리포니아 집값 예측 데이터를 가져와서 파이프라인 구축 및 그리드 서치 복습
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

import pandas as pd
import numpy  as np

data_set = fetch_california_housing()
X = pd.DataFrame(data_set.data , columns = data_set.feature_names)
y = data_set.target

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234)

pipe_line = Pipeline(
    [
        ("scaler" , StandardScaler()) ,
        ("regressor" , Ridge(random_state = 1234))
    ]
)

param_grid = {
    "scaler" : [StandardScaler()] ,
    "regressor__alpha" : [0.01 , 0.1 , 1.0 , 10 , 100]
}

grid_search = GridSearchCV(
    estimator = pipe_line ,
    param_grid = param_grid ,
    cv = 5 ,
    scoring = "neg_mean_squared_error" ,
    n_jobs = -1 ,
    verbose = 2
)

grid_search.fit(X_train , y_train)
print("최적 파라미터")
print(grid_search.best_params_)

print("최고 점수")
print(grid_search.best_score_ * -1)
"""


"""
기초 통계 = 현재의 상황을 정리하는 것 , 어떤 집단의 성격을 통계량을 통해서 알아냄
- 평균 , 분산 , 표준편차 , 중간값 , 최빈값
- 평균 : 모든 요소를 더한값/전체데이터 개수
- 오차 : 기대값(예상값) 과 평균값의 차이를 다 더하면 0 임
- 분산 : 오차의 제곱의 합 , 절대값 안 쓰고 제곱을 쓴 이유는 오차를 크게 보이기 위함
- 표준분산 : 통계학자들이 표본 중에서 몇 개만 뽑아볼거라서 자유도((기대값 - 평균값) 의 제곱의 합 / n-1)
* 사이킷런은 그냥 n 으로 나눔
- 표준편차 : 분산의 제곱근 , 데이터의 흩어짐의 정보 , boxplot 로 보면 네모가 크게 나타남
* 평균은 같은데 표준편차가 크다라는 의미는 데이터가 극단적이라는 의미
(예: A 학생의 점수 평균이 60 이고 표준편차가 20 이면 점수가 40 ~ 80 사이를 왔다갔다 하는것)
(예: B 학생의 점수 평균이 70 이고 표준편차가 5 이면 점수가 65 ~ 75 사이를 왔다갔다 하는것)
- 중간값 : 중간에 위치한 값 , 데이터 개수가 11개면 6이 중간이 됨
* 표준편차가 크면(이상치가 있는 경우) 평균을 왜곡시킬 수 있어서 이 때 대표값으로 중간값을 사용함

범주형자료(카테고리타입) = 값이 불연속적
- 예시로 연비 등급을 생각해볼 수 있으며 여기서 중간값은 중요하지 않음
- 발생빈도수(Frequency) , 분할표(데이터프레임 : value_counts , 넘파이 : unique , bins)

범주형 : 연비등급 , 분할표 , 히스토그램 - 구간별로 데이터 몇 개 있는지 , 차이검정
비범주형(연속형) : 연비자체 , 평균 , 표준편차 , 중간값 , 차이검정

대립 가설 : 현재의 가설을 폐기할 가설(한국 남자 키가 173 보다 작다 또는 173 보다 크다)
귀무 가설 : 현재의 상태(한국 남자 키가 173)

추론 통계
- 기초 통계를 바탕으로 예측이 들어갈 때 , 머신 러닝 , 딥러닝
[1] 지도학습 : 라벨이 있을 때 , 타겟이 있을 때
[2] 비지도학습 : 라벨이 없을 때 , 타겟이 없을 때 , 보통은 지도학습 전단계로 특성공학을 담당하고 있음
* 새로운 특성을 만들거나 , 차원을 축소하거나 , 연관성을 찾아보거나 , 스케일링 등
[3] 강화학습 : 알파고 , 게임알고리즘한테 당근과 채찍을 주는 경우(파이썬 3.9 이하까지만 지원 중)
* DFS(깊이 우선) , BFS(너비 우선) : 둘 다 안 쓰고 있음
* 해보고 싶다면 반드시 별도의 가상환경을 만들어야 함

# 데이터 머신러닝 순서
[1] 타겟이 분류냐 회귀냐 확인
- 회귀의 목적은 연속된 값 한 개 맞춤 - 키가 집값 , 성적도 '점수' 로 맞추면 회귀
- 분류는 이진 분류 , 다중 분류가 있음(확률(무엇인가 될 확률) - 합격할 확률 , 개가 될 확률 등)
* boxplot , 산포도(히트맵) , 히스토그램(분류) , 분할표(분류)

[2] 각 필드 별 결측치 확인
- 결측치를 열을 제거하거나 행을 제거할 수도 있음
- 혹은 지나치게 결측치가 많을 경우에는 대체값(비범주형(평균, 중간) , 범주형(최빈값)) 을 사용

[3] 이상치 제거
- boxplot 이 시각화해줌
- 맨 아래 , 맨 위에 있는 동그라미가 이상치임
- IQR 방식 알고리즘을 많이 사용함, 함수는 내가 직접 만들어야 함

[4] 중복값 제거

[5] 데이터 자체가 잘못 들어온 값
- value_counts 함수나 Unique 로 체크
- 값 바꾸기를 하거나 행을 삭제

[6] 라벨인코딩 또는 원핫인코딩 , get_dummies
* 성별 , male , female 등 정보가 문자열로 들어오면 연산이 불가능하니깐 male = 0 , female = 1 등으로 말 그대로 라벨링 하는 것
- 라벨링의 범위가 큰 경우 (예: 직업 등)
* 라벨링 > 꽃이미지 분류시 타겟팅을 한 것

[7] 스케일링
- 연산이니깐 값의 범위가 너무 차이 나면 큰 값 기준으로 가중치를 결정함
- 서포트벡터머신 하고 딥러닝은 단위가 영향을 미치는 알고리즘임
- 스케일을 맞춤 (비슷한 용어 : 정규화 , 표준화)
"""
"""
평가 지표
- 회귀인 경우와 분류인 경우가 다름

회귀인 경우
mae - Mean Absolute Error : 평균절대오차 , (기대값 - 실제값) / 개수 , 오차가 크게 보이지 않아 이상치에 덜 민감함
mse - Mean Squared Error  : 평균제곱오차 , (기대값 - 실제값) ** 2 / 개수 , 오차가 크게 보이기에 이상치에 민감하게 반응함
* 딥러닝에서 손실함수(오차 계산 시에 많이 사용됨)
rmse - Root Mean Squared Error : mse 의 제곱근
R2 - 결정계수 , 현재 회귀계열에서 score 함수의 결과값이 결정계수임
* 1 이 될수록 예측이 뛰어나고, 0 으로 갈수록 예측률이 떨어짐 , - 로 가면 매우 심각한 상태
* 독립변수(특성) 의 수가 증가하면 예측률이 높지 않은데 이 값이 좋아지는 취약점이 있음 => 따라서 업그레이드 버전으로 Adjusted R-Squared(R 언어) 를 사용함
mape - Mean Absolute Percentage Error : 퍼센트로 따진거

분류인 경우
문제점 : 데이터의 불균형성 때문에 제대로 예측이 안되는 경우가 있음 , 암환자 데이터의 경우 예측의 정확성만 가지고 좋은 모델이라고 평가할 수 있는가?
오차 행렬(Confution Matrix) : 대각선이 정상임

1) 정확도 - 올바르게 예측한 비율 , 불균형데이터 셋일때(위험한 상태 예측) 같은 경우 정확도는 도움이 되지 않음
* 분류 모델들의 score 함수는 정확도를 이야기함 , 아주 운 나쁜 경우에 한가지만 대답해도 정확도는 높을 수 있음(이것이 문제)
2) 정밀도(precision) - 모델이 양성으로 예측했는데 실제 양성으로 예측한 비율
* 스팸이 아닌데 스팸으로 예측하고 스팸함으로 보낸 경우가 문제가 될 수 있음
3) 재현율(recall) - (민감도) , 실제 양성인 것 중에서 모델이 양성으로 예측한 것들
* 암환자 , 오차 측정을 줄이기 위해 중요함
4) f1-score - 정밀도와 재현율의 조화 평균
"""

"""
# 캘리포이나 집값 회귀 분석 및 평가 예제
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error , mean_squared_error , r2_score
from sklearn.preprocessing import StandardScaler

# 1. 캘리포니아 집값 데이터셋 로드
housing = fetch_california_housing()
print(type(housing))

# 차트를 그리려면 numpy > 요소를 하나씩 그려야 해서 차트를 그리고 싶음
# Dataframe : 데이터프레임 자체가 차트를 제공하기도 하고 , seaborn 차트 , plotly 차트(interactive 차트)
# python 코드로 차트를 그리면 plotly 는 html 과 css 와 자바스크립트로 움직이는 차트가 만들어짐
# 예전에는 R 언어만 지원했는데 현재 python
# 넘파이 배열 , 컬럼명

X = pd.DataFrame(housing.data , columns = housing.feature_names)
y = pd.Series(housing.target , name = "houseval")

print(X.head())
print(X.columns)
print(y[:10])

# 2. 훈련셋 쪼개기 - numpy 2차원(dataframe) , 1차원(series)
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42)

# 3. 결측치와 이상치가 없다고 판단

# 4. 스케일링 처리(표준화 , 정규화)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # 비지도 학습 fit > transform
X_test_scaled  = scaler.fit_transform(X_test)

# 5. 선형회귀모델학습
model = LinearRegression()
model.fit(X_train_scaled , y_train)

# 6. 테스트 데이터로 예측
y_pred = model.predict(X_test_scaled)

# 7. 회귀모델 평가지표
mae = mean_absolute_error(y_test , y_pred)
print("mae : 평균 절대 오차 = " , mae)

mse = mean_squared_error(y_test , y_pred)
print("mse : 평균 제곱 오차 = " , mse)

rmse = np.sqrt(mse)
print("rmse : 평균 제곱근 오차 = " , rmse)

r2 = r2_score(y_test , y_pred)  # 평상시 score 함수와 동일함 , 결정계수는 1에 가까울 수록 좋음
print("결정계수 = " , r2)
print("모델 score = " , model.score(X_test_scaled , y_test))
# 특성의 개수가 많아지면 결정 계수 값은 예측력하고는 상관없이 1에 가까워지며 좋아짐
# 특성이 많아질때는 mae 나 mse 를 사용해야함 , mse 는 제곱이기 때문에 이상치에 영향을 많이 받음
# 차트를 그릴떄는 dataframe 으로 변환하고 그리는 것이 좋음

print("데이터 개수")    # 데이터 개수가 2만개가 넘음 , 차트를 그려보고 , 너무 오래 걸리면 데이터 샘플링 진행
print(X.shape)

X["hosuingval"] = y
print(X.head())

df_sample = X.sample(n = 2000 , random_state = 42)  # 데이터를 원하는 만큼 적당히 샘플링함
print(df_sample.shape)

import matplotlib.pyplot as plt
import seaborn as sns

sns.pairplot(
    df_sample , 
    diag_kind = "kde" , # 대각선 히스토그램 밀도(부드럽게)
    kind = "scatter" # 산포도
    )
plt.show()
"""

"""
# 차트에 한글 지원하기
# 차트 내부의 폰트를 변경시켜야함
# 차트 그리기 전에 두개를 넣어주어야 함
# plt.rcParams["font.family"] = "Gulim"    # 나눔고딕 폰트 이름 변경
# plt.rcParams["axes.unicode_minus"] = False          # 마이너스 부호 깨짐 방지

import matplotlib.font_manager as fm
fm.fontManager.ttflist
# tt = Truetype : 비트맵이 아닌 벡터 방식으로 확대, 축소해도 깨지지 않음
# tt 방식 이전에는 비트맵 방식의 글꼴을 사용했는데 비트맵 방식은 글꼴 확대 시 깨짐

fontlist = [font.name for font in fm.fontManager.ttflist]
print(fontlist)

import matplotlib.pyplot as plt
import seaborn as sns

# 차트 그리기 전에 seaborn 차트도 동일하게 적용됨
plt.rcParams["font.family"] = "Gulim"
plt.rcParams["axes.unicode_minus"] = False

iris = sns.load_dataset("iris")
sns.pairplot(iris , hue = "species")
plt.suptitle("iris 데이터셋 산포도 행렬")
plt.show()
"""

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix , classification_report

plt.rcParams["font.family"] = "Gulim"
plt.rcParams["axes.unicode_minus"] = False

cancer = load_breast_cancer()
X = pd.DataFrame(cancer.data , columns = cancer.feature_names)
y = cancer.target

y_changed = np.where(y == 0 , 1 , 0)

print(y[:20])
print(y_changed[:20])

# 데이터가 불균형 셋인지 확인
print(dict(zip(*np.unique(y_changed , return_counts = True))))

# 데이터 쪼개기
X_train , X_test , y_train , y_test = train_test_split(X , y_changed , random_state = 1)

# 특성 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

# 모델 학습
model = LogisticRegression(random_state = 1 , solver = "liblinear")
model.fit(X_train_scaled , y_train)

y_pred = model.predict(X_test_scaled)

# 양성을 예측한 것만 가져오기 , 악성에 대한 예측 확률 하나만 가져오기
y_pred_proba = model.predict_proba(X_test_scaled)[: , 1]

# 오차 행렬 구하기
cm = confusion_matrix

# 분류 리포트
report = classification_report(y_test , y_pred , target_names = ["양성" , "악성"])
print(report)


# seaborn 차트를 이용한 시각화
plt.figure(figsize = (7,6))
sns.heatmap(cm , annot = True , fmt = "d" , cmap = "Blues" , cbar = False , xticklabels = ["양성" , "악성"] , yticklabels = ["양성" , "악성"])
plt.xlabel("예측 클래스")
plt.ylabel("실제 클래스")
plt.title("오차행렬")
plt.show()

# ROC 곡선 , roc_curve 함수가 3개의 반환값을 줌
fpr , tpr , thresholds = roc_curve(y_test , y_pred_proba)
auc_score = roc_auc_score(y_test , y_pred_proba)
plt.plot(fpr , tpr , color = "darkorange" , lw = 2 , label = f"ROC곡선(AUC : {auc_score})")
plt.plot([0.1] , [0 , 1] , color = "navy" , linestyle = "--" , label = "기준점(AUC = 0.5)")
plt.xlim([0.0 , 1.0])   # 눈금 범위
plt.ylim([0.0 , 1.05])  # 눈금 범위
plt.xlabel("False posigitve rate(FDR)")
plt.ylabel("True posigitve rate(TPR)/Recall")

plt.title("ROC 곡선")
plt.legend(loc = "lower right") # 범주는 오른쪽 하단에
plt.grid(True)
plt.show()
"""

"""
# 차트
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib import font_manager, rc
import seaborn as sns
#font_manager - 폰트를 폰트객체화 
#rc - 폰트를 지정할 영역 (차트영역)

sns.set_style("darkgrid")
# 한글 세팅(plt.rcParams) 이전에 선언되어야 하며, 세팅 이후에 선언되면 오류가 발생할 수 있음

# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/Gulim.TTF").get_name()
# font_name = font_manager.FontProperties(fname="./fonts/HYBDAM.TTF").get_name()
# plt.rcParams["font.family"] = "Gulim"
# plt.rcParmas["axes.unicode_minus"] = False

# x = np.linspace(0 , 2 , 100)    # 구간을 나눈다. 0 ~ 2 사이를 100개로 쪼개서 값을 np.array 로 줌
# print(x[:20])

# 히스토그램 - 분포도(통계학적으로 중요함)
# 히스토그램은 seaborn 의 displot 함수가 제공함
# loc : float = ..., 평균
# scale : float = ..., 표준편차
# size : None = ... 개수
x = np.random.normal(loc = 70 , scale = 20 , size = 500)
x = np.random.normal(size = 1000)   # 정규분포가 되도록 데이터를 생성
sns.displot(x , bins = 20 , kde = True , rug = False , label = "Histogram") # bins = 구간 개수 , kde = 커널 밀도 , rug = 러그 표시 여부
sns.utils.axlabel("value" , "frequency")

# x 축의 데이터 개수와 y 축의 데이터 개수는 반드시 일치해야 함
# plt.plot(x , x , label = "Linear" , color = "g")
# plt.plot(x , x**2 , label = "Two" , color = "b")
# plt.plot(x , x**3 , label = "Three" , color = "r")
plt.title("TITLE")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
"""

"""
# 인터렉티브 차트
import plotly.graph_objects as go
import pandas as pd
import numpy  as np

# 차트 그리는 함수 하나씩 만들어서 호출하기
def create_scatter() :  # 산포도 그리는 함수
    print("===== 산포도 =====")
    df = pd.DataFrame({
        "x_data" : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] ,
        "y_data" : [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10] ,
        "size_data" : [10 , 10 , 40 , 20 , 50 , 60 , 10 , 10, 10 , 10]
    })
    
    # 차트에 대한 기본 정보 , 데이터와 데이터를 출력할 때 marker 를 사용함
    chart1 = go.Scatter(
        x = df["x_data"] ,
        y = df["y_data"] ,
        mode = "markers" ,
        marker = dict(size = df["size_data"] , color = " red" , opacity = 0.7 , line = dict(width = 1 , color = "DarkSlateGrey")) ,
        name = "산포도"
    )
    
    # 축에 대한 정보를 따로 생성함
    layout = go.Layout(
        title = "산점도" ,
        xaxis = {"title" : "X축"} ,
        yaxis = {"title" : "Y축"} ,
        hovermode = "closest"
        )
    
    fig = go.Figure(data = [chart1] , layout = layout)
    fig.show()  # 브라우저가 작동
    fig.write_html("산포도.html")
    
if __name__ == "__main__" :
    create_scatter()
"""

"""
# 텍스트 분석
# + , - , * , / 연산이 가능하게 바꾸어주어야 함

# sklearn 이 CounterVectorizer 라는 클래스를 제공함(RNN)
from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer()

bards_words = ["I like star" , "red star, blue star" , "I like dog"]
# 1. 학습해서 사전을 만들고
vect.fit(bards_words)

print("어휘사전 크기 : " , len(vect.vocabulary_))
print("어휘사전 내용 : " , vect.vocabulary_)

# 2. 사전을 바탕으로 벡터화
bag_of_words = vect.transform(bards_words)
print(bag_of_words)
print(bag_of_words.toarray())
"""

"""
# 로이터 뉴스 , IMDB 영화평론 사이트
# 1. 토큰화 > 토큰을 나눔 > 단어로 나눔 > 바꿔서 처리 가능
# 2. 어휘사전 구축 > 단어한테 고유 숫자를 줌 > 어휘사전이 충분히 커야함
# 3. 단어 빈도수 계산
# 4. 문서단어 행렬 : 단어 빈도수를 행렬로 표시함

# 영화 학습
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy  as np

reviews_train = load_files("./csv_data/aclImdb/train")
print(reviews_train["DESCR"])

text_train = reviews_train.data
y_train    = reviews_train.target

# bunch 가 numpy 배열로 주니깐 Dataframe 으로 변경
df = pd.DataFrame(text_train , columns = ["text"])

df["target"] = y_train
df.to_csv("./csv_data/imdb.csv" , encoding = "utf-8-sig" , index = False)
print(df.head())

# 벡터화
# 일종의 비지도 학습 , fit 학습을 하고 transform 을 통해서 문장을 연산 가능한 벡터로 만들어서 반환
vect = CountVectorizer().fit(text_train)
X_train = vect.transform(text_train)

# 컬럼명을 만듬
feature_names = vect.get_feature_names_out()
print("특성의 개수" , len(feature_names))
print("특성 맨 앞 20개" , feature_names[:20])

# 문자열 앞에 'b' 가 오는데 이것은 바이너리의 약자임
# 즉, 쓸모 없는 데이터로 삭제가 필요함 => 쓸데없는 것들 바꿔치기(br 태그)
text_train = [i.replace(b"<br/>" , b"") for i in text_train]

vect = CountVectorizer().fit(text_train)
X_train = vect.transform(text_train)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train , y_train)
print(model.score(X_train , y_train))
"""


from sklearn.datasets import load_files 
import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer 
import matplotlib.pyplot as plt 
import re #정규식 처리 하는 라이브러리 

#파일을 읽는다 - 구분자가 탭키다 
#keep_default_na - NaN 값을 None으로 바꾼다
df_train = pd.read_csv("./csv_data/aclimdb/ratings_train.txt", delimiter="\t", keep_default_na=False)
print( df_train.head() )
text_train, y_train = df_train["document"].values, df_train["label"].values
print( text_train[:3])
print( y_train[:3])

#text_traind을 벡터화하자 
from konlpy.tag import Okt  #현재 가장 많이 사용하는 형태소 분리 알고리즘 
okt = Okt() 
stop_words = ["아", "..", "?", "있는" ]
def okt_tokenizer(text):
    #특수문자를 제거하기 (한글, 숫자, 영어, \s - 공백  )
    text = re.sub(r"[^\uAC00-\uD7A3\s]", "", text)
    temp = okt.morphs(text)
    #제거할거 있으면 제거시켜서 보내기, 불필요한 단어나 한글자는 삭제시키고 나머지만 
    temp = [word for word in temp if word not in stop_words and len(word)>=2]
    return temp 

for i in range(0, 10):
    print( okt_tokenizer(text_train[i] ))

#CountVectorizer의 tokenizer 매개변수에 우리가 토큰나이저 만들어서 주면된다. 
#한글 토큰나이저로 바꿔치기를 한다. 경고는 무시해도 된다. 
vect = CountVectorizer(tokenizer=okt_tokenizer).fit(text_train)

feature_names = vect.get_feature_names_out() 
print("특성의 개수 ", len(feature_names))
print(feature_names[:20])

X_train = vect.transform(text_train)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)
print( model.score(X_train, y_train))