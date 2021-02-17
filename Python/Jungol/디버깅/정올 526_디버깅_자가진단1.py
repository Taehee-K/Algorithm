# [정올 526/Python] 디버깅 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=163&sca=1040
 
# 2개의 실수(double)를 입력
x, y = map(float,input().split()) #Python 'float' type만 사용

# 두 수의 곱을 정수로 변환한 결과값과 두 수를 각각 정수로 변환하여 곱을 구한 결과값
print("%d %d" %(x*y, int(x)*int(y)))
