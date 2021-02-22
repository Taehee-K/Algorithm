# [정올 147/Python] 반복제어문3 - 형성평가8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=47&sca=1080

n = int(input())

num = 1
for i in range(n):
    for j in range(n):
        if j<i: print(" ", end=" ")
        else: 
            print(num, end=" ")
            num+=1
    print()