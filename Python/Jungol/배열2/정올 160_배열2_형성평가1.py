# [정올 160/Python] 배열2 - 형성평가1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=60&sca=10a0

num = list(map(int, input().split()))
dice = [1, 2, 3, 4, 5, 6]
count = [0]*6

for i in range(len(num)):
    index = dice.index(num[i])
    count[index]+=1

for i in range(6):
    print("%d : %d"%(dice[i], count[i]))