"""

오름차순의 경우
셀렉트 정렬 : 제일 작은 사람은 첫번째 방에 / 두번째 작은 사람은 두번째 방에 / 세번째 작은 사람은 세번째 방에
- 왼쪽부터 정렬되는 것
- a[i] 와 a[j] 를 비교

버블 정렬 : 바로 옆에 사람 비교함 / 계속 바꿔치기
- 제일 큰 사람이 계속 뒤로 밀리며 거품이 보글거리를 느낌을 받음
- a[i] 와 a[i+1] 을 비교

"""

# 내가 작성한 버블 정렬
# def bubbleSort(list) :
#     for index in range(0,len(list)) :
#         for index_2 in range(0,len(list)-1) :
#             if list[index_2] > list[index_2 + 1] :
#                 list[index_2] , list[index_2 + 1] = list[index_2 + 1] , list[index_2]
#             print(list)

# if __name__ == "__main__" :
#     no_sort_list = [ 9 , 7 , 25 , 6 , 8 , 4 , 3]
    
#     bubbleSort(no_sort_list)
    
"""

알고리즘
속도가 빠르면 메모리를 많이 차지함
속도가 느리면 메모리를 덜 차지함
최근에는 메모리가 엄청 싸서 속도 위주의 알고리즘을 선택함


퀵정렬 - 재귀호출
기준점 0 ~ 11   : 0 번방을 기준으로 
                Left = 0
                right = 11
                a[0] > a[left] 일때까지 left 증가
                
                Left = 1
                a[0] < a[right] 일때까지 right 감소
                right = 8
                
                a[left] <=> a[right]
            
"""

arr = [5,1,6,4,8,3,7,9,2,10]

# arr[0 ~ 9]
# arr[0 ~ 4] , 기준점 , a[6 ~ 9]
def quicksort(arr , start , end) :
    if start >= end :
        return
    
    pivot = arr[start]
    left = start + 1
    right = end
    
    print(f"Left : {left} right : {right}")
    while left <= right :
        # left > right 가 되면 배분이 종료된 것
        # left 증가 시키면서 arr[left] 가 피벗(기준점) 보다 큰 것을 만날때까지
        # left 가 end 보다 작은 동안
        while left <= end and arr[left] < pivot :
            left += 1
        while right > start and arr[right] > pivot :
            right -= 1
            
        print(f"Left : {left} right : {right}")
        
        if left < right :
            arr[left] , arr[right] = arr[right] , arr[left]
        else :
            break
    
    arr[start] , arr[right] = arr[right] , arr[start]
    print(arr)
    
    quicksort(arr , start , right - 1)
    quicksort(arr , right + 1 , end)

quicksort(arr , 0 , len(arr) - 1)