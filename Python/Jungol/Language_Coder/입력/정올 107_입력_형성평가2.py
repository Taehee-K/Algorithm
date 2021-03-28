# [정올 107/Python] 입력 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=7&sca=1020

# 실수형 변수를 2개 선언
# 각각에 80.5 22.34를 대입
# 두 수의 합을 구하여 각각의 숫자를 10칸씩 오른쪽에 맞추어 소수 둘째자리까지 출력

x = 80.5
y = 22.34
sum = x+y
print("{:>10.2f}{:>10.2f}{:>10.2f}".format(x,y,sum))