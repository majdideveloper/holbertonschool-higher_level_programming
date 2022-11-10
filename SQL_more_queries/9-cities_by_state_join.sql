-- script that lists all cities contained in the database hbtn_0d_usa
SELECT C.id 'id', C.name 'name', S.name 'name'
FROM cities C
INNER JOIN states S
WHERE C.state_id = S.id
ORDER BY C.id ASC;
