import pandas as pd
import numpy  as np

"""
# 판다스 1
a = [1,2,3,4,5]
s = pd.Series(a)
print(type(s))
print()

b = {"a" : 1 , "b" : 2 , "c" : 3 , "d" : 4 , "e" : 5}
s2 = pd.Series(b)   # dict -> Series 타입으로

print(s[0])
print(s[1])
print(s[2])
print(s[:3])

print(s[s >= 3])

print(s[np.logical_and(s >= 3 , s <= 4)])
print(s[[0,3,2]])

print(s2[:3])
print(s2["a"])
print(s2["a":"c"])
print(s2[["d","a","c"]])
print(s2.iloc[[4,2,1]])
"""


# 판다스 2
data = {
    "name"  : ["홍길동" , "임꺽정" , "장길산" , "홍경래"] ,
    "kor"   : [90 , 80 , 70 , 70 ] ,
    "eng"   : [80 , 70 , 60 , 50 ] ,
    "mat"   : [90 , 70 , 70 , 60 ]
}

data_frame = pd.DataFrame(data)
print(type(data_frame))
print(data_frame)

# Dataframe 데이터 엑세스
# iloc[0,0] 또는 loc[0,"name"] 둘 중 하나의 방법으로 접근
# .head(숫자) = 디폴트는 5 이고 데이터를 정해진 갯수만큼만 출력하는 함수
print(data_frame.head(3))
print(data_frame.iloc[0,0])
print(data_frame.loc[0,"name"])

# 하나의 column 을 통으로 보여주는 것
print(data_frame["name"])
print(data_frame["kor"])

for i in range(0 , len(data_frame)) :
    print(data_frame.iloc[i , 0])

print(data_frame.iloc[3,2])
print(data_frame.iloc[2:4,2])
print(data_frame.iloc[2:4 , 2:4])