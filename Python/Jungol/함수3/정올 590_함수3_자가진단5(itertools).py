# [정올 590/Python] 함수3 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=227&sca=10d0

# itertools.combinations 활용한 풀이 -> Memory Limit Exceeded 에러
from itertools import combinations
def Dice(n):
    dice = range(1,7) # 주사위 숫자 1-6
    # 각 숫자가 주사위를 던진 만큼 중복되게 함
    dice = [num for num in dice for _ in range(n)]
    
    result = sorted(set(list(combinations(dice, 3)))) # 3개 조합
    # set -> get unique combinations (set 은 순서가 없다)
    # sorted -> print in order (sorted() 함수 사용해 순서대로 출력)
    for subset in result: 
        for i in list(subset): print(i, end =" ") 
        print()

n = int(input())
Dice(n)