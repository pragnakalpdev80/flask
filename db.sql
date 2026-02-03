DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
	user_id SERIAL PRIMARY KEY,
  	username VARCHAR (80) UNIQUE NOT NULL,
  	email VARCHAR (120) UNIQUE NOT NULL,
  	password_hash VARCHAR (255) NOT NULL,
  	is_active BOOLEAN NOT NULL 
);

CREATE TABLE IF NOT EXISTS users (
	id SERIAL PRIMARY KEY,
  	username VARCHAR (80) UNIQUE NOT NULL,
  	email VARCHAR (120) UNIQUE NOT NULL,
  	password_hash VARCHAR (255) NOT NULL 
);

INSERT INTO users(username,email,password_hash,is_active) VALUES
('hill3','hillsoni3@gmail.com',123,false);

CREATE TABLE IF NOT EXISTS books (
	id SERIAL PRIMARY KEY,
  	title VARCHAR (200) NOT NULL,
  	author VARCHAR (100) NOT NULL,
  	isbn VARCHAR (13) UNIQUE NOT NULL
);

SELECT * FROM books;

