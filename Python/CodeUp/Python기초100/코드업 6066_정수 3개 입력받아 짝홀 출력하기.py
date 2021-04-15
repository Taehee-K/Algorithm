# [코드업 6066/Python] 선택실행구조 - 정수 3개 입력받아 짝홀 출력하기
# https://codeup.kr/problem.php?id=6066

a, b, c = map(int, input().split())
print("even") if a%2==0 else print("odd")
print("even") if b%2==0 else print("odd")
print("even") if c%2==0 else print("odd")
