from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
        'nome':'rafael',
    'habilidades':['Python','Flask']},
    {'id':1,
        'nome':'galleani',
    'habilidades':['Python','django']},

]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de Id {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
            return response
        except Exception:
            mensagem = 'erro desconhecido'
            response = {'status':'erro', 'mensagem':mensagem}
            return response
        print(response)
        return response
    
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self,id):
        desenvolvedores.pop(id)
        return ({'status':'sucesso','mensagem':'registro excluido'})

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads( request.data )
        indice = len(desenvolvedores)
        dados['id'] = indice
        desenvolvedores.append(dados)
        return desenvolvedores[indice]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades')

if __name__ == '__main__':
    app.run(debug=True)