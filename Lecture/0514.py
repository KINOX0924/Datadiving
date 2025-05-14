# 5월 14일 강의

# 정규 표현식
# 복잡한 문자열을 처리할 때 사용하는 기법으로 파이썬 뿐만이 아니라 문자열을 사용하는 모든 곳에서 사용하는 일종의 형식 언어
# 패턴은 문자열 \ - 이건 기본적으로 escape 문자로 사용하기에 패턴에서는 \ 문자 자체가 필요한건지 아닌지 모르기에 항상 escape 탈출 문자인 'r' 을 붙혀야 함

import re
pattern = r"비"

text = "하늘에 비가 오고 있습니다. 어제도 비가 내렸고 오늘도 비가 내리고 있습니다. 비가 계속해서 내리고 있습니다. 목요일에도 비가 내린답니다. 주말에는 비가 안 내린답니다."

regex  = re.compile(pattern)
result = regex.findall(text)
print(text)
print(result)