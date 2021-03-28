# [정올 149/Python] 반복제어문3 - 형성평가A
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=49&sca=1080

n = int(input())
num=1

for i in range(n):
    for j in range(n):
        print((2*num-1)%10,end=" ")
        num+=1
    print()