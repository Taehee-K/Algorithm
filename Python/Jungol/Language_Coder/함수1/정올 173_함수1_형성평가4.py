# [정올 173/Python] 함수1 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=73&sca=10b0

def exp(large, small):
    return (large**2 - small**2)
    
x, y = map(int, (input().split()))
if x<y: print(exp(y, x))
else: print(exp(x, y))
