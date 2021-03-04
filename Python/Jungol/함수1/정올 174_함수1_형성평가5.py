# [정올 174/Python] 함수1 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=74&sca=10b0

def grade():
    score = []
    for i in range(3):
        new = list(map(int, input().split()))
        score.append(new)
        total = 0
        for sc in new:
            total+=sc
            print(sc, end = " ")
        print(total)

    final = 0
    for i in range(3):
        total = 0
        for j in range(3):
            total+=score[j][i]
        final+=total
        print(total, end = " ")
    print(final)
    
grade()