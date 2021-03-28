# [정올 554/Python] 반복제어문3 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=191&sca=1080

n = int(input())
ch = ord("A") # 문자 ASCII 코드값으로
num = 1

for i in range(n):
    for j in range(n+1):
        if (j<n-i):
            print(num, end=" ")
            num+=1
        else:
            print(chr(ch), end=" ")
            ch+=1
    print()