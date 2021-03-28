# [정올 154/Python] 배열1 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=54&sca=1090

num = list(map(float, input().split()))

total = 0
for i in range(len(num)):
    total+=num[i]

print(round(total/len(num), 1))