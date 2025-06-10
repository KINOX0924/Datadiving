"""
그리디 알고리즘
* 그리디 : 욕심쟁이 , 탐욕

그리디 알고리즘은 반드시 정렬을 해야 문제를 풀 수 있음

거스름돈으로 줄 수 있는 동전이 500원 , 100원 , 50원 , 10원이 있을 때 ,
거스름돈 금액 N 원을 입력받아 동전의 최소 개수를 구하라
"""
"""
class CalChange :
    def __init__(self , change) :
        self.change = change
        self.coin_list = [500 , 100 , 50 , 10]
    
    def calculrator(self) :
        coin_count = [0 , 0 , 0 , 0]
        
        while self.change > 0 :
            if self.change >= self.coin_list[0] :
                self.change -= self.coin_list[0]
                coin_count[0] += 1
            elif self.change >= self.coin_list[1] :
                self.change -= self.coin_list[1]
                coin_count[1] += 1
            elif self.change >= self.coin_list[2] :
                self.change -= self.coin_list[2]
                coin_count[2] += 1
            else :
                self.change -= self.coin_list[3]
                coin_count[3] += 1
        
        return coin_count

if __name__ == "__main__" :
    change = 10530
    
    c1 = CalChange(change)
    coin_count = c1.calculrator()
    
    print(f"500 원 : {coin_count[0]} || 100 원 : {coin_count[1]} || 50 원 : {coin_count[2]} || 10 원 : {coin_count[3]}")
"""

"""
그리디 알고리즘 2
N 개의 회의에 대해 각 회의의 시작 시간과 종료시간이 주어짐
한 회의실에서 아용할 수 있는 최대 회의 개수를 구하시오
(회의가 겹치면 안됨)

meetings = [(1,4) , (3,5) , (0,6) , (5,7) , (8,9) , (5,9)]
"""

"""
[1] 기준점을 어떻게 설정할 것인가?
- 각 튜플사이의 시간으로 설정? -> (1,4) 보다 (3,5) 가 더 짧음
- 불가 ----

[2] (i,j) 라고 할때 i 를 0 부터 시작해서 j 는 (i , i + 1) 씩 해가면서 확인? 그 중에서 가장 짧은 것?
- 불가 ----

[3] 종료시간이 가장 낮은 숫자인 것 -> 회의가 빨리 끝난다는 것
- 종료시간이 가장 낮은 숫자로 정렬
- 그 다음으로 찾아야 할 것 [기준점의 종료시간보다 시작시간이 가장 가까우면서 시작시간과 종료시간의 텀이 가장 짧은 것]
=> 기준점의 종료시간보다 큰 시작 시간을 가진 튜플을 찾아냄 -> (5,7) , (8,9) , (5,9)
= meetings[i][1] > meetings[j][0]

=> 찾아낸 각 튜플중에서 종료시간이 가장 낮은 것을 찾아냄
* 기준점의 종료시간보다 낮은 시작시간을 가진 데이터는 버리면됨
* 버리면 여러번 확인을 할 필요가 없음

[4] 종료는 어떻게 할 것인가?
- 종료시간이 9 인 데이터가 들어오면? => 그 날 9시에 끝나는 회의가 없으면? 또는 9시 전에 끝나는 회의가 들어오는데 더 많은 회의를 진행하는 방법이라면?
- 미팅의 모든 데이터를 다 순회할때까지? => 위에서 데이터를 버리는 방법으로는 불가

* 스택?
- 스택으로 한다고 가정했을 때
[1] (1,4) 가 들어감 기준점
[2] (3,5) 가 왔을 때 (1,4) 의 종료시간이 (3,5) 의 시작 시간보다 높으니 푸쉬하지 않음
[3] (0,6) 가 왔을 때 (1,4) 의 종료시간이 (0,6) 의 시작 시간보다 높으니 푸쉬하지 않음
[4] (5,7) 가 왔을 때 (1,4) 의 종료시간이 (5,7) 의 시작 시간보다 낮으니 푸쉬함
[5] (8,9) 가 왔을 때 (5,7) 의 종료시간이 (8,9) 의 시작 시간보다 낮으니 푸쉬함
[6] (5,9) 가 왔을 때 (8,9) 의 종료시간이 (5,9) 의 시작 시간보다 높으니 푸쉬하지 않음
* 근데 .pop() 을 하는 것이 없으니 스택은 아닌 것 같음 ㅋㅋㅋㅋ

* meetings.sort(key=lambda x : x[1])
"""

class Searchmeeting :
    def __init__(self , meeting_times) :
        self.meeting_times = meeting_times
        self.meeting_times.sort(key = lambda x : x[1])
        self.set_meet = []
    
    def setMeeting(self) :
        for index in range(0 , len(self.meeting_times)) :
            if len(self.set_meet) == 0 :
                self.set_meet.append(self.meeting_times[0])
                print(self.set_meet)
            elif len(self.set_meet) != 0 :
                if self.set_meet[-1][1] < self.meeting_times[index][0] :
                    self.set_meet.append(self.meeting_times[index])
        
        print(self.set_meet)

if __name__ == "__main__" :
    meetings = [(1,4) , (3,5) , (0,6) , (5,7) , (8,9) , (5,9)]
    
    s1 = Searchmeeting(meetings)
    s1.setMeeting()