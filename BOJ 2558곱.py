A = int(input())
B = int(input())
# B의 첫째 자리
b1 = B % 10
# B의 둘째 자리
b2 = (B // 10) % 10
# B의 셋째 자리
b3 = B // 100

if (100 <= A <= 999 and 100 <= B <= 999):
    print(A * b1)
    print(A * b2)
    print(A * b3)
    print(A * B)
