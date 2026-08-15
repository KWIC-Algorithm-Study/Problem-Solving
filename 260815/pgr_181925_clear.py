def solution(numLog):
    answer = ''
    
    # 0번은 시작점이니까 1번 인덱스부터 끝까지 반복합니다!
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]  # 현재 값 - 이전 값
        
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        elif diff == -10:
            answer += 'a'
            
    return answer