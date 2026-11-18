def solution(b, h, w):
    answer = 0
    move=[[1,0],[-1,0],[0,1],[0,-1]]
    leng=len(b)
    for i,j in move:
        if 0<=h+i<leng and 0<=w+j<leng and b[h+i][w+j]==b[h][w]:
            answer+=1
    return answer
