# HTML 태그가 올바르게 열리고 닫혔는지 확인하는 알고리즘을 작성
# HTML 태그는 태그 별로 하나씩 입력되는 것이 아닌 하나의 문자열로 입력됨    예:)) "<html><body></body></html>"
# 일단 안에 있는 태그 명령어가 올바른 명령어인지는 확인하지 않음

class TagParent :
    def __init__(self , tag_str) :
        self.tag      = tag_str
        self.tag_list = []
        self.stack    = []

    def transList(self) :
        self.temp = ""
        
        for word in self.tag :
            if word == ">" :
                self.temp += word
                self.tag_list.append(self.temp)
                self.temp = ""
            else :
                self.temp += word
        
        print(self.tag_list)    # 디버깅

    def distinctTag(self) :
        for tag in self.tag_list :
            if tag.startswith(r"</") and tag.endswith(r">") :     # 닫힘태그 구분
                if tag[2:-1] == self.stack[-1] :
                    self.stack.pop()
                else :
                    self.stack.append(tag[2:-1])
                print(f"pop : {self.stack}")    # 디버깅
            elif tag.startswith(r"<") and not tag.startswith(r"</") and tag.endswith(r">"):       # 열림 태그 구분
                self.stack.append(tag[1:-1])
                print(f"append : {self.stack}")     # 디버깅
            else :
                print("괄호가 제대로 쌓이지 않은 태그가 들어갔습니다.")
                return
        
    def result(self) :
        if len(self.stack) == 0 :
            print("올바른 태그 그룹입니다.")
        else :
            print("올바르지 않은 태그 그룹입니다.")

if __name__ == "__main__" :
    tag_str = "<html><body><t1></t1></body></html>"
    
    t1 = TagParent(tag_str)
    t1.transList()
    t1.distinctTag()
    t1.result()