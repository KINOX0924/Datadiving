"""
머신러닝 , 기계학습
[1] 분류 또는 회귀
[1-1] 분류는 반드시 데이터가 '범주형' 이어야함
    범주형의 예:)) 타이타닉에서 생존자 분류하기(생존자가 생존할 확률 - 생존 예측)
    범주형의 예:)) 암환자 예측 , 종류 예측(카테고리)
    분류의 첫번째 모델은 로지스틱회귀분석

[1-2] 회귀는 연속적 값들 , 키(사람의 키) , 부동산 가격 , 대기중 이산화탄소 양 예측 등의 것들
    예:)) 방사능의 양은 회귀지만, 방사능의 양에 따라 사람이 죽느냐 마느냐를 예측하는 것은 분류
    회귀의 첫번째 모델은 선형회귀모델

* 회귀는 실수값으로 말해야하고 , 분류는 확률로 결과를 말해야함

[2] 휴리스틱분석 과정
    어림짐작으로 경험치를 사용해서 분석을 하며, 결과가 안 맞으면 처음부터 다시 진행됨
[2-1] 데이터 수집
    어떤 특성이 결과에 영향을 미칠지 알 수 없음 , 그래서 일단 아무거나 수집함
    * 결측치 - 어떤 특성이 NaN 값이 절반을 넘음 , 완전히 특성제거를 할지 아니면 대체값으로 대체를 할지,
            대체값이 평균을 할지 중간값(회귀)으로 할지 아니면 최빈수(분로)로 할지 특성의 성격에 따라 각기 다른 대응 필요
    * 이상치 제거 - 지나치게 이상한 값들 제거하기 위해서 IQR 을 많이 사용함
    * 중복치 제거 - 데이터 수집 단계에서 잘못 수집된 것들을 제거하는 것
    범주형 타입의 경우 특성의 타입이 문자열이거나 또는 숫자라도 카테고리타입을 지정해주어야함
    라벨인코딩(범주의 범위가 작을때) , 원핫인코딩(범주의 범위가 클때)
    
[2-2] 모델을 결정해서 학습 진행
    모델을 걸정하고 학습을 하고 이 모델이 실제 데이터를 맞출지 안 맞출지를 확신이 서지 않음
    따라서 최소한 데이터를 훈련세트와 테스트셋으로 나누고 ,
    훈련셋을 기반으로 학습을 하고 그 다음에 테스트셋을 가지고 테스트를 함
    그 뒤 평가를 진행하며 이 때 회귀와 분류에 따라서 평가 방법이 다름
    * 목표 : 일반화(특정 데이터셋에 맞춰지는 것이 아니라 새로운 데이터셋에도 적용되 되어야함)
        - 과소 적합 : 학습이 덜 된 상태 , 훈련셋도 예측율이 낮고 테스트셋도 낮음
                    하지만 원래 데이터셋이 너무 작은 경우 그 작은 예측율이 과대적합일 수도 있음
        - 과대 적합 : 지나치게 학습이 많이 된 상태 , 훈련셋 예측률과 테스트셋 예측률이 차이가 많이 나는 경우를 과대 적합이라고 함
        * 데이터셋이 많아야함
        * 특성이 너무 많아도 과대적합이 일어남 : 특성이 많아지면 모델 내부가 너무 복잡해져서 과대적합이 일어남
        그래서 중요 특성만 추출(의사결정트리) 등을 통해서 특성을 제거시키거나 PCA(주요성분분석) 등으로 특성들을 조작(과정을 거쳐서) 새로운 특성을 만들어냄
        * 알고리즘들에 있는 하이퍼파라미터를 조절하여 적절한 값을 찾아내야함(그리드서치(옵투나) 나 파리프라인 등을 활용)
        * 서포트벡터머신 , 랜덤포레스트(앙상블) , 그라디언트부스팅(xgboost)
        * 스케일링 : 단위 맞춰주기 , 서포트 벡터머신하고 딥러닝에 유용함
[2-3] 검증하기(kfold)
"""

"""
# 범주형 자료의 경우를 처리하는 방법
# 범주형 자료가 문자열로 들어오는 경우도 있고 , 숫자형 형태인경우(1 = 대 , 2 = 중 , 3 = 소) 등
# 범주형 데이터를 정확히 찾아서 범주형으로 바꾸어주고 라벨링이나 원핫인코딩을 하는 것

# 결과는 문자열도 알아서 처리하고 있어서 굳이 우리쪽에서 추가적인 작업을 할 필요가 없음
# 입력데이터는 반드시 처리 작업을 진행해주어야 함

import mglearn.datasets
import pandas as pd
import numpy  as np
import mglearn
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 데이터를 가져오고 , 필드명 붙히기
data = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH , "adult.data") , header = None , index_col = False ,
                    names = ['age', 'workclass', 'fnlwgt', 'education',  'education-num',
                             'marital-status', 'occupation', 'relationship', 'race', 'gender',
                             'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                             'income']
                    )
print(data.head())

# 사람별로 수익을 예측하기 위해 필요한 데이터만 가져옴
data = data[["age" , "workclass" , "education" , "gender" , "hours-per-week" , "occupation" , "income"]]    # 마지막 필드가 타겟
print(data.head())

# get_dummies : 스스로 더미 데이터를 만들어 넣고 값을 바꾸어줌
data = pd.get_dummies(data)
print(data.head())
print(data.columns)

# 타겟이 있는 바람에 타겟도 원핫인코딩이 된 상태
X = data.loc[: , "age" : "occupation_ Transport-moving"]    # loc 를 써서 필드를 가져올때는 넣은 필드명까지를 가져옴
print(X.head())

y = data.loc[: , "income_ >50K"]
print(y.head())

# 모델 선택 후 학습 진행
model = LogisticRegression()
model.fit(X , y)

print(model.score(X , y))
"""

"""
# 특성이 원래는 카테고리인데 숫자 형태로 입력될 경우 처리 방법
# get_dummies 함수 : 숫자형의 범주데이터를 범주로 파악하지 못함(숫자로 들어오는 값을 범주로 이해하지 못함)
import pandas as pd
import numpy  as np
from sklearn.preprocessing import OneHotEncoder # 원핫인코더 라이브러리

demo_df = pd.DataFrame({
        "숫자특성" : [0 , 1 , 2 , 1] ,
        "범주형특성" : ["양말" , "여우" , "양말" , "상자"]
    })

df1 = pd.get_dummies(demo_df)
print(df1)

# 첫번째 특성에 대해서는 그냥 숫자로 받아들이고 , 두번째 특성은 문자열의 경우만 범주로 받음
# 첫번쨰 특성을 문자열 또는 카테고리형으로 바꾼 뒤 다시 get_dummies 함수 실행
# demo_df["숫자특성"] = demo_df["숫자특성"].astype(str)
# df1 = pd.get_dummies(demo_df)
# print(df1)

# OneHotEncoder 클래스를 사용
# sparse_output = False : 희소 행렬이거나 , numpy 배열이거나 False 일 경우 , numpy 배열로 반환함
ohe = OneHotEncoder(sparse_output = False)
# OneHotEncoder 반환값을 별도로 받아야하는데 리턴값이 numpy 배열 형태임
n = ohe.fit_transform(demo_df)  # fit -> transform
print(ohe.get_feature_names_out())  # 필드 이름만 반환
print(n)    # 이 리턴값을 입력값으로 사용해야함
"""

"""
# 전처리 작업
# ColumnTransFormer 클래스
# 컬럼 단위로 전처리 작업을 해야할 때 쭉 지정해놓으면 이것저것 적용을 해줌
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import mglearn.datasets
import pandas as pd
import os

# 데이터를 가져오고 , 필드명 붙히기
data = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH , "adult.data") , header = None , index_col = False ,
                    names = ['age', 'workclass', 'fnlwgt', 'education',  'education-num',
                             'marital-status', 'occupation', 'relationship', 'race', 'gender',
                             'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                             'income']
                    )
print(data.head())

# 사람별로 수익을 예측하기 위해 필요한 데이터만 가져옴
data = data[["age" , "workclass" , "education" , "gender" , "hours-per-week" , "occupation" , "income"]]    # 마지막 필드가 타겟

st = ColumnTransformer([
    ("scaling" , StandardScaler() , ["age" , "hours-per-week"]) ,
    ("onehot" , OneHotEncoder(sparse_output = False) , ["workclass" , "education" , "gender" , "occupation"])
])

st.fit(data)
print(st.transform(data))
"""

"""
# 하이퍼파라미터
import numpy  as np
import pandas as pd
from sklearn.datasets import load_iris , load_breast_cancer
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.svm import SVC # SVC 가 하이퍼파라미터가 많음
from sklearn.metrics import classification_report , accuracy_score
# classfication_report = 분류 모델 중에서도 이진 분류 평가 라이브러리
# accuracy_score = 단순 정확도 판단 기준 평가 라이브러리

# GridSearchCV : 파라미터를 주면 각 파라미터 별로 전체 조합을 만들어서 다 돌려봄

data_set = load_breast_cancer()
X = data_set.data
y = data_set.target

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234)

# 파라미터 설정하기
# 우리가 직접 학습을 진행하는 것이 아니고 GridSearchCV 함수에 학습을 맡기는 것

param_grid = {
    "svc" : {
        "C"      : [0.1 , 1 , 10 , 100] ,    # 오차 사용범위를 조절 , 내부적으로 오차를 조율하는데 오차의 허용 범위를 설정함 (값이 크면 과대적합)
        "gamma"  : [1, 0.1 , 0.01 , 0.001] , # 커널의 영향 범위를 설정 , 클수록 과대적합
        "kernel" : ["rbf" , "linear"]        # 비선형(데이터가 비선형일때 좋음) , 선형구조(데이터가 선형일 떄)
    
    } ,
    "random_forest" : {
        "n_estimators" : [50 , 100 , 200] ,      # 트리의 총 개수
        "max_depth"   : [None , 3 , 10 , 20] ,  # 최대 깊이
        "min_samples_split" : [2 , 5 , 10]      # 가지치기 개수
    } ,
    "gradient_boosting" : {
        "n_estimators" : [50 , 100 , 200] ,
        "max_depth"   : [None , 3 , 10 , 20] ,
        "learning_rate" : [0.01 , 0.1 , 0.2]    # 학습율
    }
}

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
results = []
models = {
    'svc':SVC(),
    'random_forest':RandomForestClassifier(),
    'gradient_boosting':GradientBoostingClassifier()
}

results = {}
models = {
    'svc': SVC(),
    'random_forest': RandomForestClassifier(random_state=42),
    'gradient_boosting': GradientBoostingClassifier(random_state=42)
}

#모델에 저장된요소마다 파라미터를 이용해 적용해 본다. 
for model_name, model in models.items():
    print(f"Running GridSearchCV for {model_name}...")
    grid = GridSearchCV(estimator=model, 
                        param_grid=param_grid[model_name], cv=5, verbose=2, scoring='accuracy')
    grid.fit(X_train, y_train)
    results[model_name] = {
        'best_params': grid.best_params_,
        'best_score': grid.best_score_,
        'best_model': grid.best_estimator_
    }

# 4. 테스트 데이터에 대한 성능 평가
for model_name, result in results.items():
    print(f"\nModel: {model_name}")
    print("Best Parameters:", result['best_params'])
    print("Best Cross-Validation Score:", result['best_score'])
    
    # 테스트 데이터로 예측
    y_pred = result['best_model'].predict(X_test)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("Test Set Accuracy:", accuracy_score(y_test, y_pred))
"""

"""
# 일단은 파라미터 없는 SVC 이용
no_parm_SVC = SVC()
no_parm_SVC.fit(X_train , y_train)
print("훈련셋 평가 : " , no_parm_SVC.score(X_train , y_train))
print("테스트셋 평가 : " , no_parm_SVC.score(X_test , y_test))

grid = GridSearchCV(estimator = no_parm_SVC , param_grid = param_grid , cv = 5 , verbose = 2 , scoring = "accuracy")
# estimator  = 학습모델 객체전달
# param_grid = 파라미터로 쓸 대상
# cv         = kfold 검증 , 데이터가 충분히 많으면 10까지 가능
# verbose    = 출력로그 || 0 : 없음 , 1 : 간단 , 2 : 자세히
# scoring    = 평가 수단을 정확도에 맞춤

grid.fit(X_train , y_train)
print("최적의 파라미터")
print(grid.best_params_)

print("최고 스코어")
print(grid.best_score_)


# parm_svc = grid.best_estimator_
# parm_svc = SVC(C = 10 , gamma =1 , kernel = "linear")
# parm_svc.fit(X_train , y_train)

# print("훈련셋 평가 : " , parm_svc.score(X_train , y_train))
# print("테스트 평가 : " , parm_svc.score(X_test , y_test))
"""

# 데이터 작업 순서
# 필요없는 순서 제거(passengerId , name , SibSp , Parch)
# 각 필드명 결측치 확인 후 제거(열 또는 행) , 또는 지나치게 결측치가 많은 경우에는 대체값(평균 , 중간값(비범주형일때는 평균 또는 중간값) , 최빈값(범주형))
# 이상치 제거
# 중복값 제거
# 데이터 자체가 잘못 들어온 값 제거(Value_counts 함수나 Unique 로 체크하기) - 체크 후 값바꾸기 또는 행을 삭세
# 라벨링 또는 원핫인코딩
# 스케일링(서포트벡터머신에 도움이 됨)
# 학습하고 특성의 개수가 많을 경우는 특성의 중요도 확인(DecisionTree 를 많이 사용)
# 주성분 분석
# 여러가지 모델로 학습하기 , GridSearchCV

"""
import pandas as pd
import numpy  as np
from sklearn.preprocessing import OneHotEncoder

# 데이터 가져오기
train_data = pd.read_csv("./csv_data/titanic_train.csv")
print(train_data.head())

# 필요없는 데이터 제거
train_data = train_data[["Pclass" , "Sex" , "Age" , "Ticket" , "Fare" , "Embarked"]]
y = train_data[["Survived"]]
print(train_data.head())

# 결측치 확인 후 제거
print(train_data.isnull().sum())

mean_age     = train_data["Age"].mean()
train_data["Age"].fillna(mean_age , inplace = True)
train_data["Embarked"] = train_data["Embarked"].replace(np.nan , "C")

print(train_data.isnull().sum())

# 이상치 , 중복값 , 잘못된 입력값 제거
print(train_data.value_counts())

ohe = OneHotEncoder(sparse_output = False)
n   = ohe.fit_transform(train_data)
print(ohe.get_feature_names_out())
print(n)
"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # 중요도 파악
from sklearn.preprocessing import StandardScaler
import os   #파일이나 폴더 경로를 정확히 지정하기 위함
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
import seaborn as sns

# [1] 데이터 가져오기
train = pd.read_csv("./csv_data/titanic_train.csv")
test  = pd.read_csv("./csv_data/titanic_test.csv")

# [2] 불필요한 열 삭제
print(train.head())

train = train.drop(columns = ["PassengerId" , "Name" , "SibSp" , "Parch" , "Cabin"])
test  = test.drop(columns = ["PassengerId" , "Name" , "SibSp" , "Parch" , "Cabin"])

# 선택한 열이 삭제되었는 지 확인
print(train.head())
print(test.head())

# [3] 결측치 제거
print(train.isna().sum())   # 결측치 확인 , Age = 177개 , Embarked = 2개
print(test.isna().sum())    # 결측치 확인 , Age = 86개 , Fare = 1개
# Age , Embarked , Fare 는 평균값으로 대체

print(train.describe()) # 평균값을 쓸 지 말지 , 이상치가 있는 지 먼저 확인

# 평균값으로 대체
mean_age_tr = train["Age"].mean()
train["Age"].fillna(mean_age_tr , inplace = True)
print("TRAIN : " , train.isna().sum())

mean_age_ts = test["Age"].mean()
test["Age"].fillna(mean_age_ts , inplace = True)
print("TEST : " , test.isna().sum())

# NaN 값 제거
train = train.dropna(axis = 0 , how = "any")
test  = train.dropna(axis = 0 , how = "any")
print("TRAIN : " , train.isna().sum())
print("TEST : " , test.isna().sum())

# [4] 이상치 제거
train.boxplot()
plt.show()

def outfliers_iqr(data) :
    q1 , q3 = np.percentile(data , [25 , 75])
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return lower_bound , upper_bound

# 두 개의 필드 Fare , Age 필드에서 이상치가 발견되어 이상치 제거
for i in ["Fare" , "Age"] :
    lower , upper = outfliers_iqr(train[i])
    train[i][train[i] < lower] = lower
    train[i][train[i] > upper] = upper
    
for i in ["Fare" , "Age"] :
    lower , upper = outfliers_iqr(test[i])
    test[i][test[i] < lower] = lower
    test[i][test[i] > upper] = upper

train.boxplot()
plt.show()

# [5] 원핫인코딩
train = pd.get_dummies(train)
print(train.head())

"""
# 산포도 행렬 또는 상관계수 그리기
# print(train.corr()) # 상관계수를 구할 수 없는 필드들이 있어서 그려지지 않음
sns.pairplot(train , diag_kind = "kde" , hue = "Survived" , palette  = "bright")
plt.show()
"""
# [6] 데이터와 타켓으로 나누기
X = train.iloc[: , 1:]
y = train.iloc[: , 0]
print(X.shape)
print(y.shape)

# [7] 모델 선택 , 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators = 100)
model.fit(X , y)
print(model.score(X , y))