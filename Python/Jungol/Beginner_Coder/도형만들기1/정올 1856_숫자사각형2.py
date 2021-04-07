# [정올 1856/Python] 숫자사각형2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1129&sca=20

n, m = map(int, input().split()) # n: 높이, m: 너비

# 숫자사각형 생성
num = [[(j+1)+(m)*(i) for j in range(m)]for i in range(n)] 

for i in range(n):
    for j in range(m):
        if i%2==0: print(num[i][j], end = " ")
        else: print(num[i][m-j-1], end = " ")
    print()

