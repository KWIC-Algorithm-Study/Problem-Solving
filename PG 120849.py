def solution(my_string):
    answer = ""
    vowels = ["a", "e", "i", "o", "u"]
    for a in my_string:
        if a not in vowels:
            answer += a
    return answer