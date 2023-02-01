from flask_restful import Resource, request
import json

lista_habilidades = ['Python', 'Java','Flask','Php']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        if dados['habilidade'] not in lista_habilidades:
            lista_habilidades.append(dados['habilidade'])
            return lista_habilidades
        return {'status':'erro','mensagem':'Habilidade {} já está na lista'.format(dados['habilidade'])}
    
class GereHabilidades(Resource):
    def put(self,id):
        dados = json.loads(request.data)
        
        lista_habilidades[id] = dados['habilidade']
        return lista_habilidades
    def delete(self,id):
        del lista_habilidades[id]
        return lista_habilidades