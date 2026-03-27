-- Write your PostgreSQL query statement below
SELECT p.firstName,p.lastName,c.city,c.state FROM Person p LEFT JOIN Address c on p.personId=c.personId
