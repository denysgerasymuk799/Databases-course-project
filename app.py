from flask import Flask, redirect, url_for, render_template, request, session
from sqlalchemy.sql import text
from datetime import date

from init_config import db, app
from models import Customer


@app.route('/', methods=['GET', 'POST'])
def get_main_page():
    return render_template("index.html")


@app.route('/request1', methods=['GET', 'POST'])
def request_page_action1():
    if request.method == 'GET':
        statement = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")

        agronomists_list = db.session.execute(statement).all()
        db.session.commit()
        db.session.close()

        return render_template("request1.html", agronom_lst=agronomists_list)

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
            # data["from_date"] = today.strftime("%Y-%m-%d")
            data["from_date"] = '2013-01-01'

        if data["to_date"] == '':
            data["to_date"] = today.strftime("%Y-%m-%d")

        print("data in request1_handle -- ", data)

        statement = text(
            """
            SELECT customer_id FROM 
                (SELECT customer_id, COUNT(*) AS num FROM ordering WHERE agronomist_id = :agronom_id 
                    AND order_date BETWEEN :from_date AND :to_date GROUP BY customer_id)  AS foo
                WHERE num >= :sold_times;
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
        customer_names = []
        for customer_id in results:
            print("type(customer_id) -- ", type(customer_id[0]))
            customer_names.append(Customer.query.filter_by(customer_id=customer_id[0]).first().customer_name)

        print("customer_names -- ", customer_names)
        return 'Hello1'


@app.route('/request2', methods=['GET', 'POST'])
def request_page_action2():
    statement = text("""SELECT customer_id, customer_name FROM customer""")

    rs = db.session.execute(statement).all()
    db.session.commit()
    db.session.close()

    print("request_page_action2", rs)
    customer_values_sample = [(1, "Lima"), (3, "Huka")]

    return render_template("request2.html", customer_lst=customer_values_sample)


@app.route('/request2_handled', methods=['POST'])
def request2_handle():
    # Get a data in json format(similar)
    data = request.form

    statement = text("""SELECT DISTINCT product_id FROM ordering WHERE customer_id = 
    :cus_id AND order_date BETWEEN :date_start AND :date_end;""")

    rs = db.session.execute(statement, **data).all()
    db.session.commit()
    db.session.close()

    print("request2_handle -- ", rs)
    # TODO print all products
    return 'Hello2'


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
