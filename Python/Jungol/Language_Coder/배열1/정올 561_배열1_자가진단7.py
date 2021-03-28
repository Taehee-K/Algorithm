# [정올 561/Python] 배열1 - 자가진단7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=198&sca=1090


num = list(map(int, input().split()))

under = [] # 100 미만의 수를 저장할 배열
over = [] # 100 이상의 수를 저장할 배열

for i in range(len(num)):
    if num[i] <100: # 100 미만의 수
        under.append(num[i]) # 100 미만의 수 따로 저장
    else: 
        over.append(num[i]) # 100 이상의 수 저장

# 100 미만의 수 중 최대값, 100 이상의 수 중 최소값 출력
if len(under)==0 :
    under.append(100)
if len(over)==0 :
    over.append(100)

print(max(under), min(over)) 