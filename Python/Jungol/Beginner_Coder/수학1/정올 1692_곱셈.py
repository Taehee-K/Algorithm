# [정올 1692/Python] 곱셈
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=965&sca=2030

x = int(input())
y = input()

mul = []    # 각 자리의 숫자와 곱셈한 결과값 저장
for i in range(3):
    print(x*int(y[2-i]))   
    mul.append(x*int(y[2-i])*10**(i))   
print(sum(mul))
