def solution(num_list):
    even_count = sum(1 for x in num_list if x % 2 == 0)
    odd_count = sum(1 for x in num_list if x % 2 != 0)
    return [even_count, odd_count]
