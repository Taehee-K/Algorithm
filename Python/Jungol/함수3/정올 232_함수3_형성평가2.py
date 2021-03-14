# [정올 232/Python] 함수3 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=132&sca=10d0

def Recursive(n):
    if n>0:
        arr.append(n)
        Recursive(n-2)
    else: 
        arr.reverse()
        for i in arr: print(i, end = " ")
arr = []
n = int(input())
Recursive(n)