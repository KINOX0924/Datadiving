"""
문자열에서 알파벳만 골라 각 알파벳이 몇 번 등장했는 지 빈도수로 정렬해서 출력하는 알고리즘

조건
- 주어진 문자열에서 알파벳 문자만 골라낼 것
- 그 알파벳 문자가 몇 번 나왔는지 카운트 할 것
- 등장 빈도수가 높은 순으로 정렬해서 출력할 것
- 등장 빈도수가 동일한 문자일 경우 사전순으로 출력할 것
- 알파벳은 대소문자를 구분하지 않음
"""

class Alpha :
    def __init__(self , string) :
        self.string        = string
        self.division_dict = {}
        self.count_dict    = {}
        self.sort_list     = []
        
    """
    입력받은 문자열에서 isalpha() 함수를 사용하여 알파벳만 가져옴
    딕셔너리를 사용해서 각 알파벳 별 빈도수를 확인함
    등장 빈도수가 높은 순으로 정렬해서 출력만 하는 것이라면 쉬우나 등장 빈도수가 같을 경우 사전순으로 출력하는 것이 어려움
    """
    def division(self) :
        for char in self.string :
            if char.isalpha() :
                if char.lower() not in self.division_dict.keys() :
                    self.division_dict[char.lower()] = 1
                else :
                    self.division_dict[char.lower()] += 1
        
        print(self.division_dict)   # TODO 디버깅
    
    """
    키값을 사용하여 각 빈도수가 동일한 문자들끼리 한 리스트에 넣어두는 방식
    일단 해보자 -> 각 빈도수 별로 동일한 문자들끼리 하나의 딕셔너리 타입에 모이긴 했음
    """
    def freDivision(self) :
        for key in self.division_dict.keys() :
            if self.division_dict[key] not in self.count_dict.keys() :
                self.count_dict[self.division_dict[key]] = key
            else :
                self.count_dict[self.division_dict[key]] += key
        
        print(self.count_dict)      # TODO 디버깅
    
    """
    다음은 키값으로 각 문자들을 빈도수가 높은 순으로 정렬을 해야함
    스택과 리스트를 사용? 아니면 컴프리헨션으로 키값 리스트만 뽑아낸 다음에 리스트를 활용해서 밸류값을 정렬?
    마찬가지로 일단 해보자
    """
    def sortList(self) :
        key_list = [ key for key in self.count_dict.keys() ]
        key_list = sorted(key_list , reverse = True)
        
        print(key_list)             # TODO 디버깅
        
        for key in key_list :
            self.sort_list += sorted(self.count_dict[key])
        
        print(self.sort_list)       # TODO 디버깅
    
    """
    마지막으로 출력
    출력은 가장 먼저 뽑았던 딕셔너리를 가지고 출력
    """
    def printChar(self) :
        for key in self.sort_list :
            print(f"문자 : {key} || 빈도수 : {self.division_dict[key]}")
        
if __name__ == "__main__" :
    string = r"The Quick Brown Fox Jumps Over The Lazy Dog! 12345 $$$$$ aaaa BBBB cCddEEffGG"
    
    A1 = Alpha(string)
    A1.division()
    A1.freDivision()
    A1.sortList()
    A1.printChar()