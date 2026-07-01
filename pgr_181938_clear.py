def solution(a, b):
    ab = int(str(a) + str(b))
    num = 2 * a * b
    if ab >= num:
        return ab
    elif ab < num:
        return num