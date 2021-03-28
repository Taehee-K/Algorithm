# [정올 570/Python] 배열2 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=207&sca=10a0

array = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        if array[i-1][j]==0 or array[i][j-1]==0:
            array[i][j]=1
        else:
            array[i][j]= array[i-1][j]+ array[i][j-1]

        print(array[i][j], end = " ")
    print()


