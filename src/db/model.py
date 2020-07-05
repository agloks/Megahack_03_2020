from datetime import datetime

import mongoengine as db
from extras_mongoengine.fields import StringEnumField

from DI import ENV
from schema_enum import (GostoOrigemEnum, GostoMovimentacaoEnum, GostoTipoEnum, FumanteEnum, RendaEnum,
						AlcoolismoEnum, AtivoEnum, PerfilOrigemEnum, PerfilMovimentacaoEnum, PerfilTipoEnum,
						RegraFumanteEnum, StatusEnum, ModoEnum)



db.connect('megahack3', username='admin', password='1234', authentication_source='admin') # coneção com o banco

########## ENTIDADE CONSUMIDOR ###########

class Consumidor(db.Document):

	nome = db.StringField(max_length=50, required=True)
	telefone = db.StringField(max_length=20, required=True, unique=True)
	gastos_origem = StringEnumField(GostoOrigemEnum, default=GostoOrigemEnum.japonesa)
	gosto_movimentacao = StringEnumField(GostoMovimentacaoEnum)
	gosto_tipo = StringEnumField(GostoTipoEnum)
	estabelecimento_visitados = db.IntField()
	fumante = StringEnumField(FumanteEnum)
	renda = StringEnumField(RendaEnum)
	alcoolismo = StringEnumField(AlcoolismoEnum)
	create_at = db.DateTimeField()
	modified_at = db.DateTimeField(default=datetime.now)

	meta = {
		'ordering': ['create_at'],
		'collection': 'consumidor'
	}


########### ENTIDADE CUPOM (EMBEDDIING) #########

class Cupom(db.EmbeddedDocument):

	nome = db.StringField(max_length=100, required=True)
	desconto = db.IntField(required=True)
	ativo = StringEnumField(AtivoEnum)
	total_usado = db.IntField(default=0)
	create_at = db.DateTimeField()
	modified_at = db.DateTimeField(default=datetime.now)

	meta = {
		'ordering': ['create_at'],
		'collection': 'cupom'
	}

class Estoque(db.EmbeddedDocument):

	nome = db.StringField(max_length=100, required=True)
	quantidade = db.IntField(default=0)
	create_at = db.DateTimeField()
	modified_at = db.DateTimeField(default=datetime.now)



##########	ENTIDADE ESTABELECIMENTO ##########

class Estabelecimento(db.Document):

	nome = db.StringField(max_length=50, required=True)
	telefone = db.StringField(max_length=20, required=True, unique=True)
	perfil_origem = StringEnumField(PerfilOrigemEnum)
	perfil_movimento = StringEnumField(PerfilMovimentacaoEnum)
	perfil_tipo = StringEnumField(PerfilTipoEnum)
	latitude = db.IntField(max_length=50, required=True, unique=True)
	longitude = db.IntField(max_length=50, required=True, unique=True)
	endereco = db.StringField(max_length=50, required=True)
	cnpj = db.StringField(max_length=50, required=True, unique=True)
	consumidores_visitados = db.IntField()
	google_rating = db.IntField()
	google_rating_total = db.IntField()
	regra_fumante = StringEnumField(RegraFumanteEnum)
	level_preco = db.IntField()
	qrcode_token = db.StringField(max_length=30, unique=True)
	vendas = db.IntField()
	create_at = db.DateTimeField()
	modified_at = db.DateTimeField(default=datetime.now)
	lista_consumidores = db.ListField(db.ReferenceField("Consumidor"))
	itens_vendidos = db.ListField(db.ReferenceField("Pagamento"))
	cupom = db.ListField(db.EmbeddedDocumentField("Cupom"))
	estoque = db.ListField(db.EmbeddedDocumentField("Estoque"))

	meta = {
		'ordering': ['create_at'],
		'collection': 'estabelecimento'
	}



##########	ENTIDADE PAGAMENTO ##########

class Pagamento(db.Document):

	cliente = db.ReferenceField('Consumidor', reverse_delete_rule=db.CASCADE)
	estabelecimento = db.ReferenceField('Estabelecimento', reverse_delete_rule=db.CASCADE)
	valor = db.IntField(required=True)
	status = StringEnumField(StatusEnum)
	modo = StringEnumField(ModoEnum)
	voucher = db.StringField(max_length=100)
	create_at = db.DateTimeField()
	modified_at = db.DateTimeField(default=datetime.now)

	meta = {
		'ordering': ['create_at'],
		'collection': 'pagamento'
	}



if __name__ == '__main__':

	'''
	data = Reservations.objects(restaurant=rest, 
               customer__in=Customers.objects.filter(id="your filter id")).all()
	'''
	
	consumidor1 = Consumidor(nome="Igo", telefone="+5586994550066", gastos_origem="ITALIANA", 
		gosto_movimentacao="CALMO", gosto_tipo="BAR", estabelecimento_visitados=4, fumante="SIM",
		renda="ALTA", alcoolismo="RARO", create_at=datetime.now(), modified_at=datetime.now())

	consumidor2 = Consumidor(nome="Luana", telefone="+55994288940", gastos_origem="CHINESA", 
		gosto_movimentacao="BADALADO", gosto_tipo="RESTAURANTE", estabelecimento_visitados=4, fumante="NAO",
		renda="BAIXA", alcoolismo="RARO", create_at=datetime.now(), modified_at=datetime.now())


	estabelecimento = Estabelecimento(nome="meu chefe", telefone="+5586994288940", perfil_origem="BRASILEIRA",
		perfil_movimento="CALMO", perfil_tipo="BAR", latitude=394828382, longitude=-324344943, 
		endereco="rua jose ovideo bona, 1428, cariri", cnpj="212.1213.1231-212", consumidores_visitados=3,
		google_rating=4, google_rating_total=1000, regra_fumante="SIM", level_preco=1, qrcode_token="poiKJKJKKJKJJHkjkjKJKJK",
		vendas=40, create_at=datetime.now(), modified_at=datetime.now())


	pagamento1 = Pagamento(cliente="Igo", estabelecimento="meu chefe", valor=300, status="FALHA",
		modo="QRCODE", voucher="seila", create_at=datetime.now(), modified_at=datetime.now())

	pagamento2 = Pagamento(cliente="Heytor", estabelecimento="meu chefe", valor=200, status="PROCESSAMENTO",
		modo="QRCODE", voucher="seila", create_at=datetime.now(), modified_at=datetime.now())



	
	consumidor1.save()
	consumidor2.save()
	
	cupom = Cupom()
	cupom.nome = "desconto20"
	cupom.desconto = 40
	cupom.ativo = "SIM"
	cupom.total_usado = 100
	cupom.create_at = datetime.now()
	cupom.modified_at = datetime.now()

	estoque = Estoque()
	estoque.nome = "Açucar"
	estoque.quantidade = 100
	estoque.create_at = datetime.now()
	estoque.modified_at = datetime.now()

	pagamento1.save()
	pagamento2.save()

	estabelecimento.cupom.append(cupom)
	estabelecimento.estoque.append(estoque)

	estabelecimento.lista_consumidores = [consumidor1, consumidor2]
	estabelecimento.itens_vendidos = [pagamento1, pagamento2]

	estabelecimento.save()


