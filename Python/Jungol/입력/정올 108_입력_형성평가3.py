# [정올 108/Python] 입력 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=8&sca=1020

# 정수형 변수 한 개를 선언하여 50을 대입 
# 실수형 변수 한 개를 선언하여 100.12를 대입
# 출력 결과: 100.12 * 50 = 5006
# (결과값은 소수점 이하에서 반올림) 

x = 50
y = 100.12
mul = x*y
print(y,'*',x,'=','{:.0f}'.format(mul))