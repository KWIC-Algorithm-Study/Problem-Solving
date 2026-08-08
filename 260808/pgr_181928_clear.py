def solution(num_list):
    odd_str = ""   # 홀수 글자를 붙일 상자
    even_str = ""  # 짝수 글자를 붙일 상자
    
    for num in num_list:
        if num % 2 != 0:
            odd_str += str(num) 
        else:
            even_str += str(num)
            

    return int(odd_str) + int(even_str)