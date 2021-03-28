# [정올 146/Python] 반복제어문3 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=46&sca=1080

n = int(input())

ch = ord('A') # ASCII code for 'A'
num = 0
for i in range(n):
    for j in range(n):
        if j<(n-i):
            print(chr(ch), end=" ")  # ASCII code to character
            ch+=1
        else: 
            print(num, end=" ")
            num+=1
    print()

