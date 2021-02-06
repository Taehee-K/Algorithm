# [정올 519/Python] 연산자 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=156&sca=1030

# 정수 2개를 입력
# 첫 번째 수에는 100을 증가시켜 저장
# 두 번째 수는 10으로 나눈 나머지를 저장
# 두 수를 차례로 출력

x,y = input().split()
x= int(x)+100
y = int(y)%10

print(x,y)