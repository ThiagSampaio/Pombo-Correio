from flask import Flask, render_template, request, jsonify
from flask.wrappers import Response
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


@app.route('/data', methods=['GET', 'POST'])
def data():

    coluna = request.args.get('coluna')
    coluna_email = request.args.get('coluna_email')
    f = request.args.get('database')
    data = pd.read_excel(f)
    data = data[[coluna, coluna_email]]
    dicionario = data.groupby([coluna])[coluna_email].apply(list).to_dict()

    return data


if __name__ == '__main__':

    app.run(debug=True)
