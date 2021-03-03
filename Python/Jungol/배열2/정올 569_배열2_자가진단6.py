# [정올 569/Python] 배열2 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=206&sca=10a0

def evaluate(score):
    total = 0
    for i in range(4):
        total+=score[i]
    return total/4

succ = 0
for i in range(5):
    score = list(map(int, input().split()))
    if evaluate(score)>=80:
        print("pass")
        succ+=1
    else: print("fail")
print("Successful : %d"%(succ))