# [정올 553/Python] 반복제어문3 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=190&sca=1080

n = int(input())
ch = ord('A')  # ord() 사용해 ASCII 코드값 구하기
for i in range(n):
    for j in range(n-i):
        print(chr(ch), end="")  # chr() 사용해 ASCII->char   
        ch+=1
    print()