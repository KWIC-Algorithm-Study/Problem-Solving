def solution(mats, park):
    mats.sort(reverse=True)
    h=len(park)
    w=len(park[0])
    for size in mats:
        if size>h or size>w:
            continue
        for row in range(h-size+1):
            for col in range(w-size+1):
                if [r[col:col+size] for r in park[row:row+size]]==[["-1"]*size]*size:
                    return size
    return -1
