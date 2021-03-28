# [정올 580/Python] 함수2 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=217&sca=10c0

def date(month, day):
    if month<1 or month>12 or day<1:
        print("BAD!")
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        if day<=31: print("OK!")
        else: print("BAD!")
    elif month in [4, 6, 9, 11]:
        if day<31: print("OK!")
        else: print("BAD!")
    else:
        if day<30: print("OK!")
        else: print("BAD!")
            

month, day = map(int, input().split())
date(month, day)