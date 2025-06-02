# 10 개의 정수 리스트를 받아서 세 개의 숫자의 만들 수 있는 모든 조합으로 합을 기준으로 세번째로 큰 합을 구하라
# itertools.combinations / itertools.combinations(iterable , r)
# 주어진 iterable 에서 r 개의 요소를 뽑는 모든 조합을 만들어주는 함수
# 예:)) [1,2,3] = (1,2) , (2,3) , (3,1)

import itertools

def insertNumber() :
    number_list = []
    
    while len(number_list) < 10 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력")
    
    return number_list

def addThreeCombi(number_list) :
    combi_list  = []
    combination = itertools.combinations(number_list , 3)
    
    for threecombi in combination :
        combi_list.append(sum(threecombi))
    
    combi_list = list(sorted(set(combi_list) , reverse = True))
    print(f"세번째로 큰 수 : {combi_list[2]}")
    

if __name__ == "__main__" :
    number_list = insertNumber()
    addThreeCombi(number_list)