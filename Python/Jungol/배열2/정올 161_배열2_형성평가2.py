# [정올 161/Python] 배열2 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=61&sca=10a0

score = list(map(int, input().split()))
tens = []

for i in range(len(score)):
    if score[i]==0:
        tens.sort(reverse=True) # 10점 단위별로 내림차순 정렬
        count = [0]*len(tens)
        for j in range(len(score[:i])):
            index = tens.index(score[j]//10)    # 해당 점수대의 인덱스
            count[index]+=1 # 해당 점수대의 학생 추가
    else:
        if score[i]//10 not in tens:    # 해당 점수대의 학생이 없다면
            tens.append(score[i]//10)   # 추가

for i in range(len(tens)):
    print("%d : %d person"%(tens[i]*10, count[i]))