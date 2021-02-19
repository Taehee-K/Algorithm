# [정올 532/Python] 선택제어문 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=169&sca=1050
 
# 두 개의 실수를 입력
x, y = map(float, input().split())

# 모두 4.0 이상이면 "A", 모두 3.0 이상이면 "B", 아니면 "C" 출력
if x>=4.0 and y>=4.0: print("A")
elif x>=3.0 and y>=3.0: print("B")
else: print("C")