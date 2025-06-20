"""
주제
단어의 길이가 짝수이면서 단어의 앞 절반과 뒤 절반이 같은 단어만 골라서 출력
문장에서 단어들을 추출한 뒤 단어의 길이가 짝수이고 , 앞 절반과 뒤 절반이 동일한 단어만 골라 리스트로 출력하시오

조건
- 단어와 단어 사이에는 공백이 반드시 존재함
- 각 단어에 대해 전체 길이가 짝수이고 , 앞 절반과 뒤 절반이 완전히 동일한 문자열일 것
- 대소문자 구분 없음(전부 소문자로 구분하거나 , 대문자로 구분하거나)
- 단 출력은 원래 형태 그대로 유지해서 출력할 것
"""

class MirrorWord :
    def __init__(self , string = "") :
        self.string = string
        self.words  = []
        self.Mirror_words = []
        
    def getWords(self) :
        self.words = self.string.split(" ")
        
    def evenWords(self) :
        self.words = [ x for x in self.words if len(x) % 2 == 0 ]
        print(self.words)   # 디버깅
    
    def getMirrorWords(self) :
        self.Mirror_words = [ x for x in self.words if x[:len(x)//2].lower() == x[len(x)//2:len(x)].lower() ]
        print(self.Mirror_words)
        
        return self.Mirror_words

if __name__ == "__main__" :
    string_1 = "noon deed rotor abcddcba racecar wow ABab abAB abcdabcd"
    
    MW = MirrorWord(string_1)
    MW.getWords()
    MW.evenWords()
    result = MW.getMirrorWords()
    
    print(result)
    