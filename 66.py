# mongo nlp100 --quiet --eval 'db.artists.count({area:"Japan"});'

from pymongo import MongoClient

client = MongoClient("localhost")
db = client.nlp100
collection = db.artists

# 22821
print(collection.count({"area": "Japan"}))
