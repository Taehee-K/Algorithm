# [정올 165/Python] 배열2 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=65&sca=10a0

array = [[0]*5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i==0 and j%2==0: array[i][j]=1    # 1행의 1열과 3열 5열을 각각 1로 초기화
        
        # 위행의 왼쪽과 오른쪽의 값을 더하여 채운 후 출력
        else: 
            if j==0:
                array[i][j] = array[i-1][j+1]
            elif j==4:
                array[i][j] = array[i-1][j-1]
            else:
                array[i][j] = array[i-1][j-1]+ array[i-1][j+1]
        print(array[i][j], end = " ")
    print()