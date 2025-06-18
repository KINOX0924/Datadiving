import numpy as np

arr = np.array([1 , 2 , 3 , 4] , ndmin = 5)

print(arr)
print("number of dimenstions : " , arr.ndim)

"""
# 배열의 차원을 확인하는 함수 "ndim"

a = np.array(1)
b = np.array([1 , 2 , 3 , 4 , 5])
c = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
d = np.array([[[1 , 2 , 3] , [4 , 5 , 6]] , [[1 , 2 , 3] , [4 , 5 , 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
"""

"""
# 3-D 배열

arr = np.array([[[1 , 2 , 3] , [4 , 5 , 6]] , [[1 , 2 , 3] , [4 , 5 , 6]]])

print(arr)
"""

"""
# 2-D 배열

arr = np.array([[1 , 2 , 3] , [4 , 5 , 6]])

print(arr)
"""

"""
# 1-D 배열

arr = np.array([ 1 , 2 , 3 , 4 , 5 ])

print(arr)
"""

"""
# 0-D 배열

arr = np.array(42)

print(arr)
"""

"""
# ndarray 의 소개

# arr = np.array([ 1 , 2 , 3 , 4 , 5 ])
arr = np.array(( 1 , 2 , 3 , 4 , 5 ))

print(arr)

print(type(arr))
"""