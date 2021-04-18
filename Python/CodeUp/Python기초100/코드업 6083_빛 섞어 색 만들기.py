# [코드업 6083/Python] 종합 - 빛 섞어 색 만들기
# https://codeup.kr/problem.php?id=6083

r, g, b = map(int, input().split())

color = []
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count+=1
print(count)