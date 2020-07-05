from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from src.whataspp import handler_conversation, whastapp_api
from settings import connect

#####################################################################################################


app = Flask(__name__)

CORS(app)

app.config['SECRET_KEY'] = 'time21'

#ONLY FOR DEVELOPMENT
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route("/API/V1/listenerMessage/", methods=['POST'])
def listenerMessage():
  print("[listenerMessage] Receveing message...")
  receveid = request.get_json()
  name_people = None
  number_people = None
  text_message = None

  #0)Check request: 
  try:
    if( (receveid["direction"] != "IN") and (receveid["channel"] != "whatsapp") ):
      return jsonify({"Status": "Invalid Request"}), 400
  except Exception as e:
    print("[ERROR #0 /API/V1/listenerMessage/]")
    print(e)
    return jsonify({"Status": "Invalid Request"}), 400

  #1)TODO: save the data
  
  #2)handle with the message
  try:
    name_people = receveid["message"]["visitor"]["name"]
    number_people = receveid["message"]["from"]
    text_message = receveid["message"]["contents"][1]["text"]
  except Exception as e:
    print("[ERROR #2 /API/V1/listenerMessage/]")
    print(e)
    return jsonify({"Status": "Invalid Request"}), 400

  #3)handle return response
  try:
    handlerConversation = handler_conversation.HandlerConversation(name_people, number_people, text_message)
    text_response = handlerConversation.run()
    
    whastapp_api.response_to(text_response, number_people)
  except Exception as e:
    print("[ERROR #3 /API/V1/listenerMessage/]")
    print(e)

  return receveid, 200


##### Consumidor ######
@app.route('/consumidor', methods=['GET'])
def consumidor():

    consumidor = []
    collection = connect()

    for query in collection['consumidor'].find({}):

        consumidor.append({
          "nome": query["nome"],
          "telefone" : query["telefone"],
          "gostos_origem" : query['gostos_origem'],
          "gosto_movimentacao" : query['gosto_movimentacao'],
          "gosto_tipo" : query['gosto_tipo'],
          "estabelecimento_visitados" : query['estabelecimento_visitados'],
          "fumante" : query['fumante'],
          "renda" : query['renda'],
          "alcoolismo" : query['alcoolismo'],
          "create_at" : query['create_at'],
          "modified_at" : query['modified_at']
        })



    return jsonify({'consumidor': consumidor})


##### Estabelecimento #######
@app.route('/estabelecimento', methods=['GET'])
def estabelecimento():

    estabelecimento = []
    collection = connect()

    for query in collection['estabelecimento'].find({}):

        estabelecimento.append({
            'nome': query["nome"],
            'telefone': query["telefone"],
            'perfil_origem': query["perfil_origem"],
            'perfil_movimento': query["perfil_movimento"],
            'perfil_tipo': query["perfil_tipo"],
            'latitude': query["latitude"],
            'longitude': query["longitude"],
            'endereco': query["endereco"],
            'cnpj': query["cnpj"],
            'consumidores_visitados': query["consumidores_visitados"],
            'google_rating': query["google_rating"],
            'google_rating_total': query["google_rating_total"],
            'regra_fumante': query["regra_fumante"],
            'level_preco': query["level_preco"],
            'qrcode_token': query["qrcode_token"],
            'vendas': query["vendas"],
            'create_at': query["create_at"],
            'modified_at': query["modified_at"],
            'lista_consumidores': str(query["lista_consumidores"]),
            'itens_vendidos': str(query["itens_vendidos"]),
            'cupom': query["cupom"],
            'estoque': query["estoque"]
        })

    return jsonify({'estabelecimento': estabelecimento})

######## Pagamento ###########
@app.route('/pagamento', methods=['GET'])
def pagamento():
    pagamentos = []
    collection = connect()

    for query in collection['pagamento'].find({}):
        pagamentos.append({
            'cliente': query['cliente'],
            'estabelecimento': query['estabelecimento'],
            'valor': query['valor'],
            'status': query['status'],
            'modo': query['modo'],
            'voucher': query['voucher'],
            'create_at': query['create_at'],
            'modified_at': query['modified_at']
        })

    return jsonify({'pagamentos': pagamentos})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)