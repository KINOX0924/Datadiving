"""
숫자 문자열에서 연속된 숫자 구간 중 짝수만 골라 총 합을 출력

조건
- 연속된 숫자 구간은 문자열에서 숫자가 연달아 나온 부분 전체 (예 : "006" -> 6)
- 문자와 숫자가 섞은 구조를 전제
- 최종 결과는 짝수 숫자 구간들의 합
"""

class SumEven :
    def __init__(self , string) :
        self.string = string
    
    def getNumbers(self) :
        num_list = []
        temp = ""
        
        for char in self.string :
            if temp != "" and char.isdigit() == False :
                num_list.append(temp)
                temp = ""
            elif char.isdigit() :
                temp += char
        num_list.append(temp)
                
        print(num_list)     # 디버깅
        return num_list
        
    def sumEven(self , num_list) :
        sum_Even = 0
        
        for number in num_list :
            if int(number) % 2 == 0 :
                sum_Even += int(number)
        
        return sum_Even

if __name__ == "__main__" :
    string = "ab12c007d99ef000gh456ij3k8!!77mn100"
    
    num_list = []
    
    E1 = SumEven(string)
    num_list = E1.getNumbers()
    sum_Even = E1.sumEven(num_list)
    
    print(f"짝수 숫자 구간의 총 합 : {sum_Even}")