-- [프로그래머스 Lv2/SQL] 중복 제거하기
-- https://programmers.co.kr/learn/courses/30/lessons/59408

SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
-- COUNT() << 괄호 안에 DISTINCT 가 들어가야 한다