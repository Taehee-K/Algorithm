# [정올 145/Python] 반복제어문3 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=45&sca=1080

n = int(input())

for i in range(n):
    num=1
    for j in range(n):
        if j<(n-i-1):
            print(" ", end=" ")
        else:
            print(num, end=" ")
            num+=1
    print()
