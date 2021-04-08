# [정올 1307/Python] 문자사각형3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2071&sca=20

n = int(input())

letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
square = [['A']*n for _ in range(n)] # 임시 list

index = 0
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        square[j][i] = letter[index%len(letter)]
        index+=1

for i in range(n):
    for j in range(n):
        print(square[i][j], end = " ")
    print()