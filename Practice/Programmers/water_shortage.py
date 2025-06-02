# 물이 부족해지지 않으면 -1 을 , 물이 부족하다면 0 을 리턴

def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage * (100 + change[i])/100
        # usage = total_usage * change[i]/100
        total_usage += usage
        if total_usage > storage:
            return i
    return -1
        
if __name__ == "__main__" :
    storage = 5141
    usage   = 500
    change  = [10, -10, 10, -10, 10, -10 , 10, -10 , 10, -10]
    
    # storage = 1000
    # usage   = 2000
    # change  = [-10 , 25 , 33]
    
    print(solution(storage , usage , change))