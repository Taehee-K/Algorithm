# [정올 122/Python] 선택제어문 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=22&sca=1050
 
# 년도를 입력받아 윤년(leap year)인지 평년(common year)인지 판단

# 400으로 나누어떨어지면 윤년
# 4로 나누어떨어지고 100으로 나누어떨어지지 않으면 윤년
# 나머지는 모두 평년

year = int(input())

if year%400==0 or (year%4==0 and year%100!=0): print("leap year")
else: print("common year")