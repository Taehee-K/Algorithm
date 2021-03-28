# [정올 601/Python] 문자열1 - 자가진단9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=238&sca=10e0

string = input().strip() # strip()으로 뒤에 공백 제거
for i in range(len(string)): # 문자수만큼 오른쪽으로 한 바퀴 회전하여 출력
    print(string[-(i+1):]+string[:-(i+1)])
    