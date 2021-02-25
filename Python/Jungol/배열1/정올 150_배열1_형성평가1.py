# [정올 150/Python] 배열1 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=50&sca=1090

# 10개의 문자를 입력
char = input().split()

# 마지막으로 입력받은 문자부터 첫 번째 입력받은 문자까지 차례로 출력
for i in range(len(char)):
    print(char[len(char)-i-1], end = " ")
