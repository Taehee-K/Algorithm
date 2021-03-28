# [정올 546/Python] 반복제어문2 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=183&sca=1070

# 10 이하의 과목수 n
n = int(input())
# 정수로 주어진 n개 과목의 점수를 입력
grade = map(int, input().split())

total = 0
for score in grade:
    total += score

# 실수 평균을 구하여 출력
avg = total/n
print("avg : {:.1f}".format(avg)) # 평균은 소수 첫째자리까지

# 평균이 80점이상이면 "pass", 80점 미만이면 "fail"
if avg>=80: print('pass')
else: print('fail')

