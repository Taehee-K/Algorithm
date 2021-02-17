# [정올 113/Python] 연산자 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=13&sca=1030

# 직사각형의 가로와 세로의 길이를 정수형 값으로 입력
x,y = map(int, input().split())

# 가로의 길이는 5 증가
x +=5

# 세로의 길이는 2배
y*=2

# 가로의 길이 세로의 길이 넓이를 차례로 출력
print("width =",x)
print("length =",y)
print("area =",x*y)
