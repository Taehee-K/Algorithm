# [정올 2046/Python] 숫자사각형4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1316&sca=20

n, m = map(int, input().split())

for i in range(n):
    for j in range(n):
        if m==1:    # 종류 1번
            print(i+1, end = " ")
        if m==2:    # 종류 2번
            if i%2==0: print(j+1, end = " ")
            else: print(n-j, end = " ")
        if m==3:    # 종류 3번
            print((j+1)*(i+1), end = " ")
    print()



