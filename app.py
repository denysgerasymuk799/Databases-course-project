from flask import Flask, redirect, url_for, render_template, request, session
from sqlalchemy.sql import text
from datetime import date

from init_config import db, app
from models import Customer, Agronomist


@app.route('/', methods=['GET', 'POST'])
def get_main_page():
    return render_template("index.html")


@app.route('/request1', methods=['GET', 'POST'])
def request_page_action1():
    statement = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")

    agronomists_list = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    table_cols = ["customer_name"]
    if request.method == 'GET':
        return render_template("request1.html",
                               agronomists_lst=agronomists_list,
                               selected_agr_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               customers=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "agronomist_id": int(request.form.get("agronomist_id")),
            "n_times": int(request.form.get("n_times")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request1_handle -- ", data)

        statement = text(
            """
            SELECT customer_name FROM Customer WHERE customer_id IN 
(SELECT customer_id FROM
(SELECT customer_id, COUNT(customer_id) AS num FROM Ordering WHERE agronomist_id = :agronomist_id
	AND order_date BETWEEN :from_date AND :to_date GROUP BY customer_id) h 
WHERE h.num > :n_times);
            """
        )

        rs = db.session.execute(statement, {
            "agronomist_id": data["agronomist_id"],
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request1_handle -- ", results)

        return render_template("request1.html",
                               agronomists_lst=agronomists_list,
                               selected_agr_id=data["agronomist_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               customers=results)


@app.route('/request2', methods=['GET', 'POST'])
def request_page_action2():
    statement = text("""SELECT customer_id, customer_name FROM customer""")

    customer_values_sample = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action2", customer_values_sample)

    table_cols = ["product_name"]
    if request.method == 'GET':
        return render_template("request2.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               products=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "cust_id": int(request.form.get("cust_id")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2010-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request2_handle -- ", data)

        statement = text(
            """
            SELECT product_name FROM Product WHERE product_id IN
             (SELECT DISTINCT product_id FROM Ordering 
               WHERE customer_id = :cust_id AND order_date BETWEEN :from_date AND :to_date);
            """
        )

        rs = db.session.execute(statement, {
            "cust_id": data["cust_id"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request2_handle results -- ", results)

        return render_template("request2.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=data["cust_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               products=results)


@app.route('/request3', methods=['GET', 'POST'])
def request_page_action3():
    statement = text("""SELECT customer_id, customer_name FROM customer""")

    customer_values_sample = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action3", customer_values_sample)

    table_cols = ["agronomist_name"]
    if request.method == 'GET':
        return render_template("request3.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               agronomists=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "cust_id": int(request.form.get("cust_id")),
            "n_times": int(request.form.get("n_times")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2010-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request3_handle -- ", data)

        statement = text(
            """
            SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN
	(SELECT agronomist_id FROM (SELECT agronomist_id, COUNT(agronomist_id) AS num FROM 
	Degustation INNER JOIN Degustation_Customer ON 
	Degustation.degustation_id = Degustation_Customer.degustation_id 
	WHERE Degustation_Customer.customer_id = :cust_id AND degustation_date BETWEEN :from_date AND :to_date GROUP BY agronomist_id) h
 WHERE h.num >= :n_times);
            """
        )

        rs = db.session.execute(statement, {
            "cust_id": data["cust_id"],
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request3_handle results -- ", results)

        return render_template("request3.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=data["cust_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               agronomists=results)



@app.route('/request4', methods=['GET', 'POST'])
def request_page_action4():
    statement = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")

    agronomists_list = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    # print("request_page_action2", customer_values_sample)

    table_cols = ["agronomist_name"]
    if request.method == 'GET':
        return render_template("request4.html",
                               agronomists_list=agronomists_list,
                               selected_agronomist_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               agronomists=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "agronomist_id": int(request.form.get("agronomist_id")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2010-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request4_handle -- ", data)

        statement = text(
            """
            SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN 
(SELECT DISTINCT agronomist_id FROM Trip_Agronomist WHERE agronomist_id != :agronomist_id AND trip_id IN
(SELECT trip_id FROM business_trip WHERE trip_date BETWEEN :from_date AND :to_date AND trip_id IN 
(SELECT trip_id FROM Trip_Agronomist WHERE agronomist_id = :agronomist_id)));
            """
        )

        rs = db.session.execute(statement, {
            "agronomist_id": data["agronomist_id"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request4_handle results -- ", results)

        return render_template("request4.html",
                               agronomists_list=agronomists_list,
                               selected_cust_id=data["agronomist_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               agronomists=results)



@app.route('/request5', methods=['GET', 'POST'])
def request_page_action5():
    statement = text("""SELECT customer_id, customer_name FROM customer""")

    customer_values_sample = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action5", customer_values_sample)

    table_cols = ["agronomist_name"]
    if request.method == 'GET':
        return render_template("request5.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               agronomists=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "cust_id": int(request.form.get("cust_id")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2010-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request5_handle -- ", data)

        statement = text(
            """
            SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN 
	(SELECT agronomist_id FROM Ordering
	 WHERE customer_id = :cust_id AND order_date BETWEEN :from_date AND :to_date)
AND agronomist_id IN
	(SELECT agronomist_id FROM Degustation WHERE degustation_id IN 
	(SELECT degustation_id FROM degustation_customer WHERE customer_id = :cust_id)
 	AND degustation_date BETWEEN :from_date AND :to_date);
            """
        )

        rs = db.session.execute(statement, {
            "cust_id": data["cust_id"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request5_handle results -- ", results)

        return render_template("request5.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=data["cust_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               agronomists=results)


@app.route('/request6', methods=['GET', 'POST'])
def request_page_action6():

    table_cols = ["customer_name"]
    if request.method == 'GET':
        return render_template("request6.html",
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               customers=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "n_times": int(request.form.get("n_times")),

            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request6_handle -- ", data)

        statement = text(
            """
            SELECT customer_name FROM Customer WHERE customer_id IN
(SELECT customer_id FROM 
 (SELECT customer_id, COUNT(DISTINCT product_id) AS num FROM Ordering INNER JOIN Ordering_Product ON Ordering.order_id = Ordering_Product.order_id 
  WHERE order_date BETWEEN :from_date AND :to_date GROUP BY customer_id) h
 WHERE h.num > :n_times);
            """
        )

        rs = db.session.execute(statement, {
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request6_handle -- ", results)

        return render_template("request6.html",
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               customers=results)



@app.route('/request7', methods=['GET', 'POST'])
def request_page_action7():
    statement = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")

    agronomists_list = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    table_cols = ["agronomist_id"]
    if request.method == 'GET':
        return render_template("request7.html",
                               agronomists_lst=agronomists_list,
                               selected_agr_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               agronomists=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "agronomist_id": int(request.form.get("agronomist_id")),
            "n_times": int(request.form.get("n_times")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request7_handle -- ", data)

        statement = text(
            """
             SELECT agronomist_name FROM Agronomist WHERE agronomist_id IN (
 SELECT agronomist_id FROM (SELECT agronomist_id, COUNT(sort_id) AS num FROM Harvest
				WHERE harvest_date BETWEEN :from_date AND :to_date GROUP BY agronomist_id) h
 WHERE h.num > :n_times);
            """
        )

        rs = db.session.execute(statement, {
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request7_handle -- ", results)

        return render_template("request7.html",
                               agronomists_lst=agronomists_list,
                               selected_agr_id=data["agronomist_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               agronomists=results)


@app.route('/request8', methods=['GET', 'POST'])
def request_page_action8():
    statement1 = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")
    statement2 = text("""SELECT customer_id, customer_name FROM customer""")

    customer_values_sample = db.session.execute(statement2).all()
    agronomists_list = db.session.execute(statement1).all()
    db.session.commit()
    db.session.close()

    table_cols = ["degustation_id"]
    if request.method == 'GET':
        return render_template("request8.html",
                               agronomists_lst=agronomists_list,
                               customer_lst=customer_values_sample,
                               selected_cust_id=1,
                               selected_agr_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               degustaions=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "cust_id": int(request.form.get("cust_id")),
            "agronomist_id": int(request.form.get("agronomist_id")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request8_handle -- ", data)

        statement = text(
            """
            SELECT DISTINCT Degustation.degustation_id FROM Degustation
INNER JOIN Degustation_Customer
ON Degustation.degustation_id = Degustation_Customer.degustation_id 
WHERE Degustation_Customer.customer_id = :cust_id AND Degustation.agronomist_id = :agronomist_id
AND Degustation.degustation_date BETWEEN :from_date AND :to_date;
            """
        )

        rs = db.session.execute(statement, {
            "cust_id": data["cust_id"],
            "agronomist_id": data["agronomist_id"],

            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request8_handle -- ", results)

        return render_template("request8.html",
                               agronomists_lst=agronomists_list,
                               customer_lst=customer_values_sample,
                               selected_agr_id=data["agronomist_id"],
                               selected_cust_id=data["cust_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               degustations=results)



@app.route('/request9', methods=['GET', 'POST'])
def request_page_action9():
    statement = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")

    agronomists_list = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    table_cols = ["product_id", "number_times"]
    if request.method == 'GET':
        return render_template("request9.html",
                               agronomists_lst=agronomists_list,
                               selected_agr_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               result=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "agronomist_id": int(request.form.get("agronomist_id")),
            "n_times": int(request.form.get("n_times")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request9_handle -- ", data)

        statement = text(
            """
            SELECT product_id, COUNT(product_id) FROM Degustation WHERE degustation_id IN (
SELECT degustation_id FROM (SELECT Degustation.degustation_id, COUNT(DISTINCT Degustation_Customer.customer_id) AS num FROM Degustation 
INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id  
WHERE degustation_date BETWEEN :from_date AND :to_date
AND agronomist_id = :agronomist_id GROUP BY Degustation.degustation_id) h WHERE h.num > :n_times) GROUP BY product_id;
            """
        )

        rs = db.session.execute(statement, {
            "agronomist_id": data["agronomist_id"],
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request9_handle -- ", results)

        return render_template("request9.html",
                               agronomists_lst=agronomists_list,
                               selected_agr_id=data["agronomist_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               result=results)



@app.route('/request10', methods=['GET', 'POST'])
def request_page_action10():
    statement = text("""SELECT customer_id, customer_name FROM customer""")

    customer_values_sample = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action10", customer_values_sample)

    table_cols = ["month", "number_times"]
    if request.method == 'GET':
        return render_template("request10.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               result=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "cust_id": int(request.form.get("cust_id")),
            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2010-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request10_handle -- ", data)

        statement = text(
            """
            SELECT EXTRACT(YEAR FROM return_date) AS years, EXTRACT (MONTH FROM return_date) AS months, COUNT(return_id) AS TOTALCOUNT 
FROM Order_Return WHERE return_date BETWEEN :from_date AND :to_date
GROUP BY years, months
ORDER BY years, months;
            """
        )

        rs = db.session.execute(statement, {
            "cust_id": data["cust_id"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request10_handle results -- ", results)

        return render_template("request10.html",
                               customer_lst=customer_values_sample,
                               selected_cust_id=data["cust_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               result=results)



@app.route('/request11', methods=['GET', 'POST'])
def request_page_action11():

    table_cols = ["harvest_name"]
    if request.method == 'GET':
        return render_template("request11.html",
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               result=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "n_times": int(request.form.get("n_times")),

            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request11_handle -- ", data)

        statement = text(
            """
            CREATE OR REPLACE VIEW hrvsts AS (SELECT sort_name, f.agronomist_name, harvest_date, 
    CASE 
      WHEN trips IS NULL THEN 0 
    ELSE trips 
    END
    FROM (
    SELECT * FROM (sort s INNER JOIN harvest h ON s.sort_id = h.sort_id) d INNER JOIN agronomist a ON d.agronomist_id = a.agronomist_id 
WHERE harvest_date BETWEEN :from_date AND :to_date ) f 
    LEFT JOIN 
        (SELECT agronomist_name, COUNT(agronomist_name) trips FROM agronomist a 
     INNER JOIN trip_agronomist ta on a.agronomist_id = ta.agronomist_id GROUP BY agronomist_name) g 
     on f.agronomist_name = g.agronomist_name );

SELECT sort_name, CASE
    WHEN sort_name IN 
        (SELECT sort_name FROM hrvsts
         group by (sort_name, agronomist_name)
         having count(agronomist_name) > :n_times)
		 THEN SUM(trips)/COUNT(agronomist_name)
  ELSE 0
  END AS av_trips
FROM hrvsts 
GROUP BY sort_name
ORDER BY av_trips DESC
            """
        )

        rs = db.session.execute(statement, {
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request11_handle -- ", results)

        return render_template("request11.html",
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               result=results)



@app.route('/request12', methods=['GET', 'POST'])
def request_page_action12():

    table_cols = ["product_name", "percentage"]
    if request.method == 'GET':
        return render_template("request12.html",
                               selected_from_date="-",
                               selected_to_date="-",
                               table_cols=table_cols,
                               result=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "n_times": int(request.form.get("n_times")),

            "from_date": request.form.get("from_date"),
            "to_date": request.form.get("to_date")
        }

        today = date.today()
        if data["from_date"] == '':
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request12_handle -- ", data)

        statement = text(
            """
            SELECT product_name, ROUND(CAST(returned AS DECIMAL)/bought * 100, 2) perc FROM
(SELECT d.product_name, bought, CASE 
   WHEN returned IS NULL THEN 0
   ELSE returned
   END AS returned
FROM 
(SELECT product_name, COUNT(product_name) bought FROM (ordering o LEFT JOIN ordering_product op ON o.order_id = op.order_id) f 
LEFT JOIN product p ON f.product_id = p.product_id
GROUP BY product_name) d LEFT JOIN
(SELECT product_name, COUNT(product_name) returned FROM ((SELECT op.order_id, product_id FROM ordering o LEFT JOIN ordering_product op ON o.order_id = op.order_id) f 
LEFT JOIN product p ON f.product_id = p.product_id) n RIGHT JOIN order_return orr ON n.order_id = orr.order_id  
WHERE return_date BETWEEN :from_date AND :to_date
GROUP BY product_name) g on d.product_name = g.product_name
WHERE bought >= :n_times) h
ORDER BY perc DESC
            """
        )

        rs = db.session.execute(statement, {
            "n_times": data["n_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request12_handle -- ", results)

        return render_template("request12.html",
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               table_cols=table_cols,
                               result=results)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
