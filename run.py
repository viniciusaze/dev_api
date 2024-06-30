from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {"id": 0, "nome": "Vinicius", "habilidades": ["Python", "Flask"]},
    {"id": 1, "nome": "Francisco", "habilidades": ["Python", "Django"]}
]

# Devolve, altera e deleta um desenvolvedor pelo ID
@app.route("/dev/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):

    # Método GET = Visualização
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": "erro", "mensagem": f"desenvolvedor de id {id} não existe"}
        except Exception:
            response = {f"status": "erro", "mensagem": "erro desconhecido, procure o administrador da API"}
        return jsonify(response)

    # Método PUT = Modificação
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)

    # Método DELETE = Remoção
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({"status": "sucesso", "mensagem": "registro excluido"})


# Lista e inclui um novo desenvolvedor
@app.route("/dev/", methods=['POST', 'GET'])
def lista_desenvolvedores():
    # Método POST = Inserção
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])

    # Retornando todos da lista
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run(debug=True)