import  pymongo


url = "localhost"
port = 27017
client = pymongo.MongoClient(host=url , port=port)
db = client['site']
user_db = db['user']
