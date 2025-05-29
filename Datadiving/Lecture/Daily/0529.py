# 5월 29일 강의

# 리플랙션 - 거울
# 클래스를 만들면 , 언어 번역가들이 클래스 정보를 읽어서 정보를 해석해서 저장하고
# 그 정보에 접근할 수 있게 해줌
# 프로그램이 실행 중에 객체 , 클래스 , 함수 등의 정보를 확인하거나 조작하는 기능을 말함
# 요약하자면 코드가 자기 자신을 들여다보고(거울) 조작할 수 있는 능력

# 리플랙션 기능은 프레임워크를 만들때 필요함
# -> 사용자가 클래스를 설계

import inspect # inspect 라이브러리는 각 요소가 함수인지 아닌지 확인할 수 있음

class Person :
    # 생성자에서 두개를 만들었으니 두 개의 필드에 생성된 것
    def __init__(self , name = "" , age = 20) :
        self.name = name
        self.age  = age
    
    def greet(self) :
        print(f"Hello , {self.name}")
        
p = Person("Tom" , 12)


# 클래스 내의 속성을 가져오는 함수
a = getattr(p , "name") # 특정 개체로부터 속성을 가져옴
print(a)

# dir 명령어를 사용하면 클래스 내부의 구조를 전부 보여줌
print(dir(p))

# dir 명령어 - 필터링을 사용해서 사용자가 만든거만 확인
# 컴프리헨션
fields = [ x for x in dir(p) if not x.startswith("__")]
print(fields)

# 객체에서 속성이나 메서드를 가져오는 함수
for field in fields :
    print(getattr(p , field))

# 특정 개체 안에 있는 모든 메서드와 변수들을 다 가져옴
# ismethod = 메서드인지 확인
# isfunction = 함수인지 확인
print(inspect.getmembers(p))
for item , value in inspect.getmembers(p) :
    if inspect.ismethod(value) or inspect.isfunction(value) :
        print("함수" , item)
    else :
        print("변수" , item)