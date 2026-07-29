def solution(picks, minerals):
    answer=0
    #5개씩 묶어서 점수 합산하고 0,25,125  0,5,25
    score_lst=[]
    el=[0,0,0]
    for i in range(len(minerals)):
        if minerals[i]=="diamond":
            el[0], el[1], el[2] = el[0] + 1, el[1] + 5, el[2] + 25
        elif minerals[i]=="iron":
            el[0], el[1], el[2] = el[0] + 1, el[1] + 1, el[2] + 5
        else:
            el[0], el[1], el[2] = el[0] + 1, el[1] + 1, el[2] + 1
        if (i+1)%5==0 or i+1==len(minerals):
            score_lst.append(el)
            el=[0,0,0]
        #사용할 수 있는 곡괭이 수만큼 자르기
        score_lst=score_lst[0:sum(picks)]
    #max값 순으로 정렬
    score_lst.sort(key=max, reverse=True)
    for i in score_lst:
        if picks[0]!=0:
            picks[0]-=1
            answer+=i[0]
        elif picks[1]!=0:
            picks[1]-=1
            answer+=i[1]
        elif picks[2]!=0:
            picks[2]-=1
            answer+=i[2]
    return answer