# [정올 119/Python] 디버깅 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=19&sca=1040
 
from datetime import datetime

now = datetime.now()
a = 0
print(a, end = ' ')

a = now.year - 1900 # p
print(a, end = ' ')

a += now.month - 1  # q

a += now.day
print(a, end = '')  

# print(p,q,r)     #r