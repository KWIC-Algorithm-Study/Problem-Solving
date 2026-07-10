def solution(quiz):
    answer = []
    for q in quiz:
        X, operator, Y, _, Z = q.split()
        X = int(X)
        Y = int(Y)
        Z = int(Z)
        
        if operator == '+':
            result = X + Y
        else:
            result = X - Y
        
        if result == Z:
            answer.append('O')
        else:
            answer.append('X')
            
    return answer