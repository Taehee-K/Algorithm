# [정올 1314/Python] 문자사각형2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2072&sca=20

n = int(input())

letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
square = [['A']*n for _ in range(n)] # 임시 list

index = 0
for i in range(n):
    for j in range(n):
        if i%2==0:square[j][i] = letter[index%len(letter)]
        else: square[n-j-1][i] = letter[index%len(letter)]
        index+=1
for i in range(n):
    for j in range(n):
        print(square[i][j], end= " ")
    print()