# [정올 596/Python] 문자열1 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=233&sca=10e0

string, num = input().split()
reverse = string[::-1] # string 반대로 돌리기
print(reverse[:int(num)]) # 뒤에서 n개 출력
