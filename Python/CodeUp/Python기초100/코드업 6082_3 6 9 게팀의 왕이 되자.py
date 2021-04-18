# [코드업 6082/Python] 종합 - 3 6 9 게임의 왕이 되자
# https://codeup.kr/problem.php?id=6082

n = int(input())
for i in range(1, n+1):
    ten = i//10
    one = i%10
    if ten in [3, 6, 9] and one in [3, 6, 9]: print('XX', end = " ")
    elif ten in [3, 6, 9] or one in [3, 6, 9]: print('X', end = " ")
    else: print(i, end = " ")