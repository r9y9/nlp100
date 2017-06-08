# mongo nlp100
# > db.artists.find({name: { $in: ["Yuki", "Queen"]} })

from pymongo import MongoClient

client = MongoClient("localhost")
db = client.nlp100
collection = db.artists

for doc in collection.find({"name": {"$in": ["Yuki", "Queen"]}}):
    print(doc)
