import re
import time

from DI import handlerJson

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

        1) ajuda
        2) comer
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
 
    1) recomendação
    2) próximos
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
      
#generic response to handle with commands not was able to understand
def unknow_response(commands):
  
  return f'''
    Desculpe, não consegui te entender, por favor seleciona o numero ou o texto dos possiveis comandos abaixo:

    {commands}
  '''

def isCached(data):
  '''
  :rtype: True = it's cached
          False = it's not cached
  '''
  time_min = time.gmtime().tm_min
  diff_time_min = int(data["time_min"]) - time_min
  
  #minutes scale
  if(diff_time_min > 2):
    return False

  return True

class PhasesConversation:
  def __init__(self, name, phone, text):
    self.phone = phone
    self.name = name
    self.text = text
    self.data_to_cache = {
      "namePerson": self.name,
      "phonePerson": self.phone,
      "phaseStagePerson": 0 
    }
    self.phase_stage = 0
    self.commands = f'''
        1) Recomendação
        2) Próximos
      '''

  def _updateStage(self, level):
    self.phase_stage = level
    self.data_to_cache["phaseStagePerson"] = self.phase_stage
    
    #must to ben run at root folder project
    handlerJson.writeToJSONFile(self.data_to_cache, "./temp/", self.phone)

  def phase_0(self):
    self._updateStage(1)
    return stage_0(self.name)

  def phase_1(self):
    pattern = re.compile(".*((?P<number>1|2)|(?P<command>ajuda|comer))", re.I | re.M)
    #set to not take duplicate of the same word
    regex_result = pattern.match(self.text)
    
    self.commands = f'''
      1) Ajuda
      2) Comer
    '''

    if(regex_result == None):
      unknow_response(self.commands)
      return -1

    #taking the result obtained from regex_result, which will only one command that not was None
    action = [item for item in regex_result.groupdict().values() if item != None][0].lower()
    if((action == "2") or (action == "comer")):
      self._updateStage(2)

    return stage_1(action)

  def phase_2(self):
    self.data_to_cache["endereco"] = self.text
    self._updateStage(3)
    return stage_2()

  def phase_3(self):
    pattern = re.compile(".*((?P<number>1|2|3)|(?P<command>recomendação|próximos))", re.I | re.M)
    #set to not take duplicate of the same word
    regex_result = pattern.match(self.text)
    
    self.commands = f'''
      1) Recomendação
      2) Próximos
    '''

    if(regex_result == None):
      return unknow_response(self.commands)

    #taking the result obtained from regex_result, which will only one command that not was None
    action = [item for item in regex_result.groupdict().values() if item != None][0].lower()
    possibles_commands_list = ["1", "2", "recomendação", "próximos"]
    if(not action in possibles_commands_list):
      return unknow_response(self.commands)
      
    return stage_3(action)

class HandlerConversation(PhasesConversation):
  def __init__(self, name, phone, text):
    super().__init__(name, phone, text)
    self.name = name
    self.phone = phone
    self.text = text

  def run(self):
    #must to ben run at root folder project
    data_cached = handlerJson.loadJson("./temp/", self.phone)
    if(data_cached):
      #if it overcome the limit of the 2 min without update, reset the stage
      if(not isCached(data_cached)):
        self._updateStage(0)
      self.phase_stage = data_cached["phaseStagePerson"]

    phases = {
      0: self.phase_0,
      1: self.phase_1,
      2: self.phase_2,
      3: self.phase_3
    }

    try:
      return phases[self.phase_stage]()
    except Exception as e:
      return unknow_response(self.commands)

if __name__ == '__main__':

  conversation_test_one = [
    "oi",
    "Eu queor uma comer",
    "Cambuci, São Paulo",
    "Próximos"
  ]

  for text in conversation_test_one:
    handlerConversation = HandlerConversation("Amanda", "551195069324", text)
    time.sleep(1)
    print(handlerConversation.run())