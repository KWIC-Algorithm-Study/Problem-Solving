n = int(input())
data=[]

for _ in range(n):
    a,b=map(int, input().split())
    data.append((a, b))

data.sort()
for a,b in data:
    print(a,b)
