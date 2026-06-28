def solution(p):
    l=len(p)
    answer = '*'*(l-4)
    for i in range(4):
        answer+=p[-4+i]
    return answer