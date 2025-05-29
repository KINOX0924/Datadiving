# 10 개의 숫자를 리스트로 받아서, 가장 많이 등장한 숫자와 그 횟수를 출력하는 알고리즘을 작성

def insertNumber() :
    number_list = []
    
    while len(number_list) < 10 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력")
    
    return number_list

def maxOrminNumber(number_list) :
    counting_number = {}
    key_list        = []
    value_list      = []
    
    for number in number_list :
        if str(number) in counting_number :
            counting_number[str(number)] += 1
        else :
            counting_number[str(number)] = 1
    
    for key , value in counting_number.items() :
        key_list.append(int(key))
        value_list.append(int(value))
    
    return key_list , value_list

def print_number(key_list , value_list) :
    max_number        = max(value_list)
    max_number_indexs = [index for index , value in enumerate(value_list) if value == max_number]
    
    max_numbers       = []
    min_number = 0
    
    if len(max_number_indexs) == 1 :
        print(f"최고 빈도 숫자 : [{key_list[max_number_indexs[0]]}] || 입력된 횟수 : [{value_list[max_number_indexs[0]]}]")
        return
    
    for index , value in enumerate(max_number_indexs) :
        max_numbers.append(key_list[value])
        min_number = min(max_numbers)
    
    print(f"최고 빈도 숫자 중 가장 작은 숫자 : [{min_number}] || 입력된 횟수 : [{value_list[max_number_indexs[0]]}]")
        
if __name__ == "__main__" :
    key_list   = []
    value_list = []
    
    number_list = insertNumber()
    key_list , value_list = maxOrminNumber(number_list)
    print_number(key_list , value_list)