-- 1 Для агронома A знайти усiх споживачiв, яким вiн продавав продукт хоча б N разiв
-- за вказаний перiод (з дати F по дату T)
SELECT customer_name FROM Customer WHERE customer_id IN 
(SELECT customer_id FROM
(SELECT customer_id, COUNT(customer_id) AS num FROM Ordering WHERE agronomist_id = 1
	AND order_date BETWEEN '2010-01-01' AND '2021-01-01' GROUP BY customer_id) h 
WHERE h.num > 0);

--2 Для споживача С знайти усi продукти, якi вiн придбав за вказаний перiод (з дати F по дату T)
SELECT product_name FROM Product WHERE product_id IN
	(SELECT DISTINCT product_id FROM Ordering
	 WHERE customer_id = 18 AND order_date BETWEEN '2000-01-01' AND '2021-01-01');

-- example of no such order
SELECT product_name FROM Product WHERE product_id IN
	(SELECT DISTINCT product_id FROM Ordering
	 WHERE customer_id = 10 AND order_date BETWEEN '2000-01-01' AND '2021-01-01');

--3 Для споживача С знайти усiх агрономiв, якi проводили для нього дегустацiю хоча б N разiв
-- за вказаний перiод (з дати F по дату T)
SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN
	(SELECT agronomist_id FROM (SELECT agronomist_id, COUNT(agronomist_id) AS num FROM 
	Degustation INNER JOIN Degustation_Customer ON 
	Degustation.degustation_id = Degustation_Customer.degustation_id 
	WHERE Degustation_Customer.customer_id = 5 AND degustation_date BETWEEN '2000-01-01' AND '2021-01-01' GROUP BY agronomist_id) h
 WHERE h.num > 0);

--4 Для агронома А знайти усiх агрономiв, з якими вiн їздив у вiдрядження протягом
-- вказаного перiоду (з дати F по дату T)
SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN 
(SELECT DISTINCT agronomist_id FROM Trip_Agronomist WHERE agronomist_id != 2 AND trip_id IN
(SELECT trip_id FROM business_trip WHERE trip_date BETWEEN '2000-01-01' AND '2021-01-01' AND trip_id IN 
(SELECT trip_id FROM Trip_Agronomist WHERE agronomist_id = 2)));
 
--5 Для споживача С знайти усiх агрономiв, якi продали йому хоча б щось та провели для нього
-- хоча б одну дегустацiю протягом вказаного перiоду (з дати F по дату T)
SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN 
	(SELECT agronomist_id FROM Ordering
	 WHERE customer_id = 1 AND order_date BETWEEN '2000-01-01' AND '2021-01-01')
AND agronomist_id IN
	(SELECT agronomist_id FROM Degustation WHERE degustation_id IN 
	(SELECT degustation_id FROM degustation_customer WHERE customer_id = 1)
 	AND degustation_date BETWEEN '2000-01-01' AND '2021-01-01');

--6 Знайти усiх споживачiв, якi купили щонайменше N рiзних продуктiв за вказаний перiод
-- (з дати F по дату T)
SELECT customer_name FROM Customer WHERE customer_id IN
(SELECT customer_id FROM 
 (SELECT customer_id, COUNT(DISTINCT product_id) AS num FROM Ordering
  WHERE order_date BETWEEN '2010-01-01' AND '2021-01-01' GROUP BY customer_id) h
 WHERE h.num > 1);
 
--7 Знайти усiх агрономiв, якi збирали урожай хоча б N рiзних сортiв коноплi
-- за вказаний перiод (з дати F по дату T)
 SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN (
 SELECT agronomist_id FROM (SELECT agronomist_id, COUNT(sort_id) AS num FROM Harvest
				WHERE harvest_date BETWEEN '2010-01-01' AND '2021-01-01' GROUP BY agronomist_id) h
 WHERE h.num > 0);
 
 --8 Знайти усi спiльнi дегустацiї для споживача С та агронома А
 -- за вказаний перiод (з дати F по дату T)
SELECT DISTINCT Degustation.degustation_id FROM Degustation
INNER JOIN Degustation_Customer
ON Degustation.degustation_id = Degustation_Customer.degustation_id 
WHERE Degustation_Customer.customer_id = 5 AND Degustation.agronomist_id = 1
AND Degustation.degustation_date BETWEEN '2009-01-01' AND '2021-01-01';

--9 Для агронома A та кожного продукту, дегустацiю якого вiн проводив, знайти скiльки разiв
-- за вказаний перiод (з дати F по дату T) вiн проводив дегустацiю для щонайменше N споживачiв
SELECT product_id, COUNT(product_id) FROM Degustation WHERE degustation_id IN (
SELECT degustation_id FROM (SELECT Degustation.degustation_id, COUNT(DISTINCT Degustation_Customer.customer_id) AS num FROM Degustation 
INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id  
WHERE degustation_date BETWEEN '2000-01-01' AND '2021-01-01'
AND agronomist_id = 1 GROUP BY Degustation.degustation_id) h WHERE h.num > 0) GROUP BY product_id;

--10 Для споживача С знайти сумарну кiлькiсть вiдгукiв по мiсяцях, якi вiн залишив за вказаний перiод
-- (з дати F по дату T)


--11 Вивести сорти коноплi у порядку спадання середньої кiлькостi вiдряджень, у якi їздили агрономи,
-- що збирали його урожай хоча б N разiв за вказаний перiод (з дати F по дату T)
CREATE OR REPLACE VIEW hrvsts AS (SELECT sort_name, f.agronomist_name, harvest_date, 
    CASE 
      WHEN trips IS NULL THEN 0 
    ELSE trips 
    END
    FROM (
    SELECT * FROM (sort s INNER JOIN harvest h ON s.sort_id = h.sort_id) d INNER JOIN agronomist a ON d.agronomist_id = a.agronomist_id 
WHERE harvest_date BETWEEN '2000-01-01' AND '2020-01-01' ) f 
    LEFT JOIN 
        (SELECT agronomist_name, COUNT(agronomist_name) trips FROM agronomist a 
     INNER JOIN trip_agronomist ta on a.agronomist_id = ta.agronomist_id GROUP BY agronomist_name) g 
     on f.agronomist_name = g.agronomist_name );

SELECT sort_name, CASE
    WHEN sort_name IN 
        (SELECT sort_name FROM hrvsts
         group by (sort_name, agronomist_name)
         having count(agronomist_name) >= 1) THEN ROUND(SUM(trips)/COUNT(agronomist_name), 1)
  ELSE 0
  END AS av_trips
FROM hrvsts 
GROUP BY sort_name
ORDER BY av_trips DESC

--12 Вивести продукти, якi були придбанi щонайменше N рiзними споживачами у порядку
-- спадання вiдсотку повернень за вказаний перiод (з дати F по дату T)
SELECT product_name, ROUND(CAST(returned AS DECIMAL)/bought * 100, 2) perc FROM
(SELECT d.product_name, bought, CASE 
   WHEN returned IS NULL THEN 0
   ELSE returned
   END AS returned
FROM 
(SELECT product_name, COUNT(product_name) bought FROM ORDERING o INNER JOIN product p ON o.product_id = p.product_id
GROUP BY product_name) d LEFT JOIN
(SELECT product_name, COUNT(product_name) returned FROM (ORDERING o INNER JOIN product p ON o.product_id = p.product_id) f
RIGHT JOIN order_return orr ON f.order_id = orr.order_id WHERE return_date BETWEEN '01/01/2000' AND '01/01/2020'
GROUP BY product_name) g on d.product_name = g.product_name
WHERE bought >= 2) h
ORDER BY perc DESC