# [정올 559/Python] 배열1 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=196&sca=1090


grade = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]

x, y = map(int, input().split())
add = grade[x-1]+ grade[y-1]
print("{:.1f}".format(add))