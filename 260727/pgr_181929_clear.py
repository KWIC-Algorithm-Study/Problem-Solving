def solution(num_list):
    # 1. 모든 원소의 곱 구하기
    multiply = 1
    for num in num_list:
        multiply *= num  # multiply = multiply * num 과 같아요!
        
    # 2. 모든 원소의 합의 제곱 구하기
    sum_square = sum(num_list) ** 2
    
    # 3. 크기 비교하기 (곱 < 합의 제곱 이면 1, 아니면 0)
    if multiply < sum_square:
        return 1
    else:
        return 0