-- script that lists all cities contained in the database hbtn_0d_usa
SELECT cities.id 'id', cities.name 'name', states.name 'name'
FROM cities
WHERE state_id = states.id
ORDER BY id ASC;
