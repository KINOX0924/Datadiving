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

# 데이터 준비
data = load_digits()
X = data["data"]
y = data["target"]

print(X.shape)
print(X[:10])

# 이미지 출력 확인
print(data.images[:10])
images = data.images
"""
"""
# 이미지 출력 함수
def drawNumbers() :
    # # 이미지 한개 출력
    # plt.figure(figsize = (10,4))            # figsize : 차트의 크기
    # plt.imshow(images[0] , cmap = "gray_r") # cmap : 팔레트(gray_r : 회색으로 표현)
    # plt.show()

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
"""


"""
# 이미지를 ndarray 로 바꾸는 방법
import PIL.Image as pilimg 
import numpy as np

img = pilimg.open("./images/1.jpg")
print(type(img))

pix = np.array(img) # 이미지가 ndarray 로 변경됨
print(pix.shape)    # 컬러 이미지는 3차원으로 변함

# for i in range(pix.shape[0]) :
#     for j in range(pix.shape[1]) :
#         for k in range(pix.shape[2]) :
#             print("{0:3}".format(pix[i][i][k] , end = " "))
#     print()

# 형식을 바꾸어 저장
img.save("./images/1.bmp")
"""

"""
# 이미지 변환 및 저장
import PIL.Image as pilimg
import os  
# 파이썬에서 os 명령어를 사용할 수 있게 함
# 디렉토리 검색해서 해당 디텍토리의 파일 목록을 통째로 가져옴

import matplotlib.pyplot as plt # 모든 그래픽 출력은 모두 pyplot 로 해야함
import numpy as np
# 특정 폴더의 이미지를 읽어서 전부 numpy 배열로 바꾸고 다 더해서 npz 파일로 저장하기
# 이미지(4차원 , 3차원 이미지가 여러장이라서) 를 2차원 ndarray 로 바꾸는 방법

path = "./images/animal"
filenameList = os.listdir(path) # 해당 경로에 있는 모든 파일을 읽어서 파일 목록을 전달함
print(filenameList)

img_list = []
for filename in filenameList :
    filepath = path + "/" + filename
    temp = pilimg.open(filepath)
    
    # 이미지 크기 축소
    img = temp.resize((80 , 80)) # 튜플로 전달
    img = np.array(img)
    
    # print(img.shape)
    img_list.append(img)

np.savez("data1.npz" , data = img_list)

data1 = np.load("data1.npz")["data"]
plt.figure(figsize = (20 , 5))
for i in range(1 , len(data1) + 1) :
    plt.subplot(1 , 11 , i)
    plt.imshow(data1[i-1])
plt.show()
"""

"""
import PIL.Image as pilimg
import os
import matplotlib.pyplot as plt
import numpy as np

path = "./images/mnist"
filenameList = os.listdir(path)
print(filenameList)

img_list = []
i = 1
for filename in filenameList :
    filepath = path + "/" + filename
    temp = pilimg.open(filepath)
    
    img = temp.resize((80 , 80))
    img = np.array(img)
    
    img_list.append(img)
    i += 1
    if i == 11 : break

np.savez("data2.npz" , data = img_list)

data2 = np.load("data2.npz")["data"]
plt.figure(figsize = (20 , 5))
for i in range(1 , len(data2) + 1) :
    plt.subplot(1 , 11 , i)
    plt.imshow(data2[i-1])
plt.show()
"""

"""
# 제미나이

# 압축을 풀고 daisy , dandalion , rose , sunflower , tulip
# 각 이미지들로 머신러닝을 하고 싶음 , 입력데이터는 무조건 2d , 라벨링은 폴더별로 0 , 1 , 2 , 3 , 4
import os
import PIL.Image as pilimg
import matplotlib.pyplot as plt
import numpy as np

data_path = "./images/flowers"

img_list   = []
label_list = []

# flowers 폴더의 경로를 불러와서 라벨링 번호(i) 와 flowers 폴더를 반복
# flowers 안에 있는 5개의 폴더에 라벨링 번호(i) 를 부여함
class_to_label = {flowers : i for i , flowers in enumerate(sorted(os.listdir(data_path)))}
print("클래스-라벨 매핑 :" , class_to_label)

# class_to_label dict 안에 있는 아이템들(flowers(폴더명) , label) 을 가져옴
# 폴더명과 data_path 를 사용해서 이미지가 있는 경로를 flowers_path 에 저장
for flowers , label in class_to_label.items() :
    flowers_path = os.path.join(data_path , flowers)
    
    # flowers_path 안에 저장된 주소를 타고 들어가 image 의 이름을 하나씩 불러와서 img_file 에 저장
    # 각 이미지의 주소를 flowers_paht 와 img_file 을 사용해서 실제 이미지의 주소 img_path 에 저장
    # img_path 를 사용해서 이미지를 열고 , resize 를 사용해서 이미지 크기를 변환
    # 변환 후 img_list 에는 변환된 이미지를 , label_list 에는 각 이미지에 맞는 라벨을 넣어줌
    for img_file in os.listdir(flowers_path) :
        img_path = os.path.join(flowers_path , img_file)
        
        try :
            img = pilimg.open(img_path)
            img_resize = img.resize((80 , 80))
            
            img_list.append(img_resize)
            label_list.append(label)
        except Exception as err :
            print("[에러]" , err)

# 모든 이미지를 불러오고 나면 성공 메세지 출력
print("이미지 불러오기 성공")

# 불러온 이미지와 라벨을 각각 ndarray 배열로 만들어줌
X = np.array(img_list)
y = np.array(label_list)
print(X.shape)

num_images = X.shape[0]
X_flattened = X.reshape(num_images , -1)

print("최종 2D Array X 의 모양 : " , X_flattened.shape)
print("최종 label y 의 모양 : " , y.shape)
"""

# 강사님 코드
import numpy as np
import pandas as pd
import os
import PIL.Image as pilimg
import imghdr

def makeData(folder , label) :
    data   = []  # 이미지의 피처를 저장
    labels = []  # 라벨 저장
    
    path = "./images/flowers" + "/" + folder
    
    for filename in os.listdir(path) :
        try :
            kind = imghdr.what(path + "/" + filename)   # 파일의 종류를 확인하기 위한 파이썬 명령어
            # 확장자는 윈도우 OS 만 있고 리눅스에는 파일 정보에 종류가 저장되어 있음
            if kind in ["gif" , "png" , "jpg" , "jpeg"] :
                img = pilimg.open(path + "/" + filename)
                # 이미지 크기가 다르면 분석할 수 없어 동일한 이미지 크기로 해야함
                # 이미지 크기가 너무 크면 학습할 때 피쳐 개수가 너무 많아서 학습이 어려움
                # 적당한 크기로 이미지를 잘라야함
                
                resize_img = img.resize((80 , 80))  # 이미지 크기 변경
                pixel = np.array(resize_img)        # 크기가 변환된 이미지를 ndarrary 로 변경
                
                if pixel.shape == (80 , 80 , 3) :   # 이미지 크기가 같은 것만 취급
                    data.append(pixel)
                    labels.append(label)
        except :
            print(filename + "error")   # 어떤 파일이 에러인지 찾아서 직접 삭제
    np.savez("{}.npz".format(folder) , data = data , targets = labels)
    
# [1] 파일로 저장하기
def filesave() :
    makeData("daisy" , "0")
    makeData("dandelion" , "1")
    makeData("rose" , "2")
    makeData("sunflower" , "3")
    makeData("tulip" , "4")

# [2] 파일 불러오기
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


# data 차원을 2차원으로 변경
# 4차원 머신 러닝 , 딥러닝 => 딥러닝(CNN : 합성곱신경망)
# 사람과 같은 4차원을 그대로 받아들이는 딥러닝
data_list = data_list.reshape(data_list.shape[0] , 80 * 80 * 3)
print(data_list.shape)

# 머신러닝의 일부 알고리즘과 딥러닝은 반드시 정규화를 해주어야함(또는 스케일링)
# 0 부터 1 사이의 값으로 축소시키는 것이 유리함
data_list = data_list/255.0


from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(data_list , target , random_state = 0 , test_size = 0.5)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors = 3)

model.fit(X_train , y_train)

print("훈련세트 : " , model.score(X_train , y_train))
print("테스트세트 : " , model.score(X_test , y_test))
