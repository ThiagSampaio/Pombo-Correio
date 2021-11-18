from flask import Flask, render_template, request, jsonify
from email_send.send_mail_test import *
import pandas as pd
import csv


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    email = request.args.get("email")
    senha = request.args.get("senha")
    retorno = send_mail(email, senha)
    return jsonify({'resposta_bol': retorno[0], 'mensagem': retorno[1]})


@app.route('/data', methods=['GET'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('data.html', data=data)


if __name__ == '__main__':

    app.run(debug=True)
