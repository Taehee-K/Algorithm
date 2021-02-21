# [정올 545/Python] 반복제어문2 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=182&sca=1070

# 10개의 정수를 입력
num = list(map(int, input().split()))

# 3의 배수의 개수와 5의 배수의 개수를 각각 출력
three = 0; five = 0;
for i in range(len(num)):
    if num[i]%3==0:
        three+=1
    if num[i]%5==0:
        five+=1

print("Multiples of 3 :", three)
print("Multiples of 5 :", five)