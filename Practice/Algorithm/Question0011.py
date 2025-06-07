# 문자열 압축 (Run-Length Encoding , RLE)
# 연속으로 반복되는 문자가 있을 때 , "문자 + 반복횟수" 형태로 압축된 문자열을 만드는 알고리즘을 작성하시오
# 예:)) "aaabbbcccdaa" -> "a3b3c3d1a2"

# 조건
# 같은 문자가 반복되지 않으면 그냥 1로 처리됨
# 문자열은 알파벳 소문자만 주어진다고 가정되며 대소문자 구분 없음
# 어떤 문자든 상관없이 같은 문자라면 압축

class RLE :
    def __init__(self , string) :
        self.string = string
        self.word_counter_stack = []
        self.encoding_str = ""
        
    def word_count(self) :
        for word in self.string :
            if word not in self.word_counter_stack and len(self.word_counter_stack) == 0 :
                self.word_counter_stack.append(word)
                self.word_counter_stack.append(1)
                print(self.word_counter_stack)    # 디버깅
            elif word not in self.word_counter_stack and len(self.word_counter_stack) != 0 :
            # elif word == self.word_counter_stack[-2] and len(self.word_counter_stack) != 0 :
                temp_2 , temp_1 = self.word_counter_stack.pop() , self.word_counter_stack.pop()
                self.encoding_str += temp_1
                self.encoding_str += str(temp_2)
                self.word_counter_stack.append(word)
                self.word_counter_stack.append(1)
                print(self.word_counter_stack)    # 디버깅
            elif word in self.word_counter_stack :
                self.word_counter_stack[-1] += 1
                print(self.word_counter_stack)    # 디버깅
        
        temp_2 , temp_1 = self.word_counter_stack.pop() , self.word_counter_stack.pop()
        self.encoding_str += temp_1
        self.encoding_str += str(temp_2)
        
        print(self.encoding_str)    # 디버깅

if __name__ == "__main__" :
    string = r"aaabbbcccaaddd"
    
    e1 = RLE(string)
    e1.word_count()