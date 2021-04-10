# [코드업 6018/Python] 입출력 - 시간 입력받아 그대로 출력하기
# https://codeup.kr/problem.php?id=6018

a, b = input().split(":")  # 시:분 형식으로 입력, ":" 기준으로 split
print(a, b,sep=":") # sep = ":" 이용해 ":" 사이에 두고 출력 