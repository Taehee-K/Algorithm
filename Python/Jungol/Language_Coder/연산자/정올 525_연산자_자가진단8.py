# [정올 525/Python] 연산자 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=162&sca=1030
 
x, y, z = map(int, input().split())

if (x > (y or z)): print(1)
else: print(0)

if (x==y==z): print(1)
else: print(0)
