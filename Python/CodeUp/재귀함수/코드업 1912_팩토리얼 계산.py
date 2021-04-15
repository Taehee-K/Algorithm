# [코드업 1912/Python] 재귀함수 - 팩토리얼 계산
# https://codeup.kr/problem.php?id=1912

def Factorial(n, ans):
    ans*=n
    if n>1: Factorial(n-1, ans)
    else: print(ans)
n = int(input())
Factorial(n, 1)