def solution(code):
    ret = ''
    mode = 0
    
    # enumerate를 쓰면 idx(인덱스 번호)와 char(글자)를 동시에 꺼내줍니다!
    for idx, char in enumerate(code):
        # 1. "1"을 만나면 mode를 전환!
        if char == "1":
            mode = 1 - mode  # mode가 0이면 1이 되고, 1이면 0이 되는 파이썬 꿀팁!
            
        # 2. "1"이 아닐 때
        else:
            # mode가 0이고 짝수 인덱스거나, mode가 1이고 홀수 인덱스일 때만 줍기
            if mode == 0 and idx % 2 == 0:
                ret += char
            elif mode == 1 and idx % 2 != 0:
                ret += char
                
    # 3. 바구니가 비어있다면 "EMPTY" 반환, 아니면 ret 반환
    return ret if ret != "" else "EMPTY"