# [정올 168/Python] 배열2 - 형성평가9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=68&sca=10a0

n = int(input()) # get number of rows

pascal = []
for i in range(n):
    pascal.append([1]*(i+1)) # 새로운 행 1로 초기화
    for j in range(i+1):
        if j==0 or j==i:
            continue
        else:
            pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j]

for i in range(n):
    for j in range(n-i):
        print(pascal[n-i-1][j], end = " ")
    print()
