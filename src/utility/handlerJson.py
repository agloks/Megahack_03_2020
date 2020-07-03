import time
import json
import os

def writeToJSONFile(data, path, filename, stamptime=True):
  fileToSave = os.path.join(path, filename + '.json')

  if(stamptime):
    data["time_min"] = time.gmtime().tm_min
  
  with open(fileToSave, 'w') as fp:
      json.dump(data, fp)
      
def loadJson(path, filename):
  try:
    fileToRead = os.path.join(path, filename + '.json')
    data = None

    with open(fileToRead) as file_data:
      data = json.load(file_data)
  except Exception as e:
    return False

  return data