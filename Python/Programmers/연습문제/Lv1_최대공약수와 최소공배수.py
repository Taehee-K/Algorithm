# [프로그래머스 Lv1/Python] 최대공약수와 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940

import math
def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = (n*m)/gcd
    return [gcd, lcm]