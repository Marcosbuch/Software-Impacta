from flask import Flask, request, jsonify, render_template
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuração da conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Buch_159753",  # Insira a senha do MySQL
        database="assessoria_financeira"
    )

# Página inicial
@app.route('/')
def home():
    return render_template('home.html')


# Cadastramento Receita

# Página de cadastro de receita
@app.route('/cadastrar-receita', methods=['GET'])
def render_cadastrar_receita():
    return render_template('cadastrar_receita.html')

# Rota para cadastrar receita
@app.route('/cadastrar-receita', methods=['POST'])
def cadastrar_receita():
    data = request.json
    descricao_receita = data.get('descricao_receita')
    tipo_receita = data.get('tipo_receita')
    indicador1_receita = data.get('indicador1_receita')
    indicador2_receita = data.get('indicador2_receita')
    compoe_dre_receita = data.get('compoe_dre_receita')
    compoe_dfc_receita = data.get('compoe_dfc_receita')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        sql = """
        INSERT INTO plano_contas_receitas 
        (descricao_receita, tipo_receita, indicador1_receita, indicador2_receita, compoe_dre_receita, compoe_dfc_receita, data_receita) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (descricao_receita, tipo_receita, indicador1_receita, indicador2_receita, compoe_dre_receita, compoe_dfc_receita, datetime.now())
        cursor.execute(sql, values)
        connection.commit()
        message = 'Receita cadastrada com sucesso!'
    except Exception as e:
        connection.rollback()
        message = f'Ocorreu um erro: {str(e)}'
    finally:
        cursor.close()
        connection.close()

    return jsonify({'message': message})


# Cadastramento Despesa

# Página de cadastro de despesa
@app.route('/cadastrar-despesa', methods=['GET'])
def render_cadastrar_despesa():
    return render_template('cadastrar_despesa.html')

# Rota para cadastrar despesa
@app.route('/cadastrar-despesa', methods=['POST'])
def cadastrar_despesa():
    data = request.json
    descricao_despesa = data.get('descricao_despesa')
    tipo_despesa = data.get('tipo_despesa')
    indicador1_despesa = data.get('indicador1_despesa')
    indicador2_despesa = data.get('indicador2_despesa')
    compoe_dre_despesa = data.get('compoe_dre_despesa')
    compoe_dfc_despesa = data.get('compoe_dfc_despesa')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        sql = """
        INSERT INTO plano_contas_despesas 
        (descricao_despesa, tipo_despesa, indicador1_despesa, indicador2_despesa, compoe_dre_despesa, compoe_dfc_despesa, data_despesa) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (descricao_despesa, tipo_despesa, indicador1_despesa, indicador2_despesa, compoe_dre_despesa, compoe_dfc_despesa, datetime.now())
        cursor.execute(sql, values)
        connection.commit()
        message = 'Despesa cadastrada com sucesso!'
    except Exception as e:
        connection.rollback()
        message = f'Ocorreu um erro: {str(e)}'
    finally:
        cursor.close()
        connection.close()

    return jsonify({'message': message})



# Cadastramento Bancos

@app.route('/cadastrar-caixa', methods=['GET'])
def render_cadastrar_caixa():
    return render_template('cadastrar_caixa.html')

#Rota para cadastrar Caixas
@app.route('/cadastrar-caixa', methods=['POST'])
def cadastrar_caixa():
    data = request.json
    nome_banco = data.get('nome_banco')
    bandeira = data.get('bandeira')
    tipo_de_pagamento =  data.get('tipo_de_pagamento')
    taxa =  data.get('taxa')
    prazo =  data.get('prazo')

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        sql = """
        INSERT INTO caixa
        (nome_banco, bandeira, tipo_de_pagamento, taxa, prazo, data_caixa)
        VALUES(%s,%s,%s,%s,%s,%s)
        """

        values = (nome_banco, bandeira, tipo_de_pagamento, taxa, prazo, datetime.now())
        cursor.execute(sql, values)
        connection.commit()
        message= 'Caixa cadastrado com sucesso'
    except Exception as e:
        connection.rollback()
        message = f'Ocorreu um erro: {str(e)}'
    finally:
        cursor.close()
        connection.close()

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

