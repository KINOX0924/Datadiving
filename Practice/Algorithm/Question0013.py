"""
문자열에서 가장 많이 등장한 문자와 그 개수를 출력하는 알고리즘

- 입력된 문자열에서 가장 많이 등장한 문자를 찾아, 그 문자와 등장횟수를 함께 출력하는 알고리즘을 작성하시오
- 공백이나 특수문자가 포함된 문자열도 입력될 수 있음
- 가장 많이 등장한 문자가 여러 개인 경우, 사전순으로 가장 빠른 문자를 출력
- 영문일 경우 대소문자는 구분하지 않음 (모두 소문자로 취급)
"""

class Stringfre :
    def __init__(self , string) :
        self.string = string
        self.char_dict = {}
        self.max_fre = 0
        self.max_list = []
        
    def divisionStr(self) :
        for ch in self.string :
            if ch.isalpha() :
                if ch.lower() not in self.char_dict.keys() :
                    self.char_dict[ch.lower()] = 1
                else :
                    self.char_dict[ch.lower()] += 1
            else :
                if ch not in self.char_dict.keys() :
                    self.char_dict[ch] = 1
                else :
                    self.char_dict[ch] += 1
        
        print(self.char_dict)   # 디버깅
    
    def isMaxFre(self) :
        for key in self.char_dict.keys() :
            if self.char_dict[key] > self.max_fre :
                self.max_fre  = self.char_dict[key]
        
        print(self.max_fre) # 디버깅
    
    def oneOrmore(self) :
        for key in self.char_dict.keys() :
            if self.char_dict[key] == self.max_fre :
                self.max_list.append(key)
        
        if len(self.max_list) > 1 :
            self.max_list = list(sorted(self.max_list))
            return self.max_fre , self.max_list[0]
        else :
            return self.max_fre , self.max_list[0]
    
if __name__ == "__main__" :
    string = r"aaaabbbccccdddeeee@@ $%"
    
    max_fre = 0
    max_chr = ""

    s1 = Stringfre(string)
    s1.divisionStr()
    s1.isMaxFre()
    max_fre , max_chr = s1.oneOrmore()
    
    print(f"가장 많이 나온 글자 : {max_chr} || 빈도수 : {max_fre}")