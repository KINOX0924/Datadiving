"""
연속으로 반복되는 문자의 최대 길이와 해당 문자 출력

주제
- 주어진 문자열에서 같은 문자가 연속으로 등장하는 구간 중 가장 긴 구간을 찾아 해당 문자와 반복된 길이를 구하시오

조건
- 연속된 문자 구간만 비교
- 가장 긴 구간이 여러 개인 경우, 사전순으로 앞서는 문자를 출력
- 공백이나 특수문자도 포함될 수 있음 ( 단, 비교는 하되 대소문자 구분은 유지함 )

* 딕셔너리 타입으로 만듬
* 동일만 문자가 오면은 더 높은 쪽으로 Value 를 덮어 쒸워버림 -> 어차피 큰 쪽을 출력할 예정임
* 그러면 일단 a 와 a 가 나오게 되었을 때 따로따로 넣어야할 것이 필요함 -> 리스트 구조(?)
* 리스트[0] 와 리스트[1] 
"""

class LongChar :
    def __init__(self , string) :
        self.string      = string
        self.stack       = [None , 0]   # Is use stack structure but is not stack
        self.length_dict = {}
        self.max_list    = []
    
    def division(self) :
        for word in self.string :
            if self.stack[0] == None :
                self.stack[0] = word
                self.stack[1] = 1
            elif self.stack[0] != None and word == self.stack[0] :
                self.stack[1] += 1
            else :
                self.length_dict[self.stack[0]] = self.stack[1]
                self.stack[0] = word
                self.stack[1] = 1
        self.length_dict[self.stack[0]] = self.stack[1]
        print(self.length_dict)     #FIX 디버깅
    
    def getMax(self) :
        max_length = 0
        
        for key in self.length_dict.keys() :
            if max_length == 0 :
                max_length = self.length_dict[key]
            elif max_length != 0 and max_length < self.length_dict[key] :
                max_length = self.length_dict[key]
        
        return max_length

    def whoMax(self , max_length) :
        self.max_list = sorted([ key for key in self.length_dict if self.length_dict[key] == max_length ])
        print(self.max_list)    #FIX 디버깅
        
        return (self.max_list[0] , max_length)
        
if __name__ == "__main__" :
    string = "aaaBBBccddddeee!!@@@!!!!   $$$$ZZZZaaaa"
    
    L1 = LongChar(string)
    L1.division()
    max_length = L1.getMax()
    data = L1.whoMax(max_length)
    
    print(f"가장 길게 나온 문자 : {data[0]} || 길이 : {data[1]}")