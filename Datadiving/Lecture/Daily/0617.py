"""
에라토스테네스의 체

주제
N 과 K 가 주어졌을 때 K 번째로 지우는 수를 구하는 프로그램을 작성하시오

알고리즘
[1] 2 부터 N 까지 모든 정수를 적는다.
[2] 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P 라고 하고, 이 수는 소수이다.
[3] P 를 지우고, 아직 지우지 않은 P 의 배수를 크기 순서대로 지운다.
[4] 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
"""

"""
while 문 안에서 for 문이 작동 중 for 문 안에서 종료 조건을 알게 될 경우
차라리 함수면 return 을 호출하면 return 함수 종료문이기 때문에 for 도 끝나고 while 도 끝난다.

문제는 가끔 loop 안에 loop 가 있는데 내부 loop 에서 break 를 호출하면 내부 loop 만 종료한다. => 외부 loop 는 의미가 없음
"""
"""

class Eratosthenes :
    def __init__(self , N , K) :
        self.number = N
        self.count  = K
        self.num_list = [ x for x in range(2 , N + 1) ]
        
        print(self.num_list)    #TODO 디버깅
        
    def loop(self) :
        delete_num_list = []
        P = 0
        
        while len(self.num_list) != 0 :
            P = min(self.num_list)
            for index , number in enumerate(self.num_list) :
                if number == P :
                    delete_num_list.append(self.num_list.pop(index))
                elif number % P == 0 :
                    delete_num_list.append(self.num_list.pop(index))
                    
        print(self.num_list)    #TODO 디버깅
        print(delete_num_list)  #TODO 디버깅
    
        return delete_num_list[K-1]
            

if __name__ == "__main__" :
    N = 10
    K = 7
    
    E1 = Eratosthenes(N,K)
    K_delete = E1.loop()
    
    print(f"K번째로 지워진 숫자 : {K_delete}")
"""
    
def dfs(arr , depth , length) :
    # 이 함수가 끝나는 요건
    
    if depth == length :
        print(arr)  # 배열의 내용출력을 하고
        return      # 함수를 종료

    # 처음에 depth 는 0 부터 시작해서 1 , 2 , 3 , 4 식으로 나아감
    arr[depth] = "A"
    dfs(arr , depth + 1 , length)
    
    arr[depth] = "B"
    dfs(arr , depth + 1 , length)

length = 6
arr = [""] * length
dfs(arr , 0 , length)