-- [프로그래머스 Lv1/SQL] 여러 기준으로 정렬하기
-- https://programmers.co.kr/learn/courses/30/lessons/59404

SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC    -- 이름 순으로 조회, 보호 나중에 시작한 동물 순