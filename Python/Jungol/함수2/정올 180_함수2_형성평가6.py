# [정올 180/Python] 함수2 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=80&sca=10c0

data = 7

def Bubble():
    num = list(map(int, input().split()))
    for repeat in range(3): # 3번 반복
        for i in range(data-1):
            if num[i]>num[i+1]: #앞의 숫자가 더 클 시
                num[i], num[i+1] = num[i+1], num[i] #뒤의 숫자와 자리 교환
    
    for i in range(7): print(num[i], end = " ")

Bubble()