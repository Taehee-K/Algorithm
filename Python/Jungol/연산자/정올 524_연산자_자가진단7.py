# [정올 524/Python] 연산자 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=161&sca=1030
 
x, y = map(int, input().split())

print("%d %d" % (bool(x and y), bool(x or y)))  