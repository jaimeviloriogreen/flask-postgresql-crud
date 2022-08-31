CREATE DATABASE crud_flask;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL, 
    password VARCHAR(50) NOT NULL
);