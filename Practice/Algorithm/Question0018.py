"""
주제
문자열 속 숫자 구간들 중 오름차순 정렬된 숫자 구간만 골라 총합 출력

설명
문자와 숫자가 섞인 문자열이 주어질 때, 연속된 숫자 구간들 중에서 다음 조건을 만족하는 구간만 골라 합산하시오

조건
- 각 숫자 구간의 각 자리 숫자들이 오름차순 정렬되어 있어야함
"""

class SortSum :
    def __init__(self , string) :
        self.string            = string
        self.number_list       = []
        self.sortedNumber_list = []
    
    def isNumber(self) :
        temp = ""
        
        for char in self.string :
            if char.isdigit() :
                temp += char
            elif temp != "" and char.isdigit() == False :
                self.number_list.append(temp)
                temp = ""
        
        if temp.isdigit() :
            self.number_list.append(temp)

        # print(self.number_list) # 디버깅
    
    def getSortedNumber(self) :
        for number in self.number_list :
            if int(number) >= 1 and int(number) <= 9 :
                self.sortedNumber_list.append(int(number))
            elif int(number) >= 10 and number == "".join(sorted(number)) :
                self.sortedNumber_list.append(int(number))
        
        # print(self.sortedNumber_list)   # 디버깅

    def getTotal(self) :
        total = 0
        
        for number in self.sortedNumber_list :
            total += number
            
        return total
    
if __name__ == "__main__" :
    string = "a123b432c5d741e132f468g7h4891i5790j"
    
    SS = SortSum(string)
    SS.isNumber()
    SS.getSortedNumber()
    
    print(f"조건에 맞는 숫자들의 합 : {SS.getTotal()}")
    