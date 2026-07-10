def solution(array, n):
    array.sort()
    
    answer = array[0]
    min_gap = abs(n - array[0])
    
    for num in array:
        gap = abs(n - num)
        
        if gap < min_gap:
            min_gap = gap
            answer = num
    return answer