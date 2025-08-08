from flask import Flask,request,jsonify
# import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "App rodando"


@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f"ola {nome}"


@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    a=dados.get('n1',0 ) #---> ,numero diz oque retornará caso não for passado nenhum valor
    b=dados.get('n2',0)
    return jsonify ({'resultado': a+b})


@app.route('/categoria',methods=['POST'])
def categoria_jogador():
        dados=request.get_json()
        idade = dados.get('idade',0)
        if idade in range(5,9):
             return 'o jogador esta na categoria infantil'
        elif idade in range(9,11):
             return ' o jogador esta na categoria iniciado'
        elif idade in range(11,14):
             return ' o jogador esta na categoria juvenil'
        elif idade in range(14,18):
             return ' o jogador esta na categoria junior'
        else:
             return ' o jogador esta na categoria senior'
        
@app.route('/teste')
def teste():
     return 'teste'

        



if __name__=='__main__':
    app.run(debug=True)
