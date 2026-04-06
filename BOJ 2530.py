A , B, C = map(int, input().split())
D = int(input())
total_second = A * 3600 + B * 60 + C + D
hour = (total_second // 3600) % 24
minute = (total_second % 3600) // 60
second = total_second % 60
print(hour, minute, second)