def stage_0(name):
  return f'''
    Oi {name}, eu sou o meu garçom e estou aqui para te servir, ainda estou apredendo a linguagem dos humanos, então por favor não tente muita coisa pois eu sou bem novo. No que eu posso te servir no momento?

      1) Me ajuda?
      2) Quero comer aqui perto 
    '''

def stage_1(action):
  if((action == "1") or (action == "ajuda")):
    return f'''
    Claro, eu sempre vou te enviar as opções para comando a cada conversa, você pode digitar o texto ou colocar o numero. No momento tenho os seguintes comando:

      1) Ajuda
      2) Comer
      '''
  if((action == "2") or (action == "comer")):
    return f'''
    Pode me informe por favor em qual endereço você se encontra?
    Quanto mais informação como o modelo abaixo, melhor eu consigo te indicar =)

      Exemplo: Rua Santo Antonio, 601 - Bela Vista, São Paulo
      '''

def stage_2():
  return f'''
    Deseja alguma recomendação minha ou somente os mais próximos?
 
      1) Recomendação
      2) Próximos
    '''

def stage_3(action):
  if((action == "1") or (action == "recomendação")):
    return f'''
    Legal, deixe comigo só vou trazer os melhores
      '''
  if((action == "2") or (action == "próximos")):
    return f'''
    Legal, deixe comigo só vou trazer os mais próximos...
      '''

def stage_4_99():
  return f'''
    Tudo bem, imagino que você esteja sem tempo no momento, irei te mandar 
    enviar os restaurantes mais próximos... 
  '''

def stage_4_01():
  return f'''
    Eu vejo que é a sua primeira vez com a gente, e não temos suas preferências para recomendar, você poderia me responsder algumas perguntas sobre seus gostos e preferências?
 
      1) Sim
      2) Não
  '''

def stage_4_02():
  return f'''
    Que tipo de ambiente você gosta de frequentar?

      1) Calmo
      2) Badalado
      3) Retro
      4) Moderno
      5) Simples
      6) Sotisficado
  '''

def stage_4_03():
  return f'''
    Ok, obrigado, e qual seu tipo de comida predileto?

      1) Vegana
      2) Churrasco
      3) Japonesa
      4) Chinesa
      5) Nordestina
      6) Italina
  '''

def stage_4_04():
  return f'''
    Muito Obrigado, irei te recomendar os mais próximos de acordo com seu gosto!
  '''

def stage_6_01(restaurants):

  list_restaurants = []

  for item in range(1, 6):
    list_restaurants.append(
      f"""
      {item})
        Nome: {restaurants[item - 1]["name"]}
        Endereço: {restaurants[item - 1]["vicinity"]}
        Parceiro: Não
      """
    )

  return f'''
  {list_restaurants[0]}
  {list_restaurants[1]}
  {list_restaurants[2]}
  {list_restaurants[3]}
  {list_restaurants[4]}
  '''      

def stage_6_02():
  return f'''
    Dos estabelecimentos parceiros você pode já pedir o cardapio e ver as opções aqui mesmo,
    e se quiser até mesmo fazer seu pagamento adiantado, deseja ver o cardapio de algum parceiro?

    Se sim basta somente colocar o numero dele enviado na mensagem anteiro! 

    Se não, muito obrigado pela conversa comigo, espero que você tenha um bom rango e volte sempre, sentirei saudades! s2
  '''

#generic response to handle with commands not was able to understand
def unknow_response(commands):
  
  return f'''
    Desculpe, não consegui te entender, por favor seleciona o numero ou o texto dos possiveis comandos abaixo:

    {commands}
  '''