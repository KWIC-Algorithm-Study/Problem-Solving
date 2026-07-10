def solution(my_string, num1, num2):
    answer = ''
    arr = list(my_string)
    temp = arr[num1]
    arr[num1] = arr[num2]
    arr[num2] = temp
    
    answer = ''.join(arr)
    return answer