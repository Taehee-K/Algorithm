# [정올 153/Python] 배열1 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=52&sca=1090

num = list(map(int, input().split()))

for i in range(len(num)):
    if len(num)>3 and num[i]==-1:
        print(num[i-3], num[i-2], num[i-1])
    elif len(num)>2 and num[i]==-1:
        print(num[i-2], num[i-1])
    elif len(num)>1 and num[i]==-1:
        print(num[i-1])