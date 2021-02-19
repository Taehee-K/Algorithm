# [정올 116/Python] 디버깅 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=16&sca=1040
 
# 정수로 된 3과목의 점수를 입력
x, y, z = map(int, input().split())

# 평균을 구하기
avg = (x+y+z)/3

# 반올림하여 소수 첫째자리까지 출력
print(round(avg,1))