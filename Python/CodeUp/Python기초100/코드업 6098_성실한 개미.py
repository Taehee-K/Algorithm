# [코드업 6098/Python] 리스트 - 성실한 개미
# https://codeup.kr/problem.php?id=6098

# 미로 상자 입력받기 (10*10)
maze = [list(map(int, input().split())) for _ in range(10)] 

k = 1       # 시작점 
fin = False # 이중 for문 모두 빠져나오기 위해 flag
for i in range(1, 10):
    for j in range(k, 10):
        if maze[i][j]==0: maze[i][j] = 9 
        elif maze[i][j]==2: 
            maze[i][j] = 9 
            fin = True
            break
        else: 
            k = j-1
            break
    if fin==True: break

for i in range(10):
    for j in range(10):
        print(maze[i][j], end = " ")
    print()