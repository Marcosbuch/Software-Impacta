from flask import Flask, request, jsonify, render_template
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Conexão com o banco de dados
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Buch_159753",  # Insira a senha do MySQL
    database="assessoria_financeira"
)
cursor = db.cursor()

# Rota para renderizar a página principal
@app.route('/')
def home():
    return render_template('home.html')  # Página principal de navegação

# Rota para renderizar a página de cadastro de receitas
@app.route('/cadastrar-receita', methods=['GET'])
def render_cadastrar_receita():
    return render_template('cadastrar_receita.html')

# Rota para cadastrar receita no banco de dados
@app.route('/cadastrar-receita', methods=['POST'])
def cadastrar_receita():
    data = request.json
    descricao = data.get('descricao')
    tipo = data.get('tipo')
    indicador1 = data.get('indicador1')
    indicador2 = data.get('indicador2')
    compoe_dre = data.get('compoe_dre')
    compoe_dfc = data.get('compoe_dfc')

    # Adiciona a data atual
    data_atual = datetime.now().strftime('%Y-%m-%d')

    sql = "INSERT INTO plano_contas_receitas (descricao, tipo, indicador1, indicador2, compoe_dre, compoe_dfc, data) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (descricao, tipo, indicador1, indicador2, compoe_dre, compoe_dfc, data_atual)
    cursor.execute(sql, values)
    db.commit()

    return jsonify({'message': 'Receita cadastrada com sucesso!'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
