# [정올 124/Python] 선택제어문 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=24&sca=1050
 
# 1~12사이의 정수를 입력
month = int(input())

# 평년의 경우 입력받은 월을 입력받아 해당 월의 날수를 출력
if month==2: print("28")
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print("31")
else: print("30")