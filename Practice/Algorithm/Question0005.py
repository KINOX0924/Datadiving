# 10개의 정수를 리스트로 받아서 짝수는 오름차순 , 홀수는 내림차순으로 정렬해서 각각 따로 출력

def insertNumber() :
    number_list = []
    
    while len(number_list) < 10 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력")
    
    return number_list

def isEven(number_list) :
    even_list = []
    odd_list  = []
    
    for number in number_list :
        if number % 2 == 1 :
            odd_list.append(number)
        else :
            even_list.append(number)
    
    p_numberList(odd_list , even_list)

def p_numberList(odd_list , even_list) :
    print(f"[짝수 리스트(오름차순)] : {sorted(even_list)}")
    print(f"[홀수 리스트(내림차순)] : {sorted(odd_list , reverse = True)}")
    

if __name__ == "__main__" :
    number_list = insertNumber()
    isEven(number_list)