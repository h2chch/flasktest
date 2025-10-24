from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def login():
    name = request.form.get('name')
    return render_template('main.html', person=name)
