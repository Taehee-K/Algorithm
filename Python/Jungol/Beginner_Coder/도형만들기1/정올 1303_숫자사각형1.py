# [정올 1303/Python] 숫자사각형1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2069&sca=2010

n, m = map(int, input().split()) # n: 높이, m: 너비

num = 1
for i in range(n):
    for j in range(m):
        print(num, end = " ")
        num+=1
    print()