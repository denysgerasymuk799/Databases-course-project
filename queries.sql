-- 1 Works
SELECT customer_name FROM Customer WHERE customer_id IN 
(SELECT customer_id FROM
(SELECT customer_id, COUNT(customer_id) AS num FROM Ordering WHERE agronomist_id = "A" 
	AND order_date BETWEEN 'F' AND 'T' GROUP BY customer_id) h 
WHERE h.num > "N");

--2 Works
SELECT product_name FROM Product WHERE product_id IN (SELECT DISTINCT product_id FROM Ordering WHERE customer_id = "C" AND order_date BETWEEN 'F' AND 'T');

--3 Works
SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN
(SELECT agronomist_id FROM (SELECT agronomist_id, COUNT(agronomist_id) AS num FROM 
Degustation INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id 
WHERE Degustation_Customer.customer_id = "C" GROUP BY agronomist_id) h WHERE h.num > "N");

--4 Works
SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN 
(SELECT DISTINCT agronomist_id FROM Trip_Agronomist WHERE agronomist_id != "A" AND trip_id IN
(SELECT trip_id FROM business_trip WHERE trip_date BETWEEN "F" AND "T" AND trip_id IN 
(SELECT trip_id FROM Trip_Agronomist WHERE agronomist_id = "A")));
 
--5 Works
SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN 
(SELECT agronomist_id FROM Ordering WHERE customer_id = "C" AND order_date BETWEEN "F" AND "T" )
AND agronomist_id IN
(SELECT agronomist_id FROM Degustation WHERE degustation_id IN 
(SELECT * FROM degustation_customer WHERE customer_id = "C")
 AND degustation_date BETWEEN "F" AND "T");

--6 Works
SELECT customer_name FROM Customer WHERE customer_id IN
(SELECT customer_id FROM 
 (SELECT customer_id, COUNT(DISTINCT product_id) AS num FROM Ordering WHERE order_date BETWEEN "F" AND "T" GROUP BY customer_id) h
 WHERE h.num > "N");
 
--7 Works
 SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN (
 SELECT * FROM (SELECT agronomist_id, COUNT(sort_id) AS num FROM Harvest WHERE harvest_date BETWEEN "F" AND "T" GROUP BY agronomist_id) h
 WHERE h.num > "N");
 
 --8 Works
SELECT DISTINCT Degustation.degustation_id FROM Degustation INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id 
WHERE Degustation_Customer.customer_id = "C" AND Degustation.agronomist_id = "A";

--9 Works
SELECT product_id, COUNT(product_id) FROM Degustation WHERE degustation_id IN (
SELECT * FROM (SELECT Degustation.degustation_id, COUNT(DISTINCT Degustation_Customer.customer_id) AS num FROM Degustation 
INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id  
WHERE degustation_date BETWEEN "F" AND "T" AND agronomist_id = "A" GROUP BY degustation_id) h WHERE h.num > "N") GROUP BY product_id;

--10 Not done


--11 Works
CREATE OR REPLACE VIEW hrvsts AS (SELECT sort_name, f.agronomist_name, harvest_date, 
    CASE 
      WHEN trips IS NULL THEN 0 
    ELSE trips 
    END
    FROM (
    SELECT * FROM (sort s INNER JOIN harvest h ON s.sort_id = h.sort_id) d INNER JOIN agronomist a ON d.agronomist_id = a.agronomist_id 
WHERE harvest_date BETWEEN 'F' AND 'T' ) f 
    LEFT JOIN 
        (SELECT agronomist_name, COUNT(agronomist_name) trips FROM agronomist a 
     INNER JOIN trip_agronomist ta on a.agronomist_id = ta.agronomist_id GROUP BY agronomist_name) g 
     on f.agronomist_name = g.agronomist_name )

SELECT sort_name, CASE
    WHEN sort_name IN 
        (SELECT sort_name FROM hrvsts
         group by (sort_name, agronomist_name)
         having count(agronomist_name) > 'N') THEN SUM(trips)/COUNT(agronomist_name)
  ELSE 0
  END AS av_trips
FROM hrvsts 
GROUP BY sort_name
ORDER BY av_trips DESC

--12 Works
SELECT product_name, CAST(returned AS DECIMAL)/bought * 100 perc FROM
(SELECT d.product_name, bought, CASE 
   WHEN returned IS NULL THEN 0
   ELSE returned
   END AS returned
FROM 
(SELECT product_name, COUNT(product_name) bought FROM ORDERING o INNER JOIN product p ON o.product_id = p.product_id
GROUP BY product_name) d LEFT JOIN
(SELECT product_name, COUNT(product_name) returned FROM (ORDERING o INNER JOIN product p ON o.product_id = p.product_id) f
RIGHT JOIN order_return orr ON f.order_id = orr.order_id WHERE return_date BETWEEN 'F' AND 'T'
GROUP BY product_name) g on d.product_name = g.product_name
WHERE bought > 'N') h
ORDER BY perc DESC