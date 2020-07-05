from random import choice, randint
import datetime

def g_c():
    return {
        "nome" : choice(['Igo', 'Felipe', 'Flávio', 'Saulo', 'Filipe']),
        "telefone" : choice(["+5586994550066", "+5511994328745", "+551299834322", "+553298765342", "+554321847542"]),
        "gostos_origem" : choice(["ITALIANA", "CHINESA", "JAPONESA"]),
        "gosto_movimentacao" : choice(["CALMO", "BADALADO", "RETRO"]),
        "gosto_tipo" : choice(["BAR", "RESTAURANTE", "LANCHONETE"]),
        "estabelecimento_visitados" : choice([i for i in range(0, 200, 8)]),
        "fumante" : choice(["SIM", "NAO"]),
        "renda" : choice(["ALTA", "BAIXA", "MEDIA"]),
        "alcoolismo" : choice(["RARO", "OCASIAO", "FREQUENTE", "SEMPRE"]),
        "create_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d'),
        "modified_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d')
    }


def g_e():
    return {
    "nome" : choice(["Budega X", "Meu chefe", "Pao do dia", "Só sabor bom", "Dugao", "Tok Final", "Makakitos", "Bugao do churrasco"]),
    "telefone" : choice(["+5586994550066", "+5511994328745", "+551299834322", "+553298765342", "+554321847542"]),
    "perfil_origem" : choice(["BRASILEIRA", "CHINESA", "JAPONESA"]),
    "perfil_movimento" : choice(["CALMO", "BADALADO", "RETRO"]),
    "perfil_tipo" : choice(["BAR", "RESTAURANTE", "LANCHONETE"]),
    "latitude" : choice([1234343434, -988438434]),
    "longitude" : choice([-4758343434, -323872474]),
    "endereco" : choice(["rua jose ovideo bona, 1428, cariri", "rua dri, 23, centro", "av. doutor dru, 1313, almeida", "quadra 1, 4, conjunto 2"]),
    "cnpj" : choice(["212.1213.1231-212", "123.4344.1212.-1", "434.123.5455.2323-12", "0983.3234.32322.123-00"]),
    "consumidores_visitados" : choice([i for i in range(1, 5000, 73)]),
    "google_rating" : choice([i for i in range(1, 5)]),
    "google_rating_total" : choice([i for i in range(1, 100)]),
    "regra_fumante" : choice(["SIM", "NAO"]),
    "level_preco" : choice([i for i in range(1, 4)]),
    "qrcode_token" : "poiKJKJKKJKJJHkjkjKJKJlkLKjKJTRWNPOPOmOIJfcEWoMILKionONyuGYRdRYnPIMoUK",
    "vendas" : choice([i for i in range(1, 1000, 18)]),
    "create_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d'),
    "modified_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d'),

    "lista_consumidores" : [ 
        choice(["5f013777798f08b3d715fc10", "5f013777798f08b3d715fc11", "5f013777798f08b3d715fc12", "5f013778798f08b3d715fc13"]),
        choice(["5f013777798f08b3d715fc10", "5f013777798f08b3d715fc11", "5f013777798f08b3d715fc12", "5f013778798f08b3d715fc13"]) 
    ],

    "itens_vendidos" : [ 
        choice(["5f013777798f08b3d715fc10", "5f013777798f08b3d715fc11", "5f013777798f08b3d715fc12", "5f013778798f08b3d715fc13"]), 
        choice(["5f013777798f08b3d715fc10", "5f013777798f08b3d715fc11", "5f013777798f08b3d715fc12", "5f013778798f08b3d715fc13"]) 
    ],

    "cupom" : [ 
        {
            "nome" : choice(["desconto20", "descontao100", "sobora", "20maisquevoce", "shawee20", "gr1d+", "zenvia123"]),
            "desconto" : choice([10, 20, 30, 40, 50, 60, 70]),
            "ativo" : choice(["SIM", "NAO"]),
            "total_usado" : choice([i for i in range(1, 300, 6)]),
            "create_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d'),
            "modified_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d')
        }
    ],
    
    "estoque" : [ 
        {
            "nome" : choice(["Açucar", "Batata", "Carne", "Ovo", "Legumes", "Leite", "Sal", "Pão"]),
            "quantidade" : choice([i for i in range(1, 1000, 18)]),
            "create_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d'),
            "modified_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d')
        }
    ]
}

def g_p():
    return {
  
    "cliente" : choice(['Igo', 'Felipe', 'Flávio', 'Saulo', 'Filipe']),
    "estabelecimento" : choice(["Budega X", "Meu chefe", "Pao do dia", "Só sabor bom", "Dugao", "Tok Final", "Makakitos", "Bugao do churrasco"]),
    "valor" : choice([i for i in range(1, 1000)]),
    "status" : choice(["PROCESSAMENTO", "CONCLUIDO", "FALHA"]),
    "modo" : choice(["QRCODE", "WHATSAPP"]),
    "voucher" : choice(["Escolha 1", "Escolha 2", "Escolha 3", "Escolha 4", "Escolha 5"]),
    "create_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d'),
    "modified_at" : datetime.date( randint(2020, 2020), randint(1, 7), randint(1, 28) ).strftime('%Y/%m/%d')
}



'''
import json

with open("consumidor.json", "w") as json_file:
    for i in range(1, 5001):
        json.dump(g_c(), json_file, indent=4)

'''