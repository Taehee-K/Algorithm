# [정올 563/Python] 배열1 - 자가진단9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=200&sca=1090

# 10개의 정수를 입력받아 배열에 저장
num = list(map(int, input().split()))

# 내림차순으로 정렬하여 출력
# sort() 함수의 reverse parameter 사용
num.sort(reverse = True)
for n in num:
    print(n, end=" ") 