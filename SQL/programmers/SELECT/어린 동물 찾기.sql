-- [프로그래머스 코딩테스트/SQL] 어린 동물 찾기
-- https://programmers.co.kr/learn/courses/30/lessons/59037

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'