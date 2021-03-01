# [정올 564/Python] 배열2 - 자가진단1
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=201&sca=10a0

num = list(input().split())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(num)):
    if num[i] not in alphabet:
        # ! 이전의 값들 저장한 배열
        letters = num[:i]
        # ! 이전의 값 중 unique한 것 저장한 배열
        unique = sorted(list(set(letters))) # sorted() 함수로 정렬
        # unique letter의 개수 저장할 list 0으로 초기화
        count = [0]*len(unique) 

        for j in range(len(letters)):
            if letters[j] in unique:
                index = unique.index(letters[j])   # get index number
                count[index]+=1 # 해당 letter 자리의 count 증가

for i in range(len(unique)):
    print(unique[i],":",count[i])