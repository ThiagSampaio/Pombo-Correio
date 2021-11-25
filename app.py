from flask import Flask, render_template, request, jsonify
from email_send.send_mail_test import *
import pandas as pd
from email_send.processar_texto import *
from werkzeug.utils import secure_filename
import os
import sys


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    email = request.args.get("email")
    senha = request.args.get("senha")
    print(f'este é o email: {email}')
    print(f'este é a senha: {senha}')
    retorno = send_mail_test1(email, senha)
    return jsonify({'resposta_bol': retorno[0], 'mensagem': retorno[1]})


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    lista_emails_erro_final = []
    if request.method == 'POST':
        # Pegar o formulário
        email = request.form.get('email')
        senha = request.form.get('senha')
        coluna_grupo = request.form.get('coluna_grupo')
        coluna_email = request.form.get('coluna_email')
        titulo_email = request.form.get('titulo_email')

        # Pegar os arquivos 1 -> docx 2-> xlms
        texto_email = request.files['texto']
        texto_email.save(secure_filename(texto_email.filename))

        database = request.files['database']
        database.save(secure_filename(database.filename))

        # tratar os arquivos
        texto_email_tratado = docx_2_html(texto_email)

        data = pd.read_excel(database)
        data = data[[coluna_grupo, coluna_email]]
        data_dicionario = data.groupby([coluna_grupo])[
            coluna_email].apply(list).to_dict()

        # iterando o dicionario
        for key_estado in data_dicionario:
            emails = send_mail(
                email, senha, data_dicionario[key_estado], titulo_email, texto_email_tratado.value)
            lista_emails_erro_final.append(emails)

        return jsonify({'emails_com_erro': lista_emails_erro_final})


if __name__ == '__main__':

    # produção
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # dev
    # app.run(debug=True)
