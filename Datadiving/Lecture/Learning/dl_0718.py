"""
# 꽃 분류 딥러닝
import numpy as np 
import os 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 
import tensorflow as tf

# 1. 데이터 만들기
# folder 를 읽어서 데이터 생성
base_path = "D:/Dataset/flowers_2"
def makeData(flower_name , label , isTrain = True) :
    if isTrain :
        path = base_path + "/train/" + flower_name
    else :
        path = base_path + "/test/" + flower_name
    
    # print(path)
    
    data = []
    labels = []
    # print(os.listdir(path))
    # 해당 경로에 파일명을 모두 가져온다
    # 파일 하나씩 읽어서 넘파이 배열로 만들어서 data 에 추가시키기
    
    i = 1
    
    for filename in os.listdir(path) :
        try :
            if i % 100 == 0 :
                print(f"{i} 번째 파일 처리 중")
                
            # 파일 속성도 확인
            kind = imghdr.what(path + "/" + filename)
            if kind in ["gif" , "png" , "jpeg" , "jpg"] :   # 이미지일 때만
                img = pilimg.open(path + "/" + filename)
                resize_img = img.resize((80 , 80))
                # 사이즈는 특성이 너무 많으면 계산 시간도 오래걸리고 , 크기가 각각이면 학습이 불가능하여 크기를 맞춰줌
                    
                pixel = np.array(resize_img)
                if pixel.shape == (80 , 80 , 3) :
                    data.append(pixel)
                    labels.append(label)
            
            i += 1
        except :
            print(filename + "error")
    
    title = "train"
    
    if not isTrain :
        title = "test"
        
    savefileName = "imagedata{}.npz".format(str(label) + "_" + title)
    np.savez(savefileName, data = data , targets = labels)

def initData() :
    flowers = ["daisy" , "dandelion"]
    i = 0
    for flower in flowers :
        makeData(flower , i , True)
        makeData(flower , i , False)
        i += 1
        
# 로드 데이터
def loadData() :
    pass
    file1 = np.load("D:/Dataset/flowers_2/imagedata0_train.npz")
    file2 = np.load("D:/Dataset/flowers_2/imagedata1_train.npz")
    
    d1 = file1["data"]
    t1 = file1["targets"]
    
    d2 = file2["data"]
    t2 = file2["targets"]
    
    X_train = np.concatenate((d1 , d2) , axis = 0)
    Y_train = np.concatenate((t1 , t2) , axis = 0)
    
    
    file1 = np.load("D:/Dataset/flowers_2/imagedata0_test.npz")
    file2 = np.load("D:/Dataset/flowers_2/imagedata1_test.npz")
    
    d1 = file1["data"]
    t1 = file1["targets"]
    
    d2 = file2["data"]
    t2 = file2["targets"]
    
    X_test = np.concatenate((d1 , d2) , axis = 0)
    Y_test = np.concatenate((t1 , t2) , axis = 0)
    
    return X_train , X_test , Y_train , Y_test

from tensorflow.keras import models , layers

def createModel() :
    network = models.Sequential(
        [
            layers.Dense(128 , activation = "relu") ,
            layers.Dense(64 , activation = "relu") ,
            layers.Dense(64 , activation = "relu") ,
            layers.Dense(32 , activation = "relu") ,
            layers.Dense(2 , activation = "softmax")
        ]
    )
    
    network.compile(
        optimizer = "rmsprop" ,
        loss      = "sparse_categorical_crossentropy" ,
        metrics   = ["accuracy"] ,
        )
    
    return network

from sklearn.preprocessing import StandardScaler
def preprocessing() :
    X_train , X_test , Y_train , Y_test = loadData()
    # 차원이 현재 4차원에서 2차원으로
    
    X_train = X_train.reshape(X_train.shape[0] , 80 * 80 * 3)
    X_test  = X_test.reshape(X_test.shape[0] , 80 * 80 * 3)
    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.fit_transform(X_test)
    
    return X_train_scaled , Y_train , X_test_scaled , Y_test
    
def main() :
    X_train , Y_train , X_test , Y_test = preprocessing()
    network = createModel()
    network.fit(X_train , Y_train , epochs = 100 , batch_size = 100)
    
    train_loss , train_acc = network.evaluate(X_train , Y_train)
    test_loss  , test_acc  = network.evaluate(X_test  , Y_test)
    
    print(f"훈련셋 손실값 : {train_loss} , 정확도 : {train_acc}")
    print(f"테스트셋 손싧값 : {test_loss} , 정확도 : {test_acc}")

if __name__ == "__main__" :
    # initData()
    main()
"""

"""
# 딥러닝 = 회귀 , 이진분류 , 다중분류 모두 가능
# 보스톤 집값 회귀 분석
import numpy  as np
import pandas as pd
import os
import tensorflow as tf
from tensorflow.keras.datasets import boston_housing

(X_train , y_train) , (X_test , y_test) = boston_housing.load_data()

# 잘 정리된 '회귀자료' 이기 때문에 스케일링 작업만 해주면 됨
print(X_train.shape)
print(X_train[:5])
print(y_train.shape)
print(y_train[:5])

# 스케일링 진행
from sklearn.preprocessing import Normalizer
normal = Normalizer()

X_train_scaled = normal.fit_transform(X_train)
X_test_scaled  = normal.fit_transform(X_test)

from tensorflow.keras import models , layers
def makeModel() :
    model = models.Sequential(
        [   # tensorflow 2.1 부터는 input_shape 는 생략가능
            layers.Dense(512 , activation = "relu" , input_shape = ((13,))) ,
            layers.Dense(256 , activation = "relu") ,
            layers.Dense(128 , activation = "relu") ,
            layers.Dense(64  , activation = "relu") ,
            layers.Dense(32  , activation = "relu") ,
            layers.Dense(16  , activation = "relu") ,
            layers.Dense(1) # 회귀의 경우는 무조건 1 이며 연산결과 딱 하나만 가져옴
        ]
    )
    
    model.compile(
        optimizer = "rmsprop" ,
        loss      = "mse"     ,
        metrics   = ["mae"]
    )
    
    return model


network = makeModel()
network.fit(X_train_scaled , y_train , epochs = 10 , batch_size = 100)

train_loss , train_acc = network.evaluate(X_train_scaled , y_train)
test_loss  , test_acc  = network.evaluate(X_test_scaled , y_test)

print(f"훈련셋 손실값 : {train_loss} , mae : {train_acc}")
print(f"테스트셋 손싧값 : {test_loss} , mae : {test_acc}")
"""

"""
# 암환자 데이터(이진 분류)
import numpy as np 
import os 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 
import tensorflow as tf

# 1. 데이터 만들기
# folder 를 읽어서 데이터 생성
base_path = "D:/Dataset/flowers_2"
def makeData(flower_name , label , isTrain = True) :
    if isTrain :
        path = base_path + "/train/" + flower_name
    else :
        path = base_path + "/test/" + flower_name
    
    # print(path)
    
    data = []
    labels = []
    # print(os.listdir(path))
    # 해당 경로에 파일명을 모두 가져온다
    # 파일 하나씩 읽어서 넘파이 배열로 만들어서 data 에 추가시키기
    
    i = 1
    
    for filename in os.listdir(path) :
        try :
            if i % 100 == 0 :
                print(f"{i} 번째 파일 처리 중")
                
            # 파일 속성도 확인
            kind = imghdr.what(path + "/" + filename)
            if kind in ["gif" , "png" , "jpeg" , "jpg"] :   # 이미지일 때만
                img = pilimg.open(path + "/" + filename)
                resize_img = img.resize((80 , 80))
                # 사이즈는 특성이 너무 많으면 계산 시간도 오래걸리고 , 크기가 각각이면 학습이 불가능하여 크기를 맞춰줌
                    
                pixel = np.array(resize_img)
                if pixel.shape == (80 , 80 , 3) :
                    data.append(pixel)
                    labels.append(label)
            
            i += 1
        except :
            print(filename + "error")
    
    title = "train"
    
    if not isTrain :
        title = "test"
        
    savefileName = "imagedata{}.npz".format(str(label) + "_" + title)
    np.savez(savefileName, data = data , targets = labels)

def initData() :
    flowers = ["daisy" , "dandelion"]
    i = 0
    for flower in flowers :
        makeData(flower , i , True)
        makeData(flower , i , False)
        i += 1
        
# 로드 데이터
def loadData() :
    pass
    file1 = np.load("D:/Dataset/flowers_2/imagedata0_train.npz")
    file2 = np.load("D:/Dataset/flowers_2/imagedata1_train.npz")
    
    d1 = file1["data"]
    t1 = file1["targets"]
    
    d2 = file2["data"]
    t2 = file2["targets"]
    
    X_train = np.concatenate((d1 , d2) , axis = 0)
    Y_train = np.concatenate((t1 , t2) , axis = 0)
    
    
    file1 = np.load("D:/Dataset/flowers_2/imagedata0_test.npz")
    file2 = np.load("D:/Dataset/flowers_2/imagedata1_test.npz")
    
    d1 = file1["data"]
    t1 = file1["targets"]
    
    d2 = file2["data"]
    t2 = file2["targets"]
    
    X_test = np.concatenate((d1 , d2) , axis = 0)
    Y_test = np.concatenate((t1 , t2) , axis = 0)
    
    return X_train , X_test , Y_train , Y_test

from tensorflow.keras import models , layers

def createModel() :
    network = models.Sequential(
        [
            layers.Dense(128 , activation = "relu") ,
            layers.Dense(64  , activation = "relu") ,
            layers.Dense(64  , activation = "relu") ,
            layers.Dense(32  , activation = "relu") ,
            layers.Dense(1   , activation = "sigmoid")
            # 이진 분류의 경우 결과값 1개이고 , 활성화함수는 sigmoid 를 사용
            # 암인지 아닌지를 물어봐야함 , Data target 이 0 이 악성이었고 , 1 이 양성
            # 1이 될 확률을 출력 > 예측 확률 > 양성일 확률이 출력됨
            # 악성이 될 확률은 1 - 양성확률
        ]
    )
    
    network.compile(
        optimizer = "rmsprop" ,
        loss      = "binary_crossentropy" ,
        # loss 가 이진분류 일때는 binary_crossentropy
        metrics   = ["accuracy"] ,
        )
    
    return network

from sklearn.preprocessing import StandardScaler
def preprocessing() :
    X_train , X_test , Y_train , Y_test = loadData()
    # 차원이 현재 4차원에서 2차원으로
    
    X_train = X_train.reshape(X_train.shape[0] , 80 * 80 * 3)
    X_test  = X_test.reshape(X_test.shape[0] , 80 * 80 * 3)
    scaler = StandardScaler()
    
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.fit_transform(X_test)
    
    return X_train_scaled , Y_train , X_test_scaled , Y_test
    
def main() :
    X_train , Y_train , X_test , Y_test = preprocessing()
    network = createModel()
    network.fit(X_train , Y_train , epochs = 100 , batch_size = 100)
    
    train_loss , train_acc = network.evaluate(X_train , Y_train)
    test_loss  , test_acc  = network.evaluate(X_test  , Y_test)
    
    print(f"훈련셋 손실값 : {train_loss} , 정확도 : {train_acc}")
    print(f"테스트셋 손싧값 : {test_loss} , 정확도 : {test_acc}")

if __name__ == "__main__" :
    # initData()
    main()
"""

"""
import numpy  as np
import pandas as pd

import tensorflow as tf

# 1. 암환자 데이터셋 불러오기
from sklearn.datasets import load_breast_cancer
b_data = load_breast_cancer()

X = b_data["data"]
y = b_data["target"]

print(X.shape)
print(y.shape)

# 2. 데이터 나누기
from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 1234 , test_size = 0.3)

# 3. 데이터 스케일링
from sklearn.preprocessing import Normalizer
normal = Normalizer()

X_train_scaled = normal.fit_transform(X_train)
X_test_scaled  = normal.fit_transform(X_test)

# 4. 모델 설계
from tensorflow.keras import models , layers
def makeModel() :
    model = models.Sequential(
        [
            layers.Dense(512 , activation = "relu") ,
            layers.Dense(256 , activation = "relu") ,
            layers.Dense(64  , activation = "relu") ,
            layers.Dense(32  , activation = "relu") ,
            layers.Dense(1   , activation = "sigmoid")
        ]
    )
    
    model.compile(
        optimizer = "rmsprop" ,
        loss      = "binary_crossentropy" ,
        metrics   = ["accuracy"]
    )
    
    return model

network = makeModel()
network.fit(X_train_scaled , y_train , epochs = 10 , batch_size = 100)

train_loss , train_acc = network.evaluate(X_train_scaled , y_train)
test_loss  , test_acc  = network.evaluate(X_test_scaled  , y_test)

print(f"훈련셋 손실값 : {train_loss} , 정확도 : {train_acc}")
print(f"테스트셋 손싧값 : {test_loss} , 정확도 : {test_acc}")
"""

import numpy  as np
import pandas as pd
import tensorflow as tf
import os
import PIL.Image as pilimg
import imghdr

# 1. 이미지 라벨링 하기
def makeData(folder , label) :
    data   = []   # 이미지의 특성을 저장
    labels = []   # 라벨 저장
    
    path = "D:/Dataset/Garbage" + "/" + folder
    
    for filename in os.listdir(path) :
        try :
            kind = imghdr.what(path + "/" + filename)
            if kind in ["gif" , "png" , "jpg" , "jpeg"] :
                img = pilimg.open(path + "/" + filename)
                
                resize_img = img.resize((80 , 80))
                pixel      = np.array(resize_img)
                
                if pixel.shape == (80 , 80 , 3) :
                    data.append(pixel)
                    labels.append(label)
        except :
            print(filename + "error")
    
    np.savez("{}.npz".format(folder) , data = data , targets = labels)

# 2. 파일 저장하기
def savedata() :
    makeData("cardboard" , 0)
    makeData("glass" , 1)
    makeData("metal" , 2)
    makeData("paper" , 3)
    makeData("plastic" , 4)

# 3. 파일 불러오기
def loaddata() :
    cardboard_data = np.load("D:/Dataset/Garbage/cardboard.npz")
    glass_data     = np.load("D:/Dataset/Garbage/glass.npz")
    metal_data     = np.load("D:/Dataset/Garbage/metal.npz")
    paper_data     = np.load("D:/Dataset/Garbage/paper.npz")
    plastic_data   = np.load("D:/Dataset/Garbage/plastic.npz")
    
    data_list = np.concatenate((
        cardboard_data["data"] ,
        glass_data["data"] ,
        metal_data["data"] ,
        paper_data["data"] ,
        plastic_data["data"]
    ))
    
    target = np.concatenate((
        cardboard_data["targets"] ,
        glass_data["targets"] ,
        metal_data["targets"] ,
        paper_data["targets"] ,
        plastic_data["targets"]
    ))
    
    print(data_list.shape)
    print(target.shape)
    
    return data_list , target

# 데이터를 나누고 스케일링 작업 진행
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
def scaling(data_list , target) :
    X_train , X_test , y_train , y_test = train_test_split(data_list , target , random_state = 1234 , test_size = 0.3)
    
    scaled = StandardScaler()
    X_train = X_train.reshape(X_train.shape[0] , 80 * 80 * 3)
    X_test  = X_test.reshape(X_test.shape[0] , 80 * 80 * 3)
    
    X_train_scaled = scaled.fit_transform(X_train)
    X_test_scaled  = scaled.fit_transform(X_test)
    
    return X_train_scaled , X_test_scaled , y_train , y_test

# 모델 설계
from tensorflow.keras import models , layers
def makeModel() :
    model = models.Sequential([
        layers.Dense(512 , activation = "relu") ,
        layers.Dense(256 , activation = "relu") ,
        layers.Dense(128 , activation = "relu") ,
        layers.Dense(64  , activation = "relu") ,
        layers.Dense(5   , activation = "softmax")
    ])
    
    model.compile(
        optimizer = "rmsprop" ,
        loss      = "sparse_categorical_crossentropy" ,
        metrics   = ["accuracy"]
    )
    
    return model

if __name__ == "__main__" :
    # savedata()
    data_list , target = loaddata()
    X_train , X_test , y_train , y_test = scaling(data_list , target)
    
    model = makeModel()
    
    model.fit(X_train , y_train , epochs = 10 , batch_size = 100)
    
    train_loss , train_acc = model.evaluate(X_train , y_train)
    test_loss  , test_acc  = model.evaluate(X_test , y_test)
    
    print(f"훈련셋 손실값 : {train_loss} , 정확도 : {train_acc}")
    print(f"테스트셋 손실값 : {test_loss} , 정확도 : {test_acc}")