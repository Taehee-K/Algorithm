# [코드업 6077/Python] 종합 - 짝수 합 구하기
# https://codeup.kr/problem.php?id=6077

n = int(input())

total = 0
for i in range(1, n+1):
    if i%2==0:
        total+=i
print(total)