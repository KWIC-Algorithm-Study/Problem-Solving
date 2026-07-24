def solution(a, d, included):
    answer = 0
    
    # i는 인덱스 번호(0, 1, 2...), flag는 True 또는 False
    for i, flag in enumerate(included):
        # flag가 True일 때만 해당 등차수열 값을 더해줍니다!
        if flag:
            answer += a + (i * d)
            
    return answer