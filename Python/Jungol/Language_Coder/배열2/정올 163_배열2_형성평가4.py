# [정올 163/Python] 배열2 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=63&sca=10a0

arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]

total = 0
for i in range(4):
    for j in range(3):
        total +=arr[i][j]
        print(arr[i][j], end = " ")
    print()
print(total)