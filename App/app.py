from flask import Flask, jsonify, request

app = Flask (__name__)

livros = [
    {
        'id':1,
        'titulo':'O senhor dos Anéis - V1',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id':2,
        'titulo':'Harry Potter e a Pedra',
        'autor': 'J.K Howling'
    },
    {
        'id':3,
        'titulo':'James Clear',
        'autor': 'Hábitos Atômicos'
    },
]
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods={'GET'})
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/livros/<int:id>',methods={'PUT'})
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
@app.route('/livros', methods={'POST'})
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

@app.route('/livros/<int:id>',methods={'DELETE'})
def excluir_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify(livros[indice])


app.run(port=5000,host='localhost',debug=True)