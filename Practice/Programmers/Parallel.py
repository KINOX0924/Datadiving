"""

점 네개의 좌표를 담은 이차원 배열이 하기와 같이 주어진다.
주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1 을 , 없으면 0 을 return 하는 함수를 만들어라

기울기가 같은 경우 평행으로 간주함
기울기를 구하는 공식
y2 - y1
-------
x2 - x1

dots = [[x1,y1] , [x2,y2] , [x3,y3] , [x4,y4]]

"""

# dots = [[3, 5], [4, 1], [2, 4], [5, 10]]
dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
# [[x1,y1] , [x2,y2] , [x3,y3] , [x4,y4]]
# 기울기를 비교하는 식 : (y2 - y1)*(x4 - x3) == (y4 - y3)*(x2 - x1)

from itertools import combinations , permutations

def printArray(list) :
    for line in list :
        print(line , end = "\n")

def calParallel(list) :
    for line in list :
        if (line[1][1] - line[0][1])*(line[3][0] - line[2][0]) == (line[3][1] - line[2][1]) * (line[1][0] - line[0][0]) :
            return 1
    
    return 0

def solution(dots) :
    index_list = list(permutations(dots , 4))
    # printArray(index_list)
    
    result = calParallel(index_list)
    # print(result)

    return result

solution(dots)