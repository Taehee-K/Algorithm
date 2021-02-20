# [정올 120/Python] 선택제어문 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=20&sca=1050
 
# 두 개의 정수를 입력
x, y = map(int, input().split())

# 큰 수에서 작은 수를 뺀 차를 출력
if x>y: print(x-y)
else: print(y-x)