# [정올 158/Python] 배열1 - 형성평가9
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=58&sca=1090

num = list(map(int, input().split()))

count = 0
total = 0
for i in range(len(num)):
    if num[i]!=0 :
        count +=1
        total+=num[i]
    elif num[i]==0:
        print(i)
        for j in range(i):
            if num[j]%2==1:
                print(num[j]*2, end=" ")
            else: print(num[j]//2, end=" ")
        break