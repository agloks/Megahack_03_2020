import pymongo 
  
class Atlas():
  def __init__(self):
    # Replace your URL here. Don't forget to replace the password. 
    connection_uri = ''
    client = pymongo.MongoClient(connection_uri) 
    self.database = client.get_database('sample_restaurants')
    #database have all collection inside as property, so to acess the collection wich we want, only pass the name them exactly as property
    self.collection = self.database.restaurants

  def getCollection(self):
    return self.collection


if __name__ == '__main__':
  o_atlas = Atlas()

  Collection = o_atlas.getCollection()
  result = Collection.find_one({})
  
  print(result)