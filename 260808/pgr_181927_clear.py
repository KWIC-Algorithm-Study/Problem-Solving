def solution(num_list):
    last = num_list[-1]   # 마지막 원소
    prev = num_list[-2]   # 그전 원소
    
    # 조건에 따라 리스트 뒤에 추가하기 (.append 사용)
    if last > prev:
        num_list.append(last - prev)
    else:
        num_list.append(last * 2)
        
    # 결과 리턴
    return num_list