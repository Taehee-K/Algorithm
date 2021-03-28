# [정올 171/Python] 함수1 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=71&sca=10b0

def add(n):
    total = 0
    for i in range(1, n+1):
        total+=i
    print(total)

add(int(input()))