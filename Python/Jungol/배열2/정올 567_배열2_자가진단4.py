# [정올 567/Python] 배열2 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=204&sca=10a0

num = [[5, 8, 10, 6, 4], [11, 20, 1, 13, 2], [7, 9, 14, 22, 3]]

for i in range(3):
    for j in range(5):
        print("{:>2}".format(num[i][j]), end = "   ")
    print()