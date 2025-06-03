# 주어진 숫자 리스트에서 연속된 숫자들이 가장 많이 반복되는 구간을 찾아 그 구간의 합을 출력하는 알고리즘을 작성하라
# 연속된 숫자들이란 1,2,3 처럼 숫자가 차례대로 나오는 구간을 의미함
# 반복되는 구간이 여러 개인 경우 가장 긴 구간을 찾고, 그 구간의 합을 출력
# 만약 가장 긴 구간이 여러개인 경우 그 중 가장 큰 수를 출력

# 숫자 열개를 받아내는 함수
def insertNumber(number_length) :
    number_list = []
    
    while len(number_list) != number_length + 1 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력")
    
    return number_list

# 리스트 내의 현 숫자와 뒤 숫자를 비교하여 구분하는 함수
def isFor(number_list) :
    for_list   = [[]]
    list_index = 0
    
    for index in range( 0 , len(number_list) - 1 ) :
        if number_list[index + 1] - number_list[index] == 1 or number_list[index + 1] - number_list[index] == - 1 :
            for_list[list_index].append(number_list[index])    
            if index == len(number_list) - 2 and (number_list[index + 1] - number_list[index] == 1 or number_list[index + 1] - number_list[index] == - 1) :
                for_list[list_index].append(number_list[index + 1])
        else :
            for_list[list_index].append(number_list[index])
            for_list.append([])
            list_index += 1
            if index == len(number_list) - 2 and (number_list[index + 1] - number_list[index] != 1 or number_list[index + 1] - number_list[index] != - 1) :
                for_list[list_index].append(number_list[index + 1])
    
    print(for_list) # 디버깅용
    
    return for_list

# 앞서 연속된 숫자들을 분류한 리스트를 가져와서 각 연속된 숫자의 길이를 확인
def getLength(for_list) :
    length_list = []
    
    for item in for_list :
        length_list.append(int(len(item)))
    
    max_sum_list = checkMax(length_list , for_list)
    
    return max_sum_list
        
def checkMax(length_list , for_list) :
    max_length = max(length_list)
    max_sum_list = []
    
    for index , length in enumerate(length_list) :
        if length == max_length :
            max_sum_list.append(sum(for_list[index]))

    return max_sum_list

if __name__ == "__main__" :
    number_list = insertNumber(10)
    for_list = isFor(number_list)
    max_sum_list = getLength(for_list)
    
    print(f"연속된 구간의 합이 가장 큰 수 : {max(max_sum_list)}")