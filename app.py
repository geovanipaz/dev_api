from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id':0,
        'nome':'rafael',
    'habilidades':['Python','Flask']},
    {'id':1,
        'nome':'galleani',
    'habilidades':['Python','django']},

]

@app.route("/dev/<int:id>", methods= ['GET', 'PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            desenvolvedor = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de Id {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
            return response
        except Exception:
            mensagem = 'erro desconhecido'
            response = {'status':'erro', 'mensagem':mensagem}
            return response
        print(desenvolvedor)
        return jsonify( desenvolvedor )
    elif request.method == 'PUT':
        dados = json.loads( request.data )
        desenvolvedores[id] = dados
        return (dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return ({'status':'sucesso','mensagem':'registro excluido'})

@app.route("/dev", methods = ['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads( request.data )
        indice = len(desenvolvedores)
        dados['id'] = indice
        desenvolvedores.append(dados)
        return desenvolvedores[indice]
    elif request.method == 'GET':
        return desenvolvedores


if __name__== '__main__':
    app.run(debug=True)