# [코드업 6095/Python] 종합 - 바둑판에 흰 돌 놓기
# https://codeup.kr/problem.php?id=6095

n = int(input())    # 흰 돌의 개수
board = [[0]*19 for i in range(19)] # 바둑판 19x19

for i in range(n):  
    x, y = map(int, input().split()) # x,y 좌표
    board[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j], end = " ")
    print()