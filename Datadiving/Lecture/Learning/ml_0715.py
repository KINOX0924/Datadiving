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

[6] 라벨링 또는 원핫인코딩 , get_dummies
라벨링
* 성별 , male , female 등 정보가 문자열로 들어오면 연산이 불가능하니깐 male = 0 , female = 1 등으로 말 그대로 라벨링 하는 것
- 라벨링의 범위가 큰 경우 (예: 직업 등)

[7] 스케일링
- 연산이니깐 값의 범위가 너무 차이 나면 큰 값 기준으로 가중치를 결정함
- 서포트벡터머신 하고 딥러닝은 단위가 영향을 미치는 알고리즘임
- 스케일을 맞춤 (비슷한 용어 : 정규화 , 표준화)

평가 지표

- 기본 평가 지표
머신러닝 모델들의 score 함수만을 사용했는데 이게 
"""