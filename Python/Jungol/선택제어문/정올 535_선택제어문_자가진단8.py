# [정올 535/Python] 선택제어문 - 자가진단8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=172&sca=1050
 
# 4.0 이상 : "scholarship"
# 3.0 이상 : "next semester"
# 2.0 이상 : "seasonal semester"
# 2.0 미만 : "retake"​

gpa = float(input())
if gpa>=4.0: print("scholarship")
elif gpa>=3.0: print("next semester")
elif gpa>=2.0: print("seasonal semester")
else: print("retake")