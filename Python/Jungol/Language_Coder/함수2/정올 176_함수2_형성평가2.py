# [정올 176/Python] 함수2 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=76&sca=10c0

from math import sqrt
def root():
    x, y = map(float, input().split())
    if x>y: x, y = y, x # x<y 가 되도록 순서 설정
    if sqrt(x)%1 == 0:
        print(int(sqrt(y)//1 - sqrt(x) + 1))
    elif sqrt(x)%1 !=0:
        print(int(sqrt(y)//1 - sqrt(x)//1))

root()