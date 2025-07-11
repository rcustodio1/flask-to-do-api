from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("database.db")

# Rota inicial com visualização
@app.route('/')
def home():
    return render_template("index.html")

# Rota para listar tarefas
@app.route('/api/tarefas', methods=['GET'])
def listar_tarefas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = [
        {"id": row[0], "titulo": row[1], "descricao": row[2], "concluida": bool(row[3])}
        for row in cursor.fetchall()
    ]
    con.close()
    return jsonify(tarefas)

# Rota para criar tarefa
@app.route('/api/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.json
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, descricao, concluida) VALUES (?, ?, ?)",
                   (dados['titulo'], dados['descricao'], False))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Tarefa criada com sucesso"}), 201

# Rota para deletar uma tarefa
@app.route('/api/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Tarefa deletada com sucesso"})

# Rota para atualizar uma tarefa
@app.route('/api/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.json

    con = conectar()
    cursor = con.cursor()

    # Buscar tarefa atual
    cursor.execute("SELECT titulo, descricao FROM tarefas WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    if not resultado:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    titulo_atual, descricao_atual = resultado

    novo_titulo = dados.get('titulo') or titulo_atual
    nova_descricao = dados.get('descricao') or descricao_atual
    concluida = int(dados.get('concluida', 0))

    cursor.execute("""
        UPDATE tarefas
        SET titulo = ?, descricao = ?, concluida = ?
        WHERE id = ?
    """, (novo_titulo, nova_descricao, concluida, id))
    con.commit()
    con.close()
    return jsonify({"mensagem": "Tarefa atualizada com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
