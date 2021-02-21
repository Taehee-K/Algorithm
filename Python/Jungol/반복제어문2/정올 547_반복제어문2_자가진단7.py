# [정올 547/Python] 반복제어문2 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=184&sca=1070

num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5):
    for j in range(i, i+5):
        print(num[j], end = " ")
    print()