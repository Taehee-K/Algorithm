# [정올 115/Python] 연산자 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=15&sca=1030

# 민수와 기영이의 키와 몸무게를 입력
min_h, min_w = map(int, input().split())
ki_h, ki_w = map(int, input().split())

# 민수가 키도 크고 몸무게도 크면 1 
if (min_h>ki_h and min_w>ki_w):
    print(1)
# 그렇지 않으면 0을 출력
else: 
    print(0)
