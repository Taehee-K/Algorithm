# [정올 584/Python] 함수2 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=221&sca=10c0

one = 1
two = 2
three = 3

def add(x, y, z):
    num = [x, y, z]
    for i in range(3):
        for j in range(3):
            print("%d + %d = %d"%(i+1, j+1, i+j+2))

add(one, two, three)