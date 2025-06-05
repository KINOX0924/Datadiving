"""

오름차순의 경우
셀렉트 정렬 : 제일 작은 사람은 첫번째 방에 / 두번째 작은 사람은 두번째 방에 / 세번째 작은 사람은 세번째 방에
- 왼쪽부터 정렬되는 것
- a[i] 와 a[j] 를 비교

버블 정렬 : 바로 옆에 사람 비교함 / 계속 바꿔치기
- 제일 큰 사람이 계속 뒤로 밀리며 거품이 보글거리를 느낌을 받음
- a[i] 와 a[i+1] 을 비교

"""

# 내가 작성한 버블 정렬
# def bubbleSort(list) :
#     for index in range(0,len(list)) :
#         for index_2 in range(0,len(list)-1) :
#             if list[index_2] > list[index_2 + 1] :
#                 list[index_2] , list[index_2 + 1] = list[index_2 + 1] , list[index_2]
#             print(list)

# if __name__ == "__main__" :
#     no_sort_list = [ 9 , 7 , 25 , 6 , 8 , 4 , 3]
    
#     bubbleSort(no_sort_list)
    
"""

알고리즘
속도가 빠르면 메모리를 많이 차지함
속도가 느리면 메모리를 덜 차지함
최근에는 메모리가 엄청 싸서 속도 위주의 알고리즘을 선택함


퀵정렬 - 재귀호출
기준점 0 ~ 11   : 0 번방을 기준으로 
                Left = 0
                right = 11
                a[0] > a[left] 일때까지 left 증가
                
                Left = 1
                a[0] < a[right] 일때까지 right 감소
                right = 8
                
                a[left] <=> a[right]
            
"""

# arr = [5,1,6,4,8,3,7,9,2,10]

# # arr[0 ~ 9]
# # arr[0 ~ 4] , 기준점 , a[6 ~ 9]
# def quicksort(arr , start , end) :
#     if start >= end :
#         return
    
#     pivot = arr[start]
#     left = start + 1
#     right = end
    
#     print(f"Left : {left} right : {right}")
#     while left <= right :
#         # left > right 가 되면 배분이 종료된 것
#         # left 증가 시키면서 arr[left] 가 피벗(기준점) 보다 큰 것을 만날때까지
#         # left 가 end 보다 작은 동안
#         while left <= end and arr[left] < pivot :
#             left += 1
#         while right > start and arr[right] > pivot :
#             right -= 1
            
#         print(f"Left : {left} right : {right}")
        
#         if left < right :
#             arr[left] , arr[right] = arr[right] , arr[left]
#         else :
#             break
    
#     arr[start] , arr[right] = arr[right] , arr[start]
#     print(arr)
    
#     quicksort(arr , start , right - 1)
#     quicksort(arr , right + 1 , end)

# quicksort(arr , 0 , len(arr) - 1)


# 괄호가 쌍이 맞는 지 확인
# import prac_stack

# class IsNormalParent :
#     def __init__(self , str) :
#         self.parent_str = str
    
#     def chkParent(self) :
#         self.parent_stack = prac_stack.Mystack(len(self.parent_str))
        
#         for word in self.parent_str :
#             if word == "(" :
#                 self.parent_stack.push(word)
#                 # print(self.parent_stack.print())    # 디버깅
#             elif self.parent_stack.stack[0] != "(" and word == ")" :
#                 self.parent_stack.push(word)
#                 break
#             elif word == ")" :
#                 self.parent_stack.pop()
#                 # print(self.parent_stack.print())    # 디버깅
            
#     def resultPrint(self) :
#         if self.parent_stack.isEmpty() == False :
#             print("괄호의 짝이 맞지 않습니다.")
#         elif self.parent_stack.isEmpty() == True :
#             print("괄호의 짝이 올바르게 있습니다.")

# if __name__ == "__main__" :
#     str = r"((a*(b+c))-d) / e"
    
#     p_1 = IsNormalParent(str)
#     p_1.chkParent()
#     p_1.resultPrint()



"""
후위 표기법
"""

import prac_stack

class TransPostfix :
    def __init__(self) :
        self.stack = prac_stack.Mystack()
        self.post_formula = ""
        self.operator = {"+" : 1 , "-" : 1 , "*" : 2 , "/" : 2}
        
    def postFormula(self , formula) :
        for word in formula :
            if word in "123456789" :
                self.post_formula += word
            elif word in "+-*/" :
                if self.stack.isEmpty() == True :
                    self.stack.push(word)
                else :
                    if self.operator[self.stack.peek()] >= self.operator[word] :
                        self.post_formula += self.stack.pop()
                        self.stack.push(word)
                    elif self.operator[self.stack.peek()] < self.operator[word] :
                        self.stack.push(word)
        
        while self.stack.isEmpty() == False :
            self.post_formula += self.stack.pop()
        
        return self.post_formula

class CalPostfix :
    def __init__(self) :
        self.number_stack = prac_stack.Mystack()
        
    def calformula(self , post_formula) :
        for word in post_formula :
            if word in "123456789" :
                self.number_stack.push(word)
            elif word in "+-*/" :
                number_2 = int(self.number_stack.pop())
                number_1 = int(self.number_stack.pop())
                
                self.number_stack.push(self.getCalResult(word , number_1 , number_2))
        
        return self.number_stack.pop()
    
    def getCalResult(self , word , number_1 , number_2) :
        if word == "+" :
            result = number_1 + number_2
        elif word == "-" :
            result = number_1 - number_2
        elif word == "*" :
            result = number_1 * number_2
        elif word == "/" :
            result = number_1 // number_2
        
        return result
                
if __name__ == "__main__" :
    formula = "3+5*2*2-5"
    print(formula)
    
    p1 = TransPostfix()
    post_formula = p1.postFormula(formula)
    print(post_formula)
    
    c1 = CalPostfix()
    cal_result = c1.calformula(post_formula)
    print(cal_result)