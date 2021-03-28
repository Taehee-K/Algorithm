# [정올 579/Python] 함수2 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=216&sca=10c0

def desc(num):
    num.sort(reverse = True)
    for n in num:
        print(n, end = " ")

n = int(input())
num = list(map(int, input().split()))
desc(num)