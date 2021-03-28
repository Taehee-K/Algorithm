# [정올 516/Python] 입력 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=153&sca=1020

# 실수 2개와 한 개의 문자를 입력 받아 출력 
# 실수는 반올림하여 소수 둘째자리까지 출력하는 프로그램 작성

x = float(input())
y = float(input())
char = input()

print("{:.2f}".format(x))
print("{:.2f}".format(y))
print(char)
