# [정올 582/Python] 함수2 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=219&sca=10c0

from math import sqrt
def getRadius(area):
    radius = sqrt(area/3.14)
    print("{:.2f}".format(radius))

area = int(input())
getRadius(area)