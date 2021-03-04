# [정올 162/Python] 배열2 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=62&sca=10a0

num = list(map(int, input().split())) # 입력 받은 두 수로 배열 초기화

for i in range(10):
    if i>1: 
        num.append((num[i-1]+num[i-2])%10)
    print(num[i], end=" ")


