# [정올 588/Python] 함수3 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=225&sca=10d0

def Recursive(n):
    if n>0:
        print(n, end = " ")
        Recursive(n-1)

n = int(input())
Recursive(n)