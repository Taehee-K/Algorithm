# [정올 574/Python] 함수1 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=211&sca=10b0

def GetMax(num):
    return max(num)

num = list(map(int, input().split()))
print(GetMax(num))