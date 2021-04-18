# [코드업 6079/Python] 종합 - 언제까지 더해야 할까?
# https://codeup.kr/problem.php?id=6079

n = int(input())

total = 0
for i in range(n):
    total+=(i+1)
    if total>=n: 
        print(i+1)
        break
