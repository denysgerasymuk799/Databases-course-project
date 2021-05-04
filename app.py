from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_main_page():
    return render_template("index.html")


@app.route('/request1', methods=['GET', 'POST'])
def request_page_action1():
    return render_template("request1.html")


@app.route('/request2', methods=['GET', 'POST'])
def request_page_action2():
    return render_template("request2.html")


@app.route('/request3', methods=['GET', 'POST'])
def request_page_action3():
    return render_template("request3.html")


if __name__ == '__main__':
    app.run(debug=True)
