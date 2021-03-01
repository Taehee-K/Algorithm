# [정올 157/Python] 배열1 - 형성평가8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=57&sca=1090

num = list(map(int, input().split()))

five = 0
total = 0
for i in range(len(num)):
    if num[i]!=0 and num[i]%5==0:
        five +=1
        total+=num[i]
    elif num[i]==0:
        n = num[:i]
        print('Multiples of 5 :', five)
        print('sum :', total)
        print('avg :', round(total/five, 1))
        break