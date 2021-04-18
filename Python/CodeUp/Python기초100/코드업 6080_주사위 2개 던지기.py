# [코드업 6080/Python] 종합 - 주사위 2개 던지기
# https://codeup.kr/problem.php?id=6080

n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(i+1, j+1)