A = int(input())
B = int(input())
C = int(input())
if (2 <= A, B, C <= 10000):
    print((A + B) % C)
    print(((A % C + B % C)) % C)
    print((A * B) % C)
    print(((A % C) * (B % C))%C)
