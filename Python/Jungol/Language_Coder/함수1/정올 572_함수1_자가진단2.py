# [정올 572/Python] 함수1 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=209&sca=10b0

def area(radius):
    area = 3.14*(radius**2)
    print("{:.2f}".format(area)) 

r = int(input())
area(r)