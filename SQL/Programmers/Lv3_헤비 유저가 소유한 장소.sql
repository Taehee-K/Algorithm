-- [프로그래머스 Lv3/SQL] 헤비 유저가 소유한 장소
-- https://programmers.co.kr/learn/courses/30/lessons/77487

-- 공간을 둘 이상 등록한 사람: 헤비 유저
-- 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회
SELECT *
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID FROM PLACES
    GROUP BY HOST_ID HAVING COUNT(ID)>1)
ORDER BY ID