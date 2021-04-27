# [코드업 6097/Python] 리스트 - 설탕과자 뽑기
# https://codeup.kr/problem.php?id=6097

h, w = map(int, input().split())        # h: 세로, w: 가로
board = [[0]*w for _ in range(h)]       # 격자판 초기화

n = int(input())                            # n: 막대의 개수
for i in range(n):                          # 막대의 개수만큼 반복
    l, d, x, y = map(int, input().split())  # l: 길이, d: 방향(0/1), (x, y): 좌표
    if d==0:    # 막대 가로로 놓여져 있을 때
        for j in range(l):
            board[x-1][y-1+j] = 1
    if d==1:    # 막대 세로로 놓여져 있을 때
        for j in range(l):
            board[x-1+j][y-1] = 1

for i in range(h): 
    for j in range(w):
        print(board[i][j], end = " ")
    print()