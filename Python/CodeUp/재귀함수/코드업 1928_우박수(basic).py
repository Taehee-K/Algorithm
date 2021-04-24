# [코드업 1928/Python] 재귀함수 - 우박수 (3n+1)(basic)
# https://codeup.kr/problem.php?id=1928

def Hailstone(n):
    print(n)
    if n==1: return
    elif n%2==1:
        n = 3*n +1
    else: n = n//2
    Hailstone(n)

n = int(input())
Hailstone(n)