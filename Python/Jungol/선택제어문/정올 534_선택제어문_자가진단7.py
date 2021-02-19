# [정올 534/Python] 선택제어문 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=171&sca=1050
 
# 'A'이면 “Excellent”, 
# 'B'이면 “Good”, 
# 'C'이면 “Usually”, 
# 'D'이면 “Effort”, 
# 'F'이면 “Failure”, 
# 그 외 문자이면 “error” 출력

# 영문 대문자 입력
letter = input().strip() #strip() 함수 통해 문자열 앞뒤 공백제거
if letter=='A':
    print("Excellent")
elif letter=='B':
    print("Good")
elif letter=='C':
    print("Usually")
elif letter=='D':
    print("Effort")
elif letter=="F":
    print("Failure")
else:
    print("error")