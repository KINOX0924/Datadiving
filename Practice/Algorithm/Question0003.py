# 10 개의 숫자를 리스트로 받아서, 각 숫자가 리스트 안에서 몇 번 나타나는지(빈도수) 를 Dict 타입으로 만들어서 출력하는 알고리즘

def insertNumber() :
    number_list = []
    
    while len(number_list) < 10 :
        try :
            number = int(input("숫자 입력 : "))
            number_list.append(number)
        except ValueError :
            print("숫자만 입력")
    
    return number_list

def countNumber(number_list) :
    count_number_list = {}
    
    for number in number_list :
        if str(number) in count_number_list :
            count_number_list[str(number)] += 1
        else :
            count_number_list[str(number)] = 1
        print(count_number_list)

if __name__ == "__main__" :
    number_list = insertNumber()
    countNumber(number_list)