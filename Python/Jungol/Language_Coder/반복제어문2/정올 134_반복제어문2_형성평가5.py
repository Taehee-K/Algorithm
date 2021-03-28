# [정올 134/Python] 반복제어문2 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=34&sca=1070

# 10개의 정수를 입력
num = list(map(int, input().split()))

# 짝수의 개수와 홀수의 개수를 각각 구하여 출력
even = 0
odd = 0
for i in range(len(num)):
    if num[i]%2==0:
        even+=1
    else: 
        odd+=1

print("even : %d"%(even))
print("odd : %d"%(odd))