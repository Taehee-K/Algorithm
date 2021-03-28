# [정올 129/Python] 반복제어문1 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=29&sca=1060

# 삼각형의 밑변의 길이와 높이를 입력받아 넓이를 출력
# "Continue? "에서 'Y' 나 'y'를 입력 받을 시 작업을 반복
# 다른 문자이면 종료

while(True):
    base = int(input("Base = "))
    height = int(input("Height = "))
    width = base*height*(1/2)
    print("Triangle width = {:.1f}".format(width))
    cont = input("Continue? ")
    if cont[0]=='y' or cont[0]=='Y':   #character 1개만 가지고 판별
        continue
    else:
        break