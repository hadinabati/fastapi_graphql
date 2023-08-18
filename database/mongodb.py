import  pymongo


# url = "localhost"
url = "172.19.0.2"
port = 27017
client = pymongo.MongoClient(host=url , port=port)
db = client['site']
user_db = db['user']
sms_db = db['sms']
