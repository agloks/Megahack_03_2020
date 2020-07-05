from pymongo import MongoClient

CONFIG = {
	'MONGO_URI': 'mongodb+srv://admin-mongodb:54321@clusterprojectmongodb-sztyp.mongodb.net/megahack3?retryWrites=true&w=majority',
	'MONGO_DB': 'megahack3'
}

def connect():
	client = MongoClient(CONFIG['MONGO_URI'])
	db = client[CONFIG['MONGO_DB']]
	return db