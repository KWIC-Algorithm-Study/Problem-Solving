def solution(num_list):
    last = num_list[-1]
    previous = num_list[-2]

    if last > previous:
        num_list.append(last - previous)
    else:
        num_list.append(last * 2)

    return num_list