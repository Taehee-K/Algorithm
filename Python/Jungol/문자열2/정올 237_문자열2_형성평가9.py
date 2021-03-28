# [정올 237/Python] 문자열2 - 형성평가9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=137&sca=10f0

import math

integer, real, word = input().split()
real = float(real)
new = integer+"{:.3f}".format(real)+word
print(new[:(math.ceil(len(new)/2))])
print(new[(math.ceil(len(new)/2)):])
