# [정올 137/Python] 반복제어문2 - 형성평가8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=37&sca=1070

# 행과 열의 수를 입력
row, col = map(int, input().split())

for i in range(row):
    for j in range(col):
        print((i+1)*(j+1), end=" ")
    print()
    
