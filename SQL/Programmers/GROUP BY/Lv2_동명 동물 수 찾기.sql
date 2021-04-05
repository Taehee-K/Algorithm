-- [프로그래머스 Lv2/SQL] 동명 동물 수 찾기
-- https://programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL  -- NULL 제외
GROUP BY NAME           -- 이름 끼리 GROUP
HAVING COUNT > 1        -- 2번 이상 쓰인 이름
ORDER BY NAME           -- 이름 순으로 정렬