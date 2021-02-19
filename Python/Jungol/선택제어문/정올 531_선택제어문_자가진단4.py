# [정올 531/Python] 선택제어문 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=168&sca=1050
 
# 복싱체급
# 50.80kg 이하를 Flyweight, 
# 61.23kg 이하를 Lightweight, 
# 72.57kg 이하를 Middleweight, 
# 88.45kg 이하를 Cruiserweight, 
# 88.45kg 초과를 Heavyweight

# 몸무게를 입력받아 체급을 출력
w = float(input())

if w<=50.8: print("Flyweight")
elif w<=61.23: print("Lightweight")
elif w<=72.57: print("Middleweight")
elif w<=88.45: print("Cruiserweight")
else: print("Heavyweight")