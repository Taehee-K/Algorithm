# [정올 577/Python] 함수1 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=214&sca=10b0

def func(x, y):
    if x>y:
        x = x//2
        y = y*2
    else:
        y = y//2
        x = x*2
    return x,y
x, y = map(int, input().split())
x, y = func(x, y)
print(x, y)