# [정올 587/Python] 함수3 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=224&sca=10d0

def Recursive(n):
    for i in range(n):
        print(n-i, end = " ")

n = int(input())
Recursive(n)