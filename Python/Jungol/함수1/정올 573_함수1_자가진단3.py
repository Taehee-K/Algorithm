# [정올 573/Python] 함수1 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=210&sca=10b0

def NumberSquare(n):
    square = [[0]*n for _ in range(n)]
    num = 0
    for i in range(n):
        for j in range(n):
            num+=1
            square[i][j] = num
            print(square[i][j], end =" ")
        print()

n = int(input())
NumberSquare(n)