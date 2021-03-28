# [정올 517/Python] 입력 - 자가진단9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=154&sca=1020

# 세 개의 실수를 입력 받아 반올림하여 소수 셋째 자리까지 출력

x = float(input())
y = float(input())
z = float(input())

print("{:.3f}".format(round(x,3)))
print("{:.3f}".format(round(y,3)))
print("{:.3f}".format(round(z,3)))
