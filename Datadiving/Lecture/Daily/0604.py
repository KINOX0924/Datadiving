"""
6월 4일 강의
큐

FIFO - 선입선출(First in First out)
- 메세지큐 또는 버퍼라고도 하며 대기줄 같은 느낌임
- 버퍼 : 컴퓨터의 입출력 장치와 메모리간의 속도차가 너무 커서 일부 메모리 공간을 잘라서 우리가 키보드를 누르면 그 값이 버퍼라는 공간에
먼저 들어갔다가 엔터키를 누르면 그 때 메모리로 들어감 / 데이터를 모아두었다가 한번에 처리하는 방식

배열          : 환형큐(동그라미)
링크드리스트   : 더블링크드리스트
우선순의 큐    : 데이터에 우선순위를 주어 우선순위에 따라서 데이터의 순서가 바뀜
              : 메세지큐 : 윈도우 O/D 안에 있으며 사람의 동작(이벤트) 이 미친듯이 발생하면 컴퓨터가 미처 감당할 수 없으니깐 각각의 이벤트에 번호를 붙여 어디서 무슨일이 있었는 지 다 기록해서 큐에 넣어놓음

양방향 큐      : 양쪽에서 데이터를 넣고 빼기가 다 가능함
기본 큐        : 한쪽 방향에서 데이터를 넣기만 하고 한쪽 방향에서는 데이터를 가져가기만 함

front : 이쪽에서 데이터를 가져감
rear  : 이쪽에서 데이터를 추가함

put     : 큐에 데이터를 넣는 연산
get     : 큐에서 데이터를 가져오는 연산
isFull  : 큐가 꽉 차있으면 True , 아니면 False
isEmpty : 큐가 비어있으면 Treu , 아니면 False
peek    : 큐의 맨 처음 값 하나만 확인하는 용도(데이터 삭제 X)

* 큐 기본 초기화 상태 : 0 1 2 3 4
* front = 0 and rear = 0 이면 Empty 상테
* put("A") 를 하면 rear 에 1 이 들어감 ->> 0 "A" 0 0 0  // 0 번 인덱스는 사용하지 않음
* put("B") 를 하면 rear 에 2 가 들어감 ->> 0 "A" "B" 0 0
* put("C") 를 하면 rear 에 3 이 들어감 ->> 0 "A" "B" "C" 0
* put("D") 를 하면 rear 에 4 가 들어감 ->> 0 "A" "B" "C" "D"
* 이때 또 다시 put 을 했을 때 (rear + 1) % 5 == front 와 동일하다면 Full 상태

* get() 을 하면 front = 1 , rear = 4 상태 ->> 0 0 "B" "C" "D" // 이때 (rear + 1) % 5 == front 상태가 아니기에 Full 상태가 아님
* get() 을 하면 front = 2 , rear = 4 상태 ->> 0 0 0 "C" "D"
* get() 을 하면 front = 3 , rear = 4 상태 ->> 0 0 0 0 "D"
* get() 을 하면 front = 4 , rear = 4 상태 ->> 0 0 0 0 0 // front == rear 가 되었으므로 Empty

"""

class MyQueue :
    def __init__(self , size = 10) :
        if size < 10 :
            self.size = 10
        else :
            self.size = size
            
        self.queue = [None] * self.size # 주어진 사이즈만큼 메모리 확보
        # print(self.queue)   # TODO 디버깅 출력
        
        self.front = 0
        self.rear  = 0
        self.count = 0
    
    def put(self , data) :
        if self.isFull() == False :
            self.rear  += 1
            self.count += 1
            self.queue[self.rear] = data
            # print(f"{data} 가 큐에 저장되었습니다.")
            for i in 
            return True , self.count
        else :
            # print("현재 대기줄이 최대로 차있습니다.")
            return False , None
            # print(self.queue)   # TODO 디버깅 출력
    
    def get(self) :
        if self.isEmpty() == True :
            print("현재 대기 중인 고객이 없습니다.")
            return False , None
        else :
            self.front += 1
            self.count -= 1
            temp = self.queue[self.front]
            self.queue[self.front] = None
            
            # print(self.queue)               # TODO 디버깅 출력
            # print(f"front : {self.front}")  # TODO 디버깅 출력
            return True , temp
    
    def peek(self) :
        if self.isEmpty() == True :
            print("현재 대기 중인 고객이 없습니다.")
        else :
            return self.queue[self.front + 1]
        
    def reset(self) :
        if self.isEmpty() == True :
            self.front = 0
            self.rear = 0
            # print("큐 대기열 초기화 완료")
        else :
            # print("큐 내부에 데이터가 남아있어 초기화 불가")
            return
    
    def isFull(self) :
        if (self.rear + 1) % self.size == self.front :
            return True
        return False
    
    def isEmpty(self) :
        if self.front == self.rear :
            return True
        return False

class bank :
    def __init__(self) :
        self.queue_1 = MyQueue(1000)
        self.count = 0
    
    def waiting(self) :
        self.count += 1
        
        now , number = self.queue_1.put(self.count)
        if now == True :
            print(f"현재 고객 대기 번호 : {self.count} || 앞에 남은 사람 : {number - 1}")
        else :
            print("현재 대기줄이 최대로 차있습니다.")
            
    def nextCustomer(self) :
        now , number = self.queue_1.get()
        if now == True :
            print(f"호출 고객 번호 : {number}")
    
if __name__ == "__main__" :
    user = bank()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    user.waiting()
    
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    user.nextCustomer()
    
    
# 은행에 가서 순번 뽑기
# 은행원 작업 완료 -> 몇 번 손님 나오세요
# 고객  : 번호 뽑기 -> 대기 인원 나와야함