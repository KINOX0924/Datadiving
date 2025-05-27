# 10개의 숫자를 받아서 중복되지 않는 가장 큰 합 찾기
# 10개의 정수 리스트를 입력 받았을 때 이 리스트에서 서로 다른 세 개의 숫자를 선택하여 그 합이 가장 크게 되도록 하는 알고리즘 함수를 만들어라

def insertNumber() :
    number_list = []
    
    while len(number_list) < 10 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력해주세요.")

    return number_list

def maxSumNumber(number_list) :
    number_list = list(sorted(set(number_list) , reverse = True))
    sum = 0
    
    for index in range(0,3) :
        sum += number_list[index]
    
    print(sum)
    
    
if __name__ == "__main__" :
    number_list = insertNumber()
    maxSumNumber(number_list)