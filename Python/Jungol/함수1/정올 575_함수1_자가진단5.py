# [정올 575/Python] 함수1 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=212&sca=10b0

def Exp(x, y):
    return x**y

x, y = map(int, input().split())
print(Exp(x, y))