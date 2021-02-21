# [정올 552/Python] 반복제어문3 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=189&sca=1080

n = int(input())

for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))