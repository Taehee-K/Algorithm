# [정올 583/Python] 함수2 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=220&sca=10c0

from math import ceil, floor # 올림 함수 ceil(), 내림 함수 floor()

def Number(num):
    large = max(num)
    num.remove(large)
    print(ceil(large), end = " ") # 올림

    small = min(num)
    num.remove(small)
    print(floor(small), end = " ") # 내림

    print(round(num[0]), end = " ") # 반올림
    

num = list(map(float, input().split()))
Number(num)