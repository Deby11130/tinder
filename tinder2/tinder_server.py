from flask import Flask, jsonify, request
import estrutura_interesses as i

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def ola():
    return "servidor do tinder"

@app.route("/pessoas", methods=['GET'])
def todas_pessoas():
    return i.todas_as_pessoas()


@app.route("/pessoas", methods=['POST'])
def adiciona_pessoa():
    dic_enviado = request.json
    i.adiciona_pessoa(dic_enviado)
    return "ok"

"http://localhost:5003/pessoas/1"
@app.route("/pessoas/<int:id_pessoa>", methods=['GET'])
def pessoa_por_id(id_pessoa):
    pessoa = i.localiza_pessoa(id_pessoa)
    return pessoa

@app.route("/reseta",methods=['POST'])
def reseta():
    i.reseta()
    return "listas resetadas"

@app.route("/sinalizar_interesse/<int:id_interesse>/<int:id_alvo>/", methods=['PUT'])
def sinaliza_interesse(id_interesse,id_alvo):
    try:
        i.localiza_pessoa(id_alvo)
        i.localiza_pessoa(id_interesse)
    except:
        return "pessoa invalida ", 404
    try:
        i.adiciona_interesse(id_interesse,id_alvo)
        return "Interesse adicionado"
    except:
        return {'erro':'interesse incompativel'}, 400

@app.route("/sinalizar_interesse/<int:id_interesses>/<int:id_alvo>/", methods=['DELETE'])
def deleta_interesse(id_interesses,id_alvo):
    try:
        i.localiza_pessoa(id_interesses)
        i.localiza_pessoa(id_alvo)
    except:
        return "Pessoa invalida ", 404
    i.remove_interesse(id_interesses, id_alvo)
    return "Retiramos essa pessoa da sua lista de intersse"
@app.route("/interesses/<int:id_interessado>/", methods=['GET'])
def devolve_lista(id_interessado):
    try:
        i.localiza_pessoa(id_interessado)
        return i.consulta_interesses(id_interessado)
    except:
        return "Id não localizado ",404
    
@app.route("/matches/<int:id_pessoa>",methods=['GET'])
def lista_matches(id_pessoa):
    try:
        i.localiza_pessoa(id_pessoa)
        return i.lista_matches(id_pessoa)
    except:
        return "Id não localizado ", 404
    


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
