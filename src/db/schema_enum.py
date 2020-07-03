from enum import Enum



############## Objetos dos campos do tipo Enum da entidade Consumidor ############

class GostoOrigemEnum(Enum):
	japonesa = 'JAPONESA'
	chinesa = 'CHINESA'
	italiana = 'ITALIANA'

class GostoMovimentacaoEnum(Enum):
	calmo = 'CALMO'
	badalado = 'BADALADO'
	retro = 'RETRO'

class GostoTipoEnum(Enum):
	restaurante = 'RESTAURANTE'
	bar = 'BAR'
	lanchonete = 'LANCHONETE'

class FumanteEnum(Enum):
	sim = 'SIM'
	nao = 'NAO'

class RendaEnum(Enum):
	alta = 'ALTA'
	media = 'MEDIA'
	baixa = 'BAIXA'

class AlcoolismoEnum(Enum):
	raro = 'RARO'
	ocasiao = 'OCASIAO'
	frequente = 'FREQUENTE'
	sempre = 'SEMPRE'



############## Objetos dos campos do tipo Enum da entidade Cupom ############
class AtivoEnum(Enum):

	sim = 'SIM'
	nao = 'NAO'



############## Objetos dos campos do tipo Enum da entidade Estabelecimento ############
class PerfilOrigemEnum(Enum):

	japonesa = 'JAPONESA'
	chinesa = 'CHINESA'
	brasileira = 'BRASILEIRA'

class PerfilMovimentacaoEnum(Enum):

	calmo = 'CALMO'
	badalado = 'BADALADO'
	retro = 'RETRO'

class PerfilTipoEnum(Enum):

	restaurante = 'RESTAURANTE'
	bar = 'BAR'
	lanchonete = 'LANCHONETE'

class RegraFumanteEnum(Enum):

	sim = 'SIM'
	nao =  'NAO'



############## Objetos dos campos do tipo Enum da entidade Pagamento ############
class StatusEnum(Enum):

	processamento = 'PROCESSAMENTO'
	concluido = 'CONCLUIDO'
	falha = 'FALHA'

class ModoEnum(Enum):

	qrcode = 'QRCODE'
	whatsapp = 'WHATSAPP'