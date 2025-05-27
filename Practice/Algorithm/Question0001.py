# 리스트에서 가장 큰 수와 가장 작은 수 찾기
# 양의 정수로 이루어진 리스트 numbers 가 주어졌을 때 , 이 리스트에서 가장 큰 숫자(최댓값) 와 가장 작은 숫자(최솟값) 을 찾아 출력하는 함수를 만들어라

def insertNumber() :
    number_list = []
    
    while len(number_list) <= 10 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력해주세요.")
        
    return number_list

def maxnminNumber(number_list) :
    max_number = number_list[0]
    min_number = number_list[0]
    
    for index , number in enumerate(number_list) :
        if number > max_number :
            max_number = number
        elif number < min_number :
            min_number = number
    
    print(f"최대값 : [{max_number}] || 최소값 : [{min_number}]")
    return

if __name__ == "__main__" :
    number_list = insertNumber()
    maxnminNumber(number_list)