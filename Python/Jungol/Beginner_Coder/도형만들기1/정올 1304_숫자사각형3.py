# [정올 1304/Python] 숫자사각형3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2070&sca=20

n = int(input())

# base 숫자사각형 생성
num = [[(j+1)+(n)*(i) for j in range(n)]for i in range(n)] 

for i in range(n):
    for j in range(n):
        print(num[j][i], end = " ")
    print()