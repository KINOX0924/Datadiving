# 주어진 괄호 문자열이 올바른 괄호 문자열인지 판별하는 알고리즘을 작성

# 괄호는 "(" 과 ")" 으로만 구성되어 있음
# 열린 괄호는 닫힌 괄호보다 먼저 나와야하며 각 열린 괄호마다 정확히 하나의 닫힌 괄호가 있어야 합
# 문자열 전체가 올바른 괄호 쌍으로 구성되어야 함

def chkParent(parent_str) :
    stack = []
    
    for parent in parent_str :
        print(stack)    # 디버깅용
        if parent == "(" :
            stack.append("(")
        elif parent == ")" and len(stack) == 0 :
            print("이 괄호 문자열은 올바르지 않습니다.")
            return
        else :
            stack.pop()
    
    if len(stack) == 0 :
        print("올바른 괄호 문자열 구조입니다.")
    else :
        print("이 괄호 문자열은 올바르지 않습니다.")

if __name__ == "__main__" :
    parent_str = "(())"
    chkParent(parent_str)
    
    
    
    