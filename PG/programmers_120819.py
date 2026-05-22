def solution(money):
    a = money // 5500
    answer = [a, money - a*5500]
    return answer
