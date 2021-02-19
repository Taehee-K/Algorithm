# [정올 530/Python] 선택제어문 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=167&sca=1050
 
# 나이를 입력
age = int(input())

# 20살 이상이면 "adult"라고 출력
if age>=20: print("adult")
# 그렇지 않으면 몇 년후에 성인이 되는지 "○ years later"출력
else: print("%d years later"%(20-age))