-- 1
SELECT customer_id FROM 
(SELECT customer_id, COUNT(*) AS num FROM ordering WHERE agronomist_id = "A" 
	AND order_date BETWEEN "F" AND "T" GROUP BY customer_id) 
WHERE num > "N";

--2 
SELECT DISTINCT product_id FROM ordering WHERE customer_id = "C" AND order_date BETWEEN "F" AND "T";

--3
SELECT agronomist_id FROM
(SELECT agronomist_id, COUNT(*) AS num FROM 
Degustation INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id 
WHERE Degustation_Customer.customer_id = "C" GROUP BY agronomist_id) WHERE num > "N";

--4
SELECT agronomist_id FROM Trip_Agronomist 
WHERE agronomist_id != "A" AND trip_id IN
(SELECT * FROM Trip WHERE trip_date BETWEEN "F" AND "T AND trip_id IN 
(SELECT * FROM Trip_Agronomist WHERE agronomist_id = "A"))
 
--5
SELECT agronomist_id FROM agronomist WHERE agronomist_id IN 
(SELECT * FROM ordering WHERE customer_id = "C" AND order_date BETWEEN "F" AND "T" ) 
AND agronomist_id IN
(SELECT * FROM Degustation WHERE degustation_id IN 
(SELECT * FROM Degustation_Customer WHERE customer_id = "C") 
 AND degustation_date BETWEEN "F" AND "T");

--6
SELECT customer_id FROM 
(SELECT * FROM 
 (SELECT customer_id, COUNT(DISTINCT product_id) AS num FROM ordering WHERE order_date BETWEEN "F" AND "T" GROUP BY customer_id)
 WHERE num > "N");