# [정올 159/Python] 배열1 - 형성평가A
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=59&sca=1090

n = int(input())
num = list(map(int, input().split()))

num.sort(reverse = True) # high -> low sort
for i in range(n):
    print(num[i])