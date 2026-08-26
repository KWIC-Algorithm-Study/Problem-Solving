def solution(l, r):
    answer = []
    
    for num in range(l, r + 1):
        # 숫자를 문자열로 바꿔서 모든 글자가 '0' 또는 '5'인지 확인
        if all(char in "05" for char in str(num)):
            answer.append(num)
            
    # 조건에 맞는 숫자가 하나도 없으면 [-1] 반환
    return answer if answer else [-1]