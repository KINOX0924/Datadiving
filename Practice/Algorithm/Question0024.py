"""
주제
문자열에서 첫 번째로 반복된 문자를 찾아 출력하시오

조건
- 문자열이 주어지면 가장 먼저 두 번 등장한 문자 하나만 출력
- 대소문자를 구별함
- 특수문자 및 공백도 하나의 문자로 취급함
- 반복된 문자가 여러개 있어도 가장 먼저 중복된 하나만 찾으면 됨
"""

class Repeat :
    def __init__(self , string) :
        self.string    = string
        self.char_dict = {}
    
    def chkRepeat(self) :
        for char in self.string :
            if char not in self.char_dict.keys() :
                self.char_dict[char] = 1
            elif char in self.char_dict.keys() :
                return char
        
        return None

if __name__ == "__main__" :
    string1 = "abcdefgABCDEFGa"
    string2 = "12$#@ 1A1"
    string3 = "AaBbCcDdEeFf"
    
    PW = Repeat(string3)
    repeat_char = PW.chkRepeat()
    
    print(repeat_char)