# [코드업 2623/Python] 탐색기반설계 - 최대공약수 구하기
# https://codeup.kr/problem.php?id=2623

a, b = map(int, input().split())
if a>b: a, b = b, a # a가 더 작은 숫자가 되도록 
if b%a==0: print(a)
else: 
    for i in range(a+1, -1, -1):
        if a%i==0 and b%i==0:
            print(i)
            break 