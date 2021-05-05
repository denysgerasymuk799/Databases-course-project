from flask import Flask, redirect, url_for, render_template, request, session
from sqlalchemy import create_engine
from sqlalchemy.sql import text

# TODO should run the server
db_string = "postgres://admin:donotusethispassword@aws-us-east-1-portal.19.dblayer.com:15813/compose"
db = create_engine(db_string)

app = Flask(__name__)
# FOR sessions
app.secret_key = "SOMESECRET"




@app.route('/', methods=['GET', 'POST'])
def get_main_page():
    return render_template("index.html")


@app.route('/request1', methods=['GET', 'POST'])
def request_page_action1():
    statement = text("""SELECT agronomist_id, agronomist_name FROM agronomist""")
    with db.connect() as conn:
        rs = conn.execute(statement)
        # TODO process the rs
        print(rs)
        agronom_values_sample = rs
    agronom_values_sample = [(1, "James"), (3, "Denys")]

    return render_template("request1.html", agronom_lst=agronom_values_sample)


@app.route('/request1_handled', methods=['POST'])
def request1_handle():
    # Get a data in json format(similar)
    data = request.form
    # print(data['ag_id'])
    # print(data['n_times'])
    # print(data['date_start'])
    # print(data['date_end'])
    statement = text("""SELECT customer_id FROM 
    (SELECT customer_id, COUNT(*) AS num FROM ordering WHERE agronomist_id = :ag_id 
    	AND order_date BETWEEN :date_start AND :date_end GROUP BY customer_id) 
    WHERE num > :n_times;""")

    with db.connect() as conn:
        rs = conn.execute(statement, **data)
        # TODO print in a better GUI way
        print(rs)

    return 'Hello1'


@app.route('/request2', methods=['GET', 'POST'])
def request_page_action2():
    statement = text("""SELECT customer_id, customer_name FROM customer""")
    with db.connect() as conn:
        rs = conn.execute(statement)
        # TODO process the rs
        print(rs)
        customer_values_sample = rs
    customer_values_sample = [(1, "Lima"), (3, "Huka")]

    return render_template("request2.html", customer_lst=customer_values_sample)


@app.route('/request2_handled', methods=['POST'])
def request2_handle():
    # Get a data in json format(similar)
    data = request.form
    # print(data['cus_id'])
    # print(data['date_start'])
    # print(data['date_end'])
    statement = text("""SELECT DISTINCT product_id FROM ordering WHERE customer_id = 
    :cus_id AND order_date BETWEEN :date_start AND :date_end;""")

    with db.connect() as conn:
        rs = conn.execute(statement, **data)
        # TODO print in a better GUI way
        print(rs)

    # TODO print all products
    return 'Hello2'


@app.route('/request3', methods=['GET', 'POST'])
def request_page_action3():
    statement = text("""SELECT customer_id, customer_name FROM customer""")
    with db.connect() as conn:
        rs = conn.execute(statement)
        # TODO process the rs
        print(rs)
        customer_values_sample = rs
    customer_values_sample = [(1, "Lima"), (3, "Huka")]

    return render_template("request3.html", customer_lst=customer_values_sample)


@app.route('/request3_handled', methods=['POST'])
def request3_handle():
    # Get a data in json format(similar)
    data = request.form
    # print(data['cus_id'])
    # print(data['n_times'])
    # print(data['date_start'])
    # print(data['date_end'])
    statement = text("""SELECT agronomist_id FROM
(SELECT agronomist_id, COUNT(*) AS num FROM 
Degustation INNER JOIN Degustation_Customer ON 
Degustation.degustation_id = Degustation_Customer.degustation_id 
WHERE Degustation_Customer.customer_id = :cus_id GROUP BY agronomist_id) WHERE num > :n_times AND degustation_date 
BETWEEN :date_start AND :date_end;""")

    with db.connect() as conn:
        rs = conn.execute(statement, **data)
        # TODO print in a better GUI way
        print(rs)

    # TODO print all agronomes
    return 'Hello3'


@app.route('/request3', methods=['GET', 'POST'])
def request_page_action3():
    return render_template("request3.html")


if __name__ == '__main__':
    app.run(debug=True)
