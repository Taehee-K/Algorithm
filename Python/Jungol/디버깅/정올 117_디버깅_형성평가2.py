# [정올 117/Python] 디버깅 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=17&sca=1040
 
# 실수로 된 3과목의 점수를 입력
x, y, z = map(float, input().split())

# 총점은 정수부분의 합계를 출력
total = int(x)+int(y)+int(z)

# 평균은 실수의 평균을 구한 뒤 정수부분만 출력
avg = int((x+y+z)//3)
 
print("sum", total)
print("avg", avg)