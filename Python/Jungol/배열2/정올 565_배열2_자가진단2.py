# [정올 565/Python] 배열2 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=202&sca=10a0

num = list(map(int, list(input().split())))

tens = [] # 10의 자리 숫자 저장할 배열
for i in range(len(num)):
    if num[i]==0:
        count = [0]*len(tens) # 각 10의 자리 숫자가 몇 개인지 저장할 배열
        n = num[:i] # 0이전까지의 숫자
        tens.sort()
        for j in range(len(n)):
            ten = num[j]//10
            index = tens.index(ten)
            count[index] +=1
    else: 
        tens.append(num[i]//10)

for i in range(len(tens)):
    if count[i]==0: 
        continue
    else: 
        print("%d : %d" %(tens[i], count[i]))