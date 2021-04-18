# [코드업 6084/Python] 종합 - 소리 파일 저장용량 계산하기
# https://codeup.kr/problem.php?id=6084

h, b, c, s = map(float, input().split())

print('%.1f'% (h*b*c*s/(8*1024*1024)),'MB')