"""
문자열에서 연속된 숫자 구간 중 홀수로 시작해서 짝수로 끝나는 구간만 골라 합산

주제
문자와 숫자가 섞인 문자열이 주어질 때 , 숫자로만 이루어진 구간들 중에서 홀수로 시작하고 , 짝수로 끝나는 구간만 골라서 정수형으로 변환한 뒤 총합을 출력

조건
- 숫자 구간은 연속된 숫자로만 구성되어야 함
- 숫자 구간은 앞뒤 문자로 분리됨
- 앞자리 첫 글자는 홀수 , 뒷자리 마지막 글자는 짝수여야 포함
- 조건을 만족하는 구간만 정수로 변환하여 합산
- 숫자는 최소 1자리부터 몇 자리까지 나올 지 알 수 없음
"""

class SumNumber :
    def __init__(self , string) :
        self.string = string
    
    def getNumber(self) :
        temp = ""
        num_list = []
        
        for char in self.string :
            if char.isdigit() :
                temp += char
            elif temp != "" and char.isdigit() == False :
                if int(temp[0]) % 2 == 1 and int(temp[-1]) % 2 == 0 :
                    num_list.append(int(temp))
                temp = ""                    
                    
        if temp != "" and int(temp[0]) % 2 == 1 and int(temp[-1]) % 2 == 0 :
            num_list.append(int(temp))
            temp = ""
        
        return num_list
    
    def sumNumber(self , num_list) :
        total = 0
        
        for number in num_list :
            total += number
        
        return total

if __name__ == "__main__" :
    string = "a135b246c3d708ef4g91!82#19h7j5312k"
    
    S1 = SumNumber(string)
    num_list = S1.getNumber()
    total = S1.sumNumber(num_list)
    
    print(f"조건에 만족하는 수의 합 : {total}")