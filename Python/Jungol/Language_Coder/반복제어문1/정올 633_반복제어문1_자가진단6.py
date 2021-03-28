# [정올 633/Python] 반복제어문1 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2077&sca=1060

# 나라 이름을 출력하고 숫자를 입력받아 해당하는 나라의 수도를 출력
# 해당 번호 이외 숫자 입력시 "none" 출력 후 프로그램 종료

while(True):
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    num = int(input("number? "))
    print()

    if num==1: 
        print("Seoul\n")
    elif num==2:
        print("Washington\n")
    elif num==3:
        print("Tokyo\n")
    elif num==4:
        print("Beijing\n")
    else: 
        print("none\n")
        break

    