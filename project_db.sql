-- TABLE CREATION
CREATE TABLE customer(
	customer_id SERIAL,
	customer_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(customer_id)
);

CREATE TABLE agronomist(
	agronomist_id SERIAL,
	agronomist_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(agronomist_id)
);

CREATE TABLE sort(
	sort_id SERIAL,
	sort_name VARCHAR(100) NOT NULL,
	PRIMARY KEY(sort_id)
);

CREATE TABLE product(
	product_id SERIAL,
	product_name VARCHAR(100),
	price DECIMAL(12, 2) NOT NULL,
	PRIMARY KEY(product_id)
);

CREATE TABLE business_trip(
	trip_id SERIAL,
	trip_date DATE NOT NULL,
	PRIMARY KEY(trip_id)
);

CREATE TABLE ordering (
	order_id SERIAL,
	weight DECIMAL(10, 4) NOT NULL,
	total_price DECIMAL(12, 2) NOT NULL,
	order_date DATE NOT NULL,
	agronomist_id INT NOT NULL,
	customer_id INT NOT NULL,
	product_id INT NOT NULL,
	PRIMARY KEY(order_id),
	FOREIGN KEY (agronomist_id) REFERENCES agronomist (agronomist_id),
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
	FOREIGN KEY (product_id) REFERENCES product (product_id)
);

CREATE TABLE order_return(
	return_id SERIAL,
	order_id INT NOT NULL,
	return_date DATE NOT NULL,
	PRIMARY KEY(return_id),
	FOREIGN KEY (order_id) REFERENCES ordering (order_id)
);

CREATE TABLE review(
	review_id SERIAL,
	customer_id INT NOT NULL,
	content VARCHAR(10000) NOT NULL,
	review_date DATE NOT NULL,
	PRIMARY KEY(review_id),
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

CREATE TABLE harvest(
	harvest_id SERIAL,
	agronomist_id INT NOT NULL,
	sort_id INT NOT NULL,
	harvest_date DATE NOT NULL,
	PRIMARY KEY(harvest_id),
	FOREIGN KEY (agronomist_id) REFERENCES agronomist (agronomist_id),
	FOREIGN KEY (sort_id) REFERENCES sort (sort_id)
);

CREATE TABLE degustation (
	degustation_id SERIAL,
	agronomist_id INT NOT NULL,
	product_id INT NOT NULL,
	degustation_date DATE NOT NULL,
	PRIMARY KEY(degustation_id),
	FOREIGN KEY (agronomist_id) REFERENCES agronomist (agronomist_id),
	FOREIGN KEY (product_id) REFERENCES product (product_id)
);

CREATE TABLE sort_product(
	sort_id INT NOT NULL,
	product_id INT NOT NULL,
	FOREIGN KEY (sort_id) REFERENCES sort (sort_id),
	FOREIGN KEY (product_id) REFERENCES product (product_id)
);

CREATE TABLE degustation_customer(
	degustation_id INT NOT NULL,
	customer_id INT NOT NULL,
	FOREIGN KEY (degustation_id) REFERENCES degustation (degustation_id),
	FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);

CREATE TABLE trip_agronomist(
	trip_id INT NOT NULL,
	agronomist_id INT NOT NULL,
	FOREIGN KEY (trip_id) REFERENCES business_trip (trip_id),
	FOREIGN KEY (agronomist_id) REFERENCES agronomist (agronomist_id)
);




-- DATA 

INSERT INTO customer (customer_name) VALUES 
    ('Kenzie Zuni'),
	('Maariya Slo'),
	('Alaya Cra'),
	('Cai Basse'),
	('Jamila Mcdona'),
	('Julius Ri'),
	('Macsen Wic'),
	('Franciszek Mel'),
	('Brent Kir'),
	('Haley Winte'),
	('Calum Wee'),
	('Manon Walla'),
	('Fahad Bur'),
	('Giacomo Kei'),
	('Lewys Herri'),
	('Poppy Sa'),
	('Kelsea Lawren'),
	('Zena Andre'),
	('Jeanette Vince'),
	('Dillon Greena')
;


INSERT INTO agronomist (agronomist_name) VALUES
    ('Markus Webb'),
	('Ameera Merri'),
	('Reo Castane'),
	('Katy Bart'),
	('Brogan Ri'),
	('Mikhail Wheel'),
	('Ollie Dani'),
	('Kaeden Mell'),
	('Om Sulliv'),
	('Trent Crossl'),
	('Chantel Mill'),
	('Zohaib Morris'),
	('Anam Lenn'),
	('Anas Raymo'),
	('Bridget Knigh'),
	('Reon Phel'),
	('Simon Krueg'),
	('Ubaid Vince'),
	('Khadijah Buxt'),
	('Shamima Bu')
;

INSERT INTO sort (sort_name) VALUES
    ('Indica'),
	('Sativa'),
	('Hybrid'),
	('Ruderalis'),
	('Space weed'),
	('Mars weed'),
	('Uranus weed'),
	('Pluto weed'),
	('Venera weed'),
	('Neptun weed'),
	('Saturn weed')
;

INSERT INTO product (product_name, price) VALUES
    ('White widow', 298),
	('OG Shark', 238),
	('Afghani', 364),
	('Skywalker OG', 241),
	('Lemon sour dieser', 299),
	('Jack Herer', 232),
	('Jean Guy', 317),
	('Pink kush', 265),
	('Master kush', 264),
	('Sweet Skunk', 218),
	('Blue Dream', 339),
	('Bubba Kush', 393),
	('Granddaddy Purple', 380),
	('LA Confidential', 324),
	('Maui Wowi', 220)
;

INSERT INTO business_trip (trip_date) VALUES
    ('2010-9-8'),
    ('2013-3-10'),
    ('2017-2-19'),
    ('2001-1-15'),
    ('2002-10-15'),
    ('2003-11-15'),
    ('2003-4-10'),
    ('2011-11-17'),
    ('2006-8-27'),
    ('2019-3-4'),
    ('2003-8-16'),
    ('2003-4-21'),
    ('2005-11-4'),
    ('2001-4-17'),
    ('2006-8-9'),
    ('2003-1-27'),
    ('2009-11-30'),
    ('2005-1-1'),
    ('2015-7-8'),
    ('2002-6-24'),
    ('2006-8-29'),
    ('2003-3-1'),
    ('2003-7-28'),
    ('2016-12-27'),
    ('2000-9-24'),
    ('2006-4-27'),
    ('2012-1-22'),
    ('2015-11-30'),
    ('2005-9-14'),
    ('2004-11-6'),
    ('2017-2-28'),
    ('2001-12-21'),
    ('2013-6-27'),
    ('2012-2-6'),
    ('2004-8-14'),
    ('2009-2-14'),
    ('2003-1-9'),
    ('2015-6-22'),
    ('2002-2-5'),
    ('2012-5-10'),
    ('2018-7-18'),
    ('2020-8-17'),
    ('2018-3-29'),
    ('2017-9-6'),
    ('2002-5-18'),
    ('2005-8-15'),
    ('2005-6-12'),
    ('2019-2-12'),
    ('2011-4-17'),
    ('2007-1-28')
;
							
INSERT INTO ordering (weight, total_price, order_date, agronomist_id, customer_id, product_id) VALUES						
    (4, 4145, '2017-3-12', 20, 6, 9),
    (8, 917, '2014-5-17', 1, 9, 8),
    (7, 3462, '2013-9-10', 12, 12, 9),
    (7, 2563, '2010-6-4', 12, 20, 3),
    (8, 6998, '2007-9-29', 8, 20, 8),
    (8, 3918, '2019-10-18', 2, 9, 4),
    (6, 6070, '2015-10-4', 8, 6, 11),
    (6, 573, '2009-2-19', 17, 11, 1),
    (8, 8304, '2020-8-10', 2, 7, 2),
    (3, 9231, '2012-12-20', 9, 3, 9),
    (7, 7763, '1999-7-27', 11, 20, 1),
    (4, 7669, '2000-10-12', 10, 11, 1),
    (1, 6020, '2007-5-11', 9, 1, 9),
    (6, 8408, '2019-5-10', 8, 9, 3),
    (6, 1329, '2000-10-11', 14, 16, 7),
    (5, 7524, '2003-11-17', 20, 8, 1),
    (4, 4808, '2006-2-21', 18, 5, 12),
    (1, 382, '2007-5-20', 20, 8, 5),
    (7, 5636, '2018-12-14', 17, 2, 1),
    (2, 9844, '2012-10-2', 9, 7, 7),
    (3, 2356, '2013-9-16', 12, 6, 6),
    (1, 1830, '2018-12-10', 12, 20, 12),
    (3, 3727, '2001-7-20', 10, 15, 11),
    (2, 8513, '2009-11-22', 15, 1, 5),
    (1, 9783, '2009-6-28', 20, 5, 5),
    (2, 9924, '2020-5-13', 18, 19, 12),
    (9, 1733, '2000-4-27', 20, 15, 8),
    (4, 4971, '2017-3-2', 19, 9, 12),
    (5, 8929, '2013-2-13', 19, 16, 9),
    (6, 3282, '2017-8-13', 3, 15, 9),
    (8, 8119, '2017-2-12', 13, 5, 2),
    (5, 6407, '2005-10-16', 15, 18, 2),
    (8, 9096, '2001-12-22', 18, 15, 5),
    (6, 8764, '2008-1-10', 6, 13, 12),
    (7, 3906, '2013-6-4', 13, 9, 6),
    (5, 6766, '2015-5-7', 12, 16, 10),
    (6, 5312, '1999-10-18', 8, 18, 10),
    (1, 6867, '2008-5-21', 9, 17, 6),
    (6, 7246, '2003-2-13', 11, 13, 7),
    (5, 3818, '2007-3-3', 9, 14, 5),
    (10, 473, '2018-10-4', 6, 18, 6),
    (3, 4315, '2011-8-10', 12, 15, 1),
    (1, 7608, '2005-9-27', 6, 16, 1),
    (10, 3016, '2001-9-24', 12, 4, 3),
    (1, 9297, '2016-6-16', 20, 18, 8),
    (9, 9547, '2018-2-27', 4, 6, 3),
    (5, 8655, '2003-8-19', 17, 12, 2),
    (8, 5870, '2012-9-8', 10, 7, 3),
    (2, 915, '2000-5-22', 17, 1, 4),
    (8, 1635, '2012-9-29', 20, 13, 9),
    (9, 5867, '2016-3-29', 12, 2, 10),
    (7, 3880, '2018-11-30', 6, 5, 11),
    (1, 449, '2003-1-26', 9, 5, 10),
    (1, 5746, '2015-5-22', 6, 8, 12),
    (10, 1428, '2003-10-23', 14, 4, 11),
    (3, 1113, '1999-9-10', 16, 17, 6),
    (6, 2892, '2004-7-2', 7, 18, 8),
    (1, 1142, '2017-9-7', 1, 7, 5),
    (7, 9727, '2001-7-12', 18, 7, 9),
    (4, 9632, '2006-12-7', 17, 5, 3),
    (10, 234, '2020-3-28', 5, 6, 3),
    (3, 6316, '2010-7-8', 1, 20, 8),
    (8, 7650, '2010-4-19', 12, 20, 11),
    (4, 6653, '2015-8-20', 19, 15, 5),
    (2, 8231, '2010-7-7', 2, 13, 5),
    (9, 9997, '2016-8-23', 19, 18, 7),
    (7, 5280, '2021-2-21', 12, 5, 1),
    (10, 508, '2011-10-12', 1, 12, 7),
    (6, 7676, '1999-4-14', 14, 1, 8),
    (10, 6072, '2014-9-11', 1, 7, 5),
    (10, 3151, '2014-7-27', 16, 2, 8),
    (4, 2336, '2007-8-29', 14, 8, 8),
    (9, 9711, '2021-5-30', 11, 20, 5),
    (8, 7698, '2002-9-16', 1, 11, 2),
    (8, 8582, '2005-12-14', 9, 12, 3),
    (7, 1906, '2007-6-27', 1, 9, 12),
    (2, 1063, '2002-6-27', 6, 6, 8),
    (4, 8539, '2005-3-21', 11, 20, 1),
    (10, 4343, '2009-8-18', 17, 16, 2),
    (6, 5002, '2021-2-16', 4, 7, 8),
    (9, 9833, '2007-11-17', 17, 17, 8),
    (7, 2327, '2013-1-20', 20, 4, 9),
    (10, 6842, '2002-2-9', 7, 11, 9),
    (10, 9866, '2001-6-17', 6, 6, 7),
    (1, 1398, '2017-11-27', 17, 2, 5),
    (4, 4847, '2014-3-9', 1, 13, 6),
    (9, 5284, '2014-11-30', 13, 18, 11),
    (3, 1466, '2003-7-20', 4, 7, 9),
    (10, 1310, '2012-11-12', 17, 20, 1),
    (5, 5384, '1999-2-5', 16, 18, 8),
    (2, 2971, '2021-2-3', 9, 18, 1),
    (1, 9227, '2009-6-7', 2, 11, 5),
    (5, 7414, '2003-1-5', 11, 5, 8),
    (9, 215, '2021-6-22', 17, 20, 1),
    (2, 8358, '2018-6-1', 3, 4, 12),
    (9, 1038, '2016-9-27', 5, 14, 3),
    (6, 9211, '2004-3-12', 14, 6, 2),
    (8, 1175, '2003-12-14', 4, 11, 9),
    (5, 705, '2000-12-18', 18, 15, 8),
    (3, 4258, '2006-11-30', 4, 8, 1)
;

INSERT INTO order_return (order_id, return_date) VALUES
    (3, '2003-2-10'),
    (50, '2012-6-13'),
    (60, '2003-1-30'),
    (4, '2018-5-11'),
    (7, '2015-1-3'),
    (8, '2004-6-5'),
    (9, '2018-12-19'),
    (33, '2004-5-28'),
    (69, '2010-11-26'),
    (42, '2021-5-26'),
    (55, '2014-2-18'),
    (88, '2021-4-28'),
    (92, '2008-4-9')
;

INSERT INTO review (customer_id, content, review_date) VALUES
    (14, 'Dizzy', '2005-8-7'),
    (7, 'Dizzy', '2016-7-12'),
    (15, 'Excellent', '2006-3-4'),
    (18, 'Dizzy', '2000-12-23'),
    (14, 'Dizzy', '2002-2-19'),
    (20, 'Dizzy', '2010-3-7'),
    (15, 'Excellent', '2006-5-25'),
    (10, 'Excellent', '2013-2-17'),
    (2, 'Bad', '2021-5-4'),
    (20, 'Bad', '2001-11-14'),
    (18, 'Good', '2013-4-15'),
    (10, 'Excellent', '2021-3-4'),
    (3, 'Excellent', '2012-7-8'),
    (4, 'Good', '2020-7-4'),
    (13, 'Excellent', '2017-9-25'),
    (20, 'Bad', '2012-7-26'),
    (8, 'Dizzy', '2004-7-4'),
    (6, 'Good', '2011-10-16'),
    (1, 'Good', '2005-9-2'),
    (19, 'Dizzy', '2007-9-25'),
    (9, 'Bad', '2003-11-10'),
    (8, 'Dizzy', '2018-5-24'),
    (16, 'Good', '2021-10-11'),
    (10, 'Excellent', '2008-8-7'),
    (4, 'Excellent', '2001-7-17'),
    (19, 'Dizzy', '2000-2-10'),
    (12, 'Dizzy', '2007-8-12'),
    (13, 'Dizzy', '2005-10-11'),
    (3, 'Bad', '2018-7-23'),
    (6, 'Dizzy', '2018-3-14'),
    (20, 'Excellent', '2015-7-15'),
    (20, 'Dizzy', '2014-7-30'),
    (14, 'Excellent', '2013-10-9'),
    (1, 'Excellent', '1999-3-16'),
    (6, 'Bad', '2017-8-19'),
    (14, 'Bad', '2013-3-1'),
    (6, 'Good', '2003-3-15'),
    (11, 'Dizzy', '2019-4-7'),
    (5, 'Excellent', '2006-11-22'),
    (10, 'Good', '2018-9-5'),
    (19, 'Good', '2021-9-27'),
    (4, 'Bad', '2009-12-13'),
    (1, 'Good', '2012-9-26'),
    (6, 'Bad', '2002-4-16'),
    (16, 'Good', '2011-9-6'),
    (7, 'Dizzy', '2019-5-5'),
    (18, 'Bad', '2020-2-2'),
    (9, 'Good', '2001-9-30'),
    (14, 'Bad', '2000-6-23'),
    (7, 'Dizzy', '2015-8-20')
;

INSERT INTO harvest (agronomist_id, sort_id, harvest_date) VALUES
    (6, 2, '2007-2-6'),
    (11, 7, '2003-7-10'),
    (7, 7, '2011-7-4'),
    (9, 10, '2010-2-8'),
    (14, 6, '2003-3-11'),
    (17, 6, '1999-12-22'),
    (19, 6, '2003-10-2'),
    (1, 2, '2020-8-3'),
    (5, 6, '2005-9-9'),
    (19, 11, '2010-1-28'),
    (8, 11, '2000-11-6'),
    (8, 9, '2019-1-14'),
    (14, 10, '2004-12-15'),
    (16, 7, '2008-12-9'),
    (14, 9, '2018-9-11'),
    (5, 7, '2010-3-14'),
    (4, 7, '2011-10-17'),
    (16, 6, '2002-8-17'),
    (4, 9, '2008-10-6'),
    (9, 8, '2007-4-16')
;

INSERT INTO degustation (agronomist_id, product_id, degustation_date) VALUES
    (12, 12, '2010-7-7'),
    (7, 4, '2018-8-17'),
    (12, 1, '2008-9-26'),
    (16, 3, '2017-5-18'),
    (18, 13, '2001-6-11'),
    (16, 13, '2005-3-4'),
    (3, 5, '2008-12-25'),
    (19, 15, '2009-3-8'),
    (2, 12, '2012-5-21'),
    (10, 13, '2017-11-3'),
    (7, 15, '2004-6-26'),
    (6, 9, '2021-4-18'),
    (16, 2, '2010-3-22'),
    (20, 2, '2015-7-20'),
    (3, 8, '2011-8-15'),
    (3, 14, '2018-1-2'),
    (3, 15, '2018-1-11'),
    (14, 7, '2013-10-26'),
    (7, 2, '2019-5-3'),
    (9, 4, '2019-11-14'),
    (5, 5, '2002-8-11'),
    (2, 2, '2018-4-7'),
    (17, 6, '2010-6-10'),
    (8, 4, '2010-8-16'),
    (16, 1, '2001-1-30'),
    (14, 10, '2001-12-25'),
    (4, 8, '2004-2-12'),
    (9, 11, '2002-4-14'),
    (11, 7, '2021-5-2'),
    (7, 4, '2006-3-13'),
    (7, 7, '2015-9-7'),
    (20, 6, '2004-1-1'),
    (7, 12, '2003-11-30'),
    (6, 12, '2011-3-30'),
    (1, 12, '2009-9-3'),
    (15, 8, '2013-11-15'),
    (4, 2, '2010-1-5'),
    (8, 10, '2009-11-21'),
    (7, 3, '2012-7-24'),
    (7, 2, '2004-8-1'),
    (9, 4, '2019-8-13'),
    (4, 1, '2015-7-8'),
    (10, 13, '2007-3-1'),
    (16, 3, '2003-3-24'),
    (1, 11, '2000-12-18')
;

INSERT INTO sort_product VALUES
    (6, 1),
    (4, 13),
    (4, 15),
    (9, 13),
    (3, 8),
    (2, 3),
    (6, 6),
    (4, 5),
    (8, 3),
    (6, 5),
    (4, 2),
    (10, 12),
    (2, 8),
    (4, 9),
    (7, 7),
    (1, 15),
    (11, 4),
    (7, 14),
    (8, 11),
    (6, 3),
    (1, 5),
    (4, 13),
    (9, 3),
    (11, 10)
;


INSERT INTO degustation_customer VALUES
    (35, 5),
    (20, 1),
    (9, 8),
    (4, 16),
    (8, 4),
    (19, 1),
    (24, 15),
    (20, 18),
    (17, 2),
    (16, 1),
    (9, 9),
    (4, 3),
    (12, 3),
    (34, 3),
    (41, 12),
    (9, 14),
    (44, 4),
    (43, 12),
    (36, 14),
    (44, 19),
    (14, 12),
    (24, 13),
    (11, 10),
    (31, 17)
;

INSERT INTO trip_agronomist VALUES 
    (29, 10),
    (13, 4),
    (39, 17),
    (39, 5),
    (7, 2),
    (40, 20),
    (5, 5),
    (9, 14),
    (6, 5),
    (16, 19),
    (32, 19),
    (31, 2),
    (34, 2),
    (16, 15),
    (14, 10),
    (16, 2),
    (9, 5),
    (34, 13),
    (11, 6),
    (6, 19),
    (30, 18),
    (32, 7),
    (3, 1),
    (10, 5)
;
						
						
						
						
						
						
						