# [정올 144/Python] 반복제어문3 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=44&sca=1080

n = int(input())

for i in range(n):
    print(" "*(2*(n-1-i))+"*"*(2*i+1))