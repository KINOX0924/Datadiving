import numpy as np

arr = np.array([[1 , 2 , 3 , 4 , 5] , [6 , 7 , 8 , 9 , 10]])

print(arr[1 , -1])

"""
# 3 차원 배열 접근

arr = np.array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10,11,12]]])

print(arr[0 , 1 , 2])
"""

"""
# 2 차원 배열 접근

arr = np.array([[1 , 2 , 3 , 4 , 5] , [6 , 7 , 8 , 9 , 10]])

print("Second Element on First Row : " , arr[0,1])
print("First Element on Second Row : " , arr[1,0])
"""
 
"""
# 단일 접근 + 접근 후 동시 계산

arr = np.array([1 , 2 , 3 , 4])

print(arr[2] + arr[3])
"""

"""
# 단일 접근

arr = np.array([1 , 2 , 3 , 4])

print(arr[0])
"""