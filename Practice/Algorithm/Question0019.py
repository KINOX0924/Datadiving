"""
주제
문장이 하나 주어졌을 때 , 그 안의 단어들을 공백 기준으로 나누고, 중복 없이 단어를 등장한 순서대로 출력하시오

조건
- 대소문자는 구분하지 않음(모두 소문자로 처리 할것)
- 특수기호는 제거하지 않아도 됨
- 단어는 공백(" " , ' ') 기준으로 구분됨
- 동일한 단어가 여러번 나와도, 처음 등장한 위치만 유지됨
"""

class NoOverlap :
    def __init__(self , string) :
        self.string = string
        self.word_list = []
    
    def getWordList(self) :
        temp_list = self.string.split(" ")
        print(temp_list)        # 디버깅
        
        for word in temp_list :
            if word.lower() not in self.word_list :
                self.word_list.append(word.lower())
        
        print(self.word_list)   # 디버깅

        return self.word_list
    
if __name__ == "__main__" :
    string = "The quick brown fox jumps over the lazy dog and the quick fox runs fast"
    
    NO = NoOverlap(string)
    word_list = NO.getWordList()
    
    print(word_list)