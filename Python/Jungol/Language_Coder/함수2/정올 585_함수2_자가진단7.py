# [정올 585/Python] 함수2 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=222&sca=10c0

def Bubble(num): # 버블정렬
    for repeat in range(9):
        for i in range(10):
            if i<9 and num[i]<num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
            print(num[i], end = " ")
        print()

num = list(map(int, input().split()))
Bubble(num)