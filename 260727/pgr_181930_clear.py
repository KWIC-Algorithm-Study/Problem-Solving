def solution(a, b, c):
    # 1. 계산에 필요한 합들을 미리 변수에 담아두면 깔끔합니다!
    sum1 = a + b + c
    sum2 = a**2 + b**2 + c**2
    sum3 = a**3 + b**3 + c**3
    
    # 2. 세 숫자가 모두 같을 때
    if a == b == c:
        return sum1 * sum2 * sum3
        
    # 3. 세 숫자가 모두 다를 때
    elif a != b and b != c and a != c:
        return sum1
        
    # 4. 나머지 (두 숫자는 같고, 하나는 다를 때)
    else:
        return sum1 * sum2