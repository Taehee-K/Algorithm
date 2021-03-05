# [정올 581/Python] 함수2 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=218&sca=10c0

def Number(x, y):
    if abs(x)<abs(y): x, y = y, x
    if type(x)==int:
        print(x)
    else: print("{:.2f}".format(y))

int1, int2 = map(int, input().split())
Number(int1, int2)
real1, real2 = map(float, input().split())
Number(real1, real2)