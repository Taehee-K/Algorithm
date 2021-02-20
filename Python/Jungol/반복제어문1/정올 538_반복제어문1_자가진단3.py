# [정올 538/Python] 반복제어문1 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=175&sca=1060
 
# 한 개의 정수를 입력
# 양수(positive integer)인지 음수(negative number)인지 출력
while(True):
    num = int(input("number? "))
    if num==0:  # 0이 입력되면 종료
        break
    elif num>0: print("positive integer")
    else: print("negative number")



