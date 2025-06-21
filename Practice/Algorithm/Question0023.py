"""
주제
문자열에서 한 번만 등장한 단어만 사전순으로 출력하시오

조건
- 문자열은 공백 기준으로 단어들이 구성되어 있음
- 대소문자는 구분하지 않음
- 한 번만 등장한 단어만 선별
- 최종 출력은 사전순 오름차순으로 정렬하여 리스트로 출력
"""

class Oneword :
    def __init__(self , string) :
        self.string = string
        self.words  = []
        self.freq   = {}
        
    def getWord(self) :
        self.words = self.string.split(" ")
    
    def countfre(self) :
        for word in self.words :
            if word.lower() not in self.freq.keys() :
                self.freq[word.lower()] = 1
            else :
                self.freq[word.lower()] += 1
        
        print(self.freq)    # 디버깅
    
    def getOneword(self) :
        self.Onewords = [ x for x in self.freq.keys() if self.freq[x] == 1]
        
        print(self.Onewords)    # 디버깅
    
    def sortWords(self) :
        return list(sorted(self.Onewords))
        
if __name__ == "__main__" :
    string = "The fox and the dog saw the Fox and ran away"
    
    OW = Oneword(string)
    OW.getWord()
    OW.countfre()
    OW.getOneword()
    
    result = OW.sortWords()
    print(result)