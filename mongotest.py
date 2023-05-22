from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse

username = urllib.parse.quote_plus("aravindsimha")
password = urllib.parse.quote_plus("Rameswararao@1")
uri = f"mongodb+srv://{username}:{password}@datascience.jt95bw7.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


d = {
    "name" : "aravindsimha",
    "email" : "aravindsimha1.1@gmail.com",
    "surname" : "yerramsetty"
}

db = client['mongotest']
coll = db['test1']
coll.insert_one(d)
# hi