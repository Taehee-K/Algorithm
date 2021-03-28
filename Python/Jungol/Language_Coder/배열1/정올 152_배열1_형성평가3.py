# [정올 152/Python] 배열1 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=52&sca=1090

# 10개의 정수를 입력
num = list(map(int, input().split()))

# 홀수 번째 입력받은 정수의 합과 짝수 번째 입력받은 정수의 합을 출력
even = 0
odd = 0
for i in range(len(num)):
    if (i+1)%2==0:
        even += num[i]
    else: 
        odd += num[i]

print("odd :", odd)
print("even :", even)