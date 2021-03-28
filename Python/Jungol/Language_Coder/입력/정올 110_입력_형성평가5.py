# [정올 110/Python] 입력 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=10&sca=1020

# 실수의 yard(야드)를 입력받아 cm(센티미터)로 환산하여 입력값과 환산한 값을 출력 
# 소수 둘째자리에서 반올림하여 첫째자리까지 출력
# (단 1야드 = 91.44cm로 한다.)  

 
# python은 float만 사용!

yd_cm = 91.44
yard = float(input('yard? '))

print("{:.1f}yard = {:.1f}cm".format(yard, yd_cm*yard))