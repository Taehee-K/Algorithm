# [정올 111/Python] 연산자 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=11&sca=1030

#국어, 영어, 수학, 컴퓨터 과목 점수 입력받아 정수로 map
kor, eng, math, comp = map(int, input().split()) 

#총점 구하기
tot = kor+eng+math+comp

#평균 구하기
avg = tot//4 #평균의 소수점 이하 버림

print("sum", tot)
print("avg", avg)