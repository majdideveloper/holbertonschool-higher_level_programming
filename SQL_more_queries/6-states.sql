-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATEE TABLE IF NOT EXISTS states (id INT PRIMARY KEY UNIQUE, name VARCHAR(256) NOT NULL);
