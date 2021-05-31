-- [HackerRank Easy/SQL] Average Population
-- https://www.hackerrank.com/challenges/average-population/problem

 SELECT ROUND(SUM(POPULATION)/COUNT(POPULATION))
 FROM CITY