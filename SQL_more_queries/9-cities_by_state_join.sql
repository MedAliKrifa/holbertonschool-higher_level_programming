-- code to that creates the MySQL table
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = state_id ORDER BY cities.id ASC;