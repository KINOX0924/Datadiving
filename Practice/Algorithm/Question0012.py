"""

RLE 형태로 압축된 것을 다시 원래의 문자열로 압축 해제하는 알고리즘

조건
- 입력은 항상 '문자+숫자' 가 번갈아 나오는 구조
- 숫자는 항상 1자리 이상 (즉 , 'a12' 같은 경우도 가능)
- 문자는 알파벳 , 특수문자 모두 허용

"""

class ReverseRLE :
    def __init__(self , RLE_str) :
        self.RLE_str       = RLE_str      # 받아온 RLE 압축형태의 문자열을 self 변수에 대입
        self.word_list     = []           # word 만 담길 리스트
        self.number_list   = []           # word 의 출력 횟수가 담길 리스트
        self.decryption_str = ""
    
    def division(self) :
        temp = ""   # 숫자를 임시 저장할 공간
        for word in self.RLE_str :
            if len(self.word_list) != 0 and word.isdigit() == False :   # word_list 안에 문자가 하나라도 있고 그것이 숫자가 아니라면(즉 , 다음 문자를 만났다면)
                self.number_list.append(temp)                           # temp 를 number 리스트 안에 추가하고 temp 를 비우고 word 는 word 리스트에 넣음
                self.word_list.append(word)
                temp = ""
            elif len(self.word_list) == 0 and word.isdigit() == False:  # word_list 안에 문자가 하나도 없으면(즉, 첫 문자) 바로 word_list 안에 문자 추가
                self.word_list.append(word)
            elif word.isdigit() :                                       # word 가 숫자라면 temp 에 저장(숫자가 1 자리인지 1,000 자리인지 알수 없기에)
                temp += word
        self.number_list.append(temp)                                   # 최종적으로 마지막에 남은 숫자를 number_list 에 넣어줌
        
    def decryptionRLE(self) :                                           # RLE 문자열의 복호화 진행
        for index , word in enumerate(self.word_list) :                 # 인덱스와 word 리스트 안에 있는 문자열을 끄집어 오고
            for printing in range(0,int(self.number_list[index])) :     # number_list 와 대응하는 수만큼 복호화 문자열에 문자를 추가
                self.decryption_str += word
        
        return self.decryption_str                                      # 최종적으로 복호화된 문자열을 반환
                
if __name__ == "__main__" :
    RLE_str = r"a12b3c65$12*5)31"
    
    RRLE1 = ReverseRLE(RLE_str)
    RRLE1.division()
    decryption_str = RRLE1.decryptionRLE()
    
    print(decryption_str)