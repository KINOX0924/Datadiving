"""
주제
주어진 문자열에서 가장 짧은 단어를 출력하되 , 동률이 있는 경우 사전순으로 가장 앞선 단어를 출력

조건
- 입력은 하나의 문장 (공백 기준으로 단어 구분)
- 단어의 길이가 가장 짧은 단어를 찾아야함
- 짧은 단어가 여러 개일 경우 사전순으로 가장 앞선 단어를 출력함
- 대소문자는 구분하지 않고 비교하지만, 출력은 입력된 원래 케이스 그대로 함
"""

class ShortWord :
    def __init__(self , string) :
        self.string          = string.split(" ")
        self.min_length      = 0
        self.min_length_word = []
        self.sorted_Word     = []
        print(self.string)      # 디버깅
    
    def getMinLength(self) :
        self.min_length = min([ len(x) for x in self.string ])
        print(self.min_length)  # 디버깅
    
    def getMinLengthWord(self) :
        self.min_length_word = [ x for x in self.string if len(x) == self.min_length ]
        print(self.min_length_word)  # 디버깅
    
    def sortedWord(self) :
        self.sorted_Word = sorted(self.min_length_word , key = lambda x : x[0].lower())
        print(self.sorted_Word) # 디버깅
        
        return self.sorted_Word[0]
    
if __name__ == "__main__" :
    string_1 = "To be or not to be that is the question"
    string_2 = "The FOX is in A box With a key AND a LOCK or TO be Be To"
    
    SW = ShortWord(string_2)
    SW.getMinLength()
    SW.getMinLengthWord()
    min_word = SW.sortedWord()
    
    print(min_word)