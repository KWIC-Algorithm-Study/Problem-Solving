# AI 도움
def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        # 1. stk가 빈 배열인 경우
        if not stk:
            stk.append(arr[i])
            i += 1
        # 2. stk에 원소가 있고, 마지막 원소가 arr[i]보다 작은 경우
        elif stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        # 3. stk에 원소가 있고, 마지막 원소가 arr[i]보다 크거나 같은 경우
        else:
            stk.pop()  # 맨 뒤 원소 제거 (i는 증가시키지 않음!)
            
    return stk