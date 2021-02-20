# [정올 540/Python] 반복제어문1 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=177&sca=1060
 

while(True):
    num = int(input())  # 정수 입력
    if num==-1: # -1이 입력되면 종료
        break
    elif num%3==0:  # 3의 배수인 경우
        print(num//3)  # 3으로 나눈몫을 출력
    else:   # 3의 배수가 아닌 경우
        continue   # 아무 작업도 하지X
