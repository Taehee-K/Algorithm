# [정올 172/Python] 함수1 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=72&sca=10b0

def square(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            num = i*j
            print(num, end = " ")
        print()
    
square(int(input()))
