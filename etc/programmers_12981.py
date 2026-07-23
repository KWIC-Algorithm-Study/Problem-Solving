def solution(n, words):
    dup=[words[0]]
    for i in range(1,len(words)):
        if words[i] not in dup and dup[-1][-1] == words[i][0]:
            dup.append(words[i])   
        else:
            return [(i)%n+1,i//n+1]
    return [0,0]