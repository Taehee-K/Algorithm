# [정올 231/Python] 함수3 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=131&sca=10d0

def Number(N):
    if N>0:
        arr.append(N)
        Number(N//2)
    else:
        arr.reverse()
        for i in arr: print(i, end = " ")

arr = []
Number(N = int(input()))