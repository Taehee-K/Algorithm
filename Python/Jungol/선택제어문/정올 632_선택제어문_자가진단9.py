# [정올 632/Python] 선택제어문 - 자가진단9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=660&sca=1050
 
# 3개의 정수를 입력
x, y, z = map(int,input().split())

# 조건연산자를 이용하여 입력받은 수들 중 최소값을 출력
# [condition] ? [true] : [false] --> python에서 삼항연산자 지원하지 않음
# [true] if [condition] else [false] --> python에서의 삼항연산자 형태
min = (x if (x < z) else z) if (x < y) else (y if (y < z) else z) 

print(min)