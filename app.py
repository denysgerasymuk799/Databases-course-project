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

    table_cols = ["customer_id", "customer_name"]
    if request.method == 'GET':
        return render_template("request1.html",
                               agronom_lst=agronomists_list,
                               selected_agr_id=1,
                               selected_from_date="-",
                               selected_to_date="-",
                               sold_times=1,
                               table_cols=table_cols,
                               customers=[(0, "No result")])

    if request.method == 'POST':
        # Get a data in json format(similar)
        data = {
            "agronom_id": int(request.form.get("agronom_id")),
            "sold_times": int(request.form.get("sold_times")),
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
            SELECT customer_id, customer_name FROM Customer WHERE customer_id IN 
                (SELECT customer_id FROM
                (SELECT customer_id, COUNT(customer_id) AS num FROM Ordering WHERE agronomist_id = :agronom_id
                    AND order_date BETWEEN :from_date AND :to_date GROUP BY customer_id) h 
                WHERE h.num > :sold_times);
            """
        )

        rs = db.session.execute(statement, {
            "agronom_id": data["agronom_id"],
            "sold_times": data["sold_times"],
            "from_date": data["from_date"],
            "to_date": data["to_date"]
        })
        db.session.commit()
        db.session.close()

        results = rs.fetchall()
        print("request1_handle -- ", results)

        return render_template("request1.html",
                               agronom_lst=agronomists_list,
                               selected_agr_id=data["agronom_id"],
                               selected_from_date=data["from_date"],
                               selected_to_date=data["to_date"],
                               sold_times=data["sold_times"],
                               table_cols=table_cols,
                               customers=results)


@app.route('/request2', methods=['GET', 'POST'])
def request_page_action2():
    statement = text("""SELECT customer_id, customer_name FROM customer""")

    customer_values_sample = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action2", customer_values_sample)

    table_cols = ["product_id", "product_name"]
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
            SELECT product_id, product_name FROM Product WHERE product_id IN
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

    rs = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action3 -- ", rs)

    customer_values_sample = [(1, "Lima"), (3, "Huka")]
    return render_template("request3.html", customer_lst=customer_values_sample)


@app.route('/request3_handled', methods=['POST'])
def request3_handle():
    # Get a data in json format(similar)
    data = request.form

    statement = text("""
        SELECT agronomist_id FROM
        (SELECT agronomist_id, COUNT(*) AS num FROM 
        Degustation INNER JOIN Degustation_Customer ON 
        Degustation.degustation_id = Degustation_Customer.degustation_id 
        WHERE Degustation_Customer.customer_id = :cus_id GROUP BY agronomist_id) WHERE num > :n_times AND degustation_date 
        BETWEEN :date_start AND :date_end;
        """)

    rs = db.session.execute(statement, **data).all()
    db.session.commit()
    db.session.close()

    print("request3_handle -- ", rs)

    # TODO print all agronomes
    return 'Hello3'


if __name__ == '__main__':
    app.run(port=8000, debug=True)
