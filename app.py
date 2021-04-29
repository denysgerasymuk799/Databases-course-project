from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get_main_page():
    return render_template("index.html")


@app.route('/request1', methods=['GET', 'POST'])
def request_page_action1():
    lst1 = ['Item1', 'Item2']
    return render_template("request1.html", form1_select=lst1, form1_select_len=len(lst1))


@app.route('/request1_handled', methods=['GET', 'POST'])
def request1_handle():
    return 'Hellow'


@app.route('/request2', methods=['GET', 'POST'])
def request_page_action2():
    return render_template("request2.html")


if __name__ == '__main__':
    app.run(debug=True)
