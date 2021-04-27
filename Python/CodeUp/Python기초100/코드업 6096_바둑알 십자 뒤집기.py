# [코드업 6096/Python] 리스트 - 바둑알 십자 뒤집기
# https://codeup.kr/problem.php?id=6096

# 바둑판 초기 상태 입력받기
board = [list(map(int, input().split())) for _ in range(19)]

n = int(input())    # 뒤집기 횟수
for i in range(n):  # n 번 만큼 십자 뒤집기 진행
    x,y=map(int, input().split()) # 뒤집기 좌표 입력받기
    for j in range(19) :
        if board[j][y-1]==0:
            board[j][y-1]=1
        else:
            board[j][y-1]=0

        if board[x-1][j]==0:
            board[x-1][j]=1
        else :
            board[x-1][j]=0

for i in range(19): 
    for j in range(19): 
        print(board[i][j], end = " ")
    print()