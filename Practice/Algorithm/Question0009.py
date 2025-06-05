# 여러 종류의 괄호가 포함된 문자열이 올바른 괄호 구조인지 판별하는 알고리즘

# 조건
# 괄호는 세 종류 : () , {} , []
# 각 여는 괄호는 해당하는 닫는 괄호와 쌍을 이루어야 함
# 괄호는 중첩될 수 있으며, 열리는 순서의 반대 순서로 닫혀야함

def chkParent(parent_str) :
    parent_couple_dict = {"(" : ")" , "{" : "}" , "[" : "]"}
    stack              = []
    count              = 0
    
    for parent in parent_str :
        if len(stack) == 0 :
            stack.append(parent)
            count += 1
        elif len(stack) >= 1 :
            try :
                if parent == parent_couple_dict[stack[count-1]] :
                    stack.pop()
                    count -= 1
                else :
                    stack.append(parent)
                    count += 1
            except KeyError :
                stack.append(parent)
                count += 1
        print(stack)    # 디버깅용
    
    if len(stack) == 0 :
        print("올바른 괄호 구조입니다.")
    else :
        print("잘못된 괄호 구조입니다.")

if __name__ == "__main__" :
    parent_str = r"(()){}[)]"
    chkParent(parent_str)