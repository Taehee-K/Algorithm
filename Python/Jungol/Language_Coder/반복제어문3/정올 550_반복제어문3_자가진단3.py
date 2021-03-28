# [정올 550/Python] 반복제어문3 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=187&sca=1080

n = int(input())
for i in range(2*n):
    if i<n: print("*"*(n-i))
    else: print("*"*(1-(n-i)))
