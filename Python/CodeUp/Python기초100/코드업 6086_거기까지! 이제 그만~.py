# [코드업 6086/Python] 종합 - 거기까지! 이제 그만~
# https://codeup.kr/problem.php?id=6086

n = int(input())

total = 0
i = 0
while True:
    total+=i; i+=1
    if total>=n: print(total); break;