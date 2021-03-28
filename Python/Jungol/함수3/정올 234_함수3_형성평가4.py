# [정올 234/Python] 함수3 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=134&sca=10d0

arr = [1, 2]
def Arr(num):
    if num==0:
        print(arr[-1])
    else: 
        arr.append((arr[-1]*arr[-2])%100)
        Arr(num-1)

n = int(input())
Arr(n-2)