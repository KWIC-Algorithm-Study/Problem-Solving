def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = []  # k보다 큰 값들을 임시로 모아둘 바구니
        
        # s부터 e까지 인덱스를 순회 (e까지 포함해야 하므로 e + 1)
        for i in range(s, e + 1):
            if arr[i] > k:
                temp.append(arr[i])
                
        # 조건에 맞는 수가 존재하면 최솟값을, 없으면 -1을 추가
        if temp:
            answer.append(min(temp))
        else:
            answer.append(-1)
            
    return answer