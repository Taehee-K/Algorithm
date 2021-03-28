# [정올 131/Python] 반복제어문2 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=31&sca=1070

# 100 이하의 두 개의 정수를 입력
x, y = map(int, input().split())

# 작은 수부터 큰 수까지 차례대로 출력
if x<y: start=x; fin=y;
else: start=y; fin=x;

for i in range(start, fin+1):
    print(i)