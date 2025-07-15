#ONLY FOR TESTING NO REAL PURPOSE IN PROJECT
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://palakmathur2811:palak123@cluster0.gitft9s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#python test_mongodb.py to see if u are connected/pinged to mongodb or not