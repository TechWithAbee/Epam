-- PostgreSQL 16.0 documentation
-- https://www.postgresql.org/docs/16/index.html

-- Window functions
-- https://www.postgresqltutorial.com/postgresql-window-function/

-- Helpful while solving practical tasks
-- https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/


-- Setting up sample tables

-- First, create two tables named products and product_groups for the demonstration:
CREATE TABLE product_groups (
	group_id serial PRIMARY KEY,
	group_name VARCHAR (255) NOT NULL
);

CREATE TABLE products (
	product_id serial PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	price DECIMAL (11, 2),
	group_id INT NOT NULL,
	FOREIGN KEY (group_id) REFERENCES product_groups (group_id)
);


-- Second, insert some rows into these tables:

INSERT INTO product_groups (group_name)
VALUES
	('Smartphone'),
	('Laptop'),
	('Tablet');

INSERT INTO products (product_name, group_id,price)
VALUES
	('Microsoft Lumia', 1, 200),
	('HTC One', 1, 400),
	('Nexus', 1, 500),
	('iPhone', 1, 900),
	('HP Elite', 2, 1200),
	('Lenovo Thinkpad', 2, 700),
	('Sony VAIO', 2, 700),
	('Dell Vostro', 2, 800),
	('iPad', 3, 700),
	('Kindle Fire', 3, 150),
	('Samsung Galaxy Tab', 3, 200);


-- Introduction to PostgreSQL window functions
-- The following example uses the AVG() aggregate function to calculate 
-- the average price of all products in the products table.

SELECT
	AVG (price)
FROM
	products;


-- To apply the aggregate function to subsets of rows, you use the GROUP BY clause. 
-- The following example returns the average price for every product group.

select group_name, avg(price)
from products
inner join product_groups using (group_id)
group by group_name


-- along with the average prices of each product group.

select product_name, price, group_name, 
	avg(price) over (partition by group_name order by group_name desc) as average_price
from products
inner join product_groups using (group_id)
the PARTITION BY distributes the rows of the result set into groups 
-- and the AVG() function is applied to each group to return the average price for each.

-- The ROW_NUMBER(), RANK(), and DENSE_RANK() functions
SELECT
	product_name,
	group_name,
	price,
	ROW_NUMBER () OVER (
		PARTITION BY group_name
		ORDER BY
			price
	)
FROM
	products
INNER JOIN product_groups USING (group_id);
-- The ROW_NUMBER() function assigns a sequential number to each row in each partition.


select product_name, price, group_name,
rank() over (partition by group_name order by price) as product_ranking
from products
inner join product_groups using (group_id)
The RANK() function assigns ranking within an ordered partition. 
-- If rows have the same values, the  RANK() function assigns the same rank, with the next ranking(s) skipped.


SELECT
	product_name,
	group_name,
	price,
	DENSE_RANK () OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) as product_dense_ranking
FROM
	products
INNER JOIN product_groups USING (group_id);
-- Similar to the RANK() function, the DENSE_RANK() function assigns a rank to each row 
-- within an ordered partition, but the ranks have no gap. 
-- In other words, the same ranks are assigned to multiple rows and no ranks are skipped.


-- The FIRST_VALUE and LAST_VALUE functions
-- The FIRST_VALUE() function returns a value evaluated against the first row within its partition, 
-- whereas the LAST_VALUE() function returns a value evaluated against the last row in its partition.

-- return the lowest price for every product group.
SELECT
	product_name,
	group_name,
	price,
	FIRST_VALUE (price) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS lowest_price_per_group
FROM
	products
INNER JOIN product_groups USING (group_id);

-- return the highest price for every product group.
SELECT
	product_name,
	group_name,
	price,
	LAST_VALUE (price) OVER (
		PARTITION BY group_name
		ORDER BY
			price RANGE BETWEEN UNBOUNDED PRECEDING
		AND UNBOUNDED FOLLOWING
	) AS highest_price_per_group
FROM
	products
INNER JOIN product_groups USING (group_id);


-- The LAG and LEAD functions
-- The LAG() function has the ability to access data from the previous row, 
-- while the LEAD() function can access data from the next row.

-- return the prices from the previous row and calculates the difference 
-- between the price of the current row and the previous row.
SELECT
	product_name,
	group_name,
	price,
	LAG (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS prev_price,
	price - LAG (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS cur_prev_diff
FROM
	products
INNER JOIN product_groups USING (group_id);

-- return the prices from the next row and calculates the difference 
-- between the price of the current row and the next row.
SELECT
	product_name,
	group_name,
	price,
	LEAD (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS next_price,
	price - LEAD (price, 1) OVER (
		PARTITION BY group_name
		ORDER BY
			price
	) AS cur_next_diff
FROM
	products
INNER JOIN product_groups USING (group_id);
