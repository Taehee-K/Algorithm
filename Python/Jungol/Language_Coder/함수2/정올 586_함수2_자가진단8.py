# [정올 586/Python] 함수2 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=223&sca=10c0

def add(x, y):
    return x+y
def sub(x, y):
    return x-y

x,y = map(int, input().split())
print("(%d - %d) ^ 2 = %d"%(x, y, sub(x, y)**2))
print("(%d + %d) ^ 3 = %d"%(x, y, add(x, y)**3))