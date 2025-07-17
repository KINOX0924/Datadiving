# 머신러닝과 딥러닝의 차이점
# 머신러닝 알고리즘은 함수들의 매개변수를 조작하여, 정답률을 높여나가는 방식
# 딥러닝은 학습을 하고 오차를 수정하여 반영하여 다시 학습하는 행동을 반복적으로 하면서 학습의 적중률을 높여나감
# 딥러닝은 머신 러닝의 특정한 한 분야로서 연속된 층에서 점진적으로 의미있는 표현을 배우는 데 강점이 있음

# 딥러닝을 지원하는 파이썬 라이브러리
# 사이킷런 : 머신러닝을 지원하는 라이브러리
# Tensorflow : 구글이 제공하는 딥러닝 라이브러리 , C 언어로 구성되어 있으나 파이썬은 언더 구조상 C 언어로 작성된 라이브러리를 쉽게 사용 가능
# keras : Tensorflow 의 직접 사용이 어렵기 때문에 Tensorflow 사용하기 쉽게 만들어주는 라이브러리이며 현재 가장 많이 사용되고 있음

# 환경변수 만들기
# conda create -n dlearning_env python=3.9 -y

# 환경 활성화
# conda activate dlearning_env

# 텐서플로우 설치
# conda install tensorflow

# 설치 후 테스트
# python => import tensorflow
# 아무런 반응도 없으면 설치가 잘 된 것

"""
from tensorflow import keras
from keras.datasets import mnist
import tensorflow as tf


tf.random.set_seed(1234)

# 1. 데이터 가져오기
(train_images , train_labels) , (test_images , test_labels) = mnist.load_data()

print(type(train_images) , type(train_labels))
print(train_images.shape , train_labels.shape)
print(test_images.shape , test_labels.shape)

# 2. 딥러닝 모델(또는 네트워크) 만들기(설계)
from keras import models , layers

# 네트워크 또는 모델이라고 부름
# keras.Sequential 로 모델을 만드는데 매개변수로 list 타입 안에 레이어 객체를 전달함
model = keras.Sequential([
    # 2.1 입력층을 설계함
    # layers.Dense(출력값의 개수 , 활성화함수 , 입력데이터의 크기 - 생략가능)
    # 출력값의 개수 : 저 계층을 나왔을 때 가져올 가중치의 개수
    # 가중치의 개수를 너무 크게 주면 메모리 부족도 발생하고, 과대적합 문제도 발생할 수 있음 , 설정 시에는 주로 2의 배수로 설정함
    layers.Dense(64 , activation = "relu") ,
    
    # 2.2 중간에 다른 층 추가 가능
    layers.Dense(128 , activation = "relu") ,
    layers.Dense(256 , activation = "relu") ,
    layers.Dense(64 , activation = "relu") ,
    # 2.3 출력층 , 마지막 층은 라벨에 맞춤 , 즉 결과를 얻기 위한 층
    # 지금 데이터의 경우 손으로 쓴 숫자이깐 0 ~ 9 까지 10개 중에 하나이어야 함
    # 딥러닝의 분류를 출력데이터를 확률로 반환함
    # 각 층을 거치면서 나오는 값들은 실제는 확률이 아니고 엄청 큰 값들임
    # 이것들을 모두 합해서 1이 되는 확률로 전환해야 하는데 이 함수가 softmax 함수
    # 다중 분류의 출력층의 활성화 함수는 무조건 softmax 함수임
    layers.Dense(10 , activation = "softmax")
    
    # 출력층은 회귀 , 이진 분류 , 다중 분류랑 다 다르게 작성해야 함
    # 회귀는 출력결과 1개 작성 : layers.Dense(1)
    # 이진 분류의 경우 : layers.Dense(1 , activation = "sigmoid")
    # 다중 분류의 경우 : layers.Dense(1 , activation = "softmax")
])

# 3. 컴파일 과정
# 손실함수 , 옵티마이저 , 평가지표 지정
model.compile(
    optimizer = "rmsprop" ,
    loss = "sparse_categorical_crossentropy" ,   # 머신러닝은 라벨은 원핫인코딩이 필요없지만 딥러닝에서는 원핫인코딩이 필요함 , 이것이 그 코드
    metrics = ["accuracy"]
    )

# 4. 데이터 관련 작업
# 차원 변환 3 차원 > 2 차원
# 스케일링 : 딥러닝에서는 필수

train_images = train_images.reshape(train_images.shape[0] , 28 * 28)
train_images = train_images.astype(float) / 255

test_images = test_images.reshape(test_images.shape[0] , 28 * 28)
test_images = test_images.astype(float) / 255   # 스케일링

# loss = "sparse_categorical_crossentropy" <= 이 코드를 작성 안했으면 라벨도 원핫인코딩을 진행해주어야 함(머신러닝하고의 차이점)

# 5. 학습하기
# 학습하는 과정 속에 있었던 내용(History) 를 반환
hist = model.fit(
    train_images ,  # x , 독립변수 , 입력값
    train_labels ,  # y , 종속변수 , 목표 , 출력값
    epochs = 10 ,    # 학습 회수
    batch_size = 128
    # 데이터를 메모리를 불러올 때의 크기 지정 , 너무 크면 메모리 부족이 생기고 , 너무 작으면 속도가 느려짐
    # 전체 데이터를 batch_size 만큼 불러서 학습이 끝나는 1회 순환은 1 epochs 라고 함
    )

# 6. 평가(evaluate)
train_loss , train_acc = model.evaluate(train_images , train_labels)
print(f"훈련세트 손실 {train_loss} , 정확도 {train_acc}")

test_loss , test_acc = model.evaluate(test_images , test_labels)
print(f"테스트세트 손실 {test_loss} , 정확도 {test_acc}")
"""

"""
# 사이킷런의 iris 로 딥러닝하기
# 1. 데이터 가져오기

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf
from keras import models , layers

iris_data = load_iris()

X = iris_data["data"]
y = iris_data["target"]

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234 , test_size = 0.3)

# 2. 딥러닝 모델 설계
model = keras.Sequential([
    layers.Dense(64 , activation = "relu") ,
    layers.Dense(64 , activation = "relu") ,
    layers.Dense(3 , activation = "softmax")
])

model.compile(
    optimizer = "rmsprop" ,
    loss = "sparse_categorical_crossentropy" ,
    metrics = ["accuracy"]
)

# 3. 데이터 처리(차원변환 , 스케일링)
"""
"""
from sklearn.preprocessing import StandardScaler
scaler = StrandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.fit_transform(X_test)

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test  = to_categorical(y_test)
"""
"""
X_train = X_train.reshape(X_train.shape[0] , 2 * 2)
X_train = X_train.astype(float) / 255

X_test = X_test.reshape(X_test.shape[0] , 2 * 2)
X_test = X_test.astype(float) / 255

# from keras.utils import to_categorical
# y_train = to_categorical(y_train)
# y_test  = to_categorical(y_test)

hist = model.fit(
    X_train ,
    y_train ,
    epochs = 30 ,
    batch_size = 100
)

train_loss , train_acc = model.evaluate(X_train , y_train)
print(f"훈련세트 손실 {train_loss} , 정확도 {train_acc}")

test_loss , test_acc = model.evaluate(X_test , y_test)
print(f"테스트세트 손실 {test_loss} , 정확도 {test_acc}")
"""

import numpy as np

def fileload() :
    daisy_data     = np.load("daisy.npz")
    dandelion_data = np.load("dandelion.npz")
    rose_data      = np.load("rose.npz")
    sunflower_data = np.load("sunflower.npz")
    tulip_data     = np.load("tulip.npz")
    
    data_list = np.concatenate(
        (
            daisy_data["data"] ,
            dandelion_data["data"] ,
            rose_data["data"] ,
            sunflower_data["data"] ,
            tulip_data["data"]
        )
    )
    
    target = np.concatenate(
        (
            daisy_data["targets"] ,
            dandelion_data["targets"] ,
            rose_data["targets"] ,
            sunflower_data["targets"] ,
            tulip_data["targets"]
        )
    )
    
    print(data_list.shape)
    print(target.shape)
    
    return data_list , target

data_list , target = fileload()

data_list = data_list.reshape(data_list.shape[0] , 80 * 80 * 3)
print(data_list.shape)

data_list = data_list.astype(float) / 255

from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(data_list , target , random_state = 1234 , test_size = 0.5)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.fit_transform(X_test)

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)
y_test  = to_categorical(y_test)

from tensorflow import keras
from tensorflow.keras import models , layers
model = keras.Sequential([
    layers.Dense(128 , activation = "relu") ,
    layers.Dense(64 , activation = "relu") ,
    layers.Dense(5 ,   activation = "softmax")
])

model.compile(
    optimizer = "rmsprop" ,
    loss = "categorical_crossentropy" ,
    metrics = ["accuracy"]
)

hist = model.fit(
    X_train_scaled , 
    y_train ,
    epochs = 10 ,
    batch_size = 100
)

train_loss , train_acc = model.evaluate(X_train_scaled , y_train)
print(f"훈련세트 손실 {train_loss} , 정확도 {train_acc}")

test_loss , test_acc = model.evaluate(X_test_scaled , y_test)
print(f"테스트세트 손실 {test_loss} , 정확도 {test_acc}")