# [정올 177/Python] 함수2 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=77&sca=10c0

def AbsSum():
    num = list(map(int, input().split()))

    # 절대값의 합
    total= sum([abs(num[i]) for i in range(len(num))]) 
    print(total)
    

AbsSum()