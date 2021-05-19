-- [HackerRank Easy/SQL] Weather Observation Station 4
-- https://www.hackerrank.com/challenges/weather-observation-station-4/problem

SELECT COUNT(CITY)-COUNT(DISTINCT CITY) AS NUMBER
FROM STATION