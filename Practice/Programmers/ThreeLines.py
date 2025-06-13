class Lineoverlap :
    def __init__(self , lines_list) :
        self.lines   = lines_list
        self.overlap = [[0 for _ in range(0,201)] for _ in range(0,4)]
        # 0 부터 200 까지의 0 이 가득찬 리스트 네 개를 생성
        
        # print(self.check_overlap)   # 디버깅
    
    # 선분의 길이를 음수도 있는 환경에서 모두 양수로 변환함
    def transPositive(self) :
        for line in self.lines :
            for index in range(len(line)) :
                line[index] += 100
        
        # print(self.lines)   # 디버깅
    
    # 각 길이를 overlap 리스트에 삽입함
    def insertLine(self) :
        count = 0
        
        for line in self.overlap :
            for index in range(self.lines[count][0] , self.lines[count][1] + 1) :
                line[index] += 1
            count += 1
            if count == 3 :
                break
        
        # print(self.overlap) # 디버깅
    
    # A 라인과 B 라인의 겹치는 곳 , A 라인과 C 라인이 겹치는 곳 , B 라인과 C 라인이 겹치는 곳이 존재한다면 오버랩 리스트에 1 추가
    def checkOverlap(self) :
        for index in range(0 , len(self.overlap[0])) :
            if self.overlap[0][index] == 1 and self.overlap[1][index] == 1 and self.overlap[2][index] == 1 :
                self.overlap[3][index] = 4
            elif self.overlap[0][index] == 1 and self.overlap[1][index] == 1 :
                self.overlap[3][index] = 1
            elif self.overlap[0][index] == 1 and self.overlap[2][index] == 1 :
                self.overlap[3][index] = 2
            elif self.overlap[1][index] == 1 and self.overlap[2][index] == 1 :
                self.overlap[3][index] = 3
        
        print(self.overlap[3]) # 디버깅
    
    # stack 처럼 사용해서 길이를 구함(끊기는 구간도 있기 때문에)
    def getOverlapLength(self) :
        number_list = [1 , 2 , 3]
        stack  = 0
        length = 0
        
        # 수정 중
        for number in self.overlap[3] :
            if stack == 0 and number in number_list :
                stack = number
            elif stack == 0 and number == 4 :
                stack = number
            elif stack != 0 and number == 4 :
                stack = 4
                length += 1
            elif stack == 4 and number in number_list :
                stack = number
                length += 1
            elif stack in number_list and stack != number :
                stack = number
            elif stack == number and stack in number_list:
                length += 1
        
        print(length)   # 디버깅
    
if __name__ == "__main__" :
    # lines = [[0,1],[2,5],[3,9]]
    # lines = [[-1,1],[1,3],[3,9]]
    # lines = [[0,5],[3,9],[1,10]]
    # lines = [[0,2],[-3,-1],[-2,1]]
    lines = [[0, 5], [0, 5], [0, 5]]
    overlap = Lineoverlap(lines)
    overlap.transPositive()
    overlap.insertLine()
    overlap.checkOverlap()
    overlap.getOverlapLength()