# [정올 138/Python] 반복제어문2 - 형성평가9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=38&sca=1070

n = int(input())

for i in range(n):
    for j in range(n):
        print('(%d, %d)'%(i+1, j+1), end=" ")
    print()
