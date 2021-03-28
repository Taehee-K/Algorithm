# [정올 181/Python] 함수2 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=81&sca=10c0

pi = 3.141592

def Area(radius):
    area = radius**2 * pi
    print("area = {:.3f}".format(area))

r = float(input("radius : "))
Area(r)