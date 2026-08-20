def solution(arr, queries):
    # queries 안에 들어있는 [i, j]를 하나씩 꺼냅니다
    for i, j in queries:
        # arr의 i번째 값과 j번째 값을 서로 맞바꿉니다
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr