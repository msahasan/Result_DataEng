-- Sales Transaction table that will store sales information
CREATE TABLE sales(
   sales_id serial PRIMARY KEY,
   customer_id VARCHAR (50)  NOT NULL,
   salesperson_id VARCHAR (50) UNIQUE NOT NULL,
   card_model_id integer NOT NULL,
   iscardsold varchar(3) NOT NULL,
   created_on TIMESTAMP NOT NULL,
   FOREIGN KEY (salesperson_id,card_model_id)
);
-- Customer Table it will store customer basic info
CREATE TABLE customer(
   customer_id serial PRIMARY KEY,
   customer_name VARCHAR (50)  NOT NULL,
   customer_phone VARCHAR (50) NOT NULL,
   created_on TIMESTAMP NOT NULL
);
-- Sales Man Table it will store  sales person info
CREATE TABLE salesperson(
	salesperson_id serial PRIMARY KEY,
	salesperson_name VARCHAR(50) NOT NULL
);
-- Manufacturer table 
CREATE TABLE manufacturer(
	manufacturer_id serial PRIMARY KEY,
	manufacturer_name VARCHAR(50) NOT NULL
);
-- Car table - contains cars info
CREATE TABLE car(
	car_model_id serial PRIMARY KEY,
	car_manufacturer_id integer NOT NULL,
	car_model_name VARCHAR(50) NOT NULL,
	car_model_varient VARCHAR(50) NOT NULL,
	car_model_number VARCHAR(50) NOT NULL,
	weight NUMERIC (5, 2) NOT NULL,
	engine_capacity NUMERIC(5,3) NOT NULL,
	price NUMERIC(5,3) NOT NULL,
   FOREIGN KEY (car_manufacturer_id)
);