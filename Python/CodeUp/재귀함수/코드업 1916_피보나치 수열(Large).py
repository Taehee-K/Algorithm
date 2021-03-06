# [코드업 1916/Python] 재귀함수 - 피보나치 수열(Large)
# https://codeup.kr/problem.php?id=1916

def Fibonacci(num, n):
    num.append(num[-1]+num[-2]) # 앞의 두 수 더한 값
    if n>3: Fibonacci(num, n-1)
    else: print(num[-1]%10009)

num = [1, 1]
n = int(input())
print(1) if n==1 or n==2 else Fibonacci(num, n)