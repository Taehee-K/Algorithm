-- [프로그래머스 Lv1/SQL] 이름이 없는 동물의 아이디
-- https://programmers.co.kr/learn/courses/30/lessons/59039

SELECT ANIMAL_ID 
FROM ANIMAL_INS
WHERE NAME IS NULL