# [코드업 1929/Python] 재귀함수 - 우박수 (3n+1)(reverse)
# https://codeup.kr/problem.php?id=1929

def Hailstone(n):
    order.append(n)
    if n==1: return
    elif n%2==1: n = 3*n +1
    else: n = n//2
    Hailstone(n)

def Reverse(index):
    if index<0: return
    else:
        print(order[index])
        Reverse(index-1)
        
order = []
n = int(input())
Hailstone(n)
Reverse(len(order)-1)