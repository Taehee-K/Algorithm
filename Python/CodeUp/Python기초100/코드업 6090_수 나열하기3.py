# [코드업 6090/Python] 종합 - 수 나열하기3
# https://codeup.kr/problem.php?id=6090

a, m, d, n = map(int, input().split())

total = a*m**(n-1)
if n>2:
    for i in range(n-2, -1, -1):
        total += d*m**(i)
print(total) 