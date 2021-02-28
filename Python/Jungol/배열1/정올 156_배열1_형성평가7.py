# [정올 156/Python] 배열1 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=56&sca=1090

num = list(map(int, input().split()))


for i in range(len(num)):
    if num[i]==999:
        n = num[:i]
        print('max :', max(n))
        print('min :', min(n))
        break