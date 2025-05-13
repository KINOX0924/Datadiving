# mod1 에 있는 모듈을 사용
# 파일 전체가 메모리에 로딩됨
import mod1

if __name__ == "__main__" :
    print(mod1.add(3,4))
    print(mod1.sub(3,4))

    p2 = mod1.Person("최번개" , 7)
    p2.print()
    
# 에일리어싱(aliasing)
# 모듈 이름이 너무 길때 다른 이름으로 변경하여 사용하는 것
import mod1 as md

print(md.add(5,6))
print(md.sub(5,6))

p3 = md.Person("노진구" , 9)
p3.print()