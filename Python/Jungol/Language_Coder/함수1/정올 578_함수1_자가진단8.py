# [정올 578/Python] 함수1 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=215&sca=10b0

def Multiple(start, fin):
    for i in range(start, fin+1):
        print("== {}dan ==".format(i))
        for j in range(9):
            print("{} * {} = {:2}".format(i, j+1, i*(j+1)))
        print()

x, y = map(int, input().split())

if x > y: 
    Multiple(y, x)
else: 
    Multiple(x, y)
