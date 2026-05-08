def solution(lines):
    count = [0] * 201
    
    for start, end in lines:
        for i in range(start, end):
            count[i + 100] += 1
    result = 0
    for c in count:
        if c >= 2:
            result += 1
    return result