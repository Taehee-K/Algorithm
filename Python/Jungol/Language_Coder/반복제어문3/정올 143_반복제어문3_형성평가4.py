# [정올 143/Python] 반복제어문3 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=43&sca=1080

n = int(input())

for i in range(2*n-1):
    if i<n:
        print(" "*i+"*"*(2*(n-i)-1))
    else:
        print(" "*(2*(n-1)-i)+"*"*3+"*"*(2*(i-n)))