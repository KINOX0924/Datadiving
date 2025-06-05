class Mystack :
    def __init__(self , size = 10) :
        if size < 10 :
            self.size = 10
        else :
            self.size = size
        self.stack = []
        for i in range(0 , size) :
            self.stack.append(0)
        # 여기서 0 은 값이 비어있음을 의미

        self.top = -1
    
    # 푸시 함수
    # 데이터가 isFull 상태가 아니면 top 증가시키고 그 안에 값을 넣음
    def push(self , data) :
        
        result = self.isFull()
        if result == True :
            return
        # if self.isFull() == True :
        #   return
        
        self.top += 1
        self.stack[self.top] = data
        
    # 팝 함수
    def pop(self) :
        
        if self.isEmpty() == True :
            return None
        
        temp = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        
        return temp
    
    # isFull 스텍에 데이터가 풀인지 아닌지 확인
    def isFull(self) :
        if self.size - 1 == self.top :
            return True
        return False
    
    # 스텍에 데이터가 없는 지 확인
    def isEmpty(self) :
        if self.top == -1 :
            return True
        return False
    
    # 마지막 데이터 값을 보여줌
    def peek(self) :
        if self.isEmpty() :
            return None
        return self.stack[self.top]
    
    def print(self) :
        i = 0
        
        while i <= self.top :
            print(self.stack[i] , end = " ")
            i += 1
        print()