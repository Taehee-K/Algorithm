# [정올 179/Python] 함수2 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=79&sca=10c0

def SumAvg():
    num = list(map(float, input().split()))
    # 합계 -> 평균 -> 반올림
    print(round(sum(num)/len(num)))
    # 반올림 -> 합계 -> 평균 -> 반올림
    print(round(sum([round(num[i]) for i in range(len(num))])/len(num)))
    
SumAvg()