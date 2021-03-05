# [정올 175/Python] 함수2 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=75&sca=10c0

def reverse():
    n = int(input())
    num = list(map(int, input().split()))
    num.sort(reverse = True)

    for i in range(n):
        print(num[i], end = " ")
    

reverse()