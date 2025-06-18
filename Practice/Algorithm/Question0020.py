"""
주제 - 회문 판별
하나의 문장이 주어졌을 때 , 해당 문장이 회문인지 판단하시오

조건
- 대소문자는 구분하지 않음(전부 소문자로 변환)
- 공백은 모두 무시함
- 영문자 외 특수 문자는 무시하지 않음 (제외 조건 없음)
- 회문이면 "회문입니다" 아니면 "회문이 아닙니다" 출력
"""

class Palindrome :
    def __init__(self , string) :
        self.string = string
    
    def transLower(self) :
        return self.string.lower().replace(" " ,"")
    
    def chkPalindrome(self , string) :
        string_list = [ x for x in string ]
        print(string_list)  # 디버깅
        
        while len(string_list) > 1 :
            if string_list[0] != string_list[-1] :
                return False
            string_list.pop()
            string_list.pop(0)
        
        return True
    
if __name__ == "__main__" :
    string_1 = "Was it a car or a cat I saw"
    string_2 = "This is not a palindrome"

    S1 = Palindrome(string_2)
    
    lower_string = S1.transLower()
    print(lower_string) # 디버깅
    
    result = S1.chkPalindrome(lower_string)
    
    if result == True :
        print("회문입니다")
    else :
        print("회문이 아닙니다")